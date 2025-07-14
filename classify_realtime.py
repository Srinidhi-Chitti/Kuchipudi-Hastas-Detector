import cv2
import numpy as np
from joblib import load
from detector import extract_hog_features
import json
import os

def main():
    # Load model and data
    clf, le, pca = load("models/fast_hasta_model.pkl")
    
    with open("data/hasta_meanings.json", "r", encoding='utf-8') as f:
        hastas = json.load(f)

    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        if not ret: break
        
        # Processing
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (64, 64))
        features = pca.transform([extract_hog_features(resized)])
        pred = clf.predict(features)[0]
        label = le.inverse_transform([pred])[0]

        # Display info
        y_offset = 40
        cv2.putText(frame, f"Mudra: {label}", (20, y_offset), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        
        if label in hastas:
            # Display meaning
            y_offset += 30
            cv2.putText(frame, f"Meaning: {hastas[label]['meaning']}", 
                       (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,255), 1)
            
            # Display applications
            y_offset += 20
            applications = hastas[label].get('use_cases', [])
            for i, app in enumerate(applications[:3]):  # Show first 3 applications
                y_offset += 20
                cv2.putText(frame, f"{i+1}. {app}", 
                           (20, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200,200,255), 1)

        cv2.imshow("Kuchipudi Mudra Detector", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()