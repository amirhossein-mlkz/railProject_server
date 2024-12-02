class Messages:
    """
    Contains constant strings used as messages throughout the application.
    These messages communicate various states and feedback to the user.
    """

    # Login messages
    LOGIN_SUCCESSFULLY = 'Login successful.'  # Message displayed when login is successful.
    INVALID_USERNAME = 'Invalid username.'  # Message displayed when the provided username does not meet validity criteria.
    INCORRECT_PASSWORD = 'Incorrect password.'  # Message displayed when the entered password is wrong.

    # Password management messages
    PASSWORD_CHANGED = 'Password changed successfully.'  # Message displayed when a password is changed successfully.
    UNMATCH_CONFIRM = 'Passwords do not match.'  # Message displayed when the password and confirmation password do not match.
    WEAK_PASSWORD = 'Weak password. Please strengthen.'  # Message displayed when the entered password does not meet the strength requirements.

    # Username management messages
    USERNAME_CHANGED = 'Username changed successfully.'  # Message displayed when a username is changed successfully.
    DUPLICATE_USERNAME = 'Username already in use.'  # Message displayed when the chosen username is already in use.
    WEAK_USERNAME = 'Weak username. Please strengthen.'  # Message displayed when the entered username does not meet the strength requirements.

    # Session messages
    LOGIN_FIRST = 'Please log in first.'  # Reminder message to login before accessing certain features.

    # General form messages
    EMPTY_FIELD = 'All fields are required.'  # Message displayed when required fields are left blank.

    # Signup messages
    SIGNUP_SUCCESSFULLY = 'Signup successful.'  # Message displayed when a user is signed up successfully.

    # User management messages
    CONFIRM_DELETE_USER_TITLE = 'Confirm User Deletion'  # Title for the confirmation dialog when deleting a user.
    CONFIRM_DELETE_USER_MESSAGE = 'Are you sure you want to delete this user?'  # Confirmation message when attempting to delete a user.
    
    USER_DELETED_SUCCESSFULLY = 'User deleted successfully.'  # Message displayed when a user is deleted successfully.
    USER_EDITED_SUCCESSFULLY = 'User details updated successfully.'  # Message displayed when user details are edited successfully.

    CONFIRM_LOGOUT_USER_TITLE = 'Confirm User Logout'  # Title for the confirmation dialog when logout.
    CONFIRM_LOGOUT_USER_MESSAGE = 'Are you sure you want to logout?'  # Confirmation message when attempting to logout.