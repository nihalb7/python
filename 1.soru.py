def toplamGelirHesapla():
    x=int(input("Finansman Geliri Giriniz"))
    y=int(input("Pazar Geliri Giriniz"))
    z=int(input("Kira Geliri Giriniz"))
    toplamGelirler=x+y+z
    return toplamGelirler
def toplamGiderHesapla():
    w=int(input("Ücret Giriniz"))
    r=int(input("Finansman Gideri Giriniz"))
    t=int(input("Pazar Gideri Giriniz"))
    q=int(input("Muhasebe Gideri Giriniz"))
    toplamGiderler=w+r+t+q
    return toplamGiderler
def karHesapla():
    kar=(x+y+z)-(w+r+t+q)
x=int(input("Finansman Geliri Giriniz"))
y=int(input("Pazar Geliri Giriniz"))
z=int(input("Kira Geliri Giriniz"))
w=int(input("Ücret Giriniz"))
r=int(input("Finansman Gideri Giriniz"))
t=int(input("Pazar Gideri Giriniz"))
q=int(input("Muhasebe Gideri Giriniz"))
if (x+y+z)-(w+r+t+q)>1000:
    print ("Şirket kar yapmıştır.")
elif (x+y+z)-(w+r+t+q)==1000:
    print ("Şirket karı başabaş noktasında.")
else:
    print ("Şirket zarar etmiştir.")

    
