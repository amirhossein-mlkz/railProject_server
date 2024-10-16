
# Login Module

## Overview
The Login Module designed to manage user profiles with a robust graphical interface. It uses PySide6 to offer a responsive and intuitive user experience, integrated with backend functionalities for secure and efficient user management.

## Features
- User authentication including signup and login.
- User profile management: view, edit, and delete user profiles.
- Password and username updates with secure handling.
- Interactive and responsive user interface designed with PySide6.

## Key Components
### `app.py`
- Initializes the application and sets up the user interface.
- Integrates resource files and prepares the UI components for runtime.
- Starts the main application loop, serving as the entry point of the module.

### `userProfile_API.py`
- Provides the backend API for user management, including:
  - Login authentication.
  - Password and username updates.
  - User profile retrieval and updating.
- Interfaces with other backend managers (`usernameManager`, `passwordManager`) to ensure data integrity and security.

### `userProfile_UI.py`
- Manages all aspects of the user interface related to user profiles.
- Handles events and user interactions, updating the UI accordingly.
- Incorporates utility tools like password visibility toggles and edit/delete buttons for interactive user experience.

## Directory Structure
### `uiFiles`
- `userProfile.ui`: UI design file for user profiles.
- `editUser.ui`: UI design file for editing user profiles.
- `userProfile.py`, `editUser.py`: Python scripts for UI interactions.
- `resources/`: Contains icons and other resources for the UI.

### `backend`
- `passwordManager.py`: Manages password-related functionalities.
- `usernameManager.py`: Manages username-related functionalities.

### `Constants`
- `Constants.py`: Central definition of constants used throughout the application.
- `IconsPath.py`: Paths to icon files.
- `Messages.py`: Definitions of static messages used in the UI.

### `uiUtils`
- `editUserUI.py`: Manages the edit user interface interactions.
- `eyeButtonHandler.py`: Handles the password visibility toggle in UI.
- `editButton.py`, `deleteButton.py`: Manage edit and delete actions in the UI.
- `messageBox.py`: Custom message boxes for notifications and alerts.

### `Database`
- `usersDatabase.py`: Handles all database interactions for user management.

## Installation and Setup
### Installation Requirements
- Ensure Python 3.6+ is installed.
- Install PySide6 using pip: `pip install PySide6`.
- Verify that all dependencies are installed by running `pip install -r requirements.txt`.

## Usage
To run the application, navigate to the application's root directory and execute:
```bash
python app.py
```
To navigate between different pages within the application, use the `show_win` function from userProfile_UI by calling it with the appropriate page name. For example:
```python
main_ui.show_win(UIPages.LOGIN)
```
This will display the Login Page. Replace 'Login' with the name of the page you wish to display from Constants UIPages class.

## Contributing
We encourage contributions from the community. Please adhere to the following guidelines:
- Fork the repository and create your feature branch.
- Ensure your code adheres to the project's coding standards.
- Submit a pull request with a comprehensive description of changes.

## License
This software is licensed under Apache License. Please see the `LICENSE` file in the root directory for full license terms.
