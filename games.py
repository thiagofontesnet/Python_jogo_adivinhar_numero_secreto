import forca
import numeric_divination

print('welcome to the games, choose an option')

select = int(input('(1) forca, (2) numeric divination'))

if select == 1:
    forca.play()
elif select == 2:
    numeric_divination.play()