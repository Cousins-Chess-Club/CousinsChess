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
    from_square_number = int(input("Choose a square(0-63): "))

    from_square = chess_board[from_square_number]
    piece = from_square["piece"]
    color = from_square["color"]

    print("Square", from_square_number, "has a", color, piece)
    
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

                if len(legal_moves) == 0:
                    continue
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

            if len(legal_moves) == 0:
                    continue
        #####################################################################################
        if piece == "Rook":
            #PLACEHOLDER CODE! NOT COMPLETE!
            row_number = int

            row_0 = [0, 1, 2, 3, 4, 5, 6, 7]
            row_1 = []
            row_2 = []
            row_3 = []
            row_4 = []
            row_5 = []
            row_6 = []
            row_7 = []
            
            column_number = int

            column_0 = [0, 8, 16, 24, 32, 40, 48, 56]
            column_1 = []
            column_2 = []
            column_3 = []
            column_4 = []
            column_5 = []
            column_6 = []
            column_7 = []

            row_number = from_square_number / 8 
            column_number = from_square_number % 8

            legal_moves = row_0 + column_0

        
        #Can't move to squares with a same color piece
        if color == "White":
            legal_moves = [move for move in legal_moves if chess_board[move]["color"] != "White"]

        elif color == "Black":
            legal_moves = [move for move in legal_moves if chess_board[move]["color"] != "Black"]
        
        #Choose where you want to move
        print("Legal moves:", legal_moves)
        to_square_number = int(input("Choose where you want to move: "))
            
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

