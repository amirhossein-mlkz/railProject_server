from typing import Callable

from backend.usernameManager import usernameManager
from backend.passwordManager import passwordManager
from Constants import Constants
from Constants.Messages import Messages 
from userProfile_UI import (
    userProfile_UI,
    pagesUI,
    loginUI,
    changePasswordUI,
    changeUsernameUI,
    allUsersUI,
    signupUI,
    menuUI
)

class userProfile_API:
    """
    Manages the backend interactions for the userProfile_UI by providing API functionalities
    for various user profile operations including loading, updating, adding, and deleting users.
    """

    def __init__(self, 
            ui_handler: userProfile_UI,
            load_user_func: Callable[[str], list[dict]],
            update_user_func: Callable[[dict], None],
            load_all_users_func: Callable[[None], list[dict]],
            add_user_func: Callable[[dict], None],
            delete_user_func: Callable[[str], None],
        ) -> None:
        """
        Initializes the userProfile_API class with specific API callbacks and sets up necessary UI interactions.

        Args:
            ui_handler (userProfile_UI): The main user interface handler for the profile management system.
            load_user_func (Callable[[str], list[dict]]): Function to load user details by username.
            update_user_func (Callable[[dict], None]): Function to update user details.
            load_all_users_func (Callable[[], list[dict]]): Function to load all user profiles.
            add_user_func (Callable[[dict], None]): Function to add a new user profile.
            delete_user_func (Callable[[str], None]): Function to delete a user profile.
        """
        self.ui_handler = ui_handler

        self.__define_pages_api_obj(load_user_func, update_user_func, load_all_users_func, add_user_func, delete_user_func)
        self.__set_get_logined_user_callback()
        self.__set_set_logined_user_callback()

        self.ui_handler.set_change_page_external_callback(self.change_page)

    def __define_pages_api_obj(self, 
                               load_user_func: Callable[[str], list[dict]],
                               update_user_func: Callable[[dict], None],
                               load_all_users_func: Callable[[None], list[dict]],
                               add_user_func: Callable[[dict], None],
                               delete_user_func: Callable[[str], None]
                              ) -> None:
        """
        Defines and initializes API objects for different pages of the user profile management system.

        Args:
            load_user_func (Callable[[str], list[dict]]): Function to load user details by username.
            update_user_func (Callable[[dict], None]): Function to update user details.
            load_all_users_func (Callable[[], list[dict]]): Function to load all user profiles.
            add_user_func (Callable[[dict], None]): Function to add a new user profile.
            delete_user_func (Callable[[str], None]): Function to delete a user profile.
        """
        self.menu_api = menuAPI(self.ui_handler.menu_ui)
        self.login_api = loginAPI(self.ui_handler.login_ui, load_user_func)
        self.change_password_api = changePasswordAPI(self.ui_handler.change_password_ui, load_user_func, update_user_func)
        self.change_username_api = changeUsernameAPI(self.ui_handler.change_username_ui, load_user_func, update_user_func, load_all_users_func)
        self.all_users_api = allUsersAPI(self.ui_handler.all_users_ui, load_all_users_func, delete_user_func, update_user_func)
        self.signup_api = signupAPI(self.ui_handler.signup_ui, load_all_users_func, add_user_func)

    def __set_get_logined_user_callback(self):
        """
        Sets the callbacks to get the currently logged-in user's info for various operations.
        """
        self.change_password_api.set_get_logined_user_callback(self.get_logined_user)
        self.change_username_api.set_get_logined_user_callback(self.get_logined_user)
        self.all_users_api.set_get_logined_user_callback(self.get_logined_user)

    def __set_set_logined_user_callback(self):
        """
        Sets the callbacks to update the internally tracked logged-in user's info following login, logout or username changes.
        """
        self.menu_api.set_set_logined_user_callback(self.set_logined_user)
        self.login_api.set_set_logined_user_callback(self.set_logined_user)
        self.change_username_api.set_set_logined_user_callback(self.set_logined_user)

    def is_logined(self) -> bool:
        """Check whether any user loged-in or not.

        Returns:
            bool: True if any user loged-in.
        """
        return self.ui_handler.is_logined()

    def get_logined_user(self) -> dict:
        """
        Retrieves the currently logged-in user's info.

        Returns:
            dict: The information of the currently logged-in user.
        """
        return self.ui_handler.get_logined_user()
    
    def set_logined_user(self, user_info: dict):
        """
        Updates the internally stored user of the currently logged-in user.

        Args:
            user_info (dict): The new user info to set as currently logged-in.
        """
        self.ui_handler.logined_user = user_info
    
    def change_page(self, page: int) -> None:
        """
        Handles page change actions by performing necessary backend updates based on the page navigated to.

        Args:
            page (int): The index of the page being navigated to.
        """
        if page == Constants.UIPages.CHANGE_USERNAME:
            self.change_username_api.set_current_username()

        if page == Constants.UIPages.ALL_USERS:
            self.all_users_api.set_all_users()

