import pygame
import math
from pygame.locals import *
import ChessBoard as Board
import Piece
import Player

WIDTH = 800
HEIGHT = 800
COLOR_WHITE = (230, 230, 230)
COLOR_BLACK = (46, 46, 46)
COLOR_GREY = (82, 82, 82)
COLOR_EMPTY = (0, 0, 0, 0)
TILE_SIZE = 80


def printChessPieces(pieces):
    for i in pieces:
        i.print()


def displayChessPieces(pieces, win):
    for i in pieces:
        i.display(win)


def displayBackgroundTiles(win):
    offset = (WIDTH - (TILE_SIZE * 8)) / 2
    cnt = 1
    for i in range(8):
        for j in range(8):
            x = offset + TILE_SIZE * j
            y = offset + TILE_SIZE * i
            coord = (x, y, TILE_SIZE, TILE_SIZE)
            if (cnt % 2):
                pygame.draw.rect(win, COLOR_WHITE, coord)
            else:
                pygame.draw.rect(win, COLOR_BLACK, coord)
            cnt += 1
        cnt += 1


chess_pieces = Piece.createChessPieces()
board = Board.ChessBoard(chess_pieces)

pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill(COLOR_GREY)
mask = pygame.Surface((WIDTH, HEIGHT), flags=SRCALPHA)
mask.fill(COLOR_EMPTY)

for i in chess_pieces:
    i.display(mask)

displayBackgroundTiles(win)
copy = win.copy()
win.blit(mask, (0, 0))

selected = None
end_flag = True
players = [Player.Player("white"), Player.Player("black")]
cnt = 0

while end_flag:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == QUIT:
            end_flag = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                end_flag = False

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if x > 80 and x < 720 and y > 80 and y < 720:
                x = math.trunc(x / 80)
                y = 9 - math.trunc(y / 80)
                coord = Piece.getCoord(x, y)
                cell = board.getCell(coord)
                if selected is not None:
                    # Handle what to do with the selected piece
                    ret = selected.move(coord, board)
                    if (ret):
                        cnt += 1
                    mask.fill(COLOR_EMPTY)
                    displayChessPieces(chess_pieces, mask)
                    win.blit(copy, (0, 0))
                    win.blit(mask, (0, 0))

                cell = board.getCell(coord)
                if (cell is not None and cell != selected
                        and cell.color == players[cnt % 2].color):
                    # Select a piece
                    selected = board.getCell(coord)
                    selected.setAllowedMoves(board)
                    selected.displayAllowedMoves(mask)
                    displayChessPieces(chess_pieces, mask)
                    win.blit(copy, (0, 0))
                    win.blit(mask, (0, 0))
                else:
                    selected = None

            else:
                print("Please click on the chess board")
