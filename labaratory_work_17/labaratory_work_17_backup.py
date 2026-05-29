import os
import shutil

def make_backup(source_dir, backup_dir):
    """Создание полной резервной копии директории"""
    if os.path.exists(source_dir):
        # Если старая копия уже существует, удаляем ее перед обновлением
        if os.path.exists(backup_dir):
            shutil.rmtree(backup_dir)
        shutil.copytree(source_dir, backup_dir)
        print(f"Резервное копирование завершено. Данные из '{source_dir}' скопированы в '{backup_dir}'.")
    else:
        print(f"Ошибка резервного копирования: Директория '{source_dir}' не существует.")