class pagesAPI:
    """
    Provides a foundational API class for managing page-related functionalities in a user interface system. This class
    primarily handles callbacks related to user authentication states, such as getting and setting the logged-in user.

    Args:
        ui_handler (pagesUI): The user interface handler associated with this API, which manages the page-specific UI.
    """

    def __init__(self, ui_handler: pagesUI) -> None:
        """
        Initializes the pagesAPI with a reference to the UI handler for page interactions.

        Args:
            ui_handler (pagesUI): The UI handler that manages the user interface elements and interactions.
        """
        self.ui_handler = ui_handler

        self.get_logined_user_callback = None  # Callback to get the currently logged-in user.
        self.set_logined_user_callback = None  # Callback to set the currently logged-in user.

    def set_get_logined_user_callback(self, func: Callable[[None], dict]) -> None:
        """
        Sets the function to be called to retrieve the currently logged-in user's info.

        Args:
            func (Callable[[], dict]): A function that returns the information of the currently logged-in user.
        """
        self.get_logined_user_callback = func

    def set_set_logined_user_callback(self, func: Callable[[dict], None]) -> None:
        """
        Sets the function to be called to update the currently logged-in user's info within the system.

        Args:
            func (Callable[[dict], None]): A function that takes a user info as input and updates the logged-in user.
        """
        self.set_logined_user_callback = func

    def call_get_logined_user_callback(self) -> dict:
        """
        Calls the get logged-in user callback if it has been set, to retrieve the current user's info.

        Returns:
            dict: The info of the currently logged-in user if the callback is set, otherwise None.
        """
        if self.get_logined_user_callback:
            return self.get_logined_user_callback()
        
    def call_set_logined_user_callback(self, user_info: dict):
        """
        Calls the set logged-in user callback if it has been set, to update the current user's info.

        Args:
            user_info (dict): The new information to set for the logged-in user.

        Returns:
            The result of the callback function if it is set, otherwise None.
        """
        if self.set_logined_user_callback:
            return self.set_logined_user_callback(user_info)

class menuAPI(pagesAPI):
    """
    Manages the menu functionality by interfacing with the user interface and backend data retrieval systems.
    """

    def __init__(self, ui_handler: menuUI) -> None:
        """
        Initializes the menuAPI with UI handler..

        Args:
            ui_handler (loginUI): The UI handler that manages the login page.
            load_user_func (Callable[[str], list[dict]]): A function to retrieve user details based on username.
        """
        super(menuAPI, self).__init__(ui_handler)

        self.ui_handler.set_logout_callback(self.logout)

    def logout(self):
        self.call_set_logined_user_callback(None)
        return True

class loginAPI(pagesAPI):
    """
    Manages the login functionality by interfacing with the user interface and backend data retrieval systems.
    This class extends the pagesAPI to handle specific login-related actions.
    """

    def __init__(self, ui_handler: loginUI, 
                load_user_func: Callable[[str], list[dict]]) -> None:
        """
        Initializes the loginAPI with UI handler and user data loading functionality.

        Args:
            ui_handler (loginUI): The UI handler that manages the login page.
            load_user_func (Callable[[str], list[dict]]): A function to retrieve user details based on username.
        """
        super(loginAPI, self).__init__(ui_handler)

        self.ui_handler.set_login_callback(self.login)

        self.load_user_func = load_user_func

    def login(self, user_info: dict) -> bool:
        """
        Attempts to log in a user using the provided user information. This method retrieves the user's saved data using the provided username, 
        verifies the provided password against the stored hashed password, 
        and updates the UI and system state accordingly.

        Args:
            user_info (dict): A dictionary containing the username and password provided by the user.

        Returns:
            bool: True if the login is successful, False otherwise.
        """
        username = user_info[Constants.Keys.USERNAME_KEY]
        password = user_info[Constants.Keys.PASSWORD_KEY]

        saved_user_info = self.load_user_func(username)
        if saved_user_info and len(saved_user_info)==1:
            saved_password = saved_user_info[0][Constants.Keys.PASSWORD_KEY]
            if passwordManager.verify_password(password=password, 
                                               hashed_password=saved_password):

               self.ui_handler.set_message(Messages.LOGIN_SUCCESSFULLY, level=Constants.MessagesLevels.INFO)
               self.call_set_logined_user_callback(saved_user_info[0])
               return True 
            else:
                self.ui_handler.set_message(Messages.INCORRECT_PASSWORD, level=Constants.MessagesLevels.ERROR)
                return False
        else:
            self.ui_handler.set_message(Messages.INVALID_USERNAME, level=Constants.MessagesLevels.ERROR)
            return False

