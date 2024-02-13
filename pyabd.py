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
            output = subprocess.check_output([adbCommand, "adb"], stderr=subprocess.DEVNULL).decode().strip()
            return output if (output) else None
        except subprocess.CalledProcessError:
            return None
        
    def clearScreen(self):
        os.system("clear" if (os.name == "posix") else "cls")

    def isInstalled(self):
        return self.adbPath is not None
    
    def runADBCommand(self, command):
        subprocess.run([self.adbPath] + command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def getDevices(self):
        print("(+) Fetching connected devices...")
        time.sleep(1.5)
        self.clearScreen()

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
        self.manufacturer = self.getDeviceInfos()

    def getDeviceInfos(self):
        try:
            output = subprocess.check_output(["adb", "-s", self.serial, "shell", "getprop", "ro.product.manufacturer"], stderr=subprocess.DEVNULL).decode("utf-8").strip()
            manufacturer = output if (output) else "Unknown"
        except subprocess.CalledProcessError:
            manufacturer = "Unknown"
        
        """
        try:
            output = subprocess.check_output(["adb", "-s", self.serial, "shell", "getprop", "ro.product.model"], stderr=subprocess.DEVNULL).decode("utf-8").strip()
            model = output if (output) else "Unknown Model"
        except subprocess.CalledProcessError:
            model = "Unknown"
        """
        return manufacturer
    
    def isRooted(self):
        print("(+) Checking for ROOT access...")
        time.sleep(1.5)
        adbTool.clearScreen()

        try:
            output = subprocess.check_output(["adb", "-s", self.serial, "shell", "su", "-c", "echo", "Root"], stderr=subprocess.DEVNULL)
            return "Root" in output.decode("utf-8")
        except subprocess.CalledProcessError:
            return False
    
    def pushFile(self, localPath, devicePath):
        print("(+) Transferring content...")
        time.sleep(1.5)
        adbTool.clearScreen()

        subprocess.run(["adb", "-s", self.serial, "push", localPath, devicePath], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    def copyClipboardToFile(self, localPath):
        print("(+) Copying clipboard content to file...")
        time.sleep(1.5)
        adbTool.clearScreen()

        if (self.isRooted()):
            clipboardContent = subprocess.check_output(["adb", "-s", self.serial, "shell", "content", "query", "--uri", "content://clipboard/clip"]).decode("utf-8")
            clipboardContent = clipboardContent.strip()
        else:
            adbTool.clearScreen()
            print("(!) This fearures is coming soon. As right now, only rooted phones can use it.")
            time.sleep(1.5)

    def executeCommand(self, command):
        subprocess.run(["adb", "-s", self.serial, "shell", command], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if (__name__ == "__main__"):
    adbTool = ADBTool()

    if (not adbTool.isInstalled()):
        adbTool.clearScreen()
        print("(!) ADB is not installed. Please install the Android SDK platform tools.")
        time.sleep(1.5)
        sys.exit(1)
    
    devices = adbTool.getDevices()
    if (not devices):
        adbTool.clearScreen()
        print("(!) No devices detected. Please make sure any Android devices are connected to this computer.")
        time.sleep(1.5)
        sys.exit(1)
    
    print("[AVAILABLE DEVICES]:")
    for i, deviceSerial in enumerate(devices):
        device = Device(deviceSerial)
        print(f"[{i+1}]: {device.manufacturer} | {device.serial}")
    
    choice = input("\n(?) Enter the number of the device you want to use (default is 1): ")
    choice = int(choice) if (choice.isdigit() and 1 <= int(choice) <= len(devices)) else 1
    selectedDevices = Device(devices[choice - 1])
    adbTool.clearScreen()

    while (True):
        adbTool.clearScreen()
        print("[TRANSFER OPTIONS]")
        print("[1] PC to Phone")
        print("[2] Phone to PC")

        choice = input("\n(?) Select a valid option: ")
        adbTool.clearScreen()

        if (choice.lower() in ["1", "pc to phone", "pc"]):
            filePath = input("(?) Enter the file path to display (text/plain): ")
            adbTool.clearScreen()
            devicePath = "/mnt/sdcard/content.txt" if (selectedDevices.isRooted()) else "/data/local/tmp/content.txt"

            try:
                selectedDevices.pushFile(filePath, devicePath)
                selectedDevices.executeCommand(f"am start -a android.intent.action.VIEW -d file://{devicePath} -t text/plain")
            except Exception:
                adbTool.clearScreen()
                print(f"(!) Couldn't transfer file '{filePath}' to device '{selectedDevices.serial}'")
        elif (choice.lower() in ["2", "phone to pc", "phone"]):
            localPath = input("(?) Enter the local path on PC to save the clipboard: ")
            adbTool.clearScreen()

            try:
                selectedDevices.copyClipboardToFile(localPath)
            except subprocess.CalledProcessError as error:
                adbTool.clearScreen()
                print(f"(!) Couldn't copy clipboard content to '{localPath}'.")
                print(error)
                time.sleep(1000)
        else:
            adbTool.clearScreen()
            print("(!) Invalid option has been choosed.")
            time.sleep(1.5)
