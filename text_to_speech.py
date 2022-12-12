#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 20:00:01 2022

@author: paulo
"""

from gtts import gTTS
import os
import docx

doc = docx.Document(r"/home/paulo/Documents/PhD/own papers/mike paper/Mike MGF Paper 2_v12.docx")
result = [p.text for p in doc.paragraphs]
# mytext = "Hi, this is an example of converting text to audio. This is a bot speaking here, not a real human!"

cleanr = ' '.join([a for a in [('').join(a.split('\t')) for a in result] if a != ''])

audio = gTTS(text=cleanr, lang="en", slow=False)

audio.save("example.mp3")

# os.system("start example.mp3")