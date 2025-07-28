import os
import subprocess
from imageio_ffmpeg import get_ffmpeg_exe

# Get path to FFmpeg executable
ffmpeg_path = get_ffmpeg_exe()

# Input and output folders
input_folder = "input_videos"
output_folder = "compressed_videos"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):  # Add formats if needed
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"compressed_{filename}")

        # Compress video using FFmpeg
        subprocess.run([
            ffmpeg_path,
            '-i', input_path,
            '-vcodec', 'libx264',
            '-crf', '25',   # Lower = better quality, larger = smaller file
            output_path
        ])

        print(f"✅ Compressed: {filename} → {output_path}")
