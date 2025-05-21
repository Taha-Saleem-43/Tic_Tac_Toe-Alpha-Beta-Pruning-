import pygame
import sys
from gui import draw_lines, draw_figures, get_board_pos, print_message, update_display
from Alphabeta import AlphaBetaPruning

def check_winner(board, player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def is_draw(board):
    return ' ' not in board and not check_winner(board, 'X') and not check_winner(board, 'O')


def game_loop():
    board = [' ' for _ in range(9)]
    ai = AlphaBetaPruning()
    current_player = 'X'
    game_over = False

    draw_lines()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                index = get_board_pos(mouseX, mouseY)

                if board[index] == ' ' and current_player == 'X':
                    board[index] = 'X'
                    if check_winner(board, 'X'):
                        game_over = True
                        print_message("You Win!")
                    elif is_draw(board):
                        game_over = True
                        print_message("It's a Draw!")
                    else:
                        current_player = 'O'

            if not game_over and current_player == 'O':
                pygame.time.delay(300)
                move = ai.best_move(board)
                if move != -1:
                    board[move] = 'O'
                    if check_winner(board, 'O'):
                        game_over = True
                        print_message("AI Wins!")
                    elif is_draw(board):
                        game_over = True
                        print_message("It's a Draw!")
                    else:
                        current_player = 'X'

        update_display(board)

        if game_over:
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    game_loop()
