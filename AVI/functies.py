EASY_TEXT = """Ik hou van programmeren. Programmeren is leuk. 
Ik kan veel dingen maken met programmeren. Ik kan een website maken. 
Ik kan een spel maken. Ik kan een chatbot maken. 
Programmeren is niet moeilijk. Ik moet alleen de juiste code schrijven. 
De code moet logisch zijn. De code moet foutloos zijn. Werkende code maakt mij blij. 
Niet-werkende code chagerijnig. Programmeren is een avontuur. Ik leer elke dag iets nieuws met programmeren."""

DIFFICULT_TEXT = """Programmeren is een geweldige activiteit, die je in staat stelt om je creativiteit, 
logica en probleemoplossend vermogen te gebruiken, om allerlei soorten applicaties te maken, 
die nuttig, vermakelijk of zelfs levensveranderend kunnen zijn, afhankelijk van je doel en publiek. 
Het is ook een uitdagende bezigheid, die je voortdurend leert om nieuwe talen, technieken en concepten te leren, 
die je helpen om je code efficiënter, eleganter en robuuster te maken, zonder dat je je ooit hoeft te vervelen of te herhalen. 
Bovendien is het een leuke hobby, die je veel voldoening en plezier kan geven, als je ziet hoe je ideeën tot leven komen op het scherm, als je de interactie met je gebruikers ziet of 
als je de reacties van je vrienden en familie ziet, als je ze verrast met je eigen creaties.
"""

ALLOWED_IN_WORD = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-"
EIND_VAN_ZIN = "!?."

# depending on the type of text you wish you get an easy, difficult or text from file.
def getText(choice: str) -> str:
    if choice == 'easy':
        return EASY_TEXT
    elif choice == 'difficult':
        return DIFFICULT_TEXT
    else:
        return getFileContentAsString(choice)

def getFileContentAsString(textFile: str) -> str:
    with open(textFile, 'r') as file:
        content = file.read()
    return content

# opdracht 1
def getNumberOfCharacters(text: str) -> int:
    letter_count = 0 
    for x in text:
        if x in ALLOWED_IN_WORD:
            letter_count += 1
    return letter_count

# opdracht 2
def getNumberOfSentences(text: str) -> int:
    zin_count = 0 
    for x in text:
        if x in EIND_VAN_ZIN:
            zin_count += 1
    return zin_count

# opdracht 3
def getNumberOfWords(text: str) -> int:
    return len(text.split())

#opdracht 5
def GetAVIscore(text: str) -> int:
    woorden = getNumberOfWords(text)
    zinnen = getNumberOfSentences(text)
    gemiddelde = woorden/zinnen
    if gemiddelde <=7 >8:
        avi_score = 5
    elif gemiddelde <=8 <9:
        avi_score = 6
    elif gemiddelde <=9 >10:
        avi_score = 8
    elif gemiddelde <=10 >11:
        avi_score = 11
    elif gemiddelde <=11:
        avi_score = 12
    return avi_score