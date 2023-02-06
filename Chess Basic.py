#Create the chess board with 64 squares
chess_board = []

for i in range(64):
  chess_board.append({"piece": None, "color": None})

#Place the pieces on their starting positions
chess_board[0]["piece"] = "Rook"
chess_board[0]["color"] = "White"
chess_board[1]["piece"] = "Knight"
chess_board[1]["color"] = "White"
chess_board[2]["piece"] = "Bishop"
chess_board[2]["color"] = "White"
chess_board[3]["piece"] = "Queen"
chess_board[3]["color"] = "White"
chess_board[4]["piece"] = "King"
chess_board[4]["color"] = "White"
chess_board[5]["piece"] = "Bishop"
chess_board[5]["color"] = "White"
chess_board[6]["piece"] = "Knight"
chess_board[6]["color"] = "White"
chess_board[7]["piece"] = "Rook"
chess_board[7]["color"] = "White"

for i in range(8, 16):
  chess_board[i]["piece"] = "Pawn"
  chess_board[i]["color"] = "White"

for i in range(48, 56):
  chess_board[i]["piece"] = "Pawn"
  chess_board[i]["color"] = "Black"

chess_board[56]["piece"] = "Rook"
chess_board[56]["color"] = "Black"
chess_board[57]["piece"] = "Knight"
chess_board[57]["color"] = "Black"
chess_board[58]["piece"] = "Bishop"
chess_board[58]["color"] = "Black"
chess_board[59]["piece"] = "Queen"
chess_board[59]["color"] = "Black"
chess_board[60]["piece"] = "King"
chess_board[60]["color"] = "Black"
chess_board[61]["piece"] = "Bishop"
chess_board[61]["color"] = "Black"
chess_board[62]["piece"] = "Knight"
chess_board[62]["color"] = "Black"
chess_board[63]["piece"] = "Rook"
chess_board[63]["color"] = "Black"

#Game state
turn = "White"
  