class changePasswordAPI(pagesAPI):
    """
    Manages password change operations for the user interface. Extends pagesAPI to handle password-specific actions
    such as verifying and updating user passwords.
    """

    def __init__(self, ui_handler: changePasswordUI, 
                load_user_func: Callable[[str], list[dict]],
                update_user_func: Callable[[dict], None]) -> None:
        """
        Initializes the changePasswordAPI with handlers and functions necessary for changing a user's password.

        Args:
            ui_handler (changePasswordUI): The UI handler that manages the change password page.
            load_user_func (Callable[[str], list[dict]]): A function to retrieve user details based on username.
            update_user_func (Callable[[dict], None]): A function to update user details in the database.
        """
        super(changePasswordAPI, self).__init__(ui_handler)

        self.load_user_func = load_user_func
        self.update_user_func = update_user_func

        self.ui_handler.set_change_password_callback(self.change_password)

    def change_password(self, password_info: dict, ) -> bool:
        """
        Attempts to change the user's password using the provided password information. This method verifies the current password, 
        checks the strength of the new password, and ensures the new password matches the confirmation password before updating the user's password
        in the database.

        Args:
            password_info (dict): A dictionary containing the current, new, and confirmation passwords.

        Returns:
            bool: True if the password change is successful, False otherwise.

        """
        user_info = self.call_get_logined_user_callback()
        current_password = password_info[Constants.Keys.CURRENT_PASSWORD_KEY]
        new_password = password_info[Constants.Keys.NEW_PASSWORD_KEY]
        confirm_password = password_info[Constants.Keys.CONFIRM_PASSWORD_KEY]

        saved_user_info = self.load_user_func(user_info[Constants.Keys.USERNAME_KEY])
        if saved_user_info and len(saved_user_info)==1:
            saved_user_info = saved_user_info[0]
            saved_password = saved_user_info[Constants.Keys.PASSWORD_KEY]
            if passwordManager.verify_password(password=current_password, 
                                               hashed_password=saved_password):
                strength_check = passwordManager.check_password_strength(
                    password=new_password,
                    regex=Constants.PasswordStrength.REGEX,
                    min_length=Constants.PasswordStrength.MIN_LENGTH,
                    min_uppercases=Constants.PasswordStrength.MIN_UPPERCASES,
                    min_lowercases=Constants.PasswordStrength.MIN_LOWERCASES,
                    min_digits=Constants.PasswordStrength.MIN_DIGITS,
                    min_specialchars=Constants.PasswordStrength.MIN_SPECIALCHARS,
                )
                if strength_check:
                    if passwordManager.confirm_password(new_password, confirm_password):
                        saved_user_info[Constants.Keys.PASSWORD_KEY] = passwordManager.hash_password(new_password)
                        self.update_user_func(saved_user_info)
                        self.ui_handler.set_message(Messages.PASSWORD_CHANGED, level=Constants.MessagesLevels.INFO)
                        return True
                    else:
                        self.ui_handler.set_message(Messages.UNMATCH_CONFIRM, level=Constants.MessagesLevels.ERROR)
                        return False
                else:
                    self.ui_handler.set_message(Messages.WEAK_PASSWORD, level=Constants.MessagesLevels.ERROR)
                    return False
            else:
                self.ui_handler.set_message(Messages.INCORRECT_PASSWORD, level=Constants.MessagesLevels.ERROR)
                return False
        else:
            self.ui_handler.set_message(Messages.LOGIN_FIRST, level=Constants.MessagesLevels.ERROR)
            return False

