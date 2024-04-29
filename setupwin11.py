import os
import time
def required_packages():
    os.system("clear")
    print("[+] Checking if necessary packages are installed...")
    time.sleep(2)
    print("[+] Installing necessary packages, please wait...")
    os.system("pip install termcolor")
    os.system("apt-get install megatools wget python")
    print("[+] All necessary packages are installed. You can now run the script")
    os.system("megadl https://mega.nz/file/yJdk1ByR#M6hz2PuCHYxzySHzD9g_rW4zcw3nmkM9W8aacf6cdZ0 -p /data/data/com.termux/files/usr/win11arm/win11armmainmenu.py")
    os.system("chmod +x /data/data/com.termux/files/usr/win11arm/win11armmainmenu.py")
    os.system("python /data/data/com.termux/files/usr/win11arm/win11armmainmenu.py")
if __name__ == '__main__':
    required_packages()
