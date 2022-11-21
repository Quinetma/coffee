import numpy as np
import random as rd
def ai_student(board, player):
    tab_ref= np.zeros((6,7))
    tab1 = np.zeros((6,7))
    colonne_choisie = 0

    tab_ref[0] = [0, 10, 20, 30, 20, 10, 0]
    tab_ref[1] = [0, 10, 20, 30, 20, 10, 0]
    tab_ref[2] = [0, 10, 20, 30, 20, 10, 0]
    tab_ref[3] = [0, 10, 20, 30, 20, 10, 0]
    tab_ref[4] = [0, 10, 20, 30, 20, 10, 0]
    tab_ref[5] = [0, 10, 20, 30, 20, 10, 0]
    

    if player==1:
        advers=2
    else:
        advers=1

    
    b = np.copy(board)
    # Collects the moves which can be played (i.e. the nonfull columns)
    nonfull_cols = np.where(board[0] == 0)[0]
    for col in nonfull_cols:
        # Creates the attack and defense moves, to check if one is a winning move
        attack_board = np.copy(update_board(b, col, player))
        defense_board = np.copy(update_board(b, col, abs(player-3)))
        # Plays if winning move for him
        if check_win(attack_board, col, player):
            #print('Plays attack move')
            return col
        # Plays if winning move for opponent
        elif check_win(defense_board, col, abs(player-3)):
            #print('Plays defense move')
            return col

    count=0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0 and(i==5 or board[i+1][j]!=0 )and (j in nonfull_cols):                            
                cdd1=0
                cdd2=0
                cdg1=0
                cdg2=0
                cddh1=0
                cddh2=0
                cdgh1=0
                cdgh2=0
                cv1=0
                cv2=0
                chd1=0
                chg1=0
                chd2=0
                chg2=0
                if i+1 != 6:
                    cv1=countvertical(board,j,i+1,advers)
                    cv2=countvertical(board,j,i+1,player)                    
                else:
                    cv1=0
                    cv2=0
                if j!= 0:
                    chg1=counthorizontalgauche(board,j-1,i,advers)
                    chg2=counthorizontalgauche(board,j-1,i,player)
                else:
                    ch1=0
                    ch2=0
                if j!=6:
                    chd1=counthorizontaldroite(board,j+1,i,advers)
                    chd2=counthorizontaldroite(board,j+1,i,player)
                    
                if i!=5:     
                    if j ==0:
                        cdd1= countdiagodroite(board,j+1,i+1,advers)
                        cdd2= countdiagodroite(board,j+1,i+1,player)
                    if j==6:
                        cdg1= countdiagogauche(board,j-1,i+1,advers)
                        cdg2= countdiagogauche(board,j-1,i+1,player)
                if i!=0:     
                    if j ==0:
                        cddh1= countdiagodroitehaut(board,j+1,i-1,advers)
                        cddh2= countdiagodroitehaut(board,j+1,i-1,player)
                    if j==6:
                        cdgh1= countdiagogauche(board,j-1,i-1,advers)
                        cdgh2= countdiagogauche(board,j-1,i-1,player)                    
                liste1 = [cv1, chd1,chg1, cdd1, cdg1,cddh1,cdgh1]
                liste2 = [cv2, chd2,chg2, cdd2, cdg2,cddh2,cdgh2]
                
                for element in liste1 :
                    if element == 1 :
                        count+=0
                     
                    if element == 2 :
                        count += 30
                       
                    if element == 3 :             
                        count += 500
                        
                for element in liste2 :
                    if element == 1 :
                        count+=20
                      
                    if element == 2 :
                        count += 90
                
                    if element == 3 :
                        count += 1000
                if chg1>=1 and chd1>=1:
                    count+=30
                if chg2>=1 and chd2>=1:
                    count+=90
                if cdg1>=1 and cddh1>=1:
                    count+=30
                if cdg2>=1 and cddh2>=1:
                    count+=90
                if cdd1>=1 and cdgh1>=1:
                    count+=30
                if cdd2>=1 and cdgh2>=1:
                    count+=90
                    
                if i==0 or i == 1 :
                    if cv1<2 and cv1>=1:
                        count-=cv1
                    if cv2<2 and cv2>=1:
                        count-=cv2
                    
            tab1[i][j]=count
            count=0
    tab_final= tab1 + tab_ref

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]!=0:
                tab_final[i][j]=0
    #print (tab_final)
    maxi=np.max(tab_final)
    index_maxi = np.where(tab_final==maxi)
    indice = np.where(tab_final==maxi)[1][-1]
    x=index_maxi[0][-1]
    #print (maxi)
    
    if (x!=0):
        if len(nonfull_cols) ==1:
            colonne_choisie=nonfull_cols[0]
            return int(colonne_choisie)
        
        #on modifie le bboard pour parer l'eventualité
        matrice=np.copy(board)
        matrice[x][indice]=player
        coup_joué=0
        #print(matrice)
        matrice[x-1][indice] =abs(player-3)
        #print (matrice)
        #print(check_win(matrice,indice,abs(player-3)))

        while(check_win(matrice,indice,abs(player-3)) and coup_joué<=6):
        
            tab_final[x][indice]=0
            maxi=np.max(tab_final)
            #print(maxi)
            
            indice = np.where(tab_final==maxi)[1][-1]
            x=index_maxi[0][-1]
            #print(x)
            #print(indice)
            matrice=np.copy(board)
            matrice[x][indice]=player
            matrice[x-1][indice] =abs(player-3)
            #print(tab_final)
            #print (matrice)
            coup_joué+=1
    
    if indice not in nonfull_cols:
        if len(nonfull_cols)==1:
            indice=nonfull_cols[0]
    colonne_choisie = indice
    return int(colonne_choisie)
    
