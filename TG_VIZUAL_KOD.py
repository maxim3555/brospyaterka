import os
import random
import time
import asyncio
from vizual import *
from func_dir_foto import *
import openpyxl
import requests
import pandas as pd
from func import *
from playwright.async_api import async_playwright
from fake_useragent import UserAgent  # Assuming you have this for random user agent
from selenium.webdriver.common.action_chains import ActionChains
from func import *
from telethon import TelegramClient, events

def actual_none_profil():
    global schet_profil
    for i in range(1, 100):  # Проверяем максимум 100 строк
        if schet_profil >= len(list1['A']):  # Проверка выхода за пределы
            break

        token = list1['E'][schet_profil].value  # Получаем значение из колонки 'E'
        token_real = str(list1['A'][schet_profil].value)

        if token is None and token_real is not None:
            return schet_profil  # Если токен найден, возвращаем его

        schet_profil += 1  # Переходим к следующей строке

book = openpyxl.open(r"numb.xlsx")
list1 = book.active
schet_profil =1
obshee_vremya=0


book = openpyxl.open(r"numb.xlsx")
list1 = book.active








async def run_profile(firefox_profile_path):
    # Начинаем замер времени
        start_time = time.time()



        global obshee_vremya
        async with async_playwright() as p:
#БЛОК НАСТРОЕК ПЛЭЙВРАЙТ
            ua = UserAgent()
            random_user_agent = ua.random
            while True:
                user_agent = ua.random
                if "iPhone" in user_agent:
                    print(user_agent)
                    break


            context = await p.firefox.launch_persistent_context(
                firefox_profile_path,
                headless=False,
                user_agent=user_agent,
                #proxy=random.choice(proxies)
            )


            page = await context.new_page()


            await page.goto('https://gp.x5.ru/luckydice')
            time.sleep(3)
#нажать на кубик
            await search_element_xpath(page, '//html/body/div/div/div/button[2]/picture', 5)
            await search_element_xpath(page, '//html/body/div/div/div[1]/div[1]/div[2]/div/button/picture', 5)

            time.sleep(3)
# Конец замера времени
            end_time = time.time()
            execution_time = end_time - start_time
# Снимаем скриншот текущей страницы
            await page.screenshot(path='screenshot.png')
            await async_magnit_kupon('screenshot.png')
            await async_send_msg(f'{execution_time},{firefox_profile_path}')
            list1['E'][schet_profil].value = 1  # Получаем значение из колонки 'E'
            book.save(r"te-g.xlsx")
            await context.close()

async def main():
    global schet_profil  # если используете глобальную переменную

    while True:
        try:
            excel_file_path = "numb.xlsx"  # Укажите путь к вашему Excel-файлу
            df = pd.read_excel(excel_file_path)
            endd = actual_none_profil()

            firefox_profiles = df.iloc[:, 1].dropna().tolist()  # Предполагается, что пути в первом столбце
            print(firefox_profiles[schet_profil - 1])  # Выводим список профилей для проверки
            await run_profile(firefox_profiles[schet_profil - 1])
            #await asyncio.gather(*(run_profile(profile) for profile in firefox_profiles[:5]))

        except Exception as e:

            if schet_profil - 1 >= len(firefox_profiles):
                error_text = f"Ошибка: {repr(e)}"
                print(error_text)
                await async_send_msg(error_text)
                await async_send_msg(f'{obshee_vremya}')



                print(f"Произошла ошибка при клике: {e} ❌")

                return False
def run_with_retries():
    while True:
        try:
            asyncio.run(main())
            break
        except Exception as e:
            print(f"Ошибка в main(): {e}. Перезапускаем...")



if __name__ == "__main__":
    run_with_retries()

