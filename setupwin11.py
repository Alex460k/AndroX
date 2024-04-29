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
    os.system("wget -P /data/data/com.termux/files/usr/win11arm/ https://raw.githubusercontent.com/Alex460k/Windows-11-ARM/main/win11armmainmenu.py && cd /data/data/com.termux/files/usr/win11arm/Windows-11-ARM && mv /data/data/com.termux/files/usr/win11arm/Windows-11-ARM/win11armmainmenu.py /data/data/com.termux/files/usr/win11arm/")
    os.system("chmod +x /data/data/com.termux/files/usr/win11arm/win11armmainmenu.py")
    print("ENJOY!")
if __name__ == '__main__':
    required_packages()
