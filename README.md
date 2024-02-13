# 📱 PyADB

![Made with Python](https://img.shields.io/badge/Made%20with-Python-blue.svg)
![ADB version](https://img.shields.io/badge/ADB%20version-Latest-brightgreen.svg)

## 🚀 Overview

PyADB is a command-line utility for interacting with Android devices using ADB (Android Debug Bridge). Simplify tasks such as pushing files to connected devices and executing shell commands remotely.

## ✨ Features

- Copy the clipboard content of the PC to the selected device.
- Execute shell commands remotely.
- Automatic detection of ADB installation.
- Error handling for ADB commands and device operations.
- **Safe to Use:** PyADB has been scanned for malware, and the results on [VirusTotal](https://www.virustotal.com/gui/file/f1cd3811c25154ade9e978303add8b8f6ce27b64b8b175bef526d320d163e949/detection) confirm its safety.

## 🚀 Quick Start

1. **Install ADB:** Ensure that ADB is installed on your system. If not, you can install the [Android SDK Platform Tools](https://developer.android.com/studio/releases/platform-tools), which includes ADB.

2. **Connect Device:** Connect your Android device to your computer via USB and enable USB debugging.

3. **Run Script:** Open a terminal and navigate to the directory containing `pyadb.py`, then execute the following command:
   `python pyadb.py`

4. **Follow Prompts:** Follow the prompts to select the connected device and enter the file path you want to transfer.

5. **Enjoy:** Sit back and watch as the script transfers the clipboard content of your PC to your device.

## 🛠️ Requirements

- Python 3.x
- ADB (Android Debug Bridge)

## 💡 Note

- This script is designed for Windows operating systems. If you are using Linux or macOS, some commands and paths may need to be adjusted accordingly.
- Make sure your device is connected and USB debugging is enabled.
- If ADB is not automatically detected, ensure it is properly installed and added to your system's PATH.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have suggestions for improvements.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
