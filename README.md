# TermWin11
[+] New Emulator that can run PC Games and Apps

[+] Developed by DeathGhost

[+] Telegram Channel: t.me/

Scripts form other Developers:

<LinuxDroidMaster | Start Command for TermWin11

<Mobox Developers | Wine Explorer for TermWin11

A big Thank You to these Developers for helping this Emulator work better and faster

# Updates 
- There will be new Updates every month

# Installation Tutorial
- The only way you'll be able to install it is to come to the group chat in Telegram and ask for script, then I will give you the steps to install the script
- Download it in termux and save it as: "setup.sh" then open termux and you will be automatically redirected to "downloads" folder.
- Copy/Paste this in termux:
```
 pkg install dos2unix && dos2unix setup.sh && bash setup.sh
```

# Signal 9 Error
 - First make sure that you disabled phantom process signal 9 in termux
 - To disable folow these steps:
     - Go to settings - About phone - System Information
     - Press 10 times consecutively on the "Build Number"
     - Exit About phone and type in Search Bar "Developer Options"
     - Scroll down till you get to Wireless Debugging - press 'ON' and 'Allow everytime on this network'
     - Open in split screen view with termux apk
     - In Termux apk enter this command:
       ```
       pkg install android-tools
       ```
     - Then in Settings select option to pair with code
     - Copy address and paste in termux like this:
       ```
       adb pair your address/port
       ```
     - Then enter pairing code shown in Settings app
     - Then copy address/port from the first option in Settings
     - Type in termux:
       ```
       adb connect your address/port
       ```
     - Then copy paste the commands in termux one after the other, from this link: https://kskroyal.com/disable-phantom-process-killer-in-android-12-13/
     - Then exit termux and enter again
