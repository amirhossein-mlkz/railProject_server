import ctypes
import sys
import os

def run_as_admin():
    """Request admin privileges using UAC."""
    params = " ".join(f'"{arg}"' for arg in sys.argv)
    try:
        result = ctypes.windll.shell32.ShellExecuteW(
            None,  # Parent window handle (None for no window)
            "runas",  # Action: run as administrator
            sys.executable,  # Executable path (python.exe)
            params,  # Arguments (the script and its parameters)
            None,  # Default directory (None for current)
            1  # Show the window in normal mode
        )

        if result <= 32:
            raise Exception(f"ShellExecuteW failed with error code {result}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def create_system_file():
    """Try to create a file in a protected directory."""
    try:
        # Try to write to a protected system folder
        file_path = r"C:\Windows\System32\admin_test.txt"
        with open(file_path, "w") as f:
            f.write("Admin access successful!")
        print(f"Successfully created file at {file_path}")
    except PermissionError:
        print("PermissionError: You need admin access to write to this directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Checking admin status...")

    # Check if we are running as an admin
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Not admin. Requesting access...")
        if run_as_admin():
            print("Re-launching as admin. Please wait...")
            sys.exit(0)  # Exit the current instance to let the admin instance run
        else:
            print("Failed to obtain admin privileges. Continuing without admin rights.")
    else:
        print("Running as administrator!")

    # Perform admin-required tasks
    create_system_file()

    # Continue with application logic
    print("The app will now continue running...")
    while True:
        user_input = input("Type 'exit' to quit the application: ")
        if user_input.lower() == "exit":
            print("Exiting the application...")
            break
