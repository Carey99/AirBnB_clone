#!/usr/bin/python3

import requests
import os

image_url = "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png"

folder_path = "./web_static/images"

# Create image folder if doesn't exist

os.makedirs(folder_path, exist_ok=True)


# Send get request

response = requests.get(image_url)

if response.status_code == 200:
    with open(os.path.join(folder_path, "logo.png"), "wb") as f:
        f.write(response.content)
        print("Image saved succefully")
else:
    print("Failed to download the image")
