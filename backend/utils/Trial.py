import os
import datetime
from cryptography.fernet import Fernet

class TrialManager:
    def __init__(self, trial_file="trial_date.enc", key_file="key.key", trial_days=30):
        self.trial_file = trial_file  # File to store trial information
        self.key_file = key_file      # File to store encryption key
        self.trial_days = trial_days  # Number of days for the trial
        self.cipher = Fernet(self.load_or_generate_key())

    def load_or_generate_key(self):
        """Load or generate a key for encryption."""
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as file:
                return file.read()
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as file:
            file.write(key)
        return key

    def initialize_trial(self):
        """Initialize the trial period."""
        current_date = datetime.date.today()
        trial_data = {
            "start_date": current_date.isoformat(),
            "last_check": current_date.isoformat()
        }
        encrypted_data = self.cipher.encrypt(str(trial_data).encode())
        with open(self.trial_file, "wb") as file:
            file.write(encrypted_data)
        return trial_data

    def load_trial_data(self):
        """Load trial data from the encrypted file."""
        if not os.path.exists(self.trial_file):
            return None
        with open(self.trial_file, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = self.cipher.decrypt(encrypted_data).decode()
            return eval(decrypted_data)  # Convert string back to dictionary
        except Exception as e:
            print("Error loading trial data:", e)
            return None

    def save_trial_data(self, trial_data):
        """Save trial data back to the encrypted file."""
        encrypted_data = self.cipher.encrypt(str(trial_data).encode())
        with open(self.trial_file, "wb") as file:
            file.write(encrypted_data)

    def check_trial(self):
        """Check if the trial period is active."""
        trial_data = self.load_trial_data()
        if trial_data is None:
            print("No trial data found. Initializing trial period.")
            trial_data = self.initialize_trial()

        start_date = datetime.date.fromisoformat(trial_data["start_date"])
        last_check = datetime.date.fromisoformat(trial_data["last_check"])
        current_date = datetime.date.today()

        # Check for system date tampering
        if current_date < last_check:
            print("System date tampering detected! Trial is invalid.")
            return False

        # Update last check date
        trial_data["last_check"] = current_date.isoformat()
        self.save_trial_data(trial_data)

        # Check trial expiration
        days_elapsed = (current_date - start_date).days
        if days_elapsed > self.trial_days:
            print("Trial period has expired.")
            return False

        print(f"Trial is active. Days remaining: {self.trial_days - days_elapsed}")
        return True

    def reset_trial(self):
        """Reset the trial period."""
        if os.path.exists(self.trial_file):
            os.remove(self.trial_file)  # Delete the trial file
            print("Trial has been reset. A new trial period will start on next check.")
        else:
            print("No trial data found to reset.")

# Example Usage
if __name__ == "__main__":
    trial_manager = TrialManager(trial_days=20)
    if trial_manager.check_trial():
        print("The software is running in trial mode.")
    else:
        print("Trial has expired. Please purchase the software.")
