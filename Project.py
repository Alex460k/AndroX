import os
import time

def install():
    os.system("clear")
    print("[+] Installing Windows 11 Home packages")
    os.system("pkg update")
    os.system("pkg install x11-repo termux-x11-nightly")
    os.system("pkg install tur-repo")
    os.system("pkg update")
    os.system("pkg install git xfce4 xfce4-goodies chromium code-oss")
    print("[+] Installation done")
    time.sleep(2)

def icon():
    os.system("git clone https://github.com/yeyushengfan258/Win11-icon-theme")
    os.system("cd Win11-icon-theme")
    os.system("./install.sh")
    os.system("cd")

def update():
    print("[+] Updating")
    os.system("pkg update")
    os.system("apt update -y")

def uninstall():
    os.system("clear")
    print("[+] Uninstalling")
    os.system("pkg remove xfce4 xfce4-goodies chromium code-oss")
    os.system("pkg update")
    os.system("apt autoremove")
    time.sleep(2)

def exit():
    os.system("exit")

def start():
    os.system("bash /data/data/com.termux/files/home/Project/startxfce4_termux.sh")

def mobox():
    os.system("wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/termux_native/startxfce4_termux.sh")
    os.system("wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/termux_native/mobox_run.sh")
    os.system("chmod +x mobox_run.sh")
    os.system("chmod +x startxfce4_termux.sh")

def main_menu():
    print("Windows 11 Home")
    print("===============")
    print("1. Install")
    print("2. Uninstall")
    print("3. Update")
    print("4. Start")
    print("5. Exit")
    choice1="1"
    choice2="2"
    choice3="3"
    choice4="4"
    choice5="5"
    if choice1:
        install()
        mobox()
        icon()
        main_menu()
    if choice2:
        uninstall()
        main_menu()
    if choice3:
        update()
        main_menu()
    if choice4:
        start()
        while True:
            user_input = input(":")
            if user_input == "exit":
                main_menu()
    if choice5:
        exit()
if __name__ == '__main__':
    main_menu()
