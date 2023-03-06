from tkinter import *
import webbrowser
from tkinter import messagebox
import snscrape.modules.twitter as sntwitter
import pandas as pd
import numpy as np
import tqdm
import os
from tkinter.font import Font

messagebox.showwarning(
    "Uyarı !!!", "Bu program Serkan Durmuş Sağlam tarafından kodlanmıştır.\nKopyalanması/çoğaltılması ve izinsiz satılması yasaktır.")


def user_data():
    # Scrape buton fonksiyonu
    username = entry_1.get()
    tw_count = int(entry_2.get())

    # Web kazıma yapacağımız objeyi oluşturuyoruz.
    scraper = sntwitter.TwitterUserScraper(username)

    # Girilen sayı kadar tweeti çekiyoruz.
    tweets = []
    for tweet in tqdm.tqdm(scraper.get_items(), desc="Tweetler alınıyor", total=tw_count, bar_format="{l_bar}{bar}{r_bar}"):
        if len(tweets) > tw_count:
            break
        tweets.append(tweet)

    # Tweetleri içerik ve tarih olarak ayırıyoruz.
    data = [[tweet.content, tweet.date, tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.replyCount, tweet.url]
            for tweet in tweets]

    # Dataframe işlemleri.
    df = pd.DataFrame(data)
    df.columns = ["Tweet", "Date", "Like", "Retweet", "Quote", "Reply", "Url"]
    df['Date'] = df['Date'] + np.timedelta64(3, 'h')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Excel dosyasını kaydetme.
    df.to_excel(
        f'{username}_{tw_count}.xlsx', index=True)

    os.system('cls')
    print("İşlem tamamlandı!")

def word_popular():
    keyword = entry_1.get()
    tw_count = int(entry_2.get())

    # Tweetleri çekmek için Twitter modülünü kullanıyoruz.
    scraper = sntwitter.TwitterSearchScraper(query=f"{keyword} min_faves:1000")

    # Girilen sayı kadar tweeti çekiyoruz.
    tweets = []
    for tweet in tqdm.tqdm(scraper.get_items(), desc="Tweetler alınıyor", total=tw_count, bar_format="{l_bar}{bar}{r_bar}"):
        if len(tweets) >= tw_count:
            break
        tweets.append(tweet)

    # Tweetleri içerik ve tarih olarak ayırıyoruz.
    data = [[tweet.content, tweet.date, "@"+tweet.username,
             tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.replyCount, tweet.url] for tweet in tweets]

    # Dataframe işlemleri.
    df = pd.DataFrame(data)
    df.columns = ["Tweet", "Date","Username", "Like", "Retweet", "Quote", "Reply", "Url"]
    df['Date'] = df['Date'] + np.timedelta64(3, 'h')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Excel dosyasını kaydetme.
    df.to_excel(
        f'{keyword}_{tw_count}.xlsx', index=True)

    os.system('cls')
    print("İşlem tamamlandı!")

def word_latest():
    keyword = entry_1.get()
    tw_count = int(entry_2.get())

    # Tweetleri çekmek için Twitter modülünü kullanıyoruz.
    scraper = sntwitter.TwitterSearchScraper(query=keyword)

    # Girilen sayı kadar tweeti çekiyoruz.
    tweets = []
    for tweet in tqdm.tqdm(scraper.get_items(), desc="Tweetler alınıyor", total=tw_count, bar_format="{l_bar}{bar}{r_bar}"):
        if len(tweets) >= tw_count:
            break
        tweets.append(tweet)

    # Tweetleri içerik ve tarih olarak ayırıyoruz.
    data = [[tweet.content, tweet.date, "@"+tweet.username,
             tweet.likeCount, tweet.retweetCount, tweet.quoteCount, tweet.replyCount, tweet.url] for tweet in tweets]

    # Dataframe işlemleri.
    df = pd.DataFrame(data)
    df.columns = ["Tweet", "Date","Username" , "Like", "Retweet", "Quote", "Reply", "Url"]
    df['Date'] = df['Date'] + np.timedelta64(3, 'h')
    df['Date'] = df['Date'].dt.strftime('%Y-%m-%d %H:%M:%S')

    # Excel dosyasını kaydetme.
    df.to_excel(
        f'{keyword}_{tw_count}.xlsx', index=True)

    os.system('cls')
    print("İşlem tamamlandı!")

# Veri çekme tipine göre fonksiyon çağrılıyor.
def scrape_type():
    if var.get() == 0:
        user_data()
    elif var.get() == 1:
        word_popular()
    else:
        word_latest()
        
# Ekran temizleme fonksiyonu
def clear():
    # Clear buton fonksiyonu
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    print("Ekran temizlendi.")





window = Tk()  # tkinter kütüphanesindeki Tk sınıfıyla bir pencere oluşturuluyor.

