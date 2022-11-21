import numpy as np
import matplotlib.pyplot as plt
import connect4
import time
import ai_student

t = time.time()

N = 10 # Nb repetitions
nb_games = [10, 100, 1000,10000]
# Array with the percentage of success for player 1 for [10, 100, 1000, 10000] games, N times each
win1 = np.zeros((N, len(nb_games)))
# Array with the percentage of draws for player 1 for [10, 100, 1000, 10000] games, N times each
draw = np.zeros((N, len(nb_games)))

##################################
### START : To do for students ###
##################################

# To do : fill in arrays win1 and draw
# In order to do so, simulate games with the function connect4.run_game()
"""
row=0
count = 0
for j in range (N):
    countWin=0
    countDraw=0
    col=0
    for i in (nb_games):   
        for k in range (i):
            result=ai_student.run_game()
            ok +=1
            if result == 1:
                countWin+=1
                
            if result ==0:
                countDraw+=1
                
        win1[row][col]=(countWin/i)*100
        draw[row][col]=(countDraw/i)*100
        col+=1
        print("fin game")
    print(f"fin experience{count}")
    count+=1
    row+=1
"""
N = 10
nb_games = [10, 100, 1000,10000]
# Array with the percentage of success for player 1 for [10, 100, 1000, 10000] games, N times each
win1 = np.zeros((N, len(nb_games)))
# Array with the percentage of draws for player 1 for [10, 100, 1000, 10000] games, N times each
draw = np.zeros((N, len(nb_games)))

lose = np.zeros((N, len(nb_games)))
row = 0
col = 0
count = 0
for g in nb_games :
    
    for i in range(N):
        wi = 0
        ex = 0
        lo = 0
        for j in range(g):
           
            result = ai_student.run_game()
            if result == 0 :
                ex += 1
            if result == 1:
                wi += 1
            if result == 2 :
                lo += 1
        win1[row][col] = (wi/g)*100
        draw[row][col] = (ex/g)*100
        lose[row][col] = (lo/g)*100
        row += 1
        print("fin experience")
    print(f"fin game {count}")
    count +=1
    row = 0
    col += 1
            
    ################################
### END : To do for students ###
################################

# Computes and prints de mean for each [10, 100, 1000, 10000]
win1_mean = np.mean(win1, axis=0)
draw_mean = np.mean(draw, axis=0)
print(win1_mean)
print(draw_mean)

# Plot the results in the required format.
# Please do not modify
plt.figure()
for i in range(len(nb_games)):
    plt.scatter(np.full(N, nb_games[i]), win1[:,i], c = 'blue', s = 10)
    plt.scatter(np.full(N, nb_games[i]), draw[:,i], c = 'red', s = 10)
    plt.scatter(nb_games[i], win1_mean[i], c = 'blue', marker = 'x', s = 50)
    plt.scatter(nb_games[i], draw_mean[i], c = 'red', marker = 'x', s = 50)
plt.legend(['Victoire joueur 1', 'Ex-aequo', 'Moyenne victoire joueur 1', 'Moyenne ex-aequo'])
plt.xlabel('Nombre de parties')
plt.ylabel('Probabilite en %')
plt.xscale("log")
plt.ylim((-10,100))
plt.show()

elapsed = time.time() - t
print('Elapsed time: ', elapsed)

plt.savefig('MCplot.png', format='png')