import sys
import time
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4./100)
#intro
def vraag1():
    slowprint(''' 
	de dag begint normaal, je bent lekker doki doki aan het spelen, opeens hoor je een knal en een alarm
	A: je gaat kijken wat er gebeurt
	B: je negeert het en gaat verder speedrunnen
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag2()
    elif inputText == "B" or inputText == "b":
        vraag11()
#alle antwoorden op antwoord A
def vraag2():
    slowprint(''' 
	je ziet mensen hun spullen pakken en rennen
	A: je pakt ook je spullen en gaat weg met je familie
	B: je blijft bij je huis en hoopt dat er niks gebeurt
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a": 
     vraag3()
    elif inputText == "B" or inputText == "b":
        vraag11()

def vraag3():
    slowprint(''' 
	 je familie pakt ook snel hun spullen en je gaat weg met de auto
	 A: weg rijden over de snelweg
	 B: door de woestijn 
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag4()
    elif inputText == "B" or inputText == "b":
        vraag7()


def vraag4():
    slowprint(''' de snelweg is zo druk dat je er niet langs komt met de auto en in de file staat, je kan nog wel terug
    A: terug gaan en alsnog met het andere plan gaan
    B: alsnog blijven wachten op de snelweg en hopen dat het snel beter word
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag5()
    elif inputText == "B" or inputText == "b":
        vraag17()


def vraag5():
    slowprint(''' je komt te laat terug en de Taliban is al in je dorp
    A: snel weg gaan en een andere manier zoeken
    B: je overgeven
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag6()
    elif inputText == "B" or inputText == "b":
        vraag10()

def vraag6():
    slowprint(''' je komt weg alleen je weet niet waar je bent
    A: richting het noorden blijven lopen
    B: naar het oosten gaan
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag7()
    elif inputText == "B" or inputText == "b":
        vraag15()


#je gaat naar het noorden


def vraag7():
    slowprint(''' je komt een ander dorp tegen waar je voor nu veilig kan blijven
    A: zo lang mogelijk blijven
    B: snel weer weg en zo ver mogelijk gaan 
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag8()
    elif inputText == "B" or inputText == "b":
        vraag14()

def vraag8():
    slowprint(''' omdat je te lang bent gebleven is de Taliban nu weer in de buurt en vinden ze het dorp, de mensen van het dorp proberen het te verdedigen
    A: helpen
    B: vluchten
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag9()
    elif inputText == "B" or inputText == "b":
        vraag14()

def vraag9():
    slowprint(''' de Taliban wint en omdat je bent gebleven word je gevangen genomen
    A: je werkt mee
    B: je verzet je
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag10()
    elif inputText == "B" or inputText == "b":
        einde3()

def vraag10():
    slowprint('''je word meegenomen naar de basis van de Taliban 
    A: je werkt mee met de ondervragingen
    B: je probeert te vluchten
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     einde1()
    elif inputText == "B" or inputText == "b":
        vraag17()

#antwoorden op antwoord B

def vraag11():
    slowprint(''' omdat je het negeert komt de Taliban je huis binnen
    A: je klimt snel uit het raam voordat ze je gezien hebben
    B: je doet niks en laat je oppakken
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag12()
    elif inputText == "B" or inputText == "b":
        vraag10()

def vraag12():
    slowprint(''' je weet nog te ontsnappen en je kan snel weg rennen
    A: je rent naar het huis van je familie
    B: je probeert meteen het dorp uit te komen
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag13()
    elif inputText == "B" or inputText == "b":
        vraag14()

def vraag13():
    slowprint(''' je familie is al ontsnapt, doordat je in het dorp bleef heeft de Taliban je gezien
    A: vluchten
    B: jezelf laten oppakken
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag14()
    elif inputText == "B" or inputText == "b":
        vraag10()

def vraag14():
    slowprint(''' het is je gelukt nu moet je een bedenken welke kant je op gaat
    A: naar het noorden
    B: naar het oosten
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag7()
    elif inputText == "B" or inputText == "b":
        vraag15()

#naar het oosten

def vraag15():
    slowprint(''' in het oosten vind je een verlaten dorp
    er is schoon drink water 
    A: je drinkt wat water en gaat snel weer weg
    B: je gaat meteen door
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag16()
    elif inputText == "B" or inputText == "b":
        vraag16()


def vraag16():
    slowprint(''' je moet nog een stuk verder door de woestijn heen maar komt uiteindelijk aan de grens maar hoe ga je naar een ander land
    A: lopend over land
    B: via een boot
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     einde2()
    elif inputText == "B" or inputText == "b":
        einde4()

def vraag17():
    slowprint(''' uiteindelijk gaat de file weg en kan je verder rijden, nu kan je richting de grens
    typ A om weer verder te gaam
    ''')
    inputText = input()
    slowprint(inputText)
    if inputText == "A" or inputText == "a":
     vraag16()

#1e einde (als je alleen voor A kiest)
def einde1():
    slowprint(''' omdat je mee werkt word je uiteindelijk vrij gelaten en kan je terug naar je familie''')

def einde2():
    slowprint(''' het lopen gaat goed en er zijn weinig gevaren onderweg alleen moet je heel vaak langs checkpoints en daar moet je lang wachten ''')

def einde3():
    slowprint(''' omdat je probeert te ontsnappen word er op je geschoten en overleef je het niet ''')

def einde4():
    slowprint(''' met de boot kom je aan in griekenland en via daar ga je naar Nederland en kom je hier in een opvang kamp ''')


vraag1()