import subprocess
import ctypes

def enable_file_sharing():
    """Enable File and Printer Sharing on Windows 10."""
    try:
        # Enable Windows Firewall rules for File and Printer Sharing

        subprocess.run('netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=Yes', check=True, shell=True)
        print("File sharing has been enabled successfully.")


        
        # # Start the necessary services for file sharing

        # subprocess.run("sc config lanmanserver start= auto", check=True, shell=True)
        # subprocess.run("sc config lanmanworkstation start= auto", check=True, shell=True)
        
        # # Start the services if they are not already running
        # subprocess.run("net start lanmanserver", check=True, shell=True)
        # subprocess.run("net start lanmanworkstation", check=True, shell=True)

        return True
        

        
    except subprocess.CalledProcessError as e:
        print(f"Error enabling file sharing: {e}")
        return False

def run_as_admin(command):
    """Run a command as administrator."""
    try:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", "powershell", f"-Command {command}", None, 1
        )
        print(f"Command executed with admin privileges: {command}")
    except Exception as e:
        print(f"Failed to run command as admin: {e}")


def is_network_discovery_enabled():
    try:
        # Check if network discovery is enabled by checking the status of the firewall rule
        result = subprocess.run(
            ['powershell', '-Command', 'Get-NetFirewallRule -DisplayGroup "Network Discovery" | Select-Object -ExpandProperty Enabled'],
            capture_output=True, text=True, check=True
        )
        enabled_status = result.stdout.strip().split('\n')
        return any(status.strip().lower() == 'true' for status in enabled_status)

    except subprocess.CalledProcessError as e:
        print(f"Error checking network discovery status: {e}")
        return False

def enable_network_discovery():
    try:
        # Enable network discovery via PowerShell command
        subprocess.run(['powershell', '-Command', 'Enable-NetFirewallRule -DisplayGroup "Network Discovery"'], check=True)
        
        # Start the required services for network discovery
        subprocess.run(['powershell', '-Command', 'Start-Service -Name "FDResPub"'], check=True) # SSDP Discovery
        subprocess.run(['powershell', '-Command', 'Start-Service -Name "upnphost"'], check=True) # Universal Plug and Play

        print("Network discovery enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error enabling network discovery: {e}")

def ensure_network_discovery_enabled():
    try:
        if not is_network_discovery_enabled():
            msg = "Network discovery is not enabled. Enabling now..."
            # print(msg)
            enable_network_discovery()

            return msg

        else:
            msg = "Network discovery is already enabled."
            # print(msg)
            return msg
    except Exception as e:
        return e

if __name__ == "__main__":
    # Enable file sharing
    enable_file_sharing()