class changeUsernameAPI(pagesAPI):
    """
    Manages username change operations for a user, ensuring uniqueness and adherence to username policies.
    Extends pagesAPI to utilize common functionalities such as retrieving and updating logged-in user data.
    """

    def __init__(self, ui_handler: changeUsernameUI,
                load_user_func: Callable[[str], list[dict]],
                update_user_func: Callable[[dict], None],
                load_all_users_func: Callable[[None], list[dict]]) -> None:
        """
        Initializes the changeUsernameAPI with functions necessary for fetching and updating user data.
        
        Args:
            ui_handler (changeUsernameUI): UI handler that manages the change username interface.
            load_user_func (Callable[[str], list[dict]]): A function to retrieves user details based on username.
            update_user_func (Callable[[dict], None]): A function to updates user details.
            load_all_users_func (Callable[[], list[dict]]): A function to retrieves all user profiles from the database.
        """

        super(changeUsernameAPI, self).__init__(ui_handler)

        self.load_user_func = load_user_func
        self.update_user_func = update_user_func
        self.load_all_users_func = load_all_users_func

        self.ui_handler.set_change_username_callback(self.change_username)

    def set_current_username(self) -> None:
        """
        Fetches the current logged-in username and sets it in the username field on the UI.
        """
        user_info = self.call_get_logined_user_callback()
        username = user_info[Constants.Keys.USERNAME_KEY] if user_info else ''
        self.ui_handler.set_current_username(username)

    def change_username(self, username_info: dict, ) -> bool:
        """
        Processes the username change request by ensuring the new username is unique and meets strength criteria.

        Args:
            username_info (dict): Contains the new username proposed by the user.

        Returns:
            bool: True if the username change is successful and updated in the database, False otherwise.
        """
        current_user_info = self.call_get_logined_user_callback()
        new_username = username_info[Constants.Keys.NEW_USERNAME_KEY]

        saved_user_info = self.load_user_func(current_user_info[Constants.Keys.USERNAME_KEY])
        all_users_info = self.load_all_users_func()
        usernames = [x[Constants.Keys.USERNAME_KEY] for x in all_users_info]

        if saved_user_info and len(saved_user_info)==1:
            saved_user_info = saved_user_info[0]
            is_unique = usernameManager.is_unique(new_username, usernames)
            if is_unique:
                strength_check = usernameManager.check_username_strength(
                        username=new_username,
                        regex=Constants.UsernameStrength.REGEX,
                        min_length=Constants.UsernameStrength.MIN_LENGHT,
                        max_length=Constants.UsernameStrength.MAX_LENGTH,
                        allow_space=Constants.UsernameStrength.ALLOW_SPACE,
                        allow_start_without_letter=Constants.UsernameStrength.ALLOW_START_WITHOUT_LETTER,
                        reserved_usernames=Constants.UsernameStrength.RESERVED_USERNAMES,
                    )
                if strength_check:
                    saved_user_info[Constants.Keys.USERNAME_KEY] = new_username
                    self.update_user_func(saved_user_info)
                    self.ui_handler.set_message(Messages.USERNAME_CHANGED, level=Constants.MessagesLevels.INFO)
                    self.set_logined_user_callback(saved_user_info)
                    return True
                else:
                    self.ui_handler.set_message(Messages.WEAK_USERNAME, level=Constants.MessagesLevels.ERROR)
                    return False
            else:
                self.ui_handler.set_message(Messages.DUPLICATE_USERNAME, level=Constants.MessagesLevels.ERROR)
                return False
        else:
            self.ui_handler.set_message(Messages.LOGIN_FIRST, level=Constants.MessagesLevels.ERROR)
            return False

