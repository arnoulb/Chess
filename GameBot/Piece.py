import pygame


def getCoord(x, y):
    coord = chr(ord("a") + x - 1)
    coord += str(y)
    return(coord)


def getPosition(coord):
    x = ord(coord[0]) - ord("a") + 1
    y = int(coord[1])
    return (x, y)


def validCoord(x, y):
    ret = False
    if (x <= 8 and x > 0
            and y <= 8 and y > 0):
        ret = True
    return(ret)


def createChessPieces():
    chess_pieces = list()
    for y in range(1, 9):
        for x in range(1, 9, 1):
            color = None
            if (y == 8 or y == 7):
                color = "black"
            elif (y == 1 or y == 2):
                color = "white"

            if (y == 8 or y == 1):
                if (x == 1 or x == 8):
                    chess_pieces.append(Rook(color, x, y))
                elif (x == 2 or x == 7):
                    chess_pieces.append(Knight(color, x, y))
                elif (x == 3 or x == 6):
                    chess_pieces.append(Bishop(color, x, y))
                elif (x == 4):
                    chess_pieces.append(Queen(color, x, y))
                elif (x == 5):
                    chess_pieces.append(King(color, x, y))
            elif (y == 2 or y == 7):
                chess_pieces.append(Pawn(color, x, y))
    return(chess_pieces)


class Piece(object):
    name = None
    symbole = None
    img = None
    allowed_moves = list()
    dot = pygame.image.load("img/dot.png")
    actif = True
    first_turn = True

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        path = "img/" + color + "_" + self.name.lower() + ".png"
        self.img = pygame.image.load(path)

    def __del__(self):
        pass

    def move(self, coord, board):
        cell = board.getCell(coord)
        ret = False
        if (coord in self.allowed_moves):
            if (cell is not None and cell.color != self.color):
                cell.actif = False
            board.changeCellValue(self.getCoord(), None)
            self.first_turn = False
            board.changeCellValue(coord, self)
            self.x, self.y = getPosition(coord)
            ret = True
        return (ret)

    def getCoord(self):
        coord = chr(ord("a") + self.x - 1)
        coord += str(self.y)
        return(coord)

    def getAllowedMoves(self):
        return(self.allowed_moves)

    def print(self):
        print("Piece :", end=" ")
        print(self.color + " " + self.name, end=" ")
        print("Coord : [" + self.getCoord() + "]")

    def printMoves(self):
        print("Movements : ", end="")
        for i in self.allowed_moves:
            print(i, end=", ")
        print("")

    def display(self, win, offset=80, size=80):
        if (self.actif):
            win.blit(self.img, (size * self.x, size * (9 - self.y)))

    def displayAllowedMoves(self, win, size=80):
        for i in self.allowed_moves:
            x, y = getPosition(i)
            win.blit(self.dot, (size * x, size * (9 - y)))


class Rook(Piece):
    name = "Rook"
    symbole = "R"
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        flag = [True, True, True, True]

        for i in range(1, 8):
            for idx, (x, y) in enumerate(self.directions):
                if (validCoord(self.x + x * i, self.y + y * i)):
                    coord = getCoord(self.x + (x * i), self.y + (y * i))
                    cell = board.getCell(coord)
                    if ((cell is None
                            or (cell is not None and cell.color != self.color))
                            and flag[idx]):
                        self.allowed_moves.append(coord)
                        if (cell is not None and cell.color != self.color):
                            flag[idx] = False
                    else:
                        flag[idx] = False


class Queen(Piece):
    name = "Queen"
    symbole = "Q"
    directions = [(0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        flag = [True, True, True, True, True, True, True, True]

        for i in range(1, 8):
            for idx, (x, y) in enumerate(self.directions):
                if (validCoord(self.x + x * i, self.y + y * i)):
                    coord = getCoord(self.x + (x * i), self.y + (y * i))
                    cell = board.getCell(coord)
                    if ((cell is None
                            or (cell is not None and cell.color != self.color))
                            and flag[idx]):
                        self.allowed_moves.append(coord)
                        if (cell is not None and cell.color != self.color):
                            flag[idx] = False
                    else:
                        flag[idx] = False


class King(Piece):
    name = "King"
    symbole = "K"
    directions = [(0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        for i, j in self.directions:
            if (validCoord(self.x + i, self.y + j)):
                coord = getCoord(self.x + i, self.y + j)
                cell = board.getCell(coord)
                if (cell is None
                        or (cell is not None and cell.color != self.color)):
                    self.allowed_moves.append(coord)


class Knight(Piece):
    name = "Knight"
    symbole = "N"
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                  (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        for i, j in self.directions:
            if (validCoord(self.x + i, self.y + j)):
                coord = getCoord(self.x + i, self.y + j)
                cell = board.getCell(coord)
                if (cell is None
                        or (cell is not None and cell.color != self.color)):
                    self.allowed_moves.append(coord)


class Pawn(Piece):
    name = "Pawn"
    symbole = "P"

    def __init__(self, color, x, y):
        self.first_turn = True
        Piece.__init__(self, color, x, y)
        if (color == "white"):
            self.directions = [(0, 1), (0, 2), (1, 1), (-1, 1)]
        if (color == "black"):
            self.directions = [(0, -1), (0, -2), (1, -1), (-1, -1)]

    def setAllowedMoves(self, board):
        left_cell = None
        right_cell = None
        self.allowed_moves = list()

        for idx, (x, y) in enumerate(self.directions):
            coord = getCoord(self.x + x, self.y + y)
            cell = None
            if validCoord(self.x + x, self.y + y):
                cell = board.getCell(coord)
                if ((idx < 1 and cell is None)
                        or (idx > 1 and cell is not None and cell.color != self.color)
                        or (idx == 1 and self.first_turn and cell is None)):
                    self.allowed_moves.append(coord)


class Bishop(Piece):
    name = "Bishop"
    symbole = "B"
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        flag = [True, True, True, True]

        for i in range(1, 8):
            for idx, (x, y) in enumerate(self.directions):
                if (validCoord(self.x + x * i, self.y + y * i)):
                    coord = getCoord(self.x + (x * i), self.y + (y * i))
                    cell = board.getCell(coord)
                    if ((cell is None
                            or (cell is not None and cell.color != self.color))
                            and flag[idx]):
                        self.allowed_moves.append(coord)
                        if (cell is not None and cell.color != self.color):
                            flag[idx] = False
                    else:
                        flag[idx] = False
