import os

if not os.path.exists("bash /data/data/com.termux/files/home/startxfce4\_nethunter.sh"):
    os.system("wget https://github.com/LinuxDroidMaster/Termux-Desktops/blob/main/scripts/proot_kali/startxfce4_nethunter.sh")
    os.system("chmod +x startxfce4_nethunter.sh")
    os.system("./startxfce4_nethunter.sh")
else:
    os.system("./startxfce4_nethunter.sh")
