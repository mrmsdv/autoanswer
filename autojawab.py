import os, sys ,math

menu = ''' 1. Bangun Datar \n 2. Bangun Ruang'''

Bdatar = ''' 1. Persegi \n 2. Persegi-Panjang \n 3. Segitiga'''
Bruang = ''' 1. Kubus \n 2. kerucut \n 3. Tabung '''
#color
r="\033[31m"
g="\033[1;32m"
w="\033[1;37m"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
c="\033[36m"
y="\033[33m"
P = print
Os = os.system
def dtr():
    def persegi():
        P(f' {g}Bangun Datar (PERSEGI)')
        P( f''' {y}Yang DiKetahui Pada Soal ?\n{y} 1.{g} Luas \n{y} 2.{g} Keliling \n {y}3.{g} sisi''')
        psg = input( f'{y} Masukan Keterangan => {r}')
        if psg == '1':
            luas = int(input(f'{y} Luas = '))
            sisi = math.sqrt(luas)
            P(f' {g}Sisi {r}= {y}',math.sqrt(luas))
            P(f' {g}Keliling{r} = {y}',sisi*4)
            input(f' {r}Kembali')
            Os('clear')
            dtr()
        if psg == '2':
            keliling = int(input(f' {y}Keliling = '))
            sisi = keliling/4
            P(f' {g}Sisi {r}= {y}',sisi)
            P(f' {g}Luas {r}= {y}',sisi*sisi)
            input(f' {r}Kembali')
            Os('clear')
            dtr()
        if psg == '3':
            sisi = int(input(f' {y}sisi = '))
            P(f" {g}Luas{r} ={y}",sisi*sisi)
            P(f" {g}Keliling{r} ={y}",4*sisi)
            input(f' {r}Kembali')
            Os('clear')
            dtr()
        else:
            Os('clear')
            P(' Pilih salah satu !')
            persegi()
    P(Bdatar)
    pilih = input(' Pilihan => ')
    if pilih == '1':
        persegi()
    elif pilih == '2':
        psgp()
    elif pilih == '3':
        sgt()
    else:
        Os('clear')
        dtr()
def jenisbangun():
    while True:
        Os('clear')
        P(menu)
        pilih = input(' Pilih salah satu = ')
        if pilih == '1':
            dtr()
            break
        elif pilih == '2':
            P(Bruang)
            break
        else:
            P('Pilihan Tidak Terdaftar')

P(menu)
jenisbangun()