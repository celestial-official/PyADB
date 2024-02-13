# 📱 ADB Tool

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![ADB version](https://img.shields.io/badge/ADB%20version-Latest-brightgreen.svg)

## Overview

A simple command-line tool for interacting with Android devices using ADB (Android Debug Bridge). This tool allows users to push files to connected Android devices and execute shell commands remotely.

## Quick Start

1. **Install ADB:** Make sure you have ADB installed on your system. If not, install the [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools) which includes ADB.
  
2. **Connect Device:** Connect your Android device to your computer via USB and enable USB debugging.

3. **Run Script:** Open a terminal and navigate to the directory containing `pyabd.py`, then execute the following command:
   ```bash
   python pyabd.py
   ```

4. **Follow Prompts:** Follow the prompts to select the connected device and enter the file path you want to transfer.

5. **Enjoy:** Sit back and watch as the script transfers the file to your device and opens it using a text viewer application.

## Requirements

- Python 3.x
- ADB (Android Debug Bridge)

## Features

- Push files to connected Android devices.
- Execute shell commands remotely.
- Automatic detection of ADB installation.
- Error handling for ADB commands and device operations.

## Note

- This script is designed for Windows operating systems. If you are using Linux or macOS, some commands and paths may need to be adjusted accordingly.
- Make sure your device is connected and USB debugging is enabled.
- If ADB is not automatically detected, ensure it is properly installed and added to your system's PATH.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
