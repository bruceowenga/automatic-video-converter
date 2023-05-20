import os
import time
import moviepy.editor as mp
import shutil
import argparse
import configparser


def convert_to_wav(video_file, output_file):
    video = mp.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(output_file)


def convert_videos_in_directory(input_directory, output_directory, file_extensions):
    for root, dirs, files in os.walk(input_directory):
        relative_path = os.path.relpath(root, input_directory)
        output_folder = os.path.join(output_directory, relative_path)
        os.makedirs(output_folder, exist_ok=True)

        for file in files:
            if file.lower().endswith(tuple(file_extensions)):
                video_file = os.path.join(root, file)
                output_file = os.path.join(output_folder, os.path.splitext(file)[0] + ".wav")

                if not os.path.exists(output_file):
                    convert_to_wav(video_file, output_file)
                    print(f"Converted {video_file} to {output_file}")


def main(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)

    input_directory = config.get("General", "input_directory")
    output_directory = config.get("General", "output_directory")
    file_extensions = config.get("Conversion", "file_extensions").split(",")
    sleep_interval = config.getint("Monitoring", "sleep_interval")

    os.makedirs(output_directory, exist_ok=True)

    while True:
        for folder in os.listdir(input_directory):
            folder_path = os.path.join(input_directory, folder)
            if os.path.isdir(folder_path):
                output_folder_path = os.path.join(output_directory, folder)
                if not os.path.exists(output_folder_path):
                    shutil.copytree(folder_path, output_folder_path)
                convert_videos_in_directory(folder_path, output_folder_path, file_extensions)
        time.sleep(sleep_interval)  # Sleep for the specified interval before checking for new folders again


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automatic Video Converter")
    parser.add_argument("--config", help="Path to the configuration file", default="config.ini")
    args = parser.parse_args()

    main(args.config)
