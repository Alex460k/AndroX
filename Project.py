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
    while True:
        print("Windows 11 Home")
        print("===============")
        print("1. Install")
        print("2. Uninstall")
        print("3. Update")
        print("4. Start")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            install()
            mobox()
            icon()
        elif choice == "2":
            uninstall()
        elif choice == "3":
            update()
        elif choice == "4":
            start()
            while True:
                user_input = input(":")
                if user_input == "exit":
                    break
        elif choice == "5":
            exit()
        else:
            print("Invalid choice, try again.")
if __name__ == '__main__':
    main_menu()