###################################################################################################################
def countvertical(board,colonne,ligne,joueur):
    if ligne==5:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0
        
    i=ligne
    count=0
    while i!=5 and board[i][colonne]==joueur:
        count+=1
        i+=1
    if i==5:
        if board[i][colonne]==joueur:
            count+=1

    return count
def counthorizontaldroite(board,colonne,ligne,joueur):
    if colonne==6:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0    
    j=colonne
    count=0 
    while  j!=6 and board[ligne][j]==joueur:
        count+=1
        j+=1
    if j==6:
        if board[ligne][j]==joueur:
            count+=1
            if count==2:
                return 0
    #prise en compte du cas ou jamais il pourra alligner 4 psq trou que pr 3
    if board[ligne][j]==abs(joueur -3):
        count =0
        #predire le fait que le'advers peut jouer des 2cotés
    if count==2:
        if board[ligne][j]==0:
            count+=1
    return count

def counthorizontalgauche(board,colonne,ligne,joueur):
    if colonne==0:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0    
    j=colonne
    count=0
    while j!=0 and board[ligne][j]==joueur:
        count+=1
        j-=1
    if j==0:
        if board[ligne][j]==joueur:
            count+=1
            #faire le cas ou le bord bloque le joueur
            if count==2:
                return 0
            #idem qu'au dessus
    if board[ligne][j]==abs(joueur -3):
        count =0
        #predire le fait que le'advers peut jouer des 2cotés
    if count==2:
        if board[ligne][j]==0:
            count+=1        
    return count

def countdiagogauche(board,colonne,ligne,joueur):
    if ligne==5:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0
    count=0
 
    i=ligne
    j=colonne
    while board[i][j]==joueur and j!=0 and i!=5:
        count+=1
        i+=1
        j-=1
    if i==5:
        if j==0:
            count+=1
            return count
        if board[i][j]==joueur:
            count+=1
    if j ==0:
        if board[i][j]==joueur:
            count+=1
    if board[i][j]==abs(joueur -3):
        count =0
        #predire le fait que le'advers peut jouer des 2cotés
    if count==2:
        if board[i][j]==0:
            count+=1
    return count

