#Írj ki egy stringet txt fájlba!

kiirando_szoveg="Erik, ne püföld a billentyűzetet!"

celfajl=open("erik.txt","w")

print(kiirando_szoveg,file=celfajl)

celfajl.close()
