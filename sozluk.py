import pymysql


def selamla():
    print("Hoşgeldin!")


def mod_sorgula():
    return input(" Standart mod için s"
              " Rasgele mod için r   giriniz: ")


def secim_sorgula():
    temp = input("Turkçe     ->  İngilizce için t \n"
                  "İngilizce  ->  Türkçe    için e giriniz: ")
    secenek = "en"
    if temp == "t":
        secenek = "tr"
    return secenek


def random_mode(anahtar):
    cur.execute("SELECT {}Word FROM {} ORDER BY RAND() LIMIT 1".format(anahtar, anahtar))
    kelime = str(cur.fetchone())[2:-3]
    print("-"*25,"{}".format(kelime),"-"*25)
    getir(anahtar, kelime)


def standart(mod):

    if mod == "tr":
        kelime = kelime_sor(mod)
        getir(mod, kelime)
    else:
        mod = "en"
        kelime = kelime_sor(mod)
        getir(secim, kelime)


def getir(tercih, kelime):
    cur.execute("SELECT {}Description FROM {} WHERE {}Word='{}'".format(tercih, tercih, tercih, kelime))
    print(str(cur.fetchall())[3:-6])


def kelime_sor(t):
    sorgu = input("{} kelimeyi giriniz: ".format(t))
    return sorgu




def dongu(modumuz, secimimiz):
    i = 1
    if modumuz == "s":
        while i != "0":
            standart(secimimiz)
            i = input("cikmak icin 0 girin: ")
            print("*" * 100)
    else:
        while i != "0":
            random_mode(secimimiz)
            i = input("cikmak icin 0 girin: ")
            print("*" * 100)

def hoscakal():
    print("Güle güle :)")
selamla()


db = pymysql.connect(host="localhost",
                     	user="root",
                     	passwd="1",
                     	db="deneme",
                     	charset="utf8")
cur = db.cursor()
mod = mod_sorgula()
secim = secim_sorgula()
dongu(mod, secim)
hoscakal()
db.close()

