#rockpaperscissor
def initials():
    l = ['R','S','P']
    player1 =  np.random.choice(l)
    #player1 = input("Choose you option player-1 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
    player2 = input("Choose you option player-2 \n 1. R for rock \n 2. S for scissor \n 3. P for paper\n").upper()
    return player1,player2
def win(a,b):
      counta = 0 
      countb = 0
      if a ==  b  : print('TIE')    
      elif a =='R' and b == 'S' : 
          print('PLAYER-1 WINS') 
          counta += 1 
      elif a == 'S' and b == 'P' : 
          print('PLAYER-1 WINS') 
          counta += 1      
      elif a == 'P' and b == 'R' : 
          print('PLAYER-1 WINS') 
          counta += 1 
      elif a == 'R' and b == 'P' : 
          print('PLAYER-2 WINS') 
          countb += 1       
      elif a == 'S' and b == 'R' : 
          print('PLAYER -2 WINS') 
          countb += 1 
      elif a == 'P' and b == 'S' : 
          print('PLAYER - 2 WINS') 
          countb += 1
      else:
          print("Enter the valid option")
      return counta,countb  
     
def total(c,d):      
      if c>d  : print("Player-1 WINS MORE MATCHES")
      elif d>c: print("Player-2 WINS MORE MACTHES")
      else    : print("ITS A TIE")
          
print("-------------WELCOME TO THE GAME OF ROCK PAPER SCISSOR------------")
for i in range(0,5):  
     a,b = initials()
     c,d = win(a,b)
total(c,d)