class allUsersAPI(pagesAPI):
    """
    Manages the API interactions for the all users display, including loading all user data, and handling
    delete and edit operations on user profiles.
    """

    def __init__(self, ui_handler: allUsersUI,
                load_all_users_func: Callable[[None], list[dict]],
                delete_user_func: Callable[[str], None],
                update_user_func: Callable[[dict], None]) -> None:
        """
        Initializes the allUsersAPI with necessary functions and sets up callback bindings for UI events.

        Args:
            ui_handler (allUsersUI): The UI handler that manages the all users page.
            load_all_users_func (Callable[[], list[dict]]): A function to retrieves all user profiles from the data source.
            delete_user_func (Callable[[str], None]): A function to deletes a user profile based on username.
            update_user_func (Callable[[dict], None]): A function to updates a user profile with given details.
        """
        super(allUsersAPI, self).__init__(ui_handler)

        self.load_all_users_func = load_all_users_func
        self.delete_user_func = delete_user_func
        self.update_user_func = update_user_func

        self.ui_handler.set_delete_user_callback(self.delete_user)
        self.ui_handler.set_edit_user_callback(self.edit_user)

    def set_all_users(self) -> None:
        """
        Fetches and displays all users in the UI, applying specific permissions such as edit and delete
        based on user roles or authentication state.
        """
        self.ui_handler.setup_table()
        all_users_info = self.load_all_users_func()
        current_user_info = self.call_get_logined_user_callback()
        current_username = current_user_info[Constants.Keys.USERNAME_KEY] if current_user_info else ''

        if not current_username:
            self.ui_handler.set_message(Messages.LOGIN_FIRST, level=Constants.MessagesLevels.ERROR)
            return

        for user in all_users_info:
            if user[Constants.Keys.USERNAME_KEY] == current_username:
                self.ui_handler.append_table_row(user, edit=False, delete=False)
            else:
                self.ui_handler.append_table_row(user, edit=True, delete=True)

    def delete_user(self, user_info: dict) -> bool:
        """
        Executes the deletion of a user based on provided user information.

        Args:
            user_info (dict): The user information containing at least the username.

        Returns:
            bool: True if the deletion was successfully executed, False otherwise.
        """
        username = user_info[Constants.Keys.USERNAME_KEY]
        self.delete_user_func(username)

        self.ui_handler.set_message(message=Messages.USER_DELETED_SUCCESSFULLY, level=Constants.MessagesLevels.INFO)
        return True
    
    def edit_user(self, user_info: dict, edited_user_info) -> bool:
        """
        Processes user profile edits, ensuring that the new data adheres to constraints like username uniqueness
        and password strength.

        Args:
            user_info (dict): The original user information.
            edited_user_info (dict): The updated user information to be validated and saved.

        Returns:
            bool: True if the user profile is successfully updated, False otherwise.
        """
        edited_username = edited_user_info[Constants.Keys.USERNAME_KEY]
        edited_password = edited_user_info[Constants.Keys.PASSWORD_KEY]
        edited_confirm_password = edited_user_info[Constants.Keys.CONFIRM_PASSWORD_KEY]

        username = user_info[Constants.Keys.USERNAME_KEY]
        password = user_info[Constants.Keys.PASSWORD_KEY]

        if username != edited_username:
            all_users_info = self.load_all_users_func()
            usernames = [x[Constants.Keys.USERNAME_KEY] for x in all_users_info]

            if edited_username in usernames:
                self.ui_handler.set_message(Messages.DUPLICATE_USERNAME, level=Constants.MessagesLevels.ERROR)
                return False
            
            username_strength_check = usernameManager.check_username_strength(
                    username=edited_username,
                    regex=Constants.UsernameStrength.REGEX,
                    min_length=Constants.UsernameStrength.MIN_LENGHT,
                    max_length=Constants.UsernameStrength.MAX_LENGTH,
                    allow_space=Constants.UsernameStrength.ALLOW_SPACE,
                    allow_start_without_letter=Constants.UsernameStrength.ALLOW_START_WITHOUT_LETTER,
                    reserved_usernames=Constants.UsernameStrength.RESERVED_USERNAMES,
                )
            if not username_strength_check:
                self.ui_handler.set_message(Messages.WEAK_USERNAME, level=Constants.MessagesLevels.ERROR)
                return False

        if password != edited_password:
            strength_check = passwordManager.check_password_strength(
                password=edited_password,
                regex=Constants.PasswordStrength.REGEX,
                min_length=Constants.PasswordStrength.MIN_LENGTH,
                min_uppercases=Constants.PasswordStrength.MIN_UPPERCASES,
                min_lowercases=Constants.PasswordStrength.MIN_LOWERCASES,
                min_digits=Constants.PasswordStrength.MIN_DIGITS,
                min_specialchars=Constants.PasswordStrength.MIN_SPECIALCHARS,
            )
            if not strength_check:
                self.ui_handler.set_message(Messages.WEAK_PASSWORD, level=Constants.MessagesLevels.ERROR)
                return False

            if not passwordManager.confirm_password(edited_password, edited_confirm_password):
                self.ui_handler.set_message(Messages.UNMATCH_CONFIRM, level=Constants.MessagesLevels.ERROR)
                return False
        
            edited_user_info[Constants.Keys.PASSWORD_KEY] = passwordManager.hash_password(edited_password)

        edited_user_info.pop(Constants.Keys.CONFIRM_PASSWORD_KEY)
        user_info.update((k,v) for k,v in edited_user_info.items() if v is not None)

        self.update_user_func(user_info)
        self.ui_handler.set_message(message=Messages.USER_EDITED_SUCCESSFULLY, level=Constants.MessagesLevels.INFO)
        return True

