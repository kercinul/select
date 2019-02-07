kaynak=[]
flag=0
flagkucuk=0
limit=int(input("kaç sayı"))
for i in range(0,limit):
    s=int(input("sayı lütfen"))
    kaynak.append(s)
print(kaynak,"düz")


for i in range(len(kaynak)):
    minimum = min(kaynak[i:])
    if minimum == kaynak[0]:
        flagkucuk+=1
    minimum_index = kaynak[i:].index(minimum)  
    kaynak[i + minimum_index] = kaynak[i] 
    kaynak[i] = minimum
    flag+=1
print(kaynak,"sıralı")
print(flag,"-berat al-bayrak")
print(flagkucuk,"ilk değer")
