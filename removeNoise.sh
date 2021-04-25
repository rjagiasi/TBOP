#!/bin/sh

#filter background noise
sox Data/Processed/trial.wav output.wav lowpass 7000

#filter and clip silence
sox audio_files_harvard.wav output.wav lowpass 7000 silence 1 0.75 0.1% 1 0.75 0.1%

#plot spectrogram
sox output.wav -n spectrogram
