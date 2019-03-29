import pygame
import math
from pygame.locals import *
import ChessBoard as Board
import Piece

def playChess(board):
    end_flag = True
    counter = 1
    p = ["K", "Q", "N", "B", "R", "P"]
    while(end_flag):
        if (counter % 2):
            print("White Player : ", end="")
        else:
            print("Black Player : ", end="")
        cmd = input()
        if (len(cmd) == 3
            and cmd[0] in p 
            and ord(cmd[1]) in range(ord("a"), ord("h") + 1)
            and int(cmd[2]) in range(1,8)):
            counter += 1
        else:
            print("Wrong format")

           

def createChessBoard(chess_pieces):
    chess_board = list()
    board = {}
    ah = [chr(i) for i in range(ord("a"), ord("h") + 1)]
    for y in range(8, 0, -1):
        line = list()
        for x in ah:
            coord = x + str(y)
            board[coord] = None
            for piece in chess_pieces:
                if piece.getCoord() == coord:
                    board[coord] = piece
                    line.append(piece)
        chess_board.insert(0, line)
    return(chess_board)


def printChessPieces(pieces):
    for i in pieces:
        i.print()

def displayChessPieces(pieces, win):
    for i in pieces:
        i.display(win)

def printChessBoard(board):
    for i in board:
        for j in i:
            if (board[i] != None):
                print("Cell : " + i + " [" + board[i].symbole + "]")


def createChessPieces():
    chess_pieces = list()
    for y in range(8, 0, -1):
        for x in range(1, 9, 1):
            color = None
            if (y == 8 or y == 7):
                color = "black"
            elif (y == 1 or y == 2):
                color = "white"

            if (y == 8 or y == 1):
                if (x == 1 or x == 8):
                    chess_pieces.append(Piece.Rook(color, x, y))
                elif (x == 2 or x == 7):
                    chess_pieces.append(Piece.Knight(color, x, y))
                elif (x == 3 or x == 6):
                    chess_pieces.append(Piece.Bishop(color, x, y))
                elif (x == 4):
                    chess_pieces.append(Piece.Queen(color, x, y))
                elif (x == 5):
                    chess_pieces.append(Piece.King(color, x, y))
            elif (y == 2 or y == 7):
                chess_pieces.append(Piece.Pawn(color, x, y))
            
    return(chess_pieces)

chess_pieces = createChessPieces()
printChessPieces(chess_pieces)
chess_board = createChessBoard(chess_pieces)
board = Board.ChessBoard(chess_pieces)
board.print()
pygame.init()
width = 800
height = 800

win = pygame.display.set_mode((width, height))
mask = pygame.Surface((width, height), flags=SRCALPHA)
end_flag = True

white, black, red = (230, 230, 230), (46, 46, 46), (82, 82, 82)
empty = (0,0,0,0)
win.fill(red)
mask.fill(empty)
size = 80
offset = (width - (size * 8)) / 2
cnt = 1
for i in range(8):
    for j in range(8):
        if (cnt % 2):
            pygame.draw.rect(win, white, (offset + size * j, offset + size * i, size, size))
        else:
            pygame.draw.rect(win, black, (offset + size * j, offset + size * i, size, size))
        cnt += 1
    cnt +=1


for i in chess_pieces:
    i.display(mask);

selected = None
copy = win.copy()
win.blit(mask,(0,0))
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
                coord = chr(ord("a") + x - 1) + str(y) 
                print(coord)

                if selected != None:
                    selected.move(coord, board)
                    mask.fill(empty)

                    for i in chess_pieces:
                        i.display(mask)
                    win.blit(copy, (0,0))
                    win.blit(mask,(0,0))


                if board.getCell(coord) != None and board.getCell(coord) != selected:
                    print("select piece")
                    selected = board.getCell(coord)
                    selected.setAllowedMoves(board)
                    selected.print()
                    mask.fill(empty)
                    selected.displayAllowedMoves(mask)
                    displayChessPieces(chess_pieces, mask)
#                    for i in chess_pieces:
#                        i.display(mask)
#                        i.print()
                    win.blit(copy, (0,0))
                    win.blit(mask,(0,0))
                else:
                    selected = None

            else:
                print("Please click on the chess board")

#printChessBoard(chess_board)

#playChess(chess_board)