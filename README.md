# ML with video observations of classroom teachers

An initial proof of concept that will take video data, create a proof of concept of how to observe and provide feedback to teachers with ML on some aspect of Language of Instruction, Language of Student Response, Communication Mode (reading, speaking, listening, writing-- what the teacher elicits from the students), or Activity Structures.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.

```bash
pip install SpeechRecognition

pip install langdetect

pip install moviepy

pip install pydub
```

## Pipeline
Sample command to run audio extraction tool:
Download a video file say sample_video.asf, and put the path of the input video file in the command below:

```python
python main.py -i "sample_video.asf"

python main.py -i path_of_the_video_file_to_be_tested
```
-i stands for input. It takes as argument the path of the video file to be tested.

## Architecture Diagram

![Alt text](tbop_architecture.png?raw=true "Title")

## Project Structure
```bash
.
├── Data
│   ├── Input
│   │   └── sampleVideo.mp4
│   ├── Output
│   │   └── output.csv
│   └── Processed
│       └── output.wav
├── README.md
├── Utils
│   ├── SplitAudio.py
│   ├── SplitAudio.pyc
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── __pycache__
│   │   ├── SplitAudio.cpython-37.pyc
│   │   ├── __init__.cpython-37.pyc
│   │   ├── extractAudio.cpython-37.pyc
│   │   └── speech_recognition.cpython-37.pyc
│   ├── extractAudio.py
│   ├── extractAudio.pyc
│   ├── speech_recognition.py
│   └── speech_recognition.pyc
├── after_noise_removal.png
├── audio_files_harvard.wav
├── before_noise_removal.png
├── documentation
│   └── Spring2021
│       ├── i0.pdf
│       └── i1.pdf
├── main.py
├── noise_removed_harvard.wav
├── removeNoise.sh
├── sample.wav
├── test_video.asf
```

## Pivotal tracker for the project
Pivotal tracker account: https://www.pivotaltracker.com/n/projects/2495399

