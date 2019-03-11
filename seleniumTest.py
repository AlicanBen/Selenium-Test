# -*- coding: utf-8 -*-
"""
Created on Sat Mar  10 17:37:27 2019

@author: Ali Can BEN
"""

from selenium import webdriver
import time

def fancybox_kapatma(browser):
    try:
        iframe=browser.find_elements_by_tag_name('iframe')[1]
        browser.switch_to.frame(iframe)
        browser.find_element_by_xpath('//*[@id="icon-close-button-1454703945249"]').click()
        time.sleep(1)
    except :
        print(sys.exc_info()[0])
        
        
# ONURAIR'IN SITESINE CHROME  UZERINDEN GIRIS
browser= webdriver.Chrome()
browser.delete_all_cookies()
browser.maximize_window()
browser.get("https://www.onurair.com/tr/")
time.sleep(5) # SITENIN YUKLENMESINI BEKLEMEK ICIN

# KALKIŞ YERİ SEÇİM
nereden_menu_secimi=browser.find_element_by_xpath( '//*[@id="depPort"]/optgroup[1]/option[3]')
nereden_menu_secimi.click()
time.sleep(1)


# İNİŞ YERİ SEÇİM
nereye_menu_secimi=browser.find_element_by_xpath( '//*[@id="arrPort"]/optgroup[1]/option[3]')
nereye_menu_secimi.click()
time.sleep(1)


# TEK YÖN/GİDİŞ-DÖNÜŞ SEÇİM
tek_yon_secimi=browser.find_element_by_xpath( '//*[@id="radio"]/tbody/tr/td[2]')
tek_yon_secimi.click()
time.sleep(1)


# TARİH MENUSU AÇMAK
tarih_menu_click=browser.find_element_by_xpath( '//*[@id="departureDate"]')
tarih_menu_click.click()
time.sleep(1)

# TARİH SEÇİM
tarih_secim=browser.find_element_by_xpath( '/html/body/div[1]/div[1]/table/tbody/tr[5]/td[4]')
tarih_secim.click()
time.sleep(1)

# DEVAM BUTNUYLA BİR SONRAKİ SAYFAYA GEÇİŞ
islem_devam=browser.find_element_by_xpath( '//*[@id="btnSearch"]')
islem_devam.click()
time.sleep(5)


# SAAT VE SINIF SEÇİMİ
saat_fiyat_secimi=browser.find_element_by_xpath('//*[@id="bundleSelectDivId_0_3_0_0"]/div[2]/div[1]/div[1]')
saat_fiyat_secimi.click()
time.sleep(1)

saat_fiyat_secimi_2=browser.find_element_by_xpath('//*[@id="bundleListDivid_0_3_0_0"]/div[2]/ul/li[2]')
saat_fiyat_secimi_2.click()
time.sleep(1)

# DEVAM BUTNUYLA BİR SONRAKİ SAYFAYA GEÇİŞ
saat_fiyat_secimi_devam=browser.find_element_by_xpath('//*[@id="btnContinue"]')
saat_fiyat_secimi_devam.click()
time.sleep(5)

fancybox_kapatma(browser)

# UNVAN SECİMİ
unvan_secim=browser.find_element_by_xpath('//*[@id="tabPax1"]/div/div[2]/span[1]/label')
unvan_secim.click()
time.sleep(1)


unvan_secim2=browser.find_element_by_xpath('//*[@id="tabPax1"]/div/div[2]/span[1]/div/div/div[2]/div/div[2]')
unvan_secim2.click()
time.sleep(1)

# KİSİSEL BİLGİ GİRİŞİ
yolcu_bilgileri_ad_giris= browser.find_element_by_name('name1')
yolcu_bilgileri_ad_giris.send_keys('Selenium')
time.sleep(1)

yolcu_bilgileri_soyad_giris= browser.find_element_by_name('surname1')
yolcu_bilgileri_soyad_giris.send_keys('Test')
time.sleep(1)


uyruk_secim=browser.find_element_by_xpath('//*[@id="nationalityGroup1"]/div/div/div[1]')
uyruk_secim.click()
time.sleep(1)

uyruk_secim2=browser.find_element_by_xpath('//*[@id="nationalityGroup1"]/div/div/div[2]/div/div[1]')
uyruk_secim2.click()
time.sleep(1)