#Start the game
while True:
    
    #Choose the square with the piece you want to move
    from_square_notation = (input("Choose a piece(use notation): "))

    def square_notation_to_num(notation):
        files = "abcdefgh"
        file = files.index(notation[0])
        rank = int(notation[1]) - 1
        return 8 * rank + file
    
    from_square_number = square_notation_to_num(from_square_notation)
    
    from_square = chess_board[from_square_number]
    piece = from_square["piece"]
    color = from_square["color"]

    print("Square", from_square_notation, "has a", color, piece)
    
    if color == turn:    

        #Rules for pieces
        #####################################################################################
        if piece == "Pawn":
            if color == "White":
                legal_moves = [from_square_number + 7, from_square_number + 8, from_square_number + 9, from_square_number + 16]

                if from_square_number > 15:
                    legal_moves.remove(from_square_number + 16)
                if chess_board[from_square_number + 8]["color"] != None:   
                    if from_square_number <= 15:
                        legal_moves.remove(from_square_number + 8)
                        legal_moves.remove( from_square_number + 16)
                    else:
                        legal_moves.remove(from_square_number + 8)
                if chess_board[from_square_number + 7]["color"] != "Black":    
                    legal_moves.remove(from_square_number + 7)
                if chess_board[from_square_number + 9]["color"] != "Black":   
                    legal_moves.remove(from_square_number + 9) 

                if len(legal_moves) == 0:
                    continue
            
            elif color == "Black":
                legal_moves = [from_square_number - 7, from_square_number - 8, from_square_number - 9, from_square_number - 16]

                if from_square_number < 48:
                    legal_moves.remove(from_square_number - 16)
                if chess_board[from_square_number - 8]["color"] != None:   
                    if from_square_number >= 48:
                        legal_moves.remove(from_square_number - 8, from_square_number - 16)
                    else:
                        legal_moves.remove(from_square_number - 8)
                if chess_board[from_square_number - 7]["color"] != "White":    
                    legal_moves.remove(from_square_number - 7)
                if chess_board[from_square_number - 9]["color"] != "White":   
                    legal_moves.remove(from_square_number - 9) 
        #####################################################################################
        if piece == "Knight":
            legal_moves = [from_square_number - 17, from_square_number - 15, from_square_number - 10, from_square_number - 6, from_square_number + 6, from_square_number + 10, from_square_number + 15, from_square_number + 17]   

            if from_square_number % 8 < 2:
                if from_square_number - 10 in legal_moves:    
                    legal_moves.remove(from_square_number - 10)
                if from_square_number +6 in legal_moves:
                    legal_moves.remove(from_square_number + 6)
            if from_square_number % 8 < 1:
                if from_square_number - 17 in legal_moves:
                    legal_moves.remove(from_square_number - 17)
                if from_square_number + 15 in legal_moves:
                    legal_moves.remove(from_square_number + 15)
            if from_square_number % 8 > 5:
                if from_square_number + 10 in legal_moves:
                    legal_moves.remove(from_square_number + 10)
                if from_square_number - 6 in legal_moves:
                    legal_moves.remove(from_square_number - 6)
            if from_square_number % 8 > 6:
                if from_square_number + 17 in legal_moves:
                    legal_moves.remove(from_square_number + 17)
                if from_square_number - 15 in legal_moves:
                    legal_moves.remove(from_square_number - 15)           
            if from_square_number / 8 < 2:
                if from_square_number - 17 in legal_moves:
                    legal_moves.remove(from_square_number - 17)
                if from_square_number - 15 in legal_moves:
                    legal_moves.remove(from_square_number - 15)
            if from_square_number / 8 < 1:   
                if from_square_number - 10 in legal_moves:
                    legal_moves.remove(from_square_number - 10)
                if from_square_number - 6 in legal_moves:
                    legal_moves.remove(from_square_number - 6)
            if from_square_number / 8 > 6:
                if from_square_number + 17 in legal_moves:
                    legal_moves.remove(from_square_number + 17)
                if from_square_number + 15 in legal_moves:
                    legal_moves.remove(from_square_number + 15)
            if from_square_number / 8 > 7:   
                if from_square_number + 10 in legal_moves:
                    legal_moves.remove(from_square_number + 10)
                if from_square_number + 6 in legal_moves:
                    legal_moves.remove(from_square_number + 6)
        #####################################################################################
        if piece == "Rook":
            row_0 = [0, 1, 2, 3, 4, 5, 6, 7]
            row_1 = [8, 9, 10, 11, 12, 13, 14, 15]
            row_2 = [16, 17, 18, 19, 20, 21, 22, 23]
            row_3 = [24, 25, 26, 27, 28, 29, 30, 31]
            row_4 = [32, 33, 34, 35, 36, 37, 38, 39]
            row_5 = [40, 41, 42, 43, 44, 45, 46, 47]
            row_6 = [48, 49, 50, 51, 52, 53, 54, 55]
            row_7 = [56, 57, 58, 59, 60, 61, 62, 63]

            column_0 = [0, 8, 16, 24, 32, 40, 48, 56]
            column_1 = [1, 9, 17, 25, 33, 41, 49, 57]
            column_2 = [2, 10, 18, 26, 34, 42, 50, 58]
            column_3 = [3, 11, 19, 27, 35, 43, 51, 59]
            column_4 = [4, 12, 20, 28, 36, 44, 52, 60]
            column_5 = [5, 13, 21, 29, 37, 45, 53, 61]
            column_6 = [6, 14, 22, 30, 38, 46, 54, 62]
            column_7 = [7, 15, 23, 31, 39, 47, 55, 63]

            row_number = from_square_number // 8 
            column_number = from_square_number % 8

            row = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7][row_number]
            column = [column_0, column_1, column_2, column_3, column_4, column_5, column_6, column_7][column_number]

            legal_moves = set(row) | set(column)
        #####################################################################################
        if piece == "Bishop":
            row_number = from_square_number // 8 
            column_number = from_square_number % 8

            up_left = [from_square_number + 7, from_square_number + 14, from_square_number + 21, from_square_number + 28, from_square_number + 35, from_square_number + 42, from_square_number + 49] 
            up_right = [from_square_number + 9, from_square_number + 18, from_square_number + 27, from_square_number + 36, from_square_number + 45, from_square_number + 54, from_square_number + 63]
            down_left = [from_square_number - 9, from_square_number - 18, from_square_number - 27, from_square_number - 36, from_square_number - 45, from_square_number - 54, from_square_number - 63]
            down_right = [from_square_number - 7, from_square_number - 14, from_square_number - 21, from_square_number - 28, from_square_number - 35, from_square_number - 42, from_square_number - 49]
            #EXTREMELY BAD SOLUTION!!! FIX IT!!!!!
            up_left2 = [from_square_number + 7, from_square_number + 14, from_square_number + 21, from_square_number + 28, from_square_number + 35, from_square_number + 42, from_square_number + 49] 
            up_right2 = [from_square_number + 9, from_square_number + 18, from_square_number + 27, from_square_number + 36, from_square_number + 45, from_square_number + 54, from_square_number + 63]
            down_left2 = [from_square_number - 9, from_square_number - 18, from_square_number - 27, from_square_number - 36, from_square_number - 45, from_square_number - 54, from_square_number - 63]
            down_right2 = [from_square_number - 7, from_square_number - 14, from_square_number - 21, from_square_number - 28, from_square_number - 35, from_square_number - 42, from_square_number - 49]

            up_right = up_right[:-column_number or None] # FUCK PYTHON
            down_right = down_right[:-column_number or None]
            up_left = up_left[:-(7-column_number) or None]
            down_left = down_left[:-(7-column_number) or None]

            up_left2 = up_left2[:-row_number or None]
            up_right2 = up_right2[:-row_number or None]
            down_left2 = down_left2[:-(7-row_number) or None]
            down_right2 = down_right2[:-(7-row_number) or None]

            if len(up_right) > len(up_right2):
                final_up_right = up_right2 
            else:
                final_up_right = up_right 
            if len(up_left) > len(up_left2):
                final_up_left = up_left2 
            else:
                final_up_left = up_left
            if len(down_right) > len(down_right2):
                final_down_right = down_right2 
            else:
                final_down_right = down_right 
            if len(down_left) > len(down_left2):
                final_down_left = down_left2 
            else:
                final_down_left = down_left

            legal_moves = set(final_up_left) | set(final_up_right) | set(final_down_left) | set(final_down_right)
        #####################################################################################   
        #Queen needs to be cleaned up
        if piece == "Queen":
            row_number = from_square_number // 8 
            column_number = from_square_number % 8

            up_left = [from_square_number + 7, from_square_number + 14, from_square_number + 21, from_square_number + 28, from_square_number + 35, from_square_number + 42, from_square_number + 49] 
            up_right = [from_square_number + 9, from_square_number + 18, from_square_number + 27, from_square_number + 36, from_square_number + 45, from_square_number + 54, from_square_number + 63]
            down_left = [from_square_number - 9, from_square_number - 18, from_square_number - 27, from_square_number - 36, from_square_number - 45, from_square_number - 54, from_square_number - 63]
            down_right = [from_square_number - 7, from_square_number - 14, from_square_number - 21, from_square_number - 28, from_square_number - 35, from_square_number - 42, from_square_number - 49]

            up_left2 = [from_square_number + 7, from_square_number + 14, from_square_number + 21, from_square_number + 28, from_square_number + 35, from_square_number + 42, from_square_number + 49] 
            up_right2 = [from_square_number + 9, from_square_number + 18, from_square_number + 27, from_square_number + 36, from_square_number + 45, from_square_number + 54, from_square_number + 63]
            down_left2 = [from_square_number - 9, from_square_number - 18, from_square_number - 27, from_square_number - 36, from_square_number - 45, from_square_number - 54, from_square_number - 63]
            down_right2 = [from_square_number - 7, from_square_number - 14, from_square_number - 21, from_square_number - 28, from_square_number - 35, from_square_number - 42, from_square_number - 49]

            up_right = up_right[:-column_number or None]
            down_right = down_right[:-column_number or None]
            up_left = up_left[:-(7-column_number) or None]
            down_left = down_left[:-(7-column_number) or None]

            up_left2 = up_left2[:-row_number or None]
            up_right2 = up_right2[:-row_number or None]
            down_left2 = down_left2[:-(7-row_number) or None]
            down_right2 = down_right2[:-(7-row_number) or None]

            if len(up_right) > len(up_right2):
                final_up_right = up_right2 
            else:
                final_up_right = up_right 
            if len(up_left) > len(up_left2):
                final_up_left = up_left2 
            else:
                final_up_left = up_left
            if len(down_right) > len(down_right2):
                final_down_right = down_right2 
            else:
                final_down_right = down_right 
            if len(down_left) > len(down_left2):
                final_down_left = down_left2 
            else:
                final_down_left = down_left
            
            row_0 = [0, 1, 2, 3, 4, 5, 6, 7]
            row_1 = [8, 9, 10, 11, 12, 13, 14, 15]
            row_2 = [16, 17, 18, 19, 20, 21, 22, 23]
            row_3 = [24, 25, 26, 27, 28, 29, 30, 31]
            row_4 = [32, 33, 34, 35, 36, 37, 38, 39]
            row_5 = [40, 41, 42, 43, 44, 45, 46, 47]
            row_6 = [48, 49, 50, 51, 52, 53, 54, 55]
            row_7 = [56, 57, 58, 59, 60, 61, 62, 63]

            column_0 = [0, 8, 16, 24, 32, 40, 48, 56]
            column_1 = [1, 9, 17, 25, 33, 41, 49, 57]
            column_2 = [2, 10, 18, 26, 34, 42, 50, 58]
            column_3 = [3, 11, 19, 27, 35, 43, 51, 59]
            column_4 = [4, 12, 20, 28, 36, 44, 52, 60]
            column_5 = [5, 13, 21, 29, 37, 45, 53, 61]
            column_6 = [6, 14, 22, 30, 38, 46, 54, 62]
            column_7 = [7, 15, 23, 31, 39, 47, 55, 63]

            row = [row_0, row_1, row_2, row_3, row_4, row_5, row_6, row_7][row_number]
            column = [column_0, column_1, column_2, column_3, column_4, column_5, column_6, column_7][column_number]

            legal_moves = set(final_up_left) | set(final_up_right) | set(final_down_left) | set(final_down_right) | set(row) | set(column)
        #####################################################################################
        if piece == "King":
            legal_moves = [from_square_number - 9, from_square_number - 8, from_square_number - 7, from_square_number - 1, from_square_number + 1, from_square_number + 7, from_square_number + 8, from_square_number + 9]

            if from_square_number % 8 < 1:
                if from_square_number - 9 in legal_moves:
                    legal_moves.remove(from_square_number - 9)
                if from_square_number - 1 in legal_moves:
                    legal_moves.remove(from_square_number  - 1)
                if from_square_number + 7 in legal_moves:
                    legal_moves.remove(from_square_number + 7)
            if from_square_number % 8 > 6:
                if from_square_number - 7 in legal_moves:
                    legal_moves.remove(from_square_number - 7)
                if from_square_number + 1 in legal_moves:
                    legal_moves.remove(from_square_number + 1) 
                if from_square_number + 9 in legal_moves:
                    legal_moves.remove(from_square_number + 9)
            if from_square_number / 8 < 1:
                if from_square_number - 7 in legal_moves:
                    legal_moves.remove(from_square_number - 7)
                if from_square_number - 8 in legal_moves:
                    legal_moves.remove(from_square_number - 8)
                if from_square_number - 9 in legal_moves:
                    legal_moves.remove(from_square_number - 9)
            if from_square_number / 8 > 6:   
                if from_square_number + 7 in legal_moves:
                    legal_moves.remove(from_square_number + 7)
                if from_square_number + 8 in legal_moves:
                    legal_moves.remove(from_square_number + 8)
                if from_square_number + 9 in legal_moves:
                    legal_moves.remove(from_square_number + 9)
        #####################################################################################
        
        #Can't move to squares with a same color piece
        if color == "White":
            legal_moves = [move for move in legal_moves if chess_board[move]["color"] != "White"]

        elif color == "Black":
            legal_moves = [move for move in legal_moves if chess_board[move]["color"] != "Black"]
        
        #Choose where you want to move

        if len(legal_moves) == 0:
            continue
        
        files = 'abcdefgh'
        ranks = '12345678'

        def num_to_square_notation(square):
            file = files[square % 8]
            rank = ranks[square // 8]
            return f"{file}{rank}"

        def square_notation_to_num(notation):
            files = "abcdefgh"
            file = files.index(notation[0])
            rank = int(notation[1]) - 1
            return 8 * rank + file

        legal_move_notations = [num_to_square_notation(move) for move in legal_moves]

        print("Legal moves:", *legal_move_notations)

        to_square_notation = (input("Choose where you want to move: "))

        to_square_number = square_notation_to_num(to_square_notation)
            
        to_square = chess_board[to_square_number]

        #illegal shit
        if to_square["color"] == from_square["color"] or from_square["piece"] == None: 
            continue

        #Move piece to new square
        to_square["piece"] = piece
        to_square["color"] = color
            
        from_square["piece"] = None
        from_square["color"] = None

        #Change turn
        if turn == "White":
            turn = "Black"
        elif turn == "Black":
            turn = "White"
    
    else:
        continue
