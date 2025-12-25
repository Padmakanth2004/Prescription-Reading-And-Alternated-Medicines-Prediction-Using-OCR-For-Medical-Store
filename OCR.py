import os, io,google
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'booming-octane-423414-h6-b446a7e619e1.json'
client = vision.ImageAnnotatorClient()

def extract_tablet_name(path):
    """Detects text in the file."""

    client = vision.ImageAnnotatorClient()

    with open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        #print(f'\n"{text.description}"')

        #vertices = [
        #    f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
        #]

        #print("bounds: {}".format(",".join(vertices)))
        tablet_name = texts[0].description.replace("\n", " ").strip()  # Replace newlines with spaces
        return tablet_name
    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )

# Call the function with the path to the image
#detect_text('/Users/kolan/Downloads/doctor.jpeg')