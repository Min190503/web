import pygame
import sys

pygame.init()

# Các màu sắc và kích thước cửa sổ
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
button_color = white  # Màu nền mặc định cho các nút không được nhấn
text_color = black  # Màu chữ mặc định
screen_width, screen_height = 540, 600
cell_size = screen_width // 9
board_size = 9 * cell_size

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sudoku Game')

# Bảng Sudoku mẫu để hiển thị và điền số
initial_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solution_board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

board = [row[:] for row in initial_board]  # Tạo một bản sao của bảng mẫu

# Hàm vẽ bảng Sudoku
def draw_board():
    screen.fill(white)
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, black, (0, i * cell_size), (board_size, i * cell_size), thickness)
        pygame.draw.line(screen, black, (i * cell_size, 0), (i * cell_size, board_size), thickness)

    font = pygame.font.Font(None, 40)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                text = font.render(str(board[i][j]), True, black)
                screen.blit(text, (j * cell_size + 20, i * cell_size + 15))

    pygame.display.update()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // cell_size
    col = x // cell_size
    return row, col

def is_valid(board, row, col, num):
    # Kiểm tra hàng và cột
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Kiểm tra vùng 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def is_board_complete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def is_solution_correct(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
            num = board[i][j]
            board[i][j] = 0
            if not is_valid(board, i, j, num):
                board[i][j] = num
                return False
            board[i][j] = num
    return True

def reset_board():
    for i in range(9):
        for j in range(9):
            board[i][j] = initial_board[i][j]

def draw_button(text, rect, color):
    pygame.draw.rect(screen, color, rect)
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

check_button = pygame.Rect(200, 550, 140, 40)
show_solution_button = pygame.Rect(350, 550, 140, 40)
check_button_hover = False
show_solution_button_hover = False

running = True
selected = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            selected = get_row_col_from_mouse(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN and selected:
            row, col = selected
            if board[row][col] == 0 and event.unicode.isdigit():
                num = int(event.unicode)
                if is_valid(board, row, col, num):
                    board[row][col] = num
                    selected = None
            elif event.key == pygame.K_BACKSPACE:
                board[row][col] = 0
                selected = None

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_board()

        if event.type == pygame.MOUSEMOTION:
            # Kiểm tra nếu chuột di chuyển qua nút "Check"
            if check_button.collidepoint(event.pos):
                check_button_hover = True
            else:
                check_button_hover = False

            # Kiểm tra nếu chuột di chuyển qua nút "Show Solution"
            if show_solution_button.collidepoint(event.pos):
                show_solution_button_hover = True
            else:
                show_solution_button_hover = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_button.collidepoint(event.pos):
                if is_board_complete(board):
                    if is_solution_correct(board):
                        print("Chúc mừng! Bạn đã hoàn thành Sudoku.")
                    else:
                        print("Sudoku không chính xác.")
                else:
                    print("Vẫn còn ô trống chưa điền số.")

            if show_solution_button.collidepoint(event.pos):
                board = [row[:] for row in solution_board]

    screen.fill(white)
    draw_board()

    # Hiển thị màu sắc của nút "Check" dựa trên trạng thái hover
    if check_button_hover:
        draw_button("Check", check_button, green)
    else:
        draw_button("Check", check_button, button_color)

    # Hiển thị màu sắc của nút "Show Solution" dựa trên trạng thái hover
    if show_solution_button_hover:
        draw_button("Show Solution", show_solution_button, green)
    else:
        draw_button("Show Solution", show_solution_button, button_color)

    pygame.display.flip()

pygame.quit()
sys.exit()
