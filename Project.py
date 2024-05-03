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
    os.system("cd /data/data/com.termux/files/home/Project/Win11-icon-theme")
    os.system("bash /data/data/com.termux/files/home/Project/install.sh")
    os.system("cd")
    os.system("clear")

def update():
    print("[+] Updating")
    os.system("pkg update")
    os.system("apt update -y")
    os.system("clear")

def uninstall():
    os.system("clear")
    print("[+] Uninstalling")
    os.system("pkg remove xfce4 xfce4-goodies chromium code-oss")
    os.system("pkg update")
    os.system("apt autoremove")
    os.system("clear")
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
    print("         ██╗    ██╗ ██╗ ███╗   ██╗  ██╗ ██╗")
    print("         ██║    ██║ ██║ ████╗  ██║ ███║███║")
    print("         ██║ █╗ ██║ ██║ ██╔██╗ ██║ ╚██║╚██║")
    print("         ██║███╗██║ ██║ ██║╚██╗██║  ██║ ██║")
    print("         ╚███╔███╔╝ ██║ ██║ ╚████║  ██║ ██║")
    print("          ╚══╝╚══╝  ╚═╝ ╚═╝  ╚═══╝  ╚═╝ ╚═╝")                                                                                                 
    print("         ==================================")
    print("1. Install")
    print("2. Uninstall")
    print("3. Update")
    print("4. Start")
    print("5. Exit")
    print("Enter your choice: ", end="")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
        print("Incorrect or empty option!")
        main_menu()
    if choice == "1":
        install()
        mobox()
        icon()
        main_menu()
    if choice == "2":
        uninstall()
        main_menu()
    if choice == "3":
        update()
        main_menu()
    if choice == "4":
        start()
        while True:
                user_input = input(":")
                if user_input == "exit":
                    os.system("clear")
                    main_menu()
    if choice == "5":
        exit()
if __name__ == '__main__':
    main_menu()
