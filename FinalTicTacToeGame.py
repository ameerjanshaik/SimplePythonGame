import pygame
import sys

# Begin Tic Tac Toe Game
pygame.init()

# Constant
SCREEN_WIDTH, SCREEN_HEIGHT = 300, 300
CELL_SIZE = SCREEN_WIDTH // 3
WHITE = (0, 0, 0)
BLACK = (255, 255, 255)
RED = (255, 0, 0)

# Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize The Board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Draw The Board
def game_grid():
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_HEIGHT), 2)
        pygame.draw.line(screen, WHITE, (0, i * CELL_SIZE), (SCREEN_WIDTH, i * CELL_SIZE), 2)

# Draw Marks On The Board
def game_marks():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 10, row * CELL_SIZE + 10),
                                 ((col + 1) * CELL_SIZE - 10, (row + 1) * CELL_SIZE - 10), 2)
                pygame.draw.line(screen, RED, ((col + 1) * CELL_SIZE - 10, row * CELL_SIZE + 10),
                                 (col * CELL_SIZE + 10, (row + 1) * CELL_SIZE - 10), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, RED, ((col * CELL_SIZE) + CELL_SIZE // 2, (row * CELL_SIZE) + CELL_SIZE // 2),
                                   CELL_SIZE // 2 - 10, 2)

# Check To See For Win Or Tie Or End Game
def check_game_result(game_player):
    # Check Everything For 3 Marks
    for k in range(3):
        if all(board[k][c] == game_player for c in range(3)) or all(board[c][k] == game_player for c in range(3)):
            return True
    if all(board[k][k] == game_player for k in range(3)) or all(board[k][2 - k] == game_player for k in range(3)):
        return True
    return False

# Main Loop Of The Game
def tic_tac_toe_board():
    player_one = 'X'
    check_game_over = False
    click_counter = 0

    while not check_game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not check_game_over:
                click_counter += 1
                mouse_x, mouse_y = pygame.mouse.get_pos()
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                if board[row][col] == ' ':
                    board[row][col] = player_one

                    if check_game_result(player_one):
                        check_game_over = True
                        pygame.display.set_caption(player_one + " Won!")

                    elif click_counter == 9:
                        check_game_over = True
                        pygame.display.set_caption("Its a Draw!!!")

                    player_one = 'O' if player_one == 'X' else 'X'

        screen.fill(BLACK)
        game_grid()
        game_marks()
        pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Start The Game
tic_tac_toe_board()