import random
print("Start the game")

gameOver=0
points=0

cards=['1C','2C','3C','4C','5C','6C','7C','8C','9C','10C','11C','12C',
       '1E','2E','3E','4E','5E','6E','7E','8E','9E','10E','11E','12E',
       '1B','2B','3B','4B','5B','6B','7B','8B','9B','10B','11B','12B',
       '1O','2O','3O','4O','5O','6O','7O','8O','9O','10O','11O','12O']

cardA=cards[random.randint(0, len(cards)-1)]
cards.remove(cardA)
print('COMIENZA! Tu primera carta: ' + cardA)

while(gameOver==0):
       choice=input('Elegí M(mayor) o m(menor): ')
       cardB=cards[random.randint(0, len(cards)-1)]
       cards.remove(cardB)
       print(cardB)
       first = int(cardA[0:len(cardA)-1])
       second = int(cardB[0:len(cardB)-1])

       if((first<second and choice=='M') or (first>second and choice=='m') or first==second):
              points+=1
              cardA=cardB
       else:
              print('GAME OVER! Puntaje Total: ' + str(points))
              gameOver=1