# tuple list

list=[1,2,3]
tuple=(1,'iki',3)

print(type(list))#<class 'list'>

print(type(tuple))#<class 'tuple'>

list[0]="busra"
#tuple[0]='neva' tuple lara yeni eleman ekleyemeyiz.eklermeye calisirsak bu hata gelir #TypeError: 'tuple' object does not support item assignment
#ama tuple=('busra') diyerek eski diziyi silip yeni dizi olusturabiliriz

# tuple olarak kullanabilecegimiz iki tane metod var count ve index

print(list)
print(tuple)