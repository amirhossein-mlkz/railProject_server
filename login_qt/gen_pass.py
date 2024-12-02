from Loginbackend.passwordManager import passwordManager
if __name__ == '__main__':
    import bcrypt

    password = 'user'
    print(passwordManager.hash_password(password))
    