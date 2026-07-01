<div align="center">

# Video to ASCII Converter (with Audio Sync)

This project converts any video file into live ASCII art — rendered directly in your terminal with synchronized audio playback.  
It maintains stable frame rates and sound sync using threaded execution and dynamic frame scaling.

</div>

---

## Overview

This script processes video files frame by frame, converts each frame to ASCII characters based on pixel brightness, and displays them in the terminal in real time.  
Audio is extracted and played in parallel using Python’s threading, ensuring synchronized playback without lag.

---

## Key Features

- Converts any video (`.mp4`, `.avi`, `.mkv`, `.mov`, etc.) into terminal ASCII  
- Synchronized audio playback using multithreading  
- Automatic terminal size detection and scaling  
- Smooth playback with accurate frame timing  
- No lag — maintains video FPS consistency  
- Cross-compatible with most standard video formats  

---

## Tech Stack

| Component | Purpose |
|------------|----------|
| **Python 3.10+** | Core language |
| **OpenCV** | Frame extraction and processing |
| **NumPy** | Brightness mapping and array math |
| **MoviePy** | Audio extraction |
| **Tkinter** | File selection GUI |
| **Winsound** | Audio playback on Windows |
| **Threading** | Concurrent audio and video rendering |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/JAIMNBIDU/video-to-ascii.git
cd video-to-ascii

Install the dependencies:
pip install opencv-python numpy moviepy

On Windows, winsound comes preinstalled.
For Linux or macOS, you can replace winsound with a platform-specific player like pydub or simpleaudio.

```
Run:
```
python video_to_ascii.py

A file dialog will appear — select your video file.
The video will then play in ASCII form directly in your terminal with audio.
```
## Configuration

| Variable | Description | Default |
|:----------|:-------------|:----------|
| `width` | Output ASCII width (auto-limited by terminal size) | `120` |
| `ASCII_CHARS` | Character gradient from dark → bright | `" .:-=+*#%@"` |
| `fps` | Automatically derived from input video | Detected |
| `time_per_frame` | Frame delay calculated as `1 / fps` | Dynamic |
| `temp_audio.wav` | Temporary audio extracted from video | Auto-generated |


```

# Working:
Video Selection
Opens a file dialog to select a video via tkinter.

Frame Processing
Extracts frames using OpenCV.
Converts each frame to grayscale.
Resizes frames based on terminal dimensions.
Maps brightness to ASCII symbols.

Audio Extraction
Uses MoviePy to extract the video’s audio track.
Writes it temporarily as a .wav file.
Plays it concurrently using a background thread.

Synchronized Playback
Displays frames with timed intervals (1 / fps).
Clears the terminal each frame to simulate motion.
Maintains audio-video sync via threading.
```
## Author
### Aryan (JAIMNBIDU)
Developed with Python, OpenCV, and a dangerously high caffeine tolerance.

## License:
Licensed under the MIT License — free for modification, reuse, and learning.




