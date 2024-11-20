# Real-time License Plate Recognition
# By Michael Morales

import cv2
import pytesseract

# Path to Tesseract executable
# For Windows: Update the path below to the location of your tesseract.exe
# For Linux: The path is usually '/usr/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows Example

def detect_license_plate(frame, face_cascade):
    """
    Detects license plates in a video frame.
    
    Parameters:
        frame (ndarray): The video frame where license plates need to be detected.
        face_cascade (CascadeClassifier): The pre-trained Haar Cascade for license plate detection.
    
    Returns:
        list: A list of detected license plates (rectangles).
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    plates = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    return plates

def recognize_text_from_plate(plate_img):
    """
    Recognizes text from a cropped license plate image using OCR.
    
    Parameters:
        plate_img (ndarray): The cropped license plate image.
        
    Returns:
        str: The text recognized by OCR from the plate image.
    """
    text = pytesseract.image_to_string(plate_img, config='--psm 8')  # Set OCR mode to recognize a single line
    return text.strip()

def main():
    # Load the pre-trained Haar Cascade Classifier for license plates
    # You can replace this with a custom classifier or a deep learning-based model if needed
    plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

    # Start video capture (0 for webcam, or path to video file)
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read a frame from the webcam or video file
        ret, frame = cap.read()
        
        if not ret:
            break

        # Detect license plates
        plates = detect_license_plate(frame, plate_cascade)
        
        # Loop through each detected license plate
        for (x, y, w, h) in plates:
            # Draw a rectangle around the detected plate
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            
            # Crop the plate from the frame for text recognition
            plate_img = frame[y:y + h, x:x + w]
            
            # Recognize text from the license plate
            plate_text = recognize_text_from_plate(plate_img)
            
            # Display the recognized text on the plate
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, plate_text, (x, y - 10), font, 0.9, (255, 0, 0), 2, cv2.LINE_AA)

        # Display the frame with the license plates marked and text recognized
        cv2.imshow('License Plate Recognition', frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

# Run the license plate recognition script
if __name__ == "__main__":
    main()
