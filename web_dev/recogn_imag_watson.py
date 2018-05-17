from watson- import VisualRecognitionV3
import json

visual_recognition = VisualRecognitionV3(version='2018-03-19', api_key="**************")

with open(r'path_to_image.jpg', 'rb') as images_file:
    car_results = visual_recognition.classify(images_file=images_file)
    print(json.dumps(car_results, indent=2))

# with open(r'path_to_image.jpg', 'rb') as images_file:
#     faces_result = visual_recognition.detect_faces(images_file=images_file)
#     print(json.dumps(faces_result, indent=2))
