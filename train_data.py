import face_recognition

# Train data [bu risma]
picture_of_me = face_recognition.load_image_file("data_example/train_data.jpeg")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

# Test data pertama [bu risma], test data kedua [gus ipul]
unknown_picture = face_recognition.load_image_file("data_example/test_data.jpeg")
# unknown_picture = face_recognition.load_image_file("data_example/test_data_2.jpg")
unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]

results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

if results[0] == True:
    print("Face terdeteksi sama")
else:
    print("Face terdeteksi tidak sama")
