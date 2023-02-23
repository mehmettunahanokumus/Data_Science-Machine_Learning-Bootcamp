#################################################
# Python Alistirmalar
#################################################

#################################################
# Gorev 1: Verilen degerlerin veri yapilarini inceleyiniz.
#################################################

x = 8
y = 3.2
z = 8j + 12
a = 'Hello World'
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {'Name': 'Jake',
     'Age': 27,
     'Address': 'Downtown'}
t = ('Machine Learning', 'Data Science')
s = {'Python', 'Machine Learning', 'Data Science'}

var = [x, y, z, a, b, c, l, d, t, s]

for index, i in enumerate(var):
    print(index, type(i))

#################################################
# Gorev 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
#################################################

text = "The goal is to turn data into information, and information into insight."

(text.upper()).split()

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

# Adım 1: Verilen listenin eleman sayısına bakın.

len(lst)

# Adım 2: Sıfırıncı ve onuncu index'teki elemanları çağırın.

print(lst[0], lst[10])

# Adım 3: Verilen liste üzerinden ["D","A","T","A"] listesi oluşturun.

d_lst =  (lst[0:4])
print(d_lst)

# Adım 4: Sekizinci index'teki elemanı silin.

lst.remove(lst[8])

# Adım 5: Yeni bir eleman ekleyin.

lst.append('s')
lst.remove(lst[-2])

# Adım 6: Sekizinci index'e  "N" elemanını tekrar ekleyin.

lst.insert(8, 'N')

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()

# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict['Daisy'] = ['England', 13]

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict['Ahmet'] = ['Turkey', 24]

# Adım 5: Antonio'yu dictionary'den siliniz.

dict.pop('Antonio')



###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan
# ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]

def even_odd(list):
    odd = []
    even = []
    for l in list:
        if l % 2 == 0:
            odd.append(l)
        else:
            even.append(l)
    return odd, even

odd, even = even_odd(l)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken
# son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
# fakulte = ['Muhendislik Fakultesi', 'Tip Fakultesi']

for index, students in enumerate(ogrenciler, 1):
    if index <= 3:
        print('Muhendislik Ogrencisi ' + str(index) + '.' + 'ogrencisi: ' + students)
    else:
        print('Tip Ogrencisi ' + str(index - 3) + '.' + 'ogrencisi: ' + students)

###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu,
# kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for k, d, n in zip(kredi, ders_kodu, kontenjan):
    print('Kredisi %s olan %a kodlu dersin kontenjani %u kisidir.' % (k, d, n))


###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

kume1.issuperset(kume2)
kume2.difference(kume1)

if kume1.issuperset(kume2) == True:
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))




