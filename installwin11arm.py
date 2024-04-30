import os
import time

os.system("clear")
print("Installing Linux, please wait...")
print("When it will say what you want to install choose number 3 (nano) then enter N and then y")
print("DO NOT TYPE y after choosing number 3")
print("Also need Internet!")
time.sleep(2)
os.system("mkdir kali-arm64")
os.system("cd")
os.system("cd storage/downloads")
os.system("mv win11arm.tar.gz /data/data/com.termux/files/home/kali-arm64")
os.system("cd")
os.system("cd kali-arm64")
os.system("tar -xvzf /data/data/com.termux/files/home/kali-arm64/win11arm.tar.gz")
os.system("termux-setup-storage ; pkg install wget ; wget -O install-nethunter-termux https://offs.ec/2MceZWr ; chmod +x install-nethunter-termux ; ./install-nethunter-termux")
print("Installation Succesfully, now you can start Windows 11 ARM XFCE4!")
