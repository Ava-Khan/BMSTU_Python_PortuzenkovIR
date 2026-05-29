import os


def change_permissions(filename, mode):
    """Изменение прав доступа к файлу (аналог chmod в Linux)"""
    if os.path.exists(filename):
        os.chmod(filename, mode)
        # Переводим числовые права в привычный восьмеричный вид для вывода
        print(f"Права доступа для файла '{filename}' изменены на {oct(mode)}.")
    else:
        print(f"Ошибка: Файл '{filename}' не найден для изменения прав.")
