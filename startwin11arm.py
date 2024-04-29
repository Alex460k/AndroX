import os

if not os.path.exists("/data/data/com.termux/files/home/startxfce4_nethunter.sh"):
    os.system("wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/proot_kali/startxfce4_nethunter.sh")
    os.system("chmod +x startxfce4_nethunter.sh")
    os.system("./startxfce4_nethunter.sh")
else:
    os.system("./startxfce4_nethunter.sh")
