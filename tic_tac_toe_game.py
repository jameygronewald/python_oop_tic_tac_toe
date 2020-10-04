if __name__ == "__main__":
    
    playing = True
    player = 1
    score = [0, 0, 0]
    board = [[0, 0 ,0], [0, 0, 0], [0, 0, 0]]

    vertical_line = """|   """
    end_ver_line = "|"

    def ask_user():
        try:
            print(f"\nPLAYER {player}'s TURN")
            row_choice = int(input(f"\nPlease select the ROW you would like to place your marker in (1-3):   "))
            column_choice = int(input(f"\nPlease select the COLUMN you would like to place your marker in (1-3):   "))
        except ValueError:
            print("\nInvalid input. Please enter and integer between 1 and 3.")
            return ask_user()
        if 4 > row_choice > 0 and 4 > column_choice > 0:
            return (row_choice, column_choice)
        else:
            print("\nInvalid input. Please enter and integer between 1 and 3.")
            return ask_user()

    def print_horizontal():
        horizontal_line = """ ---"""
        horizontal_string = horizontal_line * 3
        print(horizontal_string)

    def print_vertical():
        vertical_string = vertical_line * 3 + end_ver_line
        print(vertical_string)

    def choose_marker(player):
        x_move = """| X """
        o_move = """| O """
        if player == 1:
            marker = x_move
        else:
            marker = o_move
        return marker        
    
    def switch_player_turn():
        global player
        if player == 1:
            player = 2
        else:
            player = 1

    def print_vert_with_moves(row):
        global board
        vert_list = []
        row_to_evaluate = board[row]
        for i in range(3):
            if row_to_evaluate[i] == 0:
                vert_list.append(vertical_line)
            else:
                vert_list.append(choose_marker(row_to_evaluate[i]))
        vert_list.append(end_ver_line)
        vert_string = ''.join(vert_list)
        print(vert_string)

    def evaluate_board(board):
        global playing
        if board[0][0] == board[1][1] == board[2][2]:
            match = board[0][0]
            if match != 0:
                print(f"\nPlayer {match} wins!")
                score[match - 1] += 1
                playing = False
        if board[2][0] == board [1][1] == board[0][2]:
            match = board[2][0]
            if match != 0:
                print(f"\nPlayer {match} wins!")
                score[match - 1] += 1
                playing = False
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2]:
                match = board[i][0]
                if match != 0:
                    print(f"\nPlayer {match} wins!")
                    score[match - 1] += 1
                    playing = False
            if board[0][i] == board[1][i] == board[2][i]:
                match = board[0][i]
                if match != 0:
                    print(f"\nPlayer {match} wins!")
                    score[match - 1] += 1
                    playing = False
        full = 0
        for row in board:
            if 0 not in row:
                full += 1
                if full == 3:     
                    print(f"\nIt's a cat's game!")
                    score[2] += 1
                    playing = False

    def update_board(row_int, column_int):
        global board
        if board[row_int - 1][column_int - 1] == 0:
            board[row_int - 1][column_int - 1] = player
            switch_player_turn()
        else: 
            print(f"\nInvalid move. Please select a free space.")
        evaluate_board(board)
        for i in range(3):
            print_horizontal()
            print_vert_with_moves(i)
        print_horizontal()
    
    def print_board():
        for _ in range(3):
            print_horizontal()
            print_vertical()
        print_horizontal()

    def play_again():
        global playing
        try:
            again = input(f"\nPlay again? (y/n)   ")
        except TypeError: 
            print('Invalid input. Please enter y or n.')
            play_again()
        if 'y' in again.lower():
            playing = True
            init()
        elif 'n' in again.lower():
            print('\nGood game!')
            return
        else:
            print('Invalid input. Please enter y or n.')
            play_again()
    
    def clear_board():
        for row in board:
            for i in range(3):
                row[i] = 0

    def init():
        clear_board()
        print_board()
        while playing == True:
            response = ask_user()
            row = response[0]
            column = response[1]
            update_board(row, column)
        print(f"""
        The score is:
        Player 1: {score[0]}
        Player 2: {score[1]}
        Cat's game: {score[2]}""")
        play_again()
        
    init()