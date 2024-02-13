# ADB Tool

## Overview
This script provides a simple command-line interface to interact with Android devices using ADB (Android Debug Bridge). It allows users to push files to a connected Android device and execute shell commands remotely.

## Usage
1. Make sure you have ADB installed on your system. If not, please install the Android SDK platform tools.
2. Connect your Android device to your computer via USB.
3. Run the script by executing `python pyadb.py` in your terminal.
4. Follow the prompts to select the connected device and enter the file path you want to transfer.
5. The script will transfer the file to the selected device and open it using a text viewer application.

## Requirements
- Python 3.x
- ADB (Android Debug Bridge)

## Note
- This script is designed for Windows operating systems. If you are using Linux or macOS, some commands and paths may need to be adjusted accordingly.
- Make sure your device is connected and USB debugging is enabled.
- The script will attempt to automatically detect ADB installation. If it fails, please ensure ADB is properly installed and added to your system's PATH.
