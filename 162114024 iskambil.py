import random
import time

simgeler=['Karo','Maça','Sinek','Kupa'] # Simge tanimlamalarini yapiyorum.
sayılar=['1    ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','Vale','Kız','Papaz'] # Her simgenin icinde bulunacak rakam ve sembolleri belirliyorum.
kartlar=[] # simgeler ve sayilarin birbiri ile birlesecegi bos bir kartlar dizisi tanimliyorum.
a=[] # 1. oyuncuya dagitilacak kartlari tutacak bir a dizisi tanimliyorum.
b=[] # 2. oyuncuya dagitilacak kartlari tutacak bir b dizisi tanimliyorum.
c=[] # 3. oyuncuya dagitilacak kartlari tutacak bir c dizisi tanimliyorum.
d=[] # 4. oyuncuya dagitilacak kartlari tutacak bir d dizisi tanimliyorum.

for i in simgeler: # sayilari ve simgeleri birbiri ile birlestirip kartlar dizisine atiyorum.
	for j in sayılar:
		kartlar.append(i+' '+str(j))

i=52
while i!=39: # ilk 13 kart dagitiliyor..
	ü=random.choice(kartlar)
#kartlarin daha iyi dagitilabilmesi icin
#random.choice'in her seciminin arasina 0.2 saniye bekleme kattim.
	time.sleep(0.2)
	a.append(ü) # ilk cekilen rastgele 13 kart a dizisine ataniyor.
	kartlar.remove(ü) # cekilen kart, kartlar dizisinden siliniyor.
	i=i-1

while i!=26:
	ü=random.choice(kartlar)
	time.sleep(0.2)
	b.append(ü) # ikinci cekilen rastgele 13 kart b dizisine ataniyor.
	kartlar.remove(ü)# cekilen kart, kartlar dizisinden siliniyor.
	i=i-1

while i!=13:
	ü=random.choice(kartlar) 
	time.sleep(0.2)
	c.append(ü)# ucuncu cekilen rastgele 13 kart c dizisine ataniyor.
	kartlar.remove(ü)# cekilen kart, kartlar dizisinden siliniyor.
	i=i-1

while i!=0:
	ü=random.choice(kartlar)
	time.sleep(0.2)
	d.append(ü)# dorduncu cekilen rastgele 13 kart d dizisine ataniyor.
	kartlar.remove(ü)# cekilen kart, kartlar dizisinden siliniyor.
	i=i-1

def dagit(): # dagitilan kartlari ekrana yazicak fonksiyon tanimlaniyor.
        print('Oyuncu 1 \tOyuncu 2 \tOyuncu 3 \tOyuncu 4')
        for i in range(0,13): # 0 dan  13 ' e kadar dagittigim butun dizilerin sirasiyla
                              # 0.1.2.3...12. indislerini ekrana yazdiriyorum.
                print(a[i] + '\t' + b[i] + '\t' + c[i] + ' \t' + d[i])




