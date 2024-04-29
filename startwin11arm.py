import os

if not os.path.exists("/data/data/com.termux/files/home/startxfce4\_nethunter.sh"):
    os.system("wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/proot\_kali/startxfce4\_nethunter.sh")
    os.system("chmod +x startxfce4\_nethunter.sh")
    os.system("./startxfce4\_nethunter.sh")
else:
    os.system("./startxfce4\_nethunter.sh")