yolcu_bilgileri_natId_giris= browser.find_element_by_name('natId1')
yolcu_bilgileri_natId_giris.send_keys('80669453720')
time.sleep(1)


yolcu_bilgileri_dogum_gun_giris= browser.find_element_by_xpath('//*[@id="bday_day_1-selectized"]')
yolcu_bilgileri_dogum_gun_giris.click()
time.sleep(1)

yolcu_bilgileri_dogum_gun_giris2= browser.find_element_by_xpath('//*[@id="bdateDiv0"]/div[1]/div/div/div[2]/div/div[1]')
yolcu_bilgileri_dogum_gun_giris2.click()
time.sleep(1)

yolcu_bilgileri_dogum_ay_giris= browser.find_element_by_xpath('//*[@id="bday_month_1-selectized"]')
yolcu_bilgileri_dogum_ay_giris.click()
time.sleep(1)

yolcu_bilgileri_dogum_ay_giris2= browser.find_element_by_xpath('//*[@id="bdateDiv0"]/div[2]/div/div/div[2]/div/div[1]')
yolcu_bilgileri_dogum_ay_giris2.click()
time.sleep(1)

yolcu_bilgileri_dogum_yıl_giris= browser.find_element_by_xpath('//*[@id="bday_year_1-selectized"]')
yolcu_bilgileri_dogum_yıl_giris.click()
time.sleep(1)

yolcu_bilgileri_dogum_yıl_giris2= browser.find_element_by_xpath('//*[@id="bdateDiv0"]/div[3]/div/div/div[2]/div/div[11]')
yolcu_bilgileri_dogum_yıl_giris2.click()
time.sleep(1)


iletisim_bilgileri_telefon_giris= browser.find_element_by_xpath('//*[@id="frst-tel-number0"]')
iletisim_bilgileri_telefon_giris.send_keys('5341111111')
time.sleep(1)


iletisim_bilgileri_ePosta_giris= browser.find_element_by_xpath('//*[@id="email0"]')
iletisim_bilgileri_ePosta_giris.send_keys('example@example.com')
time.sleep(1)


# DEVAM BUTNUYLA BİR SONRAKİ SAYFAYA GEÇİŞ
islem_devam2= browser.find_element_by_xpath('//*[@id="btnSave"]')
islem_devam2.click()
time.sleep(5)


# NİTELİKLİ BİLET RET SEÇİMİ
nitelikli_bilet_ret= browser.find_element_by_xpath('//*[@id="QFTK"]/tbody/tr[2]/td/label')
nitelikli_bilet_ret.click()
time.sleep(1)

# DEVAM BUTNUYLA BİR SONRAKİ SAYFAYA GEÇİŞ
islem_devam3= browser.find_element_by_xpath('//*[@id="addSSRContinueBTn"]')
islem_devam3.click()
time.sleep(5)


# KREDİ KARTI BİLGİLERİ GİRİŞ
kredi_kart_sahibi_giris= browser.find_element_by_xpath('//*[@id="card-owner"]')
kredi_kart_sahibi_giris.send_keys('Selenium Test')
time.sleep(1)

kredi_kart_numarasi_giris= browser.find_element_by_xpath('//*[@id="card-number"]')
kredi_kart_numarasi_giris.send_keys('1234 5678 9012 3456')
time.sleep(1)


kredi_kart_son_ay_giris2= browser.find_element_by_xpath('//*[@id="expiry-month"]/option[2]')
kredi_kart_son_ay_giris2.click()
time.sleep(1)

kredi_kart_son_yil_giris= browser.find_element_by_xpath('//*[@id="expiry-year"]/option[6]')
kredi_kart_son_yil_giris.click()
time.sleep(1)

kredi_kart_cvc_giris= browser.find_element_by_xpath('//*[@id="cvc"]')
kredi_kart_cvc_giris.send_keys('111')
time.sleep(1)

# SÖZLEŞME ŞARTLARI KABUL
sozlesme_sartlari_kabul= browser.find_element_by_xpath('//*[@id=\"rules-and-conditions\"]/div/label')
sozlesme_sartlari_kabul.click()
time.sleep(1)


"""
SON AŞAMA SATIN ALMA
satın_alma= browser.find_element_by_xpath('//*[@id="btnBuy"]')
satın_alma.click()
time.sleep(5)
"""

