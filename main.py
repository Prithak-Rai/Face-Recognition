import cv2
import face_recognition
from simple_facerec import SimpleFacerec

# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("Images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names=sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        if name == "Unknown":
            name = "Not a family Member"
            b, g, r = 0, 0, 255
        else:
            b, g, r = 0, 255, 0
        
        font_scale = 1.5

        cv2.putText(frame, name, (x1, y1 -10), cv2.FONT_HERSHEY_COMPLEX_SMALL, font_scale, (b, g, r), 4)
        cv2. rectangle(frame, (x1, y1), (x2,y2), (b, g, r), 4)
        print(face_loc)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()