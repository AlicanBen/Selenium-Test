# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 23:39:59 2019

@author: Ali Can BEN
"""

from selenium import webdriver
import time

# ONURAIR'IN SITESINE CHROME  UZERINDEN GIRIS

browser= webdriver.Chrome()
browser.get("https://www.onurair.com/tr/")
time.sleep(5) # SITENIN YUKLENMESINI BEKLEMEK ICIN

# ELEMENTI BULMAK VE ELEMENTE TIKLAMAK
nereden_menu_secimi=browser.find_element_by_xpath( '//*[@id="depPort"]/optgroup[1]/option[3]')
nereden_menu_secimi.click()
time.sleep(5)

nereye_menu_secimi=browser.find_element_by_xpath( '//*[@id="arrPort"]/optgroup[1]/option[3]')
nereye_menu_secimi.click()
time.sleep(5)

tek_yon_secimi=browser.find_element_by_xpath( '//*[@id="radio"]/tbody/tr/td[2]')
tek_yon_secimi.click()
time.sleep(5)

tarih_menu_click=browser.find_element_by_xpath( '//*[@id="departureDate"]')
tarih_menu_click.click()
time.sleep(5)

tarih_secim=browser.find_element_by_xpath( '/html/body/div[1]/div[1]/table/tbody/tr[5]/td[4]')
tarih_secim.click()
time.sleep(5)


islem_devam=browser.find_element_by_xpath( '//*[@id="btnSearch"]')
islem_devam.click()
time.sleep(5)