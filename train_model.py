import os
import cv2
import numpy as np
import argparse
from sklearn.ensemble import HistGradientBoostingClassifier  # Faster than LightGBM
from sklearn.preprocessing import LabelEncoder
from joblib import dump, parallel_backend
from detector import extract_hog_features
from time import time

# Configuration
parser = argparse.ArgumentParser()
parser.add_argument('--use_pca', action='store_true', help='Enable PCA for faster training')
parser.add_argument('--batch_size', type=int, default=256, help='Images per batch')
parser.add_argument('--num_workers', type=int, default=4, help='CPU cores to use')
args = parser.parse_args()

def batch_process(paths, target_size=(64,64)):
    """Process images in batches for speed"""
    batch = np.zeros((len(paths), target_size[0], target_size[1]), dtype=np.uint8)
    for i, path in enumerate(paths):
        batch[i] = cv2.resize(cv2.imread(path, 0), target_size)
    return batch

def load_data(dataset_path="dataset"):
    X, y = [], []
    print("⚡ Loading dataset in optimized mode...")
    
    # Get all image paths
    paths = []
    for label in os.listdir(dataset_path):
        label_path = os.path.join(dataset_path, label)
        if os.path.isdir(label_path):
            paths.extend([(os.path.join(label_path, f), label) for f in os.listdir(label_path)])
    
    # Process in parallel batches
    with parallel_backend('threading', n_jobs=args.num_workers):
        for i in range(0, len(paths), args.batch_size):
            batch_paths = [p[0] for p in paths[i:i+args.batch_size]]
            batch_labels = [p[1] for p in paths[i:i+args.batch_size]]
            
            images = batch_process(batch_paths)
            features = [extract_hog_features(img) for img in images]
            
            X.extend(features)
            y.extend(batch_labels)
            
            print(f"\rProcessed {min(i+args.batch_size, len(paths))}/{len(paths)}", end='')
    
    print(f"\n✅ Loaded {len(X)} samples")
    return np.array(X), y

def train():
    start_time = time()
    X, y = load_data()
    
    # Faster alternative to PCA
    if args.use_pca:
        from sklearn.decomposition import IncrementalPCA
        pca = IncrementalPCA(n_components=64, batch_size=512)
        X = pca.fit_transform(X)
    else:
        pca = None
    
    le = LabelEncoder()
    y = le.fit_transform(y)
    
    # Ultra-fast classifier
    clf = HistGradientBoostingClassifier(
        max_iter=100,
        max_leaf_nodes=32,
        early_stopping=True,
        n_iter_no_change=10,
        random_state=42
    )
    
    print("🏎️ Training model (optimized for speed)...")
    clf.fit(X, y)
    
    os.makedirs("models", exist_ok=True)
    model_path = "models/ultrafast_model.pkl"
    dump((clf, le, pca), model_path)
    
    print(f"🚀 Training completed in {time()-start_time:.2f} seconds")
    print(f"💾 Model saved to {model_path}")

if __name__ == "__main__":
    train()