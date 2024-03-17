import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('e:/rue chess/chess heatmap/dataset/chess_games.csv')
to_remove_cols = list(df.columns)
to_remove_cols.pop()  
df = df.drop(columns = to_remove_cols)
df.head(5)


def squares_dictionary_maker():
    dictionary = {}
    for i in range(8):
        for j in range(8):
            square = chr(97+i) + str(j+1)
            dictionary[square] = 0
            
    return dictionary

# print(squares_dictionary_maker())
sq_dict = squares_dictionary_maker()

#Fills the above created dictionary 
def board_heatmap(moves):  
    moves = moves.split(' ')
    moves = [move for move in moves if move.endswith('.') == False]
    for move in moves:
        if move.startswith('O-'):
            if move == 'O-O':
                index = moves.index(move)
                if index%2 == 0:
                    sq_dict['f1'] = sq_dict['f1'] + 1
                    sq_dict['g1'] = sq_dict['g1'] + 1
                else:
                    sq_dict['f8'] = sq_dict['f8'] + 1
                    sq_dict['g8'] = sq_dict['g8'] + 1
                moves[index] = ''
            elif move == 'O-O-O':
                index = moves.index(move)
                if index%2 == 0:
                    sq_dict['d1'] = sq_dict['d1'] + 1
                    sq_dict['c1'] = sq_dict['c1'] + 1
                else:
                    sq_dict['d8'] = sq_dict['d8'] + 1
                    sq_dict['c8'] = sq_dict['c8'] + 1
                moves[index] = ''
        elif move.endswith('+') or move.endswith('#'):
            if str(move[-3]) == '=':
                sq_dict[str(move[-5:-3])] = sq_dict[str(move[-5:-3])] + 1
            else:
                sq_dict[str(move[-3:-1])] = sq_dict[str(move[-3:-1])] + 1
        elif move.endswith('Q') or move.endswith('N') or move.endswith('B') or move.endswith('R'):
            sq_dict[str(move[-4:-2])] = sq_dict[str(move[-4:-2])] + 1
        elif move == '':
            continue
        else:
            sq_dict[str(move[-2:])] = sq_dict[str(move[-2:])] + 1
    
    return True


#Making a 2d-array from our dictionary
def dict_formatter(dict):  
    square_values = np.array(list(sq_dict.values())) 
    square_values = square_values.reshape(8, 8)
    sq_T = square_values.T
    sq_T = np.flip(sq_T, 0)
    return sq_T


#heat map for each pieces:
def piece_heatmap(piece, moves):
    moves = moves.split(' ')
    if piece == 'knight':
        moves = [move for move in moves if (move.startswith('N') == True)]
    elif piece == 'bishop':
        moves = [move for move in moves if (move.startswith('B') == True)]
    elif piece == 'rook':
        moves = [move for move in moves if (move.startswith('R') == True)]
    elif piece == 'king':
        moves = [move for move in moves if (move.startswith('K') == True)]
    elif piece == 'queen':
        moves = [move for move in moves if (move.startswith('Q') == True)]
    moves = ' '.join(moves)
    x = board_heatmap(moves)
    return True


sq_dict = squares_dictionary_maker()

#np.vectorize(piece_heatmap)('rook', df['Moves']) #this is for individual piece 

np.vectorize(board_heatmap)(df['Moves'])
heatmap_frame = pd.DataFrame(dict_formatter(sq_dict))
heatmap_frame.index = ['8', '7', '6', '5', '4', '3', '2', '1']
heatmap_frame.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
heatmap_frame

fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(heatmap_frame, ax=ax, annot = True, cmap='YlGnBu')


# print(heatmap_frame)
# print(dict_formatter(dict))
plt.show()