def countdiagodroite(board,colonne,ligne,joueur):
    if ligne==5:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0
    count=0
 
    i=ligne
    j=colonne
    while board[i][j]==joueur and j!=6 and i!=5:
        count+=1
        i+=1
        j+=1
    if i==5:
        if j==6:
            count+=1
            return count
        if board[i][j]==joueur:
            count+=1
    if j ==6:
        if board[i][j]==joueur:
            count+=1
    if board[i][j]==abs(joueur -3):
        count =0
        #predire le fait que le'advers peut jouer des 2cotés
    if count==2:
        if board[i][j]==0:
            count+=1       
    return count
def countdiagodroitehaut(board,colonne,ligne,joueur):
    if ligne==0:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0
    count=0
 
    i=ligne
    j=colonne
    while board[i][j]==joueur and j!=6 and i!=0:
        count+=1
        i-=1
        j+=1
    if i==0:
        if j==6:
            count+=1
            return count
        if board[i][j]==joueur:
            count+=1
    if j ==6:
        if board[i][j]==joueur:
            count+=1
    if board[i][j]==abs(joueur -3):
        count =0
        #predire le fait que le'advers peut jouer des 2cotés
    if count==2:
        if board[i][j]==0:
            count+=1        
    return count
def countdiagogauchehaut(board,colonne,ligne,joueur):
    if ligne==0:
        if board[ligne][colonne]==joueur:
            return 1
        else:
            return 0
    count=0
 
    i=ligne
    j=colonne
    while board[i][j]==joueur and j!=0 and i!=0:
        count+=1
        i-=1
        j-=1
    if i==0:
        if j==0:
            count+=1
            return count
        if board[i][j]==joueur:
            count+=1
    if j ==0:
        if board[i][j]==joueur:
            count+=1
    if board[i][j]==abs(joueur -3):
        count =0
        #predire le fait que le'advers peut jouer des 2cotés
    if count==2:
        if board[i][j]==0:
            count+=1
    return count
########################################################################################################################
# The basic AI used for section 2 of the homework
def ai_random(arg_board, player):
    board = np.copy(arg_board)
    # Collects the moves which can be played (i.e. the nonfull columns)
    nonfull_cols = np.where(board[0] == 0)[0]
    for col in nonfull_cols:
        # Creates the attack and defense moves, to check if one is a winning move
        attack_board = np.copy(update_board(board, col, player))
        defense_board = np.copy(update_board(board, col, abs(player-3)))
        # Plays if winning move for him
        if check_win(attack_board, col, player):
            #print('Plays attack move')
            return col
        # Plays if winning move for opponent
        elif check_win(defense_board, col, abs(player-3)):
            #print('Plays defense move')
            return col
    # Otherwise, plays random
    return rd.choice(nonfull_cols)
    
def update_board(arg_board, col, player):
    board = np.copy(arg_board)
    # The arguments are the board and the last move of the last player
    for i in range(5,-1,-1):
        if board[i][col] == 0:
            board[i][col] = player
            return board
            
def print_board(board):
    # For visualisation
    for i in range(6):
        print('|', end = '')
        for j in range(7):
            if board[i][j] == 1:
                print('🔴 ', end = '') # Change the red dot with '1' or 'x' if your terminal does not support colours
            elif board[i][j] == 2:
                print('🔵 ', end = '') # Change the blue dot with '2' or 'o' if your terminal does not support colours
            else:
                print('   ', end = '')
        print('|')
    print('')
    
