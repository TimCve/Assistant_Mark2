# Python Virtual Assistant Mark 2 #

### Setup instructions ###
- Clone this repository
- Create a python virtual environment in a folder inside of the repository with the following command:
```
$ virtualenv venv
```
- Activate the virtual environment:
```
$ source ./venv/bin/activate # for linux & mac
$ .\venv\Scripts\activate # for Windows
```
- Install the 'Assistant' package in editable mode by running this command in the root directory of your project (the directory where the setup.py file is):
```
$ pip install -e .
```
- Note to Windows users, the PyAudio package will likely fail to install, you have to go and download the whl file for PyAudio manually, and install it by simply running:
```
$ pip install .\PyAudio-whatever.version.you_need.whl 
```
(I have included the file for python 3.8 in the repository)
- Finally, you will need to create a file called conf.py in the config directory in 'Assistant', here is the syntax for that file:
```
# MAKE SURE TO TUNE THE SETTINGS TO YOUR NEEDS, THESE ARE TUNED SPECIFICALLY TO *MY* SETUP
# mic settings 
mic_index = 0
energy_threshhold = 500
non_speaking_duration = 0.1
pause_threshold = 0.1
```
(this will be updated every time there are new configs, the reason I don't include this file is because eventually there will be private API keys in there that can only be used by me)