window.geometry("900x600")  # Oluşturulan pencerenin boyutu 900x600 piksel olarak ayarlanıyor.
window.configure(bg="#FFFFFF")  # Oluşturulan pencerenin arka plan rengi beyaz (#FFFFFF) olarak ayarlanıyor.

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=600,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)  # Pencere içinde bir canvas (çizim alanı) oluşturuluyor.

canvas.place(x=0, y=0)  # Canvas, pencere içinde sol üst köşeye yerleştiriliyor.

image_image_1 = PhotoImage(file=("image_1.png"))  # "image_1.png" dosyasından bir resim oluşturuluyor.
image_1 = canvas.create_image(  # Canvas içinde bir resim oluşturuluyor.
    454.0,
    300.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(file=("entry_1.png"))  # "entry_1.png" dosyasından bir resim oluşturuluyor.
entry_bg_1 = canvas.create_image(  # Canvas içinde bir resim oluşturuluyor.
    510.99999999999994,
    201.0,
    image=entry_image_1
)
entry_1 = Entry(  # Tkinter Entry sınıfıyla bir metin kutusu oluşturuluyor.
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=289.99999999999994,
    y=181.0,
    width=442.0,
    height=38.0
)  # Metin kutusu, canvas içinde belirtilen konuma yerleştiriliyor.

entry_image_2 = PhotoImage(file=("entry_2.png"))  # "entry_2.png" dosyasından bir resim oluşturuluyor.
entry_bg_2 = canvas.create_image(  # Canvas içinde bir resim oluşturuluyor.
    510.99999999999994,
    319.0,
    image=entry_image_2
)
entry_2 = Entry(  # Tkinter Entry sınıfıyla bir metin kutusu oluşturuluyor.
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(  # Metin kutusu, canvas içinde belirtilen konuma yerleştiriliyor.
    x=289.99999999999994,
    y=299.0,
    width=442.0,
    height=38.0
)  

# "button_1.png" dosyasından bir fotoğraf nesnesi oluşturun
button_image_1 = PhotoImage(
    file=("button_1.png"))

# "https://github.com/serkandurmussaglam" adresini açacak olan bir buton nesnesi oluşturun
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://github.com/serkandurmussaglam"),
    relief="flat"
)

# Butonu belirtilen koordinatlara yerleştirin ve boyutunu belirleyin
button_1.place(
    x=748.0,
    y=16.0,
    width=50.0,
    height=50.0
)

# "button_2.png" dosyasından bir fotoğraf nesnesi oluşturun
button_image_2 = PhotoImage(
    file=("button_2.png"))

# "https://www.linkedin.com/in/serkan-durmus-saglam/" adresini açacak olan bir buton nesnesi oluşturun
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://www.linkedin.com/in/serkan-durmus-saglam/"),
    relief="flat"
)

# Butonu belirtilen koordinatlara yerleştirin ve boyutunu belirleyin
button_2.place(
    x=828.0,
    y=16.0,
    width=50.0,
    height=50.0
)

# "button_3.png" dosyasından bir fotoğraf nesnesi oluşturun
button_image_3 = PhotoImage(
    file=("button_3.png"))

# scrape_type() adlı bir fonksiyonu çağıracak olan bir buton nesnesi oluşturun
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: scrape_type(),
    relief="flat"
)

# Butonu belirtilen koordinatlara yerleştirin ve boyutunu belirleyin
button_3.place(
    x=322.99999999999994,
    y=395.0,
    width=144.0,
    height=44.0
)

# "button_4.png" dosyasından bir fotoğraf nesnesi oluşturun
button_image_4 = PhotoImage(
    file=("button_4.png"))

# clear() adlı bir fonksiyonu çağıracak olan bir buton nesnesi oluşturun
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear(),
    relief="flat"
)

# Butonu belirtilen koordinatlara yerleştirin ve boyutunu belirleyin
button_4.place(
    x=527.0,
    y=395.0,
    width=155.0,
    height=44.0
)

# Bir IntVar nesnesi oluşturun
var = IntVar()

# 3 değişken oluşturun ve bu değişkenleri radyo düğmeleri olarak ayarlayın
a = Radiobutton(window, text="Username", variable=var, value=0)
b = Radiobutton(window, text="Popular", variable=var, value=1)
c = Radiobutton(window, text="Latest", variable=var, value=2)


# Font değişkeni oluşturun ve boyutunu ve yazı tipini ayarlayın
font = Font(family="Times New Roman", size=12)

# Radio buttonların yerlerini ayarlayın.
a.place(x=8, y=150, width=165,
        height=35)
b.place(x=8, y=180, width=165,
        height=35)
c.place(x=8, y=210, width=165,
        height=35)

# Radio button font ayarlayın.
a.config(font=font)
b.config(font=font)
c.config(font=font)

#Pencere boyutunu sabitleyin ve bir döngü içinde çalıştırın.
window.resizable(False, False)
window.mainloop()
