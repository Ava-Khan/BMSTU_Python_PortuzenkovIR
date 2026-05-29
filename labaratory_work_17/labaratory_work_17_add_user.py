import subprocess


def add_user(username):
    """Создание нового пользователя в системе Linux"""
    # Вызываем системную утилиту useradd через sudo
    subprocess.run(["sudo", "useradd", username])
    print(f"Пользователь '{username}' успешно добавлен в систему.")


def remove_user(username):
    """Удаление пользователя из системы Linux"""
    # Вызываем системную утилиту userdel через sudo
    subprocess.run(["sudo", "userdel", username])
    print(f"Пользователь '{username}' успешно удален из системы.")



if __name__ == "__main__":
    test_user = "student_user"
    add_user(test_user)
    #remove_user(test_user)

