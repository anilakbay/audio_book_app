import PyPDF2
from gtts import gTTS
import os
import tkinter as tk
from tkinter import filedialog


def pdf_metni_cikart(pdf_yolu):
    metin = ''
    pdf_okuyucu = PyPDF2.PdfReader(open(pdf_yolu, 'rb'))               # binary = rb
    for sayfa_num in range(len(pdf_okuyucu.pages)):
        metin += pdf_okuyucu.pages[sayfa_num].extract_text()
    return metin

#metni sesli hale getiren fonksiyon

def metni_sese_cevir(metin, cikti_dosyasi):
    sesli_cevirici = gTTS(text=metin, lang='tr')
    sesli_cevirici.save(cikti_dosyasi)

#dosya seçme fonksiyonu

def dosya_sec():
    dosya_yolu = filedialog.askopenfilename(filetypes=[("PDF Dosyaları", "*pdf")])
    if dosya_yolu:
        pdf_metin = pdf_metni_cikart(dosya_yolu)
        metni_sese_cevir(pdf_metin, "kaydet.mp3")
        os.system("start kaydet.mp3")

#tkinter arayüzü

app = tk.Tk()
app.title("Sesli Kitap Uygulaması")
app.geometry("250x150")

secim_butonu = tk.Button(app, text="PDF Seç", command=dosya_sec, padx=20, pady=20)
secim_butonu.pack(pady=30)

app.mainloop()
