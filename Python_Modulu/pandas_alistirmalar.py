

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################

df = sns.load_dataset('titanic')

#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df['sex'].value_counts()

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

df.columns.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df['pclass'].unique()

#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

df['pclass'].nunique()
df['parch'].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df['embarked'].dtype
df.embarked = df['embarked'].astype('category')


#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df[df['embarked'] == 'C'].head()

#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df[df['embarked'] != 'S'].head()

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df[(df["age"] < 30) & (df["sex"] == "female")].head()

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df[(df['fare'] > 500) | (df['age'] > 70)].head()

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################

df.isnull().sum()
df.isnull().sum().sort_values(ascending=False)

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df = df.drop('who', axis=1, inplace=True)
df.head()

#########################################
# Görev 13: deck değikenindeki boş değerleri deck değişkenin
# en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df.mode()
df['deck'].mode()
df['deck'].fillna(df['deck'].mode()[0])

#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df['age'].fillna(df['age'].median())

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında
# sum, count, mean değerlerini bulunuz.
#########################################

df.groupby("survived").agg({"pclass": ["mean", "sum", "count"],
                       "survived": ["mean", "sum", "count"]})

#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında
# bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

df['age'].apply(lambda x: 1 if x < 30 else 0)
df['age_flag'] = df['age'].apply(lambda x: 1 if x < 30 else 0)
df['age_flag'].head()

#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

import seaborn as sns
tps = sns.load_dataset('tips')
tps.head()

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre
# total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

tps.groupby('time').agg({'total_bill': ['min', 'max', 'mean']})

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

tps.groupby(['day', 'time']).agg({'total_bill': ['min', 'max', 'mean']})

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve
# tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

tps[(tps['time'] == 'Lunch') & (tps['sex'] == 'Female')].groupby('day').agg({
    'total_bill': ['sum', 'min', 'max', 'mean'], 'tip': ['sum', 'min', 'max', 'mean']
})
#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

tps.loc[(tps['size']<3) & (tps['total_bill']>10), 'total_bill'].mean()
# tps['total_bill'][(tps['size'] < 3) & (tps['total_bill'] > 10)].mean()

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun.
# Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

tps['total_bill_tip_sum'] = tps['total_bill'] + tps['tip']

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe
# sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

new_tps = tps.sort_values('total_bill_tip_sum', ascending=False).iloc[:30]