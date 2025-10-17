import time

import cv2
import numpy as np
import asyncio


def matchin(match):
    if match:
        x, y, w, h = match
        # Рассчитываем координаты центра элемента для клика
        center_x = int(x + w // 2)
        center_y = int(y + h // 2)
        return center_x,center_y


    else:
        print("Совпадение не найдено")

# Функция для поиска совпадения на изображении
def find_image_on_screen(screenshot_path, template_path):
    screenshot = cv2.imread(screenshot_path)
    template = cv2.imread(template_path)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Порог для совпадения
    yloc, xloc = np.where(result >= threshold)

    if len(xloc) > 0 and len(yloc) > 0:
        # Предполагается, что найдено одно совпадение
        return (xloc[0], yloc[0], template.shape[1], template.shape[0])
    return None

async def  click_image(page,spis_foto,timer):
    start_time = time.time()  # Запоминаем время начала
    found = False  # Флаг для обозначения успешного нахождения изображения
    while time.time() - start_time < timer:  # Проверяем прошло ли 5 секунд
        time.sleep(1.5)
        for i in spis_foto:
            await page.screenshot(path='screenshot.png')
            # Путь к шаблону, который вы хотите найти
            template_path = i
            # Поиск совпадения на скриншоте
            match = find_image_on_screen('screenshot.png', template_path)
            if match:
                center_x, center_y = matchin(match)

                await  page.mouse.click(center_x, center_y)
                print(f"нашел искомое {i}")
                found = True
                return True
                break  # Выходим из цикла, если клик выполнен
        if found:
            break
async def  no_click_image(page,spis_foto,timer):
    start_time = time.time()  # Запоминаем время начала
    found = False  # Флаг для обозначения успешного нахождения изображения
    while time.time() - start_time < timer:  # Проверяем прошло ли 5 секунд
        for i in spis_foto:
            await page.screenshot(path='screenshot.png')
            # Путь к шаблону, который вы хотите найти
            template_path = i
            # Поиск совпадения на скриншоте
            match = find_image_on_screen('screenshot.png', template_path)
            if match:
                center_x, center_y = matchin(match)
                #await  page.mouse.click(center_x, center_y)
                print(f"нашел искомое {i}")
                found = True
                return True
                break  # Выходим из цикла, если клик выполнен
        if found:
            break