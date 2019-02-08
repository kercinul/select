kaynak=[]


def sort (kaynak):
    for i in range(len(kaynak)):
        minimum = min(kaynak[i:])
        minimum_index = kaynak[i:].index(minimum)
        kaynak[i + minimum_index] = kaynak[i]
        kaynak[i] = minimum
    return sort

limit=int(input("kaç sayı"))
for i in range(0,limit):
    s=int(input("sayı lütfen"))
    kaynak.append(s)




print(kaynak,"1")
sort(kaynak)
print(kaynak,"2")
