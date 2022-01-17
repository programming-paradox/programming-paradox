with open("old_type.txt", "r") as f:
    all_lines = f.readlines()
    for mails in all_lines:
        old_main = mails.split(":")
        username = open("username.txt", "a")
        password = open("password.txt", "a")
        username.write(f"\n{old_main[0]}")
        password.write(old_main[1])
        username.close()
        password.close()