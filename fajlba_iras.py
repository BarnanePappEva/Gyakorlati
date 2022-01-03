#Írj ki egy stringet txt fájlba!

kiirando_szoveg="Erik, ne püföld a billentyűzetet, mert ezzel kell dolgoznod év végéig"

celfajl=open("erik.txt","w")

print(kiirando_szoveg,file=celfajl)

celfajl.close()
