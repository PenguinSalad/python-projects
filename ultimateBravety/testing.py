pyt


aatrox = {
    "name": "aatrox",
    "diff": 7,
    "mainRune": "fleet"
}

akali = {
    "name": "akali",
    "diff": 8,
    "mainRune": "conq"
}

camille = {
    "name": "camille",
    "diff": 8,
    "mainRune": "conq"
}





champList = [aatrox["name"], akali["name"], camille["name"], cassiopeia["name"], choGath["name"], darius["name"], mundo["name"], fiora["name"], gangplank["name"], garen["name"], 
gragas["name"], hecarim["name"], heimerdinger["name"], illaoi["name"], irelia["name"], jarvan["name"], jax["name"], jayce["name"], karma["name"],
 kayle["name"], kennen["name"], kled["name"], lissandra["name"], lucian["name"], malphite["name"], maokai["name"], mordekaiser["name"], nasus["name"], 
 nautilus["name"], neeko["name"], nocturne["name"], olaf["name"], ornn["name"], pantheon["name"], poppy["name"], qiyana["name"], quinn["name"], 
 renekton["name"], rengar["name"], riven["name"], rumble["name"], ryze["name"], sett["name"], shen["name"], singed["name"], sion["name"], 
 swain["name"], sylas["name"], teemo["name"], trundle["name"], tryndamere["name"], urgot["name"], viktor["name"], vladimir["name"], wukong["name"], yasuo["name"], yorick["name"]]

inp = input("Champ: ").lower()
if inp in champList:
    print("Yes")
else:
    print("NO")

names = "Cassiopeia Cho'Gath Darius Mundo Fiora Gangplank Garen Gragas Hecarim Heimerdinger Illaoi Irelia Jarvan IV Jax Jayce Karma Kayle Kennen Kled Lissandra Lucian Malphite Maokai Mordekaiser Nasus Nautilus Neeko Nocturne Olaf Ornn Pantheon Poppy Qiyana Quinn Renekton Rengar Riven Rumble Ryze Sett Shen Singed Sion Swain Sylas Teemo Trundle Tryndamere Urgot Viktor Vladimir Wukong Yasuo Yorick"
print(names.replace(' ', '["name"], '))

"Cassiopeia" "Cho'Gath" "Darius" "Mundo" "Fiora" "Gangplank" "Garen" "Gragas" "Hecarim" "Heimerdinger" "Illaoi" "Irelia" "Jarvan" "Jax" "Jayce" "Karma" "Kayle" "Kennen" "Kled" "Lissandra" "Lucian" "Malphite" "Maokai" "Mordekaiser" "Nasus" "Nautilus" "Neeko" "Nocturne" "Olaf" "Ornn" "Pantheon" "Poppy" "Qiyana" "Quinn" "Renekton" "Rengar" "Riven" "Rumble" "Ryze" "Sett" "Shen" "Singed" "Sion" "Swain" "Sylas" "Teemo" "Trundle" "Tryndamere" "Urgot" "Viktor" "Vladimir" "Wukong" "Yasuo" "Yorick"