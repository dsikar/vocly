# Conversational AI

A work-in-progress project to create a conversational AI using OpenAI's ChatGPT and Google Cloud's Voice-to-Text and Text-to-Voice services.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Workflow](#workflow)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)

## Requirements

1. OpenAI API key
2. Google Cloud Voice-to-Text API key
3. Google Cloud Text-to-Voice API key

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd conversational-ai
   ```

3. Install the required packages (assuming you have `pip` and `virtualenv` installed):
   ```bash
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Set up your API keys:
   - OpenAI API key: Set as an environment variable or directly in the `text-to-chatgpt.py` script.
   - Google Cloud Voice-to-Text and Text-to-Voice API keys: Download the `.json` key files and set their paths in the respective scripts.
  
5. Create your virtual environment
```
# Download pyenv directly into the correct location
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
# Modify your .bashrc file, add the following lines to the bottonm of the .bashrc file

export PYENV_ROOT="$HOME/.pyenv"
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Reread .bashrc by running
exec bash

# install required libraries
sudo apt-get install -y build-essential libffi-dev libssl-dev zlib1g-dev liblzma-dev libbz2-dev libreadline-dev libsqlite3-dev

# install python 3.9.5
pyenv install 3.9.5

# create a virtual environment
pyenv virtualenv 3.9.5 myenv

# create the virtual environment in the repo top level directory
echo myenv > .python-version

# prompt should now be prefixed with (myenv)
# check the correct version is installed
python --version

# additional update pip
python -m pip install --upgrade pip

# add setuptools and wheel
pip install --upgrade pip setuptools wheel

# install pyaudio
sudo apt install python3-pyaudio

# install required modules
pip install -r requirements.txt
```

## Workflow

```
  +-------------+         +----------------+         +------------------+         +--------------+
  |  record.py  | ------> | voice-to-text.py | ------> | text-to-chatgpt.py | ------> | text-to-voice.py |
  +-------------+         +----------------+         +------------------+         +--------------+
```

1. **record.py**: Records user's voice input and saves it as an audio file.
2. **voice-to-text.py**: Converts the recorded audio to text using Google Cloud's Voice-to-Text API.
3. **text-to-chatgpt.py**: Sends the text to ChatGPT using the OpenAI API and gets a textual response.
4. **text-to-voice.py**: Converts the ChatGPT response to audio using Google Cloud's Text-to-Voice API.

## Usage

1. Start by recording your voice:
   ```bash
   python record.py
   ```

2. Convert the recorded audio to text:
   ```bash
   python voice-to-text.py
   ```

3. Send the text to ChatGPT and get a response:
   ```bash
   python text-to-chatgpt.py
   ```

4. Convert the ChatGPT response to audio:
   ```bash
   python text-to-voice.py
   ```

## Future Enhancements

- Integration with a frontend for a seamless user experience.
- Adding real-time processing capabilities.
- Incorporating more advanced conversational models and fine-tuning with domain-specific data.

--- 

