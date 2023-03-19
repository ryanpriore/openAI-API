# write_codepy [language] [prompt] [filename]
# This python script will utilize the OpenAI API in order to generate code and save directly to disk.
# Last updated: March 19, 2023
# Author: Ryan Priore (ryan.priore@gmail.com)
#
# Inputs:
#     language: the programming language for OpenAI to use (c, matlab, python, or R)
#     prompt: the prompt to send to OpenAI API
#     filename: the filename of script or function to be written to disk w/o extension
# Example:
#     python3 write_code.py "python" "calculate the first 10 prime numbers" "prime"

import argparse
import openai
import os

# Define the input arguments
parser = argparse.ArgumentParser()
parser.add_argument("language", help="The programming language for OpenAI to use")
parser.add_argument("prompt", help="The prompt to send to OpenAI API")
parser.add_argument("filename", help="The filename of script or function to be written to disk w/o extension")
args = parser.parse_args()

# Determine scripting language (lang) and filename extension (ext)
match args.language.lower():
    case "c":
        lang = "C"
        ext = ".c"
    case "matlab":
        lang = "Matlab"
        ext = ".m"
    case "python":
        lang = "Python"
        ext = ".py"
    case "r":
        lang = "R"
        ext = ".R"

# Define remaining input arguments
prompt = f"Write a {lang} script or function to {args.prompt}. Provide comments in the code but no additional text."
filename = args.filename + ext

# Get OpenAI API key (Option #1): Import from environmental variable
#openai.api_key = os.getenv("OPENAI_API_KEY")
# Get OpenAI API key (Option #2): Import from text file
with open('api_key.txt', 'r') as file:
    openai.api_key = file.read().rstrip()

# Execute OpenAI API completion request and store response
response = openai.Completion.create(
    model = "text-davinci-003",
    prompt = prompt,
    max_tokens = 2000,
    temperature = 0.5
)

# Write file to disk
response_text = response.choices[0]["text"]
with open("output/" + filename, "w") as file:
    file.write(response_text)