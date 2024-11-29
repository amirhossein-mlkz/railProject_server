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

if __name__ == "__main__":
    # Enable file sharing
    enable_file_sharing()