def check_win(board, col, player):
    # This function checks if the player won with his last move.
    # The arguments are the board and the last move of the last player.
    # First, we locate the row of this last move.
    row = 6
    for i in range(6):
        if board[i][col] == player:
            row = i
            break
    # Check left
    if col > 2:
        if board[row][col-1] == player:
            if board[row][col-2] == player:
                if board[row][col-3] == player:
                    return True
    # Check 2 lefts and 1 right
    if col > 1 and col < 6:
        if board[row][col-1] == player:
            if board[row][col-2] == player:
                if board[row][col+1] == player:
                    return True
    # Check 1 left and 2 rights
    if col > 0 and col < 5:
        if board[row][col-1] == player:
            if board[row][col+1] == player:
                if board[row][col+2] == player:
                    return True
    # Check right
    if col < 4:
        if board[row][col+1] == player:
            if board[row][col+2] == player:
                if board[row][col+3] == player:
                    return True
    # Check up
    if row > 2:
        if board[row-1][col] == player:
            if board[row-2][col] == player:
                if board[row-3][col] == player:
                    return True
    # Check 2 ups and 1 down
    if row > 1 and row < 5:
        if board[row-1][col] == player:
            if board[row-2][col] == player:
                if board[row+1][col] == player:
                    return True
    # Check 1 up and 2 downs
    if row > 0 and row < 4:
        if board[row-1][col] == player:
            if board[row+1][col] == player:
                if board[row+2][col] == player:
                    return True
    # Check down
    if row < 3:
        if board[row+1][col] == player:
            if board[row+2][col] == player:
                if board[row+3][col] == player:
                    return True
    # Check NW (North West)
    if col > 2 and row > 2:
        if board[row-1][col-1] == player:
            if board[row-2][col-2] == player:
                if board[row-3][col-3] == player:
                    return True
    # Check 2 NW and 1 SE
    if col > 1 and col < 6 and row > 1 and row < 5:
        if board[row-1][col-1] == player:
            if board[row-2][col-2] == player:
                if board[row+1][col+1] == player:
                    return True
    # Check 1 NW and 2 SE
    if col > 0 and col < 5 and row > 0 and row < 4:
        if board[row-1][col-1] == player:
            if board[row+1][col+1] == player:
                if board[row+2][col+2] == player:
                    return True
    # Check SE (South East)
    if col < 4 and row < 3:
        if board[row+1][col+1] == player:
            if board[row+2][col+2] == player:
                if board[row+3][col+3] == player:
                    return True
    # Check NE
    if col < 4 and row > 2:
        if board[row-1][col+1] == player:
            if board[row-2][col+2] == player:
                if board[row-3][col+3] == player:
                    return True
    # Check 2 NE and 1 SW
    if col > 0 and col < 5 and row > 1 and row < 5:
        if board[row-1][col+1] == player:
            if board[row-2][col+2] == player:
                if board[row+1][col-1] == player:
                    return True
    # Check 1 NE and 2 SW
    if col > 1 and col < 6 and row > 0 and row < 4:
        if board[row-1][col+1] == player:
            if board[row+1][col-1] == player:
                if board[row+2][col-2] == player:
                    return True
    # Check SW
    if col > 2 and row < 3:
        if board[row+1][col-1] == player:
            if board[row+2][col-2] == player:
                if board[row+3][col-3] == player:
                    return True
    return False
############################################################################################################################################
def run_game():
    # Run the game. In 21 turns, the board is full and the game is over
    the_board = np.full((6, 7), 0)
    for x in range(21):
        #print('Player 🔴 turn:')
        ####################################################################################
        ### Replace the line below with your own AI for sections 3 and 4 of the homework ###
        ####################################################################################
        
        #x = input("enter the column'number >>> ")
        move1 =ai_student(the_board, 1)#int(x)#  #  #lucas_ia(the_board, 1)
        if the_board[0][move1] != 0:
            print('ERROR: The chosen column is already full.')
        the_board = update_board(the_board, move1, 1)
        #print_board(the_board) # Uncomment this line for visualisation / debugging
        if check_win(the_board, move1, 1):
            #print('Player 🔴 won!')
            return 1
    
        #print('Player 🔵 turn:')
        ####################################################################################
        ### Replace the line below with your own AI for sections 3 and 4 of the homework ###
        ####################################################################################
        
        move2 =ai_random(the_board, 2) 
        if the_board[0][move2] != 0:
            print('ERROR: The chosen column is already full.')
        the_board = update_board(the_board, move2, 2)
        #print_board(the_board)  # Uncomment this line for visualisation / debugging
        if check_win(the_board, move2, 2):
            #print('Player 🔵 won!')
            return 2
    #print('Draw!')
    return 0
print(run_game())
"""
win=0
for i in range(1000):
    result = run_game()
    if result ==1:
        win+=1
print(win/1000*100)
print("fin")
"""