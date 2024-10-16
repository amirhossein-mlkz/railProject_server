class Keys:
    """
    Holds constant keys used for form fields and attribute names within the application.
    """

    DATABASE_PATH = r'C:\Users\milad\Desktop\PythonWork\RailWay\railProject_server\data.db'

    USERNAME_KEY = 'username'
    PASSWORD_KEY = 'password'
    ROLE_KEY = 'role'
    CURRENT_PASSWORD_KEY = 'current_password'
    NEW_PASSWORD_KEY = 'new_password'
    CONFIRM_PASSWORD_KEY = 'confirm_password'
    NEW_USERNAME_KEY = 'new_username'

class ReservedPassword:
    """
    Contains constants for reserved passwords or password placeholders.
    """
    RESERVED_PASSWORD = '•' * 8  # Represents a masked password typically used in UI display.
    
class UIPages:
    """
    Enumerates the indices of different pages or views within the application UI.
    """
    MENU = 0 # The menu page index.
    LOGIN = 1  # The login page index.
    CHANGE_PASSWORD = 2  # The change password page index.
    CHANGE_USERNAME = 3  # The change username page index.
    ALL_USERS = 4  # The page index for viewing all users.
    SIGNUP = 5  # The signup page index.

class RefreshRates:
    """
    Defines refresh rates for UI updates in seconds or fractional seconds.
    """
    WINDOW_MOVE = 0.01  # Refresh rate for moving windows or animations.
    MESSAGES_TIME = 2  # Time interval for showing temporary messages.

class MessagesLevels:
    """
    Specifies the severity levels for messages displayed in the UI.
    """
    INFO = 1  # Informational messages.
    WARNING = 2  # Warning messages.
    ERROR = 3  # Error messages.

class PasswordStrength:
    """
    Defines the criteria for password strength within the application.
    """
    REGEX = '' # Regular expression pattern the password must match.
    MIN_LENGTH = 6  # Minimum length of passwords.
    MIN_UPPERCASES = 1  # Minimum number of uppercase characters required in passwords.
    MIN_LOWERCASES = 1  # Minimum number of lowercase characters required in passwords.
    MIN_DIGITS = 0  # Minimum number of digits required in passwords.
    MIN_SPECIALCHARS = 0  # Minimum number of special characters required in passwords.

class UsernameStrength:
    """
    Defines the criteria for username strength and validation within the application.
    """
    REGEX = '' # Regular expression pattern the username must match.
    MIN_LENGHT = 4  # Minimum length of usernames.
    MAX_LENGTH = 10  # Maximum allowable length of usernames.
    ALLOW_SPACE = True  # Specifies whether spaces are allowed in usernames.
    ALLOW_START_WITHOUT_LETTER = False  # Specifies whether usernames can start with a non-letter character.
    RESERVED_USERNAMES = ['Userame']  # List of reserved usernames not allowed for use.

class Roles:
    """
    Defines different roles available within the application.
    """
    ADMIN = 'Admin'  # Represents an administrative user.
    USER = 'User'  # Represents a standard user.
