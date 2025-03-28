import subprocess
import pyfiglet
from pyfiglet import Figlet
# Function to run aircrack-ng command
def run_aircrack_ng(command):
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            print("Command output:\n", result.stdout)
        else:
            print("Error executing command:\n", result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage: run aircrack-ng to crack a WPA handshake file
def crack_wpa_handshake(wordlist, bssid, capture_file):
    command = f"aircrack-ng -w {wordlist} -b {bssid} {capture_file}"
    run_aircrack_ng(command)

# Example usage: capture packets (requires root privileges)
def capture_packets(interface, output_file):
    command = f"airodump-ng -w {output_file} --output-format cap {interface}"
    run_aircrack_ng(command)

# Main function
if __name__ == "__main__":
    # Example: Crack WPA handshake
    wordlist_path = "path/to/wordlist.txt"
    bssid = "00:11:22:33:44:55"
    capture_file = "path/to/captured_handshake.cap"
    crack_wpa_handshake(wordlist_path, bssid, capture_file)
    
    # Example: Capture packets (requires root privileges)
    interface = "wlan0"
    output_file = "path/to/output"
    capture_packets(interface, output_file)



f = Figlet(font='slant')
print(f.renderText('Gopalian'))
x = input("search for networks")
if x == "authenicate" {
run_aircrack_ng()

}
