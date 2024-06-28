"""This module is an example of using pyaudio to make a prediction on
audio wav data. 
https://pytorch.org/audio/stable/tutorials/audio_io_tutorial.html"""

# Import modules and download assets

import io
import os
import tarfile
import tempfile

import boto3
import matplotlib.pyplot as plt
import requests
from botocore import UNSIGNED
from botocore.config import Config
from botocore.display import Audio
from torchaudio.utils import download_asset

import sys

sys.path.insert(0, 
                os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

SAMPLE_GSM = download_asset("tutorial-assets/steam-train-whistle-daniel_simon.gsm")
SAMPLE_WAV = download_asset("tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042.wav")
SAMPLE_WAV_8000 = download_asset("tutorial-assets/Lab41-SRI-VOiCES-src-sp0307-ch127535-sg0042-8000hz.wav")

def _hide_seek(obj):
    class _wrapper:
        def __init__(self, obj):
            self.obj = obj

        def read(self, n):
            return self.obj.read(n)

    return _wrapper(obj)
