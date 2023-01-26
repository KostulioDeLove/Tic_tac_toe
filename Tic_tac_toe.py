import pygame
import sys

def winner_control(mas, sing):
    zerozero = 0
    for row in  mas:
        zerozero+=row.count(0)
        if row.count(sing) ==3:
            return sing
    for col in range(3):
        if mas[0] [col]== sing and mas[1] [col]== sing and mas[2] [col]== sing:
            return sing
    if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
        return sing
    if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
        return sing
    if zerozero==0:
        return 'Piece People'
    return  False


pygame.init()
size_block = 80
margin = 10
width = height = size_block * 3 + margin * 4

size_window = (width,height)
screen = pygame.display.set_mode(size_window)
img = pygame.image.load("Krestukzero.png")
pygame.display.set_icon(img)
pygame.display.set_caption("Крестики-нолики")


black = (0, 0, 0)
blue = (0, 0, 255)
green = (0,255, 0)
white = (255, 255, 255)
red = (255, 0, 0)
mas = [[0] * 3 for i in range(3)]
request = 0
end_game = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not end_game:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block+margin)
            row = y_mouse // (size_block + margin)
            if mas[row][col] == 0:
                if request%2==0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                request+=1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            end_game = False
            mas = [[0] * 3 for i in range(3)]
            request = 0
            screen.fill(black)
    if not end_game:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == red:
                    pygame.draw.line(screen, white, (x + 7, y + 7), (x + size_block - 7, y + size_block - 7), 3)
                    pygame.draw.line(screen, white, (x + size_block - 7, y + 7), (x + 7, y + size_block - 7), 3)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3,
                                       3)
        if (request - 1) % 2 == 0:
            end_game = winner_control(mas, 'x')
        else:
            end_game = winner_control(mas, 'o')

    if end_game:
        screen.fill(black)
        font = pygame.font.SysFont('Constantia', 40)
        text1 = font.render(end_game, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2- text_rect.width /2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])


    pygame.display.update()

