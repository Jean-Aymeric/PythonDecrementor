import time

charactersInString = input( "Entrez une liste de chiffres :" )
charactersInTab = []

for i in range( len( charactersInString ) ) :
    charactersInTab.append( charactersInString[i] )

atLeastOneDigitLeft = True
while (atLeastOneDigitLeft) :
    atLeastOneDigitLeft = False
    for i in range( len( charactersInTab ) ) :
        print( charactersInTab[i], end='' )
        if (ord( charactersInTab[i] ) >+ 127 or charactersInTab[i] == " ") :
             charactersInTab[i] = " "
        else :
            atLeastOneDigitLeft = True
            charactersInTab[i] = chr( ord( charactersInTab[i] ) - 1 ) 
    print()
    time.sleep(0.1)
