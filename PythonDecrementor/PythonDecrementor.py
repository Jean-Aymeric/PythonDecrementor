import time
import random

charactersInTab = []

for i in range( 110 ) :
    charactersInTab.append( chr( random.randint( 32, 255) ) )

atLeastOneDigitLeft = True
while (atLeastOneDigitLeft) :
    atLeastOneDigitLeft = False
    for i in range( len( charactersInTab ) ) :
        print( charactersInTab[i], end='' )
        if (ord( charactersInTab[i] ) <= 10 or charactersInTab[i] == " ") :
             charactersInTab[i] = " "
        else :
            atLeastOneDigitLeft = True
            charactersInTab[i] = chr( ord( charactersInTab[i] ) - 1 ) 
    print()
    time.sleep( 0.03 )
