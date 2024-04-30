import subprocess

if not os.path.exists("/data/data/com.termux/files/home/startxfce4_termux.sh"):
    subprocess.run(["wget", "https://raw.githubusercontent.com/LinuxDroidMaster/Termux-Desktops/main/scripts/termux_native/startxfce4_termux.sh"], shell=True)
    subprocess.run(["chmod", "+x", "startxfce4_termux.sh"], shell=True)
    subprocess.run(["./startxfce4_termux.sh"], shell=True)
else:
    subprocess.run(["./startxfce4_termux.sh"], shell=True)
