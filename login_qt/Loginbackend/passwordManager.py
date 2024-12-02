import bcrypt
import re

class passwordManager:
    """
    A class to manage password operations including checking password strength,
    scoring password strength, hashing passwords, and verifying passwords.
    """

    def __init__(self) -> None:
        """
        Initializes the passwordManager instance.
        """
        pass

    @staticmethod
    def check_password_strength(
            password: str,
            regex: str = None,
            min_length: int = 0,
            min_uppercases: int = 0,
            min_lowercases: int = 0,
            min_digits: int = 0,
            min_specialchars: int = 0
        ) -> bool:
        """
        Checks if the password meets the specified strength criteria.

        Args:
            password (str): The password to be checked.
            regex (str, optional): Regular expression pattern the password must match. Defaults to None.
            min_length (int, optional): Minimum length of the password. Defaults to 0.
            min_uppercases (int, optional): Minimum number of uppercase letters in the password. Defaults to 0.
            min_lowercases (int, optional): Minimum number of lowercase letters in the password. Defaults to 0.
            min_digits (int, optional): Minimum number of digits in the password. Defaults to 0.
            min_specialchars (int, optional): Minimum number of special characters in the password. Defaults to 0.

        Returns:
            bool: True if the password meets all the criteria, False otherwise.
        """
        check = True
        special_characters = r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        if regex and not re.match(regex, password):
            check = False

        if len(password) < min_length:
            check = False

        if sum(1 for char in password if char.isupper()) < min_uppercases:
            check = False

        if sum(1 for char in password if char.islower()) < min_lowercases:
            check = False

        if sum(1 for char in password if char.isdigit()) < min_digits:
            check = False

        if sum(1 for char in password if char in special_characters) < min_specialchars:
            check = False

        return check

    @staticmethod
    def score_password_strength(
            password: str,
            length_points: int = 1,
            uppercase_points: int = 2,
            lowercase_points: int = 2,
            digit_points: int = 2,
            special_char_points: int = 3
        ) -> int:
        """
        Calculates a score indicating the strength of the password based on various characteristics.

        Args:
            password (str): The password to score.
            length_points (int, optional): Points per character length of the password. Defaults to 1.
            uppercase_points (int, optional): Points per uppercase letter. Defaults to 2.
            lowercase_points (int, optional): Points per lowercase letter. Defaults to 2.
            digit_points (int, optional): Points per digit. Defaults to 2.
            special_char_points (int, optional): Points per special character. Defaults to 3.

        Returns:
            int: The calculated password strength score.
        """
        score = 0
        special_characters = r"!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

        score += len(password) * length_points
        score += sum(1 for char in password if char.isupper()) * uppercase_points
        score += sum(1 for char in password if char.islower()) * lowercase_points
        score += sum(1 for char in password if char.isdigit()) * digit_points
        score += sum(1 for char in password if char in special_characters) * special_char_points

        return score

    @staticmethod
    def confirm_password(password: str, confirm: str) -> bool:
        """
        Confirms if two given passwords match.

        Args:
            password (str): The original password.
            confirm (str): The confirmation password.

        Returns:
            bool: True if both passwords match, False otherwise.
        """
        return password == confirm

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hashes a password using bcrypt.

        Args:
            password (str): The password to hash.

        Returns:
            str: The hashed password as a string.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password.decode()

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        """
        Verifies a password against a hashed password.

        Args:
            password (str): The password to verify.
            hashed_password (str): The hashed password to check against.

        Returns:
            bool: True if the password matches the hashed password, False otherwise.
        """
        return bcrypt.checkpw(password.encode(), hashed_password.encode())
