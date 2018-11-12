rahasia = "Hamburger"
tebakan = ''
limit = 5
count = 0
while (count<limit):
    tebakan = input("Tebakan : ")
    if tebakan == rahasia:
        break
    count +=1
if count<limit:
    print("Tebakan anda benar")
else:
    print("Kalah")   
'''
kataRahasia = 'bakpao'
tebakan = ''
jumlahTebakan = 0
batasTebakan = 5
overTebakan = False

while tebakan != kataRahasia and not(overTebakan):
    if jumlahTebakan < batasTebakan:
        tebakan = input('Masukkan kata tebakan: ')
        jumlahTebakan += 1
    else:
        overTebakan = True

if overTebakan:
    print('Kesempatan menebak habis! Anda kalah!')
else:
print('Tebakan benar! Anda menang!')
'''     