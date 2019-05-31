qwerty = ['q', 'w', 'e', 'r', 't', 'y',
          'u', 'i', 'o', 'p', '[', ']',
          'a', 's', 'd', 'f', 'g', 'h',
          'j', 'k', 'l', ';', "'", 'z',
          'x', 'c', 'v', 'b', 'n', 'm',
          ',', '.', '/', ' ']

dvorak = ["'", ',', '.', 'p', 'y', 'f',
          'g', 'c', 'r', 'l', '/', '=',
          'a', 'o', 'e', 'u', 'i', 'd',
          'h', 't', 'n', 's', '-', ';',
          'q', 'j', 'k', 'x', 'b', 'm',
          'w', 'v', 'z', ' ']



translationNum = []

translationChar = []

userInput = input("please enter string to be translated: ")

userCharacters = list(userInput)


i = 0

while i <= (len(userCharacters) - 1):
    for position, character in enumerate(qwerty):
        if character == userCharacters[i]:
            translationNum.append(position)
            i += 1
            break
e = 0


while e <= (len(translationNum) - 1):
    translationChar.append(dvorak[translationNum[e]])
    e += 1
    
print(''.join(translationChar))
