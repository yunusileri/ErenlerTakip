import os
import xlwt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def ogrencileri_al(ogrenciler):
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('öğrenciler')
    sheet.write(0, 0, 'TC')
    sheet.write(0, 1, 'İSİM')
    sheet.write(0, 2, 'Doğum Tarihi')
    sheet.write(0, 3, 'Tel')
    sheet.write(0, 4, 'AOL')
    sheet.write(0, 5, 'Veli')
    sheet.write(0, 6, 'Veli Tel')
    sheet.write(0, 7, 'Adres')
    sheet.write(0, 8, 'Aktif')
    for y, ogrenci in enumerate(ogrenciler):
        sheet.write((y + 1), 0, ogrenci.tc)
        sheet.write((y + 1), 1, ogrenci.ad_soyad)
        sheet.write((y + 1), 2, str(ogrenci.dogum_tarihi))
        sheet.write((y + 1), 3, ogrenci.tel)
        sheet.write((y + 1), 4, ogrenci.aol_no)
        sheet.write((y + 1), 5, ogrenci.veli_ad)
        sheet.write((y + 1), 6, ogrenci.veli_tel)
        sheet.write((y + 1), 7, ogrenci.adres)
        sheet.write((y + 1), 8, ogrenci.aktif)
    workbook.save(f'{BASE_DIR}/static/öğrenciler.xls')
