import cv2
import numpy as np
import threading
import time
from moviepy import (VideoFileClip)
import tkinter as tk
from tkinter import filedialog
import os
import winsound


ASCII_CHARS = " .:-=+*#%@"

def resize_frame(frame, new_width=100):
    term_size = os.get_terminal_size()
    term_height = term_size.lines
    term_width = term_size.columns

    new_width = min(new_width, term_width)

    h, w = frame.shape
    ratio = h / w / 1.65
    new_height = int(new_width * ratio)

    if new_height > term_height - 2:
        new_height = term_height - 2
        new_width = int(new_height / ratio)

    return cv2.resize(frame, (new_width, new_height))

def frame_to_ascii(frame):
    indices = (frame.astype(np.int32) * len(ASCII_CHARS) // 256)
    ascii_rows = ["".join([ASCII_CHARS[i] for i in row]) for row in indices]
    return "\n".join(ascii_rows)

def preprocess_video(video_path, width=100):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise Exception("This video file cannot be opened (Invalid format...)")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS) or 24

    frames = []
    print("Processing video frames...")
    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = resize_frame(gray, width)
        frames.append(frame_to_ascii(resized))
    cap.release()
    return frames, fps

def play_audio(video_path):
    clip = VideoFileClip(video_path)
    audio_file = "temp_audio.wav"
    clip.audio.write_audiofile(audio_file, logger=None)
    winsound.PlaySound(audio_file, winsound.SND_FILENAME)
    os.remove(audio_file)

def play_ascii_video(video_path, width=100):
    frames, fps = preprocess_video(video_path, width)
    audio_thread = threading.Thread(target=play_audio, args=(video_path,), daemon=True)
    audio_thread.start()

    time_per_frame = 1 / fps
    print("Playing ASCII video...")
    for ascii_frame in frames:
        print("\033[H\033[J", end="")  # new line in terminal
        print(ascii_frame)
        time.sleep(time_per_frame)

def select_video_file():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(
        title="Select Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
    )
    return video_path

if __name__ == "__main__":
    video_path = select_video_file()
    if not video_path:
        print("No video selected. Exiting.")
    else:
        play_ascii_video(video_path, width=120)
