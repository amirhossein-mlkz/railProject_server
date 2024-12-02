import re

class usernameManager:
    """
    A class to manage username operations including uniqueness checks, strength validation, and verification.
    """

    def __init__(self) -> None:
        """
        Initializes the usernameManager instance.
        """
        pass

    @staticmethod
    def is_unique(username: str, usernames: list, case_sensitive: bool = True) -> bool:
        """
        Checks if the given username is unique in the provided list of usernames.

        Args:
            username (str): The username to check.
            usernames (list): A list of existing usernames to compare against.
            case_sensitive (bool, optional): Specifies whether the uniqueness check should be case sensitive. Defaults to True.

        Returns:
            bool: True if the username is unique, False otherwise.
        """
        if not case_sensitive:
            usernames = list(map(lambda x: x.lower(), usernames))
            username = username.lower()

        return username not in usernames

    @staticmethod
    def check_username_strength(
            username: str,
            regex: str = None,
            min_length: int = 0,
            max_length: int = 0,
            allow_space: bool = True,
            allow_start_without_letter: bool = True,
            reserved_usernames: list = []
        ) -> bool:
        """
        Checks the strength and validity of a username based on various criteria.

        Args:
            username (str): The username to check.
            regex (str, optional): Regular expression pattern the username must match. Defaults to None.
            min_length (int, optional): Minimum length of the username. Defaults to 0.
            max_length (int, optional): Maximum length of the username. Defaults to 0.
            allow_space (bool, optional): Specifies if spaces are allowed in the username. Defaults to True.
            allow_start_without_letter (bool, optional): Specifies if the username can start with a non-letter character. Defaults to True.
            reserved_usernames (list, optional): A list of usernames that cannot be used. Defaults to an empty list.

        Returns:
            bool: True if the username meets all the criteria, False otherwise.
        """
        check = True

        if regex and not re.match(regex, username):
            check = False

        if len(username) < min_length or len(username) > max_length:
            check = False

        if not allow_space and " " in username:
            check = False

        if not allow_start_without_letter and len(username) > 0 and not username[0].isalpha():
            check = False

        if username in reserved_usernames:
            check = False

        return check
    
    @staticmethod
    def verify_username(username1: str, username2: str, case_sensitive: bool = True) -> bool:
        """
        Verifies if two usernames are identical, considering case sensitivity.

        Args:
            username1 (str): The first username to compare.
            username2 (str): The second username to compare.
            case_sensitive (bool, optional): Specifies whether the comparison should be case sensitive. Defaults to True.

        Returns:
            bool: True if both usernames match according to the case sensitivity setting, False otherwise.
        """
        if not case_sensitive:
            username1 = username1.lower()
            username2 = username2.lower()

        return username1 == username2
