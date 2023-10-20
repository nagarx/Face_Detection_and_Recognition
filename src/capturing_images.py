import cv2
import os

save_directory = "../captured_images/person_name"  # change person_name to the name of the person
os.makedirs(save_directory, exist_ok=True)

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        cv2.imshow("Press 'c' to capture, 'q' to quit", frame)

        key = cv2.waitKey(1)

        if key == ord('c'):  # Press 'c' to capture the image
            person_name = input("Enter the name of the person: ")
            # Generate a unique filename
            filename = f"{person_name}_{str(hash(frame.tobytes()))}.jpg"
            file_path = os.path.join(save_directory, filename)
            cv2.imwrite(file_path, frame)
            print(f"Image saved to {file_path}")

        elif key == ord('q'):  # Press 'q' to quit
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
