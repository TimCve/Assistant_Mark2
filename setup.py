from setuptools import setup, find_packages

setup(
  name='Assistant',
  version='2.0',
  packages=find_packages(),
  install_requires=[
    "SpeechRecognition",
    "PyAudio"
  ]
)
