'''
count = 1
while count<5:
    count = count + 1
    print(count, end=" ")
else:
    print()
'''

# ogrencilerin not ortalaması

# ogr_say = int(input("Kac ogrenci notu gireceginizi yaziniz "))

# print(ogr_say," adet ogrenci notu giriniz")
print("Lutfen notları giriniz. Durmak için -1 giriniz")
count = 1
toplam = 0
ogr_not = 0

while ogr_not != -1:
    ogr_not = int(input(str(count) + ". ogrenci notunu giriniz "))
    if ogr_not == -1:
        break
    elif ogr_not < 0:
        print("Lutfen negatif not girmeyiniz")
        continue
    toplam += ogr_not
    count += 1

print("Ortalama", toplam / (count - 1))
