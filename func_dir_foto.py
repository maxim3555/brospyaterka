import os
import shutil
#from selenium.webdriver.common.by import By
import time
def copy_foto_dir(path):
    # Путь к папке-источнику, откуда будут копироваться изображения
    source_directory =path

    # Путь к папке назначения, куда будут скопированы изображения
    destination_directory = r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\перфект фит толстовки'

    # Путь к текущей директории (откуда будут удаляться файлы)
    current_directory = os.getcwd()

    # Получаем список всех jpg-файлов в исходной директории
    files_to_copy = [f for f in os.listdir(source_directory) if f.endswith('.png')]
    file_spis = []
    # Копирование файлов
    for file_name in files_to_copy:
        destination_file_path = os.path.join(destination_directory, file_name)

        # Проверяем, существует ли файл с таким именем в целевой директории
        if not os.path.exists(destination_file_path):
            source_file_path = os.path.join(source_directory, file_name)

            try:
                shutil.copy(source_file_path, destination_file_path)
                print(f"Скопирован файл: {file_name} в {destination_directory}")
                file_spis.append(file_name)
            except Exception as e:
                print(f"Ошибка при копировании {file_name}: {e}")
        else:
            print(f"Файл {file_name} уже существует в {destination_directory}, пропуск.")
    return file_spis
def del_foto_dir(path):
    # Путь к папке-источнику, откуда будут копироваться изображения
    source_directory = path

    # Путь к папке назначения, куда будут скопированы изображения
    destination_directory = path

    # Путь к текущей директории (откуда будут удаляться файлы)
    current_directory = os.getcwd()
    # Получаем список всех jpg-файлов в исходной директории
    files_to_copy = [f for f in os.listdir(source_directory) if f.endswith('.png')]
    # Удаление файлов из текущей директории
    for file_name in files_to_copy:
        current_file_path = os.path.join(current_directory, file_name)

        if os.path.exists(current_file_path):
            try:
                os.remove(current_file_path)
                print(f"Удален файл: {file_name} из {current_directory}")
            except Exception as e:
                print(f"Ошибка при удалении {file_name}: {e}")
        else:
            print(f"Файл {file_name} не найден в {current_directory}")
def searh_po_slovo(driver, slovo, timeout):
    elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{slovo}')]")
    if elements:
        last_element = elements[-1]
        try:
            # Ждем, пока элемент станет кликабельным
            WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(last_element))
            driver.execute_script("arguments[0].click();", last_element)
            print('Нашел телефон')
        except Exception as e:
            print(f"Ошибка при клике на элемент: {e}")