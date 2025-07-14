import cv2
from skimage.feature import hog
from joblib import Memory

# Cache features to avoid recomputation
memory = Memory("cache_dir", verbose=0)

@memory.cache
def preprocess_image(image):
    """Convert to grayscale and resize to 64x64"""
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.resize(image, (64, 64))

@memory.cache
def extract_hog_features(image):
    """Optimized HOG feature extraction"""
    if len(image.shape) != 2:
        raise ValueError("Image must be grayscale")
    return hog(image,
              orientations=6,
              pixels_per_cell=(16, 16),
              cells_per_block=(1, 1),
              block_norm='L2-Hys')