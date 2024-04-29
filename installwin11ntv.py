import os
import time
def linux():
    os.system("clear")
    print("Also need Internet!")
    time.sleep(2)
    os.system("termux-setup-storage ; pkg install x11-repo ; pkg install termux-x11-nightly ; pkg install pulseaudio ; pkg install xfce4 xfce4-goodies ; pkg install tur-repo ; pkg update ; pkg install chromium code-oss ; wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/termux_native/mobox_run.sh ; chmod +x mobox_run.sh")
    print("Instalation Succesfully, now you can start Windows 11 ARM Native!")

if __name__ == '__main__':
    linux()
