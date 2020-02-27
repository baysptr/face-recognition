import face_recognition
from PIL import Image, ImageDraw
import numpy as np

# Load train data pertama [Risma]
obama_image = face_recognition.load_image_file("data_example/train_data.jpeg")
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load train data kedua [Gus Ipul]
biden_image = face_recognition.load_image_file("data_example/test_data_2.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

# Data train tersebut dibuat menjadi array, agar dapat dilakukan pencarian
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
# Label data train
known_face_names = [
    "Risma",
    "Gus Ipul"
]

# Load test data yaitu poster kampanye gus ipul dengan wakilnya
unknown_image = face_recognition.load_image_file("data_example/test_data_two_people.jpg")

# Encoding data test tersebut
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Data test yang sudah di encode diubah menjadi array agar mudah di compare dengan data Train
pil_image = Image.fromarray(unknown_image)
# Buat image dari canvas
draw = ImageDraw.Draw(pil_image)

# Process compare dari train data dengan test data
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    name = "Unknown"

    #if True in matches:
    #    first_match_index = matches.index(True)
    #    name = known_face_names[first_match_index]

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    # Buat kotak detecetion
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Buat label pada setiap kotak yang ditemukan
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


del draw
pil_image.show()

# Jika anda save hasil compare - nya
# pil_image.save("hasil.jpg")
