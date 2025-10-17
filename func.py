import asyncio
import time
import os
import random
import requests
from playwright.async_api import async_playwright
from fake_useragent import UserAgent

async def click_on_anchor_url(page):
    try:
        # Подождем, пока элементы будут видны
        await page.wait_for_selector('a.anchor-url', state='visible')

        # Получим список всех элементов с классом 'anchor-url'
        elements = await page.query_selector_all('a.anchor-url')

        # Если есть элементы, кликнем по последнему
        if elements:
            await elements[-1].click()  # Кликнем по последнему элементу
            print("Клик по последнему элементу выполнен успешно! ✅")
        else:
            print("Элементы с классом 'anchor-url' не найдены. ❌")
    except Exception as e:
        print(f"Произошла ошибка при клике: {e} ❌")


async def click_launch_button(page):
    # Селектор для элемента с текстом "Launch"
    selector = 'text="Launch"'
    try:
        # Ожидание наличия элемента и клик по нему
        await page.click(selector)
        print("Кнопка 'Launch' нажата успешно! ✅")
    except Exception as e:
        print(f"Не удалось нажать на кнопку 'Launch'. Ошибка: {e} ❌")


async def click_popup_button(page):
    selector = 'button.popup-button:nth-child(1) > span:nth-child(2)'
    try:
        # Ожидание наличия элемента и клик по нему
        await page.click(selector)
        print("Кнопка нажата успешно! ✅")
    except Exception as e:
        print(f"Не удалось нажать на кнопку. Ошибка: {e} ❌")

async def open_last_app(page, word):
    elements = await page.query_selector_all('.reply-markup-button-text')

    for el in elements:
        text = await el.inner_text()
        if word in text:
            print("Найден элемент:", text)

    if elements:
        last_element = elements[-1]
        text_last = await last_element.inner_text()
        print("Кликаем по последнему элементу:", text_last)
        #time.sleep(1.5)
        # Добавляем проверку на доступность элемента
        is_visible = await last_element.is_visible()
        is_enabled = await last_element.is_enabled()

        if is_visible and is_enabled:
            await last_element.click()
        else:
            print("Элемент не видим или неактивен. ❌")

    return elements

async def get_src_value(page, class_name):
    try:
        element = await page.query_selector(f".{class_name}")  # Поиск элемента по классу
        if element:
            src_value = await element.get_attribute("src")  # Получение атрибута 'src'
            print(src_value)
            return src_value
    except Exception as e:
        print(f"An error occurred: {e}")

async def check_elements(page, elements_list: list):
    for word in elements_list:
        elements = await page.query_selector_all(f'//*[contains(text(), "{word}")]')
        if elements:
            last_element = elements[1] if len(elements) > 1 else elements[0]  # Проверка, что элемент существует
            last_element2 = elements[-1]
            try:
                #time.sleep(1.5)
                await last_element.wait_for_element_state("visible")
                await last_element.click()
                await last_element2.click()
                break
                print(f"Успешно кликнули на элементы для слова: {word}")
            except Exception as e:
                print(f"Ошибка при клике на элементы для слова '{word}': {e}")
        else:
            print(f"Элементы для слова '{word}' не найдены")
async def poisk_elementov_click(page, spisok_element, t):
    start = time.time()

    while time.time() < start + t:
        try:
            for i in spisok_element:
                print(i)
                element = await page.query_selector(f'xpath=//a[contains(text(), "{i}")]')
                if element:
                    await element.click()  # Клик по найденному элементу
                    print("Элемент найден и кликнут")
                    return True  # Опционально вернуть успешный результат
                else:
                    print("Элемент не найден")
        except Exception as e:
            print(f"Ошибка при поиске элемента: {e}")
            return False  # Опционально вернуть неуспешный результат


async def search_element_xpath_and_enter_text(page, xpath_selector, text):
    try:
        button = await page.wait_for_selector(f'xpath={xpath_selector}', timeout=5000)
        await button.scroll_into_view_if_needed()  # Прокручиваем страницу до элемента
        await button.click(force=True)
        await button.fill(text)  # Вводим текст
        await asyncio.sleep(1)
        await button.press('Enter')  # Нажатие Enter
    except Exception as e:
        print(f"Ошибка: {e}")


