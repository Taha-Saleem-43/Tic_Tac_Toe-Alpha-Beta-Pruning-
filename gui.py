import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
SPACE = SQUARE_SIZE // 4
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

# Screen and font setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")
screen.fill(BG_COLOR)
font = pygame.font.SysFont(None, 40)

def draw_lines():
    for row in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures(board):
    for row in range(3):
        for col in range(3):
            pos = row * 3 + col
            if board[pos] == 'X':
                start_desc = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (start_desc[0], end_desc[1]),
                                 (end_desc[0], start_desc[1]),
                                 CROSS_WIDTH)
            elif board[pos] == 'O':
                center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

def get_board_pos(x, y):
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row * 3 + col

def print_message(msg):
    screen.fill(BG_COLOR)
    text = font.render(f"{msg}", True, (255, 255, 255))
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 30))
    pygame.display.update()

def update_display(board):
    draw_lines()
    draw_figures(board)
    pygame.display.update()
