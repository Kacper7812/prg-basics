hours= int(input("Podaj liczbę godzin na ile zaparkowales auto: "))




if hours > 0 and hours<=2:
    cena=5 
    print(f"Należność za parking to {cena }zł")

elif hours>=3 and hours<=6:
    cena=15
    print(f"Należność za parking to {cena}zł")
else:
    cena=20
    print(f"Należność za parking to {cena }zł")

if hours==0:
    print("Błąd")

