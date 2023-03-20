# create_image.py [prompt] [filename] [size]
# This python script will utilize the OpenAI API in order to create and image and save directly to disk.
# Last updated: March 19, 2023
# Author: Ryan Priore (ryan.priore@gmail.com)
#
# Inputs:
#     prompt: the prompt to send to OpenAI API
#     filename: the filename of script or function to be written to disk w/o extension
#     size: small, medium or large corresponding to 256x256, 512x512, and 1024x1024
# Example:
#     python3 create_image.py "Digital art of batman drinking a martini" "batman_martini" "medium"

import argparse
from base64 import b64decode
import json
import openai
import os

# Define the input arguments
parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to OpenAI API")
parser.add_argument("filename", help="The filename of script or function to be written to disk w/o extension")
parser.add_argument("size", help="The size of the image: small (256x256), medium (512x512), or large (1024x1024)")
args = parser.parse_args()

# Determine image size
match args.size.lower():
    case "small":
        size = "256x256"
    case "medium":
        size = "512x512"
    case "large":
        size = "1024x1024"

# Define remaining input arguments
prompt = args.prompt
filename = "image_output/" + args.filename

# Get OpenAI API key (Option #1): Import from environmental variable
#openai.api_key = os.getenv("OPENAI_API_KEY")
# Get OpenAI API key (Option #2): Import from text file
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().rstrip()

# Execute OpenAI API completion request and store response
response = openai.Image.create(
  prompt = prompt,
  n = 1,
  size = size,
  response_format = "b64_json"
)

# Write image data to disk
#with open(filename + ".json", mode = "w", encoding = "utf-8") as file:
#    json.dump(response, file)
for index, image_dict in enumerate(response["data"]):
    image_data = b64decode(image_dict["b64_json"])
    with open(filename + ".png", mode = "wb") as png:
        png.write(image_data)