import datetime
import winreg


class TrialManager:
    def __init__(self, registry_path="Software\\railwayServer", trial_days=30):
        self.registry_path = registry_path
        self.trial_days = trial_days

    def save_to_registry(self, key_name, value):
        """Save a key-value pair in the registry."""
        try:
            registry_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, self.registry_path)
            winreg.SetValueEx(registry_key, key_name, 0, winreg.REG_SZ, value)
            winreg.CloseKey(registry_key)
        except WindowsError as e:
            print(f"Error writing to registry: {e}")

    def read_from_registry(self, key_name):
        """Read a value from the registry."""
        try:
            registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.registry_path, 0, winreg.KEY_READ)
            value, _ = winreg.QueryValueEx(registry_key, key_name)
            winreg.CloseKey(registry_key)
            return value
        except WindowsError:
            return None

    def initialize_trial(self):
        """Initialize trial period and save the start date in the registry."""
        current_date = datetime.date.today().isoformat()
        self.save_to_registry("start_date", current_date)
        self.save_to_registry("last_check", current_date)
        print("Trial initialized.")
        return current_date

    def check_trial(self):
        """Check if the trial period is still valid."""
        start_date_str = self.read_from_registry("start_date")
        last_check_str = self.read_from_registry("last_check")

        if not start_date_str or not last_check_str:
            print("No valid trial data found. Initializing trial.")
            start_date_str = self.initialize_trial()

        try:
            # Validate the start and last check dates
            start_date = datetime.date.fromisoformat(start_date_str)
            last_check = datetime.date.fromisoformat(last_check_str)
        except (ValueError, TypeError):
            print("Invalid trial data detected. Reinitializing trial.")
            start_date_str = self.initialize_trial()
            start_date = datetime.date.fromisoformat(start_date_str)
            last_check = datetime.date.fromisoformat(start_date_str)

        current_date = datetime.date.today()

        # Detect tampering with system date
        if current_date < last_check:
            print("System date tampering detected! Trial is invalid.")
            return False

        # Update last check date
        self.save_to_registry("last_check", current_date.isoformat())

        # Calculate days elapsed
        days_elapsed = (current_date - start_date).days
        if days_elapsed > self.trial_days:
            print("Trial period has expired.")
            return False

        remaining_days = self.trial_days - days_elapsed
        print(f"Trial is active. Days remaining: {remaining_days}")
        return True

    def reset_trial(self):
        """Reset the trial period by clearing the registry data."""
        try:
            winreg.DeleteKey(winreg.HKEY_CURRENT_USER, self.registry_path)
            print("Trial has been reset. A new trial period will start on the next check.")
        except WindowsError:
            print("No trial data found to reset.")


# Example Usage
if __name__ == "__main__":
    trial_manager = TrialManager(trial_days=30)
    
    # Check trial
    if trial_manager.check_trial():
        print("The software is running in trial mode.")
    else:
        print("Trial has expired. Please purchase the software.")
    
    # Uncomment to reset trial for testing
    # trial_manager.reset_trial()
