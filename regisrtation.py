import random
import time
#from spiski_klichek import *
import openpyxl

from func_dir_foto import *
from vizual import *
from  func import *
from playwright.async_api import async_playwright


# book1 = openpyxl.open(r"te-g.xlsx")
# list11 = book.active
async def regisrations(page,schet_profil,list1,book):
    #time.sleep(22222)
    #пора навести порядок
    del_foto_dir(r'начать игру')
    spis_foto = copy_foto_dir(r'начать игру')
    await click_image(page, spis_foto, 5)
    del_foto_dir(r'начать игру')
    #коврик
    await page.mouse.click(578, 577)
    time.sleep(1)
    #тапочки

    time.sleep(1)
    #await page.screenshot(path='screenshot343.png')
    #time.sleep(22222)

    await page.mouse.click(659, 376)
    time.sleep(1)

    #мяч
    await page.mouse.click(568, 464)
    time.sleep(1)
    #подушка
    await page.mouse.click(751, 391)
    time.sleep(1)

    #подушка2
    await page.mouse.click(763, 521)
    time.sleep(1)

    #плед
    await page.mouse.click(738, 434)
    time.sleep(1)
    # подушка3
    await page.mouse.click(505, 474)
    # коврик
    await page.mouse.click(578, 577)
    time.sleep(1)
    # тапочки
    await page.mouse.click(511, 394)
    time.sleep(1)
    #time.sleep(1)
#     #посетить центр
#     del_foto_dir(r'posetit_centr')
#     spis_foto = copy_foto_dir(r'posetit_centr')
#     await click_image(page, spis_foto, 5)
#     del_foto_dir(r'posetit_centr')
#     time.sleep(1)
#     del_foto_dir(r'posetit_centr')
#     spis_foto = copy_foto_dir(r'posetit_centr')
#     await click_image(page, spis_foto, 5)
#     del_foto_dir(r'posetit_centr')
#     time.sleep(1)
#     del_foto_dir(r'posetit_centr')
#     spis_foto = copy_foto_dir(r'posetit_centr')
#     await click_image(page, spis_foto, 5)
#     del_foto_dir(r'posetit_centr')
#     time.sleep(1)
#     del_foto_dir(r'posetit_centr')
#     spis_foto = copy_foto_dir(r'posetit_centr')
#     await click_image(page, spis_foto, 5)
#     del_foto_dir(r'posetit_centr')
#     #щенок
#     del_foto_dir(r'shenok')
#     spis_foto = copy_foto_dir(r'shenok')
#     await click_image(page,spis_foto,5)
#     del_foto_dir(r'shenok')
#     time.sleep(5)
# #кличку дать
#     text = random.choice(dog_names)
#     del_foto_dir(r'klichka')
#     spis_foto = copy_foto_dir(r'klichka')
#     await click_image(page, spis_foto, 5)
#     del_foto_dir(r'klichka')
#     await page.keyboard.type(text)
#     time.sleep(1)
#     del_foto_dir(r'nazvat')
#     spis_foto = copy_foto_dir(r'nazvat')
#     await click_image(page, spis_foto, 5)
#     del_foto_dir(r'nazvat')
    time.sleep(2)
#действия в игре
    spis_game=['korm','poiti','lakomstvo','game','vetirinar','love']
    for i in spis_game:
        time.sleep(1)
        del_foto_dir(i)
        spis_foto = copy_foto_dir(i)
        await click_image(page, spis_foto, 5)
        del_foto_dir(i)
        time.sleep(2)
        del_foto_dir('zakrit')
        spis_foto = copy_foto_dir('zakrit')
        await click_image(page, spis_foto, 5)
        del_foto_dir('zakrit')



    await search_element_xpath(page, "//html/body/div[1]/div/div/main/form/div/div/div[3]/button", 5)
    list1['E'][schet_profil].value = 1 # Получаем значение из колонки 'E'
    book.save(r"te-g.xlsx")


async def vhod_po_frame(page,schet_profil,list1,book):
    # знак участвовать
    del_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\znak_ychastvovat')
    spis_foto = copy_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\znak_ychastvovat')
    await click_image(page, spis_foto, 5)
    del_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\znak_ychastvovat')
    time.sleep(1)
    #личный кабинет
    del_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\znak_ychastvovat\lichnii_cabinet')
    spis_foto = copy_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\znak_ychastvovat\lichnii_cabinet')
    await click_image(page, spis_foto, 5)
    del_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\znak_ychastvovat\lichnii_cabinet')
    # launch
    del_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\launch')
    spis_foto = copy_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\launch')
    await click_image(page, spis_foto, 5)
    del_foto_dir(r'D:\ПРОЕКТЫ ПАЙЧАРМ\ТЕЛЕГРАММ ПРОЕКТЫ\черноголовка\START\launch')
    # получаем ссылку фрейма
    time.sleep(5)
    ssilka_na_sait = await get_src_value(page, "payment-verification")
    list1['D'][schet_profil].value = ssilka_na_sait  # Получаем значение из колонки 'E'

    book.save(r"te-g.xlsx")
    await page.goto(ssilka_na_sait)