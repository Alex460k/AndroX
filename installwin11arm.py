import os
import time
def linux():
    os.system("clear")
    print("Installing Linux, please wait...")
    print("When it will say what you want to install choose number 3 ( nano ) then enter N and then y ")
    print("DO NOT TYPE y after choosing number 3")
    print("Also need Internet!")
    time.sleep(2)
    os.system("termux-setup-storage ; pkg install wget ; wget -O install-nethunter-termux https://offs.ec/2MceZWr ; chmod +x install-nethunter-termux ; ./install-nethunter-termux")
    print("Instalation Succesfully, now you can start Windows 11 ARM XFCE4!")

if __name__ == '__main__':
    linux()
