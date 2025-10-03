
import random 
import pandas as pd


pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)



def snakes_ladders(n, num_players=4):
    final_square = n * n 
    
    dice_history = [[] for _ in range(num_players)]
    
    pos_history =[[] for _ in range(num_players)]
    
    win_status = [0] * num_players
    
    
    positions = [0] * num_players
    turn = 0
    winner_found = False
    
    #dice
    while not winner_found:
        current_player = turn % num_players
        dice_roll = random.randint(1,6)
        dice_history[current_player].append(dice_roll)
    
        
        new_position = positions[current_player] + dice_roll
            
        if new_position > final_square:
            new_position = positions[current_player]
            
        positions[current_player] = new_position
        
        
        
        pos_history[current_player].append(new_position)
    
        if new_position == final_square:
            win_status[current_player] = 1
            winner_found = True
        
        turn += 1
    
        
    df = pd.DataFrame({
        "Players":[f"Player {i+1}" for i in range(num_players)],
        "Dice Roll History":[",".join(map(str, pos)) for pos in dice_history],
        "Position History":[",".join(map(str, pos)) for pos in pos_history],
        "Win Status": win_status
    })
    
    return df
    
df = snakes_ladders(10)

print(df)
        
    
    
        
