import os
import requests
import time

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def download_file(file_url, destination):
    create_directory(os.path.dirname(destination))
    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()

        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {file_url}: {e}")

file_urls = [
    "<https://github.com/Alex460k/Windows-11-ARM/blob/main/installwin11arm.py>",
    "<https://github.com/Alex460k/Windows-11-ARM/blob/main/installwin11ntv.py>",
    "<https://github.com/Alex460k/Windows-11-ARM/blob/main/startwin11ntv.py>",
    "<https://github.com/Alex460k/Windows-11-ARM/blob/main/uninstallwin11ntv.py>",
    "<https://github.com/Alex460k/Windows-11-ARM/blob/main/startwin11arm.py>",
    "<https://github.com/Alex460k/Windows-11-ARM/blob/main/uninstallwin11arm.py>"
]

destinations = [
    "/data/data/com.termux/files/usr/win11arm/installwin11arm.py",
    "/data/data/com.termux/files/usr/win11arm/installwin11ntv.py",
    "/data/data/com.termux/files/usr/win11arm/uninstallwin11ntv.py",
    "/data/data/com.termux/files/usr/win11arm/startwin11ntv.py",
    "/data/data/com.termux/files/usr/win11arm/uninstallwin11arm.py",
    "/data/data/com.termux/files/usr/win11arm/startwin11arm.py"
]

for i in range(len(file_urls)):
    download_file(file_urls[i], destinations[i])
