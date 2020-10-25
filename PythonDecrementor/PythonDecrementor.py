digitsInString = input( "Entrez une liste de chiffres :" )
digitsInTab = []

for i in range( len( digitsInString ) ) :
    if (digitsInString[i].isdigit()) :
        digitsInTab.append( int(digitsInString[i] ))

atLeastOneDigitLeft = True
while (atLeastOneDigitLeft) :
    atLeastOneDigitLeft = False
    for i in range (len(digitsInTab)) :
        print (str(digitsInTab[i]), end='')
        if (digitsInTab[i] == 0 or digitsInTab[i] == " ") :
             digitsInTab[i] = " "
        else :
            atLeastOneDigitLeft = True
            digitsInTab[i] -= 1 
    print()
