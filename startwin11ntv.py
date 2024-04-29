import os

if not os.path.exists("/data/data/com.termux/files/home/startxfce4_termux.sh"):
    os.system("wget https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/termux_native/startxfce4_termux.sh")
    os.system("chmod +x startxfce4_termux.sh")
    os.system("./startxfce4_termux.sh")
else:
    os.system("./startxfce4_termux.sh")
