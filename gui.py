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





window = Tk()

window.geometry("900x600")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=("image_1.png"))
image_1 = canvas.create_image(
    454.0,
    300.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=("entry_1.png"))
entry_bg_1 = canvas.create_image(
    510.99999999999994,
    201.0,
    image=entry_image_1
)
entry_1 = Entry(
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
)

entry_image_2 = PhotoImage(
    file=("entry_2.png"))
entry_bg_2 = canvas.create_image(
    510.99999999999994,
    319.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=289.99999999999994,
    y=299.0,
    width=442.0,
    height=38.0
)

button_image_1 = PhotoImage(
    file=("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://github.com/serkandurmussaglam"),
    relief="flat"
)
button_1.place(
    x=748.0,
    y=16.0,
    width=50.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: webbrowser.open("https://www.linkedin.com/in/serkan-durmus-saglam/"),
    relief="flat"
)
button_2.place(
    x=828.0,
    y=16.0,
    width=50.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: scrape_type(),
    relief="flat"
)
button_3.place(
    x=322.99999999999994,
    y=395.0,
    width=144.0,
    height=44.0
)

button_image_4 = PhotoImage(
    file=("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: clear(),
    relief="flat"
)
button_4.place(
    x=527.0,
    y=395.0,
    width=155.0,
    height=44.0
)

var = IntVar()
a = Radiobutton(window, text="Username", variable=var, value=0)
b = Radiobutton(window, text="Popular", variable=var, value=1)
c = Radiobutton(window, text="Latest", variable=var, value=2)


# Font değişkeni oluşturun ve boyutunu ve yazı tipini ayarlayın
font = Font(family="Times New Roman", size=12)

a.place(x=8, y=150, width=165,
        height=35)
b.place(x=8, y=180, width=165,
        height=35)
c.place(x=8, y=210, width=165,
        height=35)

a.config(font=font)
b.config(font=font)
c.config(font=font)


window.resizable(False, False)
window.mainloop()
