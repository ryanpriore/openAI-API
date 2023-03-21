# create_image_gui.py
# This python function will utilize the OpenAI API in order to create a user-defined image within a GUI.
# Last updated: March 20, 2023
# Author: Ryan Priore (ryan.priore@gmail.com)
#
# Example:
#     python3 create_image_gui.py

from base64 import b64decode
import io
import json
import openai
import os
from PIL import Image
import PySimpleGUI as sg

# Get OpenAI API key (Option #1): Import from environmental variable
#openai.api_key = os.getenv("OPENAI_API_KEY")
# Get OpenAI API key (Option #2): Import from text file
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().rstrip()

# Define possible file types for saving
file_types = [("PNG (*.png)", "*.png")]

# Create default variables
prompt = "Origami monkey"
size = "1024x1024"
image = []

# Convert array to data
def array_to_data(array):
    im = Image.fromarray(array)
    with io.BytesIO() as output:
        im.save(output, format = "PNG")
        data = output.getvalue()
    return data

# Execute OpenAI API completion request and store response
def create_image(prompt, size):
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = size,
        response_format = "b64_json"
    )
    for index, image_dict in enumerate(response["data"]):
        image_data = b64decode(image_dict["b64_json"])
    return image_data

def main():
    elements = [
        [
            sg.Text("Describe your image:", justification = "left"),
            sg.Multiline(size = (50, 2), justification = "left", key = "prompt"),
        ],
        [
            sg.Text("Resolution:", justification = "left"),
            sg.Combo(["1024x1024", "512x512", "256x256"], size = (15, 1), default_value = "1024x1024", key = "size"),
            sg.Button("Create Image"),
        ],
        [
            sg.Text("Filename:"),
            sg.Input(size = (20, 1), key = "filename"),
            sg.Button("Save Image"),
        ],
        [sg.Image(key = "-IMAGE-")],
    ]

    window = sg.Window("DALL-E Create Image", elements, elements, size = (525, 600))

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Create Image":
            prompt = values["prompt"]
            size = values["size"]
            image_data = create_image(prompt, size)
            filename = "image_output/" + "temp.png"
            with open(filename, mode = "wb") as png:
                png.write(image_data)
            image = Image.open(filename)
            image.thumbnail((512, 512))
            bio = io.BytesIO()
            image.save(bio, format = "PNG")
            window["-IMAGE-"].update(data = bio.getvalue())
        if event == "Save Image":
            filename = "image_output/" + values["filename"]
            with open(filename + ".png", mode = "wb") as png:
                png.write(image_data)

    window.close()

if __name__ == "__main__":
    main()