def send_msg(photo):
    token = "6971511734:AAGlLBTJLnhSiwMtdIkLQ2CvXS6TgeGpBdk"
    chat_id = "970307084"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + photo
    results = requests.get(url_req)
    return results

def magnit_kupon(photo):
    chat_id = "970307084"
    token = "6971511734:AAGlLBTJLnhSiwMtdIkLQ2CvXS6TgeGpBdk"
    files = {'photo': open(photo, 'rb')}
    url_req = requests.post(f'https://api.telegram.org/bot{token}/sendPhoto?chat_id={chat_id}', files=files)
    return url_req

async def async_send_msg(photo):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, send_msg, photo)
    if result.status_code == 200:
        print("Сообщение успешно отправлено!")
    else:
        print(f"Ошибка при отправке сообщения: {result.status_code}")

async def async_magnit_kupon(photo):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, magnit_kupon, photo)
    if result.status_code == 200:
        print("Фото успешно отправлено!")
    else:
        print(f"Ошибка при отправке фото: {result.status_code}")

async def random_rename_foto():
    # Укажите путь к вашей папке с изображениями
    folder_path = r"D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\фото"
    # Получаем список всех файлов в папке
    files = [f for f in os.listdir(folder_path) if
             os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    # Проверяем, что в папке есть фотографии
    if files:
        # Выбираем случайное изображение
        random_file = random.choice(files)
        print(f"Случайное изображение: {random_file}")
        # Генерируем случайное число в диапазоне от 00000000 до 9999999999
        new_name_number = random.randint(0, 9999999999)
        new_file_name = f"{new_name_number:010}.jpg"  # Форматируем с ведущими нулями до длины 10 символов
        new_file_path = os.path.join(folder_path, new_file_name)
        # Переименование файла
        os.rename(os.path.join(folder_path, random_file), new_file_path)
        print(f"Переименовано в: {new_file_name}")
        # Возвращаем полный путь к новому файлу
        return new_file_path
    else:
        print("В папке нет изображений.")
        return None
async def delete_foto(path):
    try:
        # Удаляем файл напрямую, без открытия его
        os.remove(path)
        print("Файл успешно удален. 😊")
    except FileNotFoundError:
        print("Файл не найден. 😢")
    except PermissionError:
        print("Нет разрешения на удаление файла. ⚠️")
    except Exception as e:
        print(f"Произошла ошибка: {e}. 😟")

async def search_by_word(page, word):
    try:
        # Используем asyncio.wait_for для ограничения времени ожидания
        elements = await asyncio.wait_for(page.query_selector_all(f'//*[contains(text(), "{word}")]'), timeout=5)

        # Фильтруем только видимые элементы
        visible_elements = [el for el in elements if await el.is_visible()]

        if visible_elements:
            last_visible_element = visible_elements[-1]  # взять последний видимый элемент
            try:
                await last_visible_element.click()
                return True
            except Exception as e:
                print(f"Ошибка при клике на элемент: {e}")
        else:
            print("Нет видимых элементов, содержащих указанный текст.")
            return False
    except asyncio.TimeoutError:
        print("Время ожидания поиска элементов превысило 5 секунд.")
    except Exception as e:
        print(f"Ошибка при поиске элементов: {e}")


async def search_element_xpath(page, xpath, timeout):
    try:
        time.sleep(2)
        button = await page.wait_for_selector(f'xpath={xpath}', timeout=timeout * 1000)
        await button.scroll_into_view_if_needed()  # Прокручиваем страницу до элемента
        await button.click(force=True)
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False


async def run_profile(firefox_profile_path):
    async with async_playwright() as p:
        ua = UserAgent()
        random_user_agent = ua.random

        context = await p.firefox.launch_persistent_context(
            firefox_profile_path,
            headless=False,
            user_agent=random_user_agent
        )

        page = await context.new_page()
        await page.goto("https://web.telegram.org/k/#@tspyaterochka")

        # Ваши дальнейшие действия...
        # Например:
        # await search_element_xpath(page, "xpath_selector_here", 5)

        # Закрытие контекста
        await context.close()


# Ваша функция main или другой код для начала работы
async def main():
    # Здесь можно добавить логику, чтобы вызвать run_profile с соответствующим профилем
    await run_profile('path_to_your_firefox_profile')

# Создание списка с помощью списка
fio_list = [

    "Кузнецов Николай Николаевич",
    "Попов Сергей Сергеевич",
    "Семенов Семен Семенович",
    "Сорокин Андрей Андреевич",
    "Морозов Виктор Викторович",
    "Алексеев Алексей Алексеевич",
    "Евдокимов Павел Павлович",
    "Федоров Максим Максимович",
    "Ковалев Константин Константинович",
    "Яковлев Николай Николаевич",
    "Григорьев Виталий Витальевич",
    "Богданов Антон Андреевич",
    "Никифоров Юрий Юрьевич",
    "Баранов Степан Степанович",
    "Костенко Григорий Григорьевич",
    "Шевченко Василий Васильевич",
    "Кузьмина Дарья Дмитриевна",
    "Лебедев Алексей Владимирович",
    "Михайлов Сергей Игоревич",
    "Солдатов Артем Артемович",
    "Степанов Андрей Викторович",
    "Тихонов Антон Петрович",
    "Павлов Роман Юрьевич",
    "Захаров Олег Сергеевич",
    "Агреев Альберт Тимурович",
    "Кириллов Данил Александрович",
    "Медведев Вадим Михайлович",
    "Белов Игорь Валерьевич",
    "Семенова Виктория Андреевна",
    "Фролов Валентин Валентинович",
    "Тихомиров Григорий Васильевич",
    "Шереметев Илья Ильич",
    "Банников Артем Станиславович",
    "Соловьев Виталий Анатольевич",
    "Романов Даниил Григорьевич",
    "Тимофеев Владислав Сергеевич",
    "Коваленко Нина Семеновна",
    "Мосин Олег Геннадиевич",
    "Филиппов Алексей Юрьевич",
    "Кудрявцев Василиса Ярославовна",
    "Трусова Анастасия Николаевна",
    "Ларина Кристина Владимировна",
    "Дорофеев Алексей Павлович",
    "Погорелов Сергей Владиславович",
    "Сидорова Ольга Петровна",
    "Данилов Вячеслав Валентинович",
    "Николаева Софья Александровна",
    "Федосов Константин Артемович",
    "Карасев Денис Сергеевич",
    "Максимова Елена Николаевна",
    "Соломатин Алексей Ильич",
    "Панфилов Павел Андреевич",
    "Трофимова Валерия Игоревна",
    "Самсонов Аркадий Михайлович",
    "Беляев Игорь Валереевич",
    "Сорокина Анастасия Олеговна",
    "Яшин Виктор Викторович",
    "Малютина Алена Александровна",
    "Твердов Николай Петрович",
    "Глазунов Григорий Алексеевич",
    "Шутов Дмитрий Владимирович",
    "Потапова Людмила Георгиевна",
    "Трофимов Даниил Сергеевич",
    "Тимофеева Полина Валерьевна",
    "Леонидова Юлия Валентиновна",
    "Филиппова Дарья Петровна",
    "Рябов Валентин Олегович",
    "Сорокина Маргарита Сергеевна",
    "Зайцева Екатерина Юрьевна",
    "Савельев Степан Игоревич",
    "Голубев Николай Александрович",
    "Тихонова Анастасия Сергеевна",
    "Тимонов Илья Валерьевич",
    "Ковальчук Надежда Антоновна",
    "Бальзамов Евгений Викторович",
    "Бородин Валерий Степанович",
    "Федорова Виктория Семеновна",
    "Снегирев Станислав Геннадиевич",
    "Старков Анатолий Павлович",
    "Лаптев Вячеслав Константинович",
    "Шевченко Регина Валерьевна",
    "Сосновский Адам Валериевич",
    "Лобанов Артем Артемович",
    "Фомин Илья Михайлович",
    "Громова Надежда Викторовна",
    "Ястребова Елена Романовна",
    "Дружинин Станислав Петрович",
    "Третьяков Владислав Георгиевич",
    "Чистяков Игорь Юрьевич",
    "Садыков Вадим Валерьевич",
]

