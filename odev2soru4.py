def donemBasiStogu(koltukSayisi,yatakSayisi,dolapSayisi):
	global donemBasiStogu
	donemBasiStogu=koltukSayisi+yatakSayisi+dolapSayisi
	return donemBasiStogu
k=int(input("Koltuk sayısını giriniz:"))
l=int(input("Yatak sayısını giriniz:"))
m=int(input("Dolap sayısını giriniz:"))
donemBasiHesabi=donemBasiStogu(k,l,m)
print("Dönem başı stoğunuz:",donemBasiStogu)
def donemSonuStogu(koltukSayisi,yatakSayisi,dolapSayisi):
	global donemSonuStogu
	donemSonuStogu=koltukSayisi+yatakSayisi+dolapSayisi
	return donemSonuStogu
f=int(input("Koltuk sayısını giriniz:"))
g=int(input("Yatak sayısını giriniz:"))
d=int(input("Dolap sayısını giriniz:"))
donemSonuHesabi=donemSonuStogu(f,g,d)
print("Dönem sonu stoğunuz:",donemSonuStogu)
stokHesapla=(donemBasiStogu+donemSonuStogu)/2
ortalama=format(float(stokHesapla),".2f")
print("Ortalama stok hesabınız:",ortalama)	
