# Face Detection in Images
# By Michael Morales

import cv2

def detect_faces(image_path):
    """
    Detects faces in an image and marks them with rectangles.
    
    Parameters:
        image_path (str): The path to the input image where faces need to be detected.
    
    Returns:
        None
    """
    # Load the pre-trained Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Load the input image
    img = cv2.imread(image_path)
    
    # Convert the image to grayscale (required for face detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # If faces are detected, draw rectangles around them
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Rectangle in blue color
    
    # Display the output image with detected faces
    cv2.imshow('Face Detection', img)
    
    # Wait for a key press and then close the displayed window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    """
    Main function to run the face detection program.
    """
    image_path = input("Enter the path of the image for face detection: ")
    detect_faces(image_path)

# Run the face detection script
if __name__ == "__main__":
    main()
