# Description
A set of python functions for interacting with the OpenAI API
- create_image.py: request image and save directly to disk as a png file
- create_image_gui.py: request image and save directly to disk as a png file in a simple GUI
- write_code.py: request code (c, matlab, python, or R) script or function and save directly to disk

# Setup
## Get Your OpenAI API Key
You need an API key to make successful API calls. Sign up for the OpenAI API and create a new API key by clicking on the dropdown menu on your profile and selecting **View API keys**. Click on **Create new secret key** to create a new API key, and copy the value shown in the pop-up window. Keep this key secret! Copy the value of this key so you can later use it in your project as you will only see the key value once.

## Store Your OpenAI API Key locally
### Option 1: Environmental Variable
Make your OpenAI API key available to your Python scripts by using an environment variable.

On Linux machines:
```
export OPENAI_API_KEY="<your-key-value-here>"
```

On Windows machines:
```
$ENV:OPENAI_API_KEY = "<your-key-value-here>"
```

### Option 2: Store in Text File
Storing the OpenAI API key in a text file on your local machine allows the option for reading in the key when necessary.

## Install Necessary Python Libraries

## Create Output Directories
- code_output/
- image_output/