# PACKAGES REQUIRED:
# - PyAudio
# - SpeechRecognition

import speech_recognition as sr

# import settings from conf.py
from Assistant.config.conf import mic_index, energy_threshhold, non_speaking_duration, pause_threshold

# prints out all the available microphones, useful for debugging
counter = 0
for mic in sr.Microphone.list_microphone_names():
  print("device index: [", counter, "] " + mic)
  counter += 1

# function that recognizes voice in audio going into the mic
def recognize_voice():
  # create Recognizer instance
  r = sr.Recognizer()
  # set up microphone to be the source
  with sr.Microphone(device_index=mic_index) as source:
    # self explanatory settings for mic
    # values are in conf.py
    r.energy_threshold = energy_threshhold
    r.non_speaking_duration = non_speaking_duration
    r.pause_threshold = pause_threshold

    # initiate listening
    print("*** listening ***")
    audio = r.listen(source)

  # attempt to print out whatever was recognized and handle any errors that may come up
  try:
      print(r.recognize_google(audio))
  except sr.UnknownValueError:
      pass
  except sr.RequestError as e:
      print("Could not request results; {0}".format(e))