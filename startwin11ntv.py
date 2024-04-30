import os

if not os.path.exists("bash /data/data/com.termux/files/home/startxfce4_termux.sh"):
    os.system("wget https://github.com/LinuxDroidMaster/Termux-Desktops/blob/main/scripts/termux_native/startxfce4_termux.sh")
    os.system("chmod +x startxfce4_termux.sh")
    os.system("./startxfce4_termux.sh")
else:
    os.system("./startxfce4_termux.sh")
