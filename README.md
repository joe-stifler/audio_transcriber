# Audio Transcriber

Audio Transcriber is toy wrapper around openai-whisper library, primary created to expose a simple terminal client to convert and transcribe audio files.

## Requirements

add the ffmpeg as one of the requirements followed by a install command in ubuntu

* **ffmpeg:**
```bash
    sudo apt-get install ffmpeg
```

* **[openai-whisper](https://github.com/openai/whisper)** and other python dependencies:


```bash
    conda env create -f environment.yml
    conda activate audio_transcriber
    pip install -r requirements.txt
```

## Installation

To install Audio Transcriber, run:

```bash
    pip install -e .
```

# Usage

## Command Line Interface
To convert and transcribe a file from the command line:

```
audio_transcriber your_file.mp4
```

# Python Module

To use Audio Transcriber in your Python code:

```
from audio_transcriber.transcriber import convert_audio, transcribe_audio

# Convert and optimize an audio file
convert_audio('path/to/your_file.mp4', 'path/to/output_file.mp3')

# Transcribe the audio file to text
transcribe_audio('path/to/output_file.mp3')
```

# Configuration

Audio Transcriber allows some configurations such as disabling audio optimizations and selecting output formats for transcriptions. See the full documentation for more details.

# Contributing
Contributions to Audio Transcriber are welcome. Please refer to the contributing guidelines for more information.

# License
Audio Transcriber is released under the MIT License. See the LICENSE file for more details.
