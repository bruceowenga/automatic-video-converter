# Automatic Video Converter

The Automatic Video Converter is a Python script that converts video files to audio files in the WAV format. It monitors a specified directory for new video files, automatically converts them to audio, and saves the converted files in a separate directory with the same folder structure as the input directory.

## Features

- Converts video files (MP4, MKV) to audio files (WAV).
- Monitors a specified directory for new video files and automatically converts them.
- Preserves the folder structure of the input directory in the output directory.
- Skips conversion if the corresponding output file already exists.

## Requirements
All requirements are included in the `requirements.txt` file and can be installed using `pip install -r requirements.txt` 
However the main ones are as below:

- Python 3.x
- MoviePy library (install with `pip install moviepy`) 

## Usage

1. Clone the repository or download the script file to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Open the script file `config.ini` in a text editor.
4. Update the `input_directory` and `output_directory` variables with your desired paths.
5. (Optional) Customize the sleep duration in seconds in the `time.sleep()` function to adjust the interval for checking new folders.
6. Run the script with `python automatic-video-converter.py`.
7. The script will continuously monitor the input directory for new folders. When a new folder is found, it checks for video files and converts them to audio files in the output directory.
8. Converted files will be saved in the output directory with the same folder structure as the input directory.

## Configuration

You can modify the behavior of the script by changing the following variables in the script:

- `input_directory`: The directory to monitor for new folders containing video files.
- `output_directory`: The directory to save the converted audio files.
- `sleep_duration`: The duration in seconds to wait between checking for new folders (default: 300 seconds or 5 minutes).

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and distribute the code according to the terms of the license.

## Contributing

Contributions to the project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Disclaimer

Please note that this script is provided as-is without any warranty. Use it at your own risk.

