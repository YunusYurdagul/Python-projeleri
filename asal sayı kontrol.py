#sayıların asallığını kontrol etme#
sayac = 0
i = 0
sayı = int(input("sayı:"))
for i in range(1,sayı+1):
    if(sayı%i==0):
        sayac += 1
if(sayac>2):
    print("asal sayı değil")
else:
    print("asal sayı")