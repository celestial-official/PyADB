import subprocess
import sys
import os
import time

class ADBTool:
    def __init__(self):
        self.adbPath = self.findADBPath()
    
    def findADBPath(self):
        adbCommand = "where" if (os.name == "nt") else "which"

        try:
            ouput = subprocess.check_output([adbCommand, "adb.exe"]).decode().strip()
            return ouput if (ouput) else None
        except subprocess.CalledProcessError:
            print("(!) Couldn't check for ADB.")
            time.sleep(1.5)
            return None

    def isInstalled(self):
        return self.adbPath is not None
    
    def runADBCommand(self, command):
        subprocess.run([self.adbPath] + command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def getDevices(self):
        print("(+) Fetching connected devices...")
        time.sleep(1.5)
        os.system("cls")

        devices = []

        try:
            output = subprocess.check_output([self.adbPath, "devices"], stderr=subprocess.DEVNULL).decode("utf-8").split("\n")[1:-2]
            devices = [line.split()[0] for line in output if ("device" in line)]
        except subprocess.CalledProcessError:
            print("(!) Couldn't fetch connected devices.")
            time.sleep(1.5)
            pass
        return devices
    
class Device:
    def __init__(self, serial):
        self.serial = serial
    
    def isRooted(self):
        print("(+) Checking for ROOT access...")
        time.sleep(1.5)
        os.system("cls")

        try:
            output = subprocess.check_output(["adb", "-s", self.serial, "shell", "su", "-c", "echo", "Root"], stderr=subprocess.DEVNULL)
            return "Root" in output.decode("utf-8")
        except subprocess.CalledProcessError:
            return False
    
    def pushFile(self, localPath, devicePath):
        print("(+) Transferring content...")
        time.sleep(1.5)
        os.system("cls")

        subprocess.run(["adb", "-s", self.serial, "push", localPath, devicePath], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def executeCommand(self, command):
        subprocess.run(["adb", "-s", self.serial, "shell", command], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if (__name__ == "__main__"):
    adbTool = ADBTool()

    if (not adbTool.isInstalled()):
        os.system("cls")
        print("(!) ADB is not installed. Please install the Android SDK platform tools.")
        time.sleep(1.5)
        sys.exit(1)
    
    devices = adbTool.getDevices()
    if (not devices):
        os.system("cls")
        print("(!) No devices detected. Please make sure any Android devices are connected to this computer.")
        time.sleep(1.5)
        sys.exit(1)
    
    print("[AVAILABLE DEVICES]:")
    for i, deviceSerial in enumerate(devices):
        print(f"[{i+1}]: {deviceSerial}")
    
    choice = input("(?) Enter the number of the device you want to use (default is 1): ")
    choice = int(choice) if (choice.isdigit() and 1 <= int(choice) <= len(devices)) else 1
    selectedDevices = Device(devices[choice - 1])
    os.system("cls")

    filePath = input("(?) Enter the file path to display (default is ./content.txt): ")
    devicePath = "/mnt/sdcard/content.txt" if (selectedDevices.isRooted()) else "/data/local/tmp/content.txt"

    selectedDevices.pushFile(filePath, devicePath)
    selectedDevices.executeCommand(f"am start -a android.intent.action.VIEW -d file://{devicePath} -t text/plain")
