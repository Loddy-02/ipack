#import and from
import os
import sys
import time
import requests
from requests import get

#warna
a="\033[0;90m" #abu
a1="\033[1;90m" #terang
a2="\033[2;90m" #gelap
a3="\033[3;90m" #miring
a4="\033[4;90m" #garis
b="\033[0;91m" #merah
b1="\033[1;91m" #terang
b2="\033[2;91m" #gelap
b3="\033[3;91m" #miring
b4="\033[4;91m" #garis
c="\033[0;92m" #hijau
c1="\033[1;92m" #terang
c2="\033[2;92m" #gelap
c3="\033[3;92m" #miring
c4="\033[4;92m" #garis
d="\033[0;93m" #kuning
d1="\033[1;93m" #terang
d2="\033[2;93m" #gelap
d3="\033[3;93m" #miring
d4="\033[4;93m" #garis
e="\033[0;94m" #biru
e1="\033[1;94m" #terang
e2="\033[2;94m" #gelap
e3="\033[3;94m" #miring
e4="\033[4;94m" #garis
f="\033[0;95m" #ungu
f1="\033[1;95m" #terang
f2="\033[2;95m" #gelap
f3="\033[3;95m" #miring
f4="\033[4;95m" #garis
g="\033[0;96m" #birumuda
g1="\033[1;96m" #terang
g2="\033[2;96m" #gelap
g3="\033[3;96m" #miring
g4="\033[4;96m" #garis
h="\033[0;97m" #putih
h1="\033[1;97m" #terang
h2="\033[2;97m" #gelap
h3="\033[3;97m" #miring
h4="\033[4;97m" #garis
k="\033[100m1 Txt \033[0m" #kotakabu
k1="\033[101m Txt \033[0m" #kotakmerah
k2="\033[102m Txt \033[0m" #kotakhijau
k3="\033[103m Txt \033[0m" #kotakkuning
k4="\033[104m Txt \033[0m" #kotakbiru
k5="\033[105m Txt \033[0m" #kotakungu
k6="\033[106m Txt \033[0m" #kotakbirumuda
k7="\033[107m Txt \033[0m" #kotakputih
k8="\033[108m Txt \033[0m" #kotakhitam

#dibawah ini adalag tempat hosting scriptnya
def opn():
                    #MASUKAN LINK HOST
  response = requests.get('https://raw.githubusercontent.com/Loddy-02/ipack/main/img/20220603_125727.png')
         #MASUKAN NAMA HASIL
  with open("ipack.sh", "w") as f:
      f.write(response.text)
      os.system("rm -rf login.py")
      os.system("rm -rf .banner.py")

#dibawah ini adalah banner
def login():
     os.system("python .banner.py")
     print("")
     token = input(f"{h1}[{d1}#{h1}] MASUKAN TOKEN :{h} ")

           #dibawah ini adalah cara kerja key
     if token == 'hdiqjwosnwoqndiqbo1bs9eb1':
          time.sleep(2)
          print ("")
          print (f"{h1}[{d1}#{h1}] TOKEN BENAR {d1}✓{h}")
          time.sleep(1)
          print (f"{h1}[{d1}#{h1}] SILAKAN KETIK [ {d1}bash ipack.sh{h1} ] UNTUK MENJALAKAN FILE")
          time.sleep(2)
          opn()
     else:
          time.sleep(2)
          print ("")
          print (f"{h1}[{d1}#{h1}] TOKEN SALAH {d1}x{h}")
          time.sleep(1)
          print (f"{h1}[{d1}#{h1}] SILAKAN COBA KEMBALI {d1}!{h}")
          time.sleep(2)
          login()
login()
