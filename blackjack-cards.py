import random

CORA = chr(9829) # Character 9829 is '♥'.
DIAM = chr(9830) # Character 9830 is '♦'.
PICA = chr(9824) # Character 9824 is '♠'.
TREB = chr(9827) # Character 9827 is '♣'.

def main():
      print("""
      Rules:
            Try to get as close to 21 without going over.
            Kings, Queens, and Jacks are worth 10 points.
            Aces are worth 1 or 11 points.
            Cards 2 through 10 are worth their face value.
            (H)it to take another card.
            (S)tand to stop taking cards.
            On your first play, you can (D)ouble down to increase your bet
            but must hit exactly one more time before standing.
            In case of a tie, the bet is returned to the player.
            The dealer stops hitting at 17.

            Money: 5000
      """)
      money = 5000
      bet_input = bet()
      result = play(bet_input)
      total = result[0]
      card = result[1]
      final_bet = int(result[2])
      if total <=21:
            crupier_points = crupier(card)
            outcome(total, crupier_points, final_bet)
      close = input("Press any key to exit")             


def cards():
      cards = []
      for palo in (CORA, DIAM, PICA, TREB):
            for rank in range(2,11):
                  cards.append((str(rank), palo))
            for letra in ('J','Q','K','A'):
                  cards.append((str(letra), palo))      
      random.shuffle(cards)
      return cards

def bet():
      bet_input = input("How much do you bet? (1-5000)\n")
      return bet_input

def show(i):
      mazo = cards()
      return mazo[i]

def play(bet_input):
      i=0
      total_bet = bet_input
      player = 0
      while True:
            carta = show(i)
            print_card(carta)
            player = sum_points(carta, player)
            if player>21:
                  money = 5000 - int(total_bet)
                  print(f'You LOST! Points: {player}. Now you have: ${money}\n')
                  return (player,i, total_bet)
                  break
            else:
                  print(f'You have {player} points.\n')
            player_dec = decision()
            if player_dec == "H":
                  i = i+1
            elif player_dec == "D":
                  i = i+1
                  total_bet = int(total_bet)*2
                  print(f'----------- Now your bet is {total_bet} -----------\n')
            elif player_dec == "S":
                  print(f'============== Your final points: {player} ============== \n')
                  return (player,i, total_bet)
                  break

def sum_points(carta, points):
      if carta[0][0]=="J" or carta[0][0]=="Q" or carta[0][0]=="K":
                  points = points + 10
      elif carta[0][0]=="A":
            if points <= 10:
                  if points+11 <22:
                        points = points + 11
                  else:
                        points = points + 1
            else:
                  points = points + 1
      else:
            if len(carta[0]) == 2:
                  points = points + 10
            else:
                  points = points + int(carta[0][0])
      return points

def crupier(card):
      i = card
      crupier = 0
      print('\nCrupier Turn:')
      while True:
            carta = show(i)
            print_card(carta)
            crupier = sum_points(carta, crupier)
            i = i+1
            if crupier >= 17:
                  print(f'============== Crupier got {crupier} points ==============\n')
                  return crupier
                  break

def outcome(total, crupier, bet):
      if total == 21:
            bet = 5000 + bet
            print(f'YOU WON! Now you have ${bet}\n')
      elif total > 21:
            print(f'YOU LOSE - Total: {total}')
      else:
            if total == crupier:
                  print(f'You got your money back. You still got $5000\n')
            elif (21-total) < (21-crupier) or crupier>21:
                  bet = 5000 + bet
                  print(f'YOU WON! Now you have ${bet}\n')
            else:
                  bet = 5000 - bet
                  print(f'YOU LOST! Now you have ${bet}\n')

def decision():
      decision = input("(H)it, (S)tand, (D)ouble down: ")
      return decision.upper()

def print_card(card):
      if len(card[0]) == 2:
            print(' ___ ')
            print(f'|{card[0]} |')
            print(f'| {card[1]} |')
            print(f'|_{card[0]}|')
      else:
            print(' ___ ')
            print(f'|{card[0]}  |')
            print(f'| {card[1]} |')
            print(f'|__{card[0]}|')

if __name__ == '__main__':
      main()