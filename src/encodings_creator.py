import face_recognition
import os
import pickle

face_images_directory = '../captured_images'  # Replace with your actual path

known_faces = {}

if not os.path.exists(face_images_directory):
    print(f"The specified directory {face_images_directory} does not exist.")
    exit()

for foldername in os.listdir(face_images_directory):
    folder_path = os.path.join(face_images_directory, foldername)

    if os.path.isdir(folder_path):
        name = foldername
        print(f"Processing folder {name}")

        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                file_path = os.path.join(folder_path, filename)
                print(f"Processing file {file_path}")

                try:
                    image = face_recognition.load_image_file(file_path)
                except Exception as e:
                    print(f"Failed to load image from {file_path} due to {str(e)}")
                    continue

                # Check for face locations before getting encodings
                face_locations = face_recognition.face_locations(image)
                print(f"Found {len(face_locations)} face(s) in {file_path}")

                if face_locations:
                    encodings = face_recognition.face_encodings(image, known_face_locations=face_locations)
                    if encodings:
                        if name in known_faces:
                            known_faces[name].append(encodings[0])
                        else:
                            known_faces[name] = [encodings[0]]

print("Encodings have been generated.")
print(known_faces)

filename = '../data/known_faces.pkl'

with open(filename, 'wb') as file:
    pickle.dump(known_faces, file)

print(f"Encodings have been saved to {filename}")