def main_menu():
    os.system("clear")
    print("\033[97m#########\033[92m#################\033[94m##############################\033[92m##################\033[94m##############################\033[97m#########")
    print("\033[92m##\033[94m██╗    ██╗ ██╗ ███╗   ██╗ ██████╗   ██████╗  ██╗    ██╗ ███████╗    ██╗  ██╗     █████╗  ██████╗  ███╗   ███╗\033[92m##")
    print("\033[94m##\033[94m██║    ██║ ██║ ████╗  ██║ ██╔══██╗ ██╔═══██╗ ██║    ██║ ██╔════╝   ███║ ███║    ██╔══██╗ ██╔══██╗ ████╗ ████║\033[94m##")
    print("\033[92m##\033[94m██║ █╗ ██║ ██║ ██╔██╗ ██║ ██║  ██║ ██║   ██║ ██║ █╗ ██║ ███████╗   ╚██║ ╚██║    ███████║ ██████╔╝ ██╔████╔██║\033[92m##")
    print("\033[94m##\033[94m██║███╗██║ ██║ ██║╚██╗██║ ██║  ██║ ██║   ██║ ██║███╗██║ ╚════██║    ██║  ██║    ██╔══██║ ██╔══██╗ ██║╚██╔╝██║\033[94m##")
    print("\033[92m##\033[94m╚███╔███╔╝ ██║ ██║ ╚████║ ██████╔╝ ╚██████╔╝ ╚███╔███╔╝ ███████║    ██║  ██║    ██║  ██║ ██║  ██║ ██║ ╚═╝ ██║\033[92m##")
    print("\033[94m##\033[94m ╚══╝╚══╝  ╚═╝ ╚═╝  ╚═══╝ ╚═════╝   ╚═════╝   ╚══╝╚══╝  ╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═╝  ╚═╝ ╚═╝     ╚═╝\033[94m##")
    print("\033[97m#########\033[92m#################\033[94m##############################\033[92m##################\033[94m##############################\033[97m#########")
    print("1. Install Windows 11")
    print("2. Uninstall Windows 11")
    print("3. Start Windows 11")
    print("4. Patch Notes")
    print("5. Exit")
    print("Enter your choice: ", end="")
    choice = input()
    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        print("Incorrect or empty option!")
        main_menu()
    elif choice == "1":
        print("1. Install Windows 11 ARM XFCE4")
        print("2. Install Windows 11 ARM Native")
        print("Enter your choice: ", end="")
        choice = input()
        if choice != "1" and choice != "2":
            print("Incorrect or empty option!")
            main_menu()
        elif choice == "1":
            print("\033[94mInstalling Windows 11 ARM XFCE4...")
            os.system("cd")
            os.system("mkdir kali-arm64")
            os.system("cd storage/downloads")
            os.system("mv win11arm.tar.gz /data/data/com.termux/files/home/kali-arm64")
            os.system("cd")
            os.system("cd kali-arm64")
            os.system("tar -xvzf /data/data/com.termux/files/home/kali-arm64/win11arm.tar.gz")
            os.system("wget -P /data/data/com.termux/files/home/win11arm/installwin11arm.py https://github.com/Alex460k/Windows-11-ARM/blob/main/installwin11arm.py")
            os.system("chmod +x /data/data/com.termux/files/home/win11arm/installwin11arm.py")
            os.system("python /data/data/com.termux/files/home/win11arm/installwin11arm.py")
            print("Succesfully Installed Windows 11 ARM XFCE4!")
            time.sleep(3)
            main_menu()
        elif choice == "2":
            print("\033[94mInstalling Windows 11 ARM Native...")
            os.system("cd")
            os.system("cd storage/downloads")
            os.system("tar -zxf win11ntv.tar.gz -C /data/data/com.termux/files/ --recursive-unlink --preserve-permissions")
            os.system("cd")
            os.system("wget -P /data/data/com.termux/files/home/win11arm/installwin11ntv.py https://github.com/Alex460k/Windows-11-ARM/blob/main/installwin11ntv.py")
            os.system("chmod +x /data/data/com.termux/files/home/win11arm/installwin11ntv.py")
            os.system("python /data/data/com.termux/files/home/win11arm/installwin11ntv.py")
            print("Succesfully Installed Windows 11 ARM Native!")
            time.sleep(3)
            main_menu()
    elif choice == "2":
        print("1. Uninstall Windows 11 ARM XFCE4")
        print("2. Uninstall Windows 11 ARM Native")
        print("Enter your choice: ", end="")
        choice = input()
        if choice != "1" and choice != "2":
            print("Incorrect or empty option!")
            main_menu()
        elif choice == "1":
            print("\033[94mUninstalling Windows 11 ARM XFCE4")
            if os.path.exists("python /data/data/com.termux/files/home/win11arm/uninstallwin11arm.py"):
                1 == 1
            else:
                os.system("wget https://github.com/Alex460k/Windows-11-ARM/blob/main/uninstallwin11arm.py -O /data/data/com.termux/files/home/win11arm/uninstallwin11arm.py")
                os.system("chmod +x /data/data/com.termux/files/home/win11arm/uninstallwin11arm.py")
                os.system("python /data/data/com.termux/files/home/win11arm/uninstallwin11arm.py")
            print("Succesfully Uninstalled Windows 11 ARM XFCE4!")
            main_menu()
        elif choice == "2":
            print("\033[94mUninstalling Windows 11 ARM Native...")
            if os.path.exists("python /data/data/com.termux/files/home/win11arm/uninstallwin11ntv.py"):
                1 == 1
            else:
                os.system("wget https://github.com/Alex460k/Windows-11-ARM/blob/main/uninstallwin11ntv.py -O /data/data/com.termux/files/home/win11arm/uninstallwin11ntv.py")
                os.system("chmod +x /data/data/com.termux/files/home/win11arm/uninstallwin11ntv.py")
                os.system("python /data/data/com.termux/files/home/win11arm/uninstallwin11ntv.py")
            print("Succesfully Uninstalled Windows 11 ARM Native!")
            
    elif choice == "3":
        print("1. Start Windows 11 ARM XFCE4")
        print("2. Start Windows 11 ARM Native")
        print("Enter your choice: ", end="")
        choice = input()
        if choice != "1" and choice != "2":
            print("Incorrect or empty option!")
            main_menu()
        elif choice == "1":
            print("\033[94mStarting Windows 11 ARM XFCE4...")
            if os.path.exists("python /data/data/com.termux/files/home/win11arm/startwin11arm.py"):
                1 == 1
            else:
                os.system("wget https://github.com/Alex460k/Windows-11-ARM/blob/main/startwin11arm.py -O /data/data/com.termux/files/home/win11arm/startwin11arm.py")
                os.system("chmod +x /data/data/com.termux/files/home/win11arm/startwin11arm.py")
                os.system("python /data/data/com.termux/files/home/win11arm/startwin11arm.py")
                print("Type 'exit' in terminal to stop")
                while True:
                    user_input = input(":")
                    if user_input == "exit":
                        main_menu()
        elif choice == "2":
            print("\033[94mStarting Windows 11 ARM Native...")
            if os.path.exists("python /data/data/com.termux/files/home/win11arm/startwin11ntv.py"):
                1 == 1
            else:
                os.system("wget https://github.com/Alex460k/Windows-11-ARM/blob/main/startwin11ntv.py -O /data/data/com.termux/files/home/win11arm/startwin11ntv.py")
                os.system("chmod +x /data/data/com.termux/files/home/win11arm/startwin11ntv.py")
                os.system("python /data/data/com.termux/files/home/win11arm/startwin11ntv.py")
                print("Type 'exit' in terminal to stop")
                while True:
                    user_input = input(":")
                    if user_input == "exit":
                        main_menu()
    elif choice == "4":
        print("\033[97mPatch Notes:")
        print("[+] https://github.com/Alex460k/Windows-11-ARM")
        print("[+] https://t.me/win11armchat")
        print("[+] https://t.me/win11arm")
        print("[+] https://github.com/LinuxDroidMaster")
    elif choice == "5":
        exit()
if __name__ == '__main__':
    main_menu()
