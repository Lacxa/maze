import cv2
import face_recognition

# Load a sample image and learn to recognize it
known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

known_faces = [known_encoding]

# Initialize the webcam
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Convert the frame from BGR to RGB (face_recognition uses RGB)
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations and face encodings in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        # Draw a rectangle around the face
        color = (0, 255, 0) if True in matches else (0, 0, 255)
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

    # Show the video
    cv2.imshow("Face Recognition", frame)

    # Quit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
