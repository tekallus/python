#liste metodlari 5 mart 2024 iu

numbers=[1,2,3,4,5,6,7]
letters=['a','k','f','b','c','d','e']

val =min(numbers) # min ile en kucuk sayi 1
val1= max(letters) # max ile en buyuk harf burda alfabenin son harfi en buyuk
val=numbers[:4] # basdan basla ve 4. elemana kadar yaz

numbers.pop

numbers[4]=40 # 4. elemani 40 ile degistirir  [1, 2, 3, 4, 40, 6, 7]
numbers.append(49)#append dizinin en sonuna  eleman ekler [1, 2, 3, 92, 4, 40, 6, 7, 49]
numbers.insert(3,92)# insert 3 nolu elemani 92 ille degistir [1, 2, 3, 92, 4, 40, 6, 7, 49]
numbers.pop(0)# pop eleman siler burda 0 inci elemani sildi  [2, 3, 92, 4, 40, 6, 7, 49]
numbers.remove(49)# remove istenen degeri siler burda 49 arar ve siler [2, 3, 92, 4, 40, 6, 7]
numbers.sort()# listenin karisikligini duzenler sirali bir sekilde yazar [2, 3, 4, 6, 7, 40, 92]
numbers.reverse()#listeyi tam tersine ceviririz [92, 40, 7, 6, 4, 3, 2]

print(numbers)
print(val1)

print(len(numbers))# eleman sayisini ogrenmek icin len kullaniyoruz
print(numbers.count(6))# numbers dizisinin icinde 6 rakaminda kac tane var ogrenmek icin count kullanilir

numbers.clear()# diziyi koplle siler bos bir dizi olur
print(numbers)

#yukaridaki orneklere gore asagidaki sorulari cevaplayalim

names=['busra','neva','ufuk','ismail']
years=[2007,2009,2013,2021]


# names listesinin sonuna "Cenk" ismini ekleyin.

names.append('cenk')
# "Sena" değerini listenin başına ekleyin.
names.insert(0,'sena')
# "neva" ismini listeden silin.
names.remove('neva')
# "ufuk" isminin index'ini bulun.
names.index('ufuk')

# "Ali" listenin bir elemanı mıdır kontrol edin.
'ali ' in names

# Liste elemanlarını ters çevirin.
# Liste elemanlarını alfabetik olarak sıralayın.

# years listesini rakamsal büyüklüğe göre sıralayın.

# "Chevrolet,Dacia" karakter dizisini listeye çevirin ve saklayın.
# years dizisinin en büyük ve en küçük elemanını bulun.
# years dizisinde kaç tane 1998 değeri vardır sayın.
# years dizisinin tüm elemanlarını silin.
# Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayın.

#cozummler 100. satirda once kendin cozmeye caliis


















































# names.append('cenk')
# names.insert(0, 'Sena')
# names.remove('Deniz')
# names.index('Deniz') 
# 'Ali' in names  
# names.reverse() 
# names.sort() 
# years.sort()  
# str ="Chevrolet,Dacia" result=str.split(',') 
# max(years), min(years)  
# years.count(1998) 
# years.clear()  
# 
markalar=[] 
marka=input("marka: ")  
markalar.append(marka)  
print(markalar)