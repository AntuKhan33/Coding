import subprocess

a = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="ignore").split('\n')
a = [i.split(":")[1][1:-1] for i in a if "All User Profile" in i]

with open("wifi_passwords.txt", "w") as f:
    for i in a:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="ignore").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                f.write("{:<30}|  {:<}\n".format(i, results[0]))
                
            except IndexError:
                f.write("{:<30}|  {:<}\n".format(i, ""))
        except subprocess.CalledProcessError:
            f.write("{:<30}|  {:<}\n".format(i, "ENCODING ERROR"))

print("WiFi passwords saved to wifi_passwords.txt")
