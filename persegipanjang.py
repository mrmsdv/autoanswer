import os,sys
#color
r="\033[31m"
g="\033[1;32m"
w="\033[1;37m"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
c="\033[36m"
y="\033[33m"
P = print
Os = os.system
    def psgp():
        P(f' {g}Bangun datar ( Persegi Panjang )')
        P(f' {g}Yang di Ketahui pada soal ?')
        P(f' {r}Note : {y}Jika tidak ada di soal tekan Enter saja')
        panjang = input(' panjang = ')
        lebar = input(' lebar = ')
        luas = input(' Luas = ')
        Keliling = input(' Keliling = ')
        if luas == '' and Keliling == '':#jika panjang dan lebar di ketahui
            panjang = int(panjang)
            lebar = int(lebar)
            P(f'{g} Luas    =',panjang*lebar)
            P(f'{g} Keliling=',2*(panjang+lebar))
        elif luas == '' and panjang == '':#jika lebar dan keliling di ketahui
            lebar = int(lebar)
            Keliling = int(Keliling)
            panjang = (Keliling/2)-(lebar)
            P(f'{g} Luas    =',panjang*lebar)
            P(f'{g} panjang =',panjang)
        elif luas == '' and lebar =='':#jika panjang dan keliling di ketahui
            panjang = int(panjang)
            Keliling = int(Keliling)
            lebar = (Keliling/2)-panjang
            P(f'{y} Luas  = {c}',panjang*lebar)
            P(f'{y} lebar = {c}',lebar)
        elif Keliling == '' and lebar =='':#jika luas dan panjang di ketahui
            panjang = int(panjang)
            luas = int(luas)
            lebar = (luas/panjang)
            P(f'{y} keliling = {c}',2*(panjang+lebar))
            P(f'{y} lebar    = {c}',lebar)
        elif Keliling == '' and panjang =='':#jika luas dan lebar di ketahui
            luas = int(luas)
            lebar = int(lebar)
            panjang = luas/lebar
            P(f'{y} keliling  = {c}',2*(panjang+lebar))
            P(f'{y} panjang   = {c}',panjang)
        else:pass
psgp()        
