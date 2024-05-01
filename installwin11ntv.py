import os
import time
os.system("clear")
print("Also need Internet!")
time.sleep(2)
os.system("termux-setup-storage")
os.system("cd")
os.system("cd storage/downloads")
os.system("tar -zxf win11ntv.tar.gz -C /data/data/com.termux/files/ --recursive-unlink --preserve-permissions")
os.system("cd")
os.system("wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/termux_native/mobox_run.sh ; chmod +x mobox_run.sh")
print("Instalation Succesfully, now you can start Windows 11 ARM Native!")