class signupAPI(pagesAPI):
    """
    Manages the signup functionality by interfacing with the user interface and backend operations.
    This class extends pagesAPI to handle actions specifically related to user registration.
    """

    def __init__(self, ui_handler: signupUI,
                load_all_users_func: Callable[[None], list[dict]],
                add_user_func: Callable[[dict], None]) -> None:
        """
        Initializes the signupAPI with necessary functions for managing user registrations.

        Args:
            ui_handler (signupUI): The UI handler that manages the signup interface.
            load_all_users_func (Callable[[], list[dict]]): A function to retrieves all user profiles from the data source.
            add_user_func (Callable[[dict], None]): A function to adds a new user profile to the database.
        """
        super(signupAPI, self).__init__(ui_handler)

        self.load_all_users_func = load_all_users_func
        self.add_user_func = add_user_func

        self.ui_handler.set_singup_callback(self.signup)

    def signup(self, user_info: dict) -> bool:
        """
        Processes the user signup by validating the username and password against business rules,
        ensuring uniqueness, and adhering to security standards.

        Args:
            user_info (dict): Contains the new user's signup details like username, password, etc.

        Returns:
            bool: True if the signup is successful and the user is added to the database, False otherwise.
        """
        username = user_info[Constants.Keys.USERNAME_KEY]
        password = user_info[Constants.Keys.PASSWORD_KEY]
        confirm_password = user_info[Constants.Keys.CONFIRM_PASSWORD_KEY]

        all_users_info = self.load_all_users_func()
        usernames = [x[Constants.Keys.USERNAME_KEY] for x in all_users_info]

        if username in usernames:
            self.ui_handler.set_message(Messages.DUPLICATE_USERNAME, level=Constants.MessagesLevels.ERROR)
            return False
        
        username_strength_check = usernameManager.check_username_strength(
                username=username,
                regex=Constants.UsernameStrength.REGEX,
                min_length=Constants.UsernameStrength.MIN_LENGHT,
                max_length=Constants.UsernameStrength.MAX_LENGTH,
                allow_space=Constants.UsernameStrength.ALLOW_SPACE,
                allow_start_without_letter=Constants.UsernameStrength.ALLOW_START_WITHOUT_LETTER,
                reserved_usernames=Constants.UsernameStrength.RESERVED_USERNAMES,
            )
        if not username_strength_check:
            self.ui_handler.set_message(Messages.WEAK_USERNAME, level=Constants.MessagesLevels.ERROR)
            return False

        strength_check = passwordManager.check_password_strength(
            password=password,
            regex=Constants.PasswordStrength.REGEX,
            min_length=Constants.PasswordStrength.MIN_LENGTH,
            min_uppercases=Constants.PasswordStrength.MIN_UPPERCASES,
            min_lowercases=Constants.PasswordStrength.MIN_LOWERCASES,
            min_digits=Constants.PasswordStrength.MIN_DIGITS,
            min_specialchars=Constants.PasswordStrength.MIN_SPECIALCHARS,
        )
        if not strength_check:
            self.ui_handler.set_message(Messages.WEAK_PASSWORD, level=Constants.MessagesLevels.ERROR)
            return False

        if not passwordManager.confirm_password(password, confirm_password):
            self.ui_handler.set_message(Messages.UNMATCH_CONFIRM, level=Constants.MessagesLevels.ERROR)
            return False
        
        hashed_password = passwordManager.hash_password(password)
        user_info[Constants.Keys.PASSWORD_KEY] = hashed_password

        user_info.pop(Constants.Keys.CONFIRM_PASSWORD_KEY)
        self.add_user_func(user_info)
        self.ui_handler.set_message(Messages.SIGNUP_SUCCESSFULLY, level=Constants.MessagesLevels.INFO)
        return True