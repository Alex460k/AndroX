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
    os.system("megadl -p /data/data/com.termux/files/usr/win11arm/win11armmainmenu.py https://mega.nz/file/jJ02AQAB#ckyS-XSmxR7nERothNKfZNo8wpCzKs_QcZWQwBdFAuM")
    os.system("chmod +x /data/data/com.termux/files/usr/win11arm/win11armmainmenu.py")
    os.system("megadl -p $PREFIX/bin https://mega.nz/file/mRU12SZI#309lDCcI0eiwC0MSGxL4n_BPvawPwx_rC6i4NAjZ49o")
    os.system("chmod +x $PREFIX/bin/win11arm")
    print("Type 'win11arm' in termux to start the script. ENJOY!")
if __name__ == '__main__':
    required_packages()
