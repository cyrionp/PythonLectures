sepet = []
durum = True
tutar = 0


everything = {
    "1":
    {
        "kategori": "Tabletler",
        "markalar": {
            "1": {"marka": "Apple",
                  "ürünler": {"1": {"isim": "iPad Pro 32 GB", "price": "4000"}, "2": {"isim": "iPad Pro 16 GB", "price": "3000"},
                              "3": {"isim": "iPad Pro 8 GB", "price": "2000"}, "4": {"isim": "iPad Pro 64 GB", "price": "5000"}, "5": {"isim": "iPad Pro 128 GB", "price": "6000"}}},
            "2": {"marka": "Samsung",
                  "ürünler": {"1": {"isim": "Galaxy A 8 GB", "price": "1000"}, "2": {"isim": "Galaxy A 16 GB", "price": "2000"},
                              "3": {"isim": "Galaxy A 32 GB", "price": "3000"}, "4": {"isim": "Galaxy A 64 GB", "price": "4000"}, "5": {"isim": "Galaxy A 128 GB", "price": "5000"}}},

            "3": {"marka": "Huawei",
                  "ürünler": {"1": {"isim": "Tab 3 8GB", "price": "1000"}, "2": {"isim": "Tab 4 16GB", "price": "2000"},
                              "3": {"isim": "Tab 4 32 GB", "price": "3000"}, "4": {"isim": "Tab 4 64 GB", "price": "4000"}, "5": {"isim": "Tab 4 128 GB", "price": "5000"}}}

        }
    },
    "2": {
             "kategori": "Telefonlar",
        "markalar": {
            "1": {"marka": "Apple",
                  "ürünler": {"1": {"isim": "iPhone11 Pro 32 GB", "price": "4000"}, "2": {"isim": "iPhone11 Pro 16 GB", "price": "3000"},
                              "3": {"isim": "iPhone11 Pro 8 GB", "price": "2000"}, "4": {"isim": "iPhone11 Pro 64 GB", "price": "5000"}, "5": {"isim": "iPhone11 Pro 128 GB", "price": "6000"}}},
            "2": {"marka": "Samsung",
                  "ürünler": {"1": {"isim": "Galaxy Note 10 8 GB", "price": "1000"}, "2": {"isim": "Galaxy Note 10 16 GB", "price": "2000"},
                              "3": {"isim": "Galaxy Note 10 32 GB", "price": "3000"}, "4": {"isim": "Galaxy Note 10 64 GB", "price": "4000"}, "5": {"isim": "Galaxy Note 10 128 GB", "price": "5000"}}},

            "3": {"marka": "Huawei",
                  "ürünler": {"1": {"isim": "Huawei P30 8GB", "price": "1000"}, "2": {"isim": "Huawei P30 16GB", "price": "2000"},
                              "3": {"isim": "Huawei P30 32 GB", "price": "3000"}, "4": {"isim": "Huawei P30 64 GB", "price": "4000"}, "5": {"isim": "Huawei P30 128 GB", "price": "5000"}}}

          }},
            
         "3": {
             "kategori": "Ev Aletleri",
        "markalar": {
            "1": {"marka": "Arçelik",
                  "ürünler": {"1": {"isim": "Süpürge", "price": "4000"}, "2": {"isim": "Fırın", "price": "3000"},
                              "3": {"isim": "Mutfak Robotu", "price": "2000"}, "4": {"isim": "Ocak", "price": "5000"}, "5": {"isim": "Klima", "price": "6000"}}},
            "2": {"marka": "Vestel",
                  "ürünler": {"1": {"isim": "Süpürge", "price": "1000"}, "2": {"isim": "Fırın", "price": "2000"},
                              "3": {"isim": "Mutfak Robotu", "price": "3000"}, "4": {"isim": "Ocak", "price": "4000"}, "5": {"isim": "Klima", "price": "5000"}}},

            "3": {"marka": "Beko",
                  "ürünler": {"1": {"isim": "Süpürge", "price": "1000"}, "2": {"isim": "Fırın", "price": "2000"},
                              "3": {"isim": "Mutfak Robotu", "price": "3000"}, "4": {"isim": "Ocak", "price": "4000"}, "5": {"isim": "Klima", "price": "5000"}}}   

}},
            
"4": {
             "kategori": "Aksesuar",
        "markalar": {
            "1": {"marka": "iPhone",
                  "ürünler": {"1": {"isim": "Sarj Aleti", "price": "400"}, "2": {"isim": "Kulaklık", "price": "300"},
                              "3": {"isim": "Kılıf", "price": "200"}, "4": {"isim": "Bluetooth Kulaklık", "price": "500"}, "5": {"isim": "Sarjlı Kılıf", "price": "600"}}},
            "2": {"marka": "Samsung",
                  "ürünler": {"1": {"isim": "Sarj Aleti", "price": "100"}, "2": {"isim": "Kulaklık", "price": "200"},
                              "3": {"isim": "Kılıf", "price": "300"}, "4": {"isim": "Bluetooth Kulaklık", "price": "400"}, "5": {"isim": "Sarjlı Kılıf", "price": "500"}}},

            "3": {"marka": "Huawei",
                  "ürünler": {"1": {"isim": "Sarj Aleti", "price": "100"}, "2": {"isim": "Kulaklık", "price": "200"},
                              "3": {"isim": "Kılıf", "price": "300"}, "4": {"isim": "Bluetooth Kulaklık", "price": "400"}, "5": {"isim": "Sarjlı Kılıf", "price": "500"}}}   

}},
            
      "5": {
             "kategori": "Oyun Konsolları",
        "markalar": {
            "1": {"marka": "Nintendo",
                  "ürünler": {"1": {"isim": "Nintendo 250 GB", "price": "4000"}, "2": {"isim": "Nintendo 500 GB", "price": "5000"},
                              "3": {"isim": "Nindendo Wii ", "price": "2000"}, "4": {"isim": "Nintendo 1 TB", "price": "6000"}, "5": {"isim": "Nintendo Wii +", "price": "6000"}}},
            "2": {"marka": "Xbox",
                  "ürünler": {"1": {"isim": "Xbox 360", "price": "1000"}, "2": {"isim": "Xbox One", "price": "2000"},
                              "3": {"isim": "Xbox One S", "price": "3000"}, "4": {"isim": "Xbox One X", "price": "4000"}, "5": {"isim": "Xbox One X Special Edition", "price": "5000"}}},

            "3": {"marka": "Play Station",
                  "ürünler": {"1": {"isim": "PS 3 500 GB", "price": "1000"}, "2": {"isim": "PS 3 1 TB", "price": "2000"},
                              "3": {"isim": "PS 4 500 GB", "price": "3000"}, "4": {"isim": "PS 4 1 TB", "price": "4000"}, "5": {"isim": "PS 5 1 TB", "price": "15000"}}}   

}}      


} 
while durum == True:
    print("---Kategori Seçiniz---")
    for key in everything:
        print(str(key) + "--" + everything[key]["kategori"])
    
    kategori = input("Kategori Seçimi: ")
    if int(kategori) > 5:
        print("*****Yanlış Tuşlama*****")
        print("------------------------")
    else:
        print("---Marka Giriniz---")
        for key in everything[kategori]["markalar"]:
            print(str(key)+"--"+everything[kategori]["markalar"][key]["marka"])
        
        marka = input("Marka Seçimi: ")
        if int(marka) > 3:
            print("*****Yanlış Tuşlama*****")
        else:
            
            print("------------------------")
            for key in everything[kategori]["markalar"][marka]["ürünler"]:
                isim = everything[kategori]["markalar"][marka]["ürünler"][key]["isim"]
                fiyat = everything[kategori]["markalar"][marka]["ürünler"][key]["price"]
                print(key+"--"+isim+": "+fiyat+" TL")
            
            eklenecek_item = input("Ürün seçin: ")
            if int(eklenecek_item) > 5:
                print("*****Yanlış Tuşlama*****")
                print("------------------------")
            else:
                
                sepet.append({"isim":everything[kategori]["markalar"][marka]["ürünler"][eklenecek_item]["isim"],
                              "fiyat":everything[kategori]["markalar"][marka]["ürünler"][eklenecek_item]["price"]})
                
                
                print("Alışverişe Devam Etmek İstiyor musunuz ? ")
                print("1- Alışverişe Devam Et")
                print("2- Sepete Git")
                devamDurum = input("Seçim Giriniz : ")
                
                if devamDurum == "2":
                    durum = False
    

print("---Alışveriş Sepetiniz---")   
for i in range(len(sepet)):
    print(str(i + 1) + " - " + sepet[i]["isim"] + " => " + sepet[i]["fiyat"])
    tutar = tutar + int(sepet[i]["fiyat"])
print("Toplam Tutar : " + str(tutar))
print("-------------------")
print("---Müşteri Bilgileri---")
input("Adres : ")
input("Telefon Numarası :")
input("E-Mail : ")
print("-- Ödeme Yöntemi Seçiniz --")
print("1- Kapıda Ödeme :")
print("2- Kredi Kartı : ")
ödemesecimi = int(input("Seçim : "))
if ödemesecimi == 2:
    print("------------")
    input("Kredi Kartı Üzerinde Yazan İsim : ")
    input("Kredi Kartı Numarası : ")
    input("CVV : ")
    
print("*****  Alışverişiniz için Teşekkür Ederiz ***** ")
