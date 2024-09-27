import os
import subprocess
import shutil

CRD_SSH_Code = DISPLAY= /opt/google/chrome-remote-desktop/start-host --code="4/0AVG7fiRrNZjBi6Cwu94R_G0y7ZQl8-yMiyR6nEajERAqn-Ozh6qC5-R2nVlbziSXIuRy2w" --redirect-url="https://remotedesktop.google.com/_/oauthredirect" --name=$(hostname)
username = "user" #@param {type:"string"}
password = "root" #@param {type:"string"}
os.system(f"useradd -m {username}")
os.system(f"adduser {username} sudo")
os.system(f"echo '{username}:{password}' | sudo chpasswd")
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

Pin = 123456 #@param {type: "integer"}
Autostart = True #@param {type: "boolean"}

class CRDSetup:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChrome()
        self.finish(user)

    @staticmethod
    def installCRD():
        subprocess.run(['wget', 'https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['dpkg', '--install', 'chrome-remote-desktop_current_amd64.deb'])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Chrome Remoted Desktop Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installDesktopEnvironment():
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal")
        os.system("bash -c 'echo \"exec /etc/X11/Xsession /usr/bin/xfce4-session\" > /etc/chrome-remote-desktop-session'")
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("systemctl disable lightdm.service")
        print("Installed XFCE4 Desktop Environment !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    @staticmethod
    def installGoogleChrome():
        subprocess.run(["wget", "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb"])
        subprocess.run(["dpkg", "--install", "google-chrome-stable_current_amd64.deb"])
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'])
        print("Google Chrome Installed !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

Type=Application
Name=Colab
Exec=sh -c "sensible-browser {}"
Icon=
Comment=Open a predefined notebook at session signin.

            with open(f"/home/{user}/.config/autostart/colab.desktop", "w") as f:
                f.write(colab_autostart)
            os.system(f"chmod +x /home/{user}/.config/autostart/colab.desktop")
            os.system(f"chown {user}:{user} /home/{user}/.config")
            
        os.system(f"adduser {user} chrome-remote-desktop")
        command = f"{CRD_SSH_Code} --pin={Pin}"
        os.system(f"su - {user} -c '{command}'")
        os.system("service chrome-remote-desktop start")
        
        print("..........................................................") 
        print(".....Brought By The Disala................................") 
        print("..........................................................") 
        print("......#####...######...####....####...##.......####.......") 
        print("......##..##....##....##......##..##..##......##..##......")  
        print("......##..##....##.....####...######..##......######......") 
        print("......##..##....##........##..##..##..##......##..##......") 
        print("......#####...######...####...##..##..######..##..##......") 
        print("..........................................................") 
        print("..Youtube Video Tutorial - https://youtu.be/xqpCQCJXKxU ..") 
        print("..........................................................") 
        print("Log in PIN : 123456") 
        print("User Name : user") 
        print("User Pass : root") 
        while True:
            pass

try:
    if CRD_SSH_Code == "":
        print("Please enter authcode from the given link")
    elif len(str(Pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRDSetup(username)
except NameError as e:
    print("'username' variable not found, Create a user first")