import os
import time
def required_packages():
    os.system("clear")
    print("[+] Checking if necessary packages are installed...")
    time.sleep(2)
    print("[+] Installing necessary packages, please wait...")
    os.system("pip install termcolor requests")
    os.system("apt-get install wget python -y")
    print("[+] All necessary packages are installed. You can now run the script")
if __name__ == '__main__':
    required_packages()
