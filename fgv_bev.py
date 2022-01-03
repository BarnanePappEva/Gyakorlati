def sikerese(pontszam):
      if pontszam > 48:
            print('Sikerült a vizsga!')
      else:
            print('A vizsga sajnos nem sikerült!')
nev=None

while nev !='':
      nev=input('Kérem a vizsgázó nevét!')
      if nev != '':
            pontszam=input('Kérem a vizsgázó pontszámát!')
            pontszam=int(pontszam)
            if sikerese(pontszam):
                  print(sikerese(pontszam))
      

