def log_failed_login(username):
    print(f"Failed login attempt: {username}")


def login(username, password):
    if username == "palak" and password == "1234":
        return True

    log_failed_login(username)
    return False
