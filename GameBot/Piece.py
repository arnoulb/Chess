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

class Piece(object):
    name = None
    symbole = None
    img = None
    allowed_moves = list()
    dot = pygame.image.load("dot.png")
    actif = True

    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def __del__(self):
        pass

    def move(self, coord, board):
        cell = board.getCell(coord)
        if (cell != None and cell.color != self.color):
            print("REMOVE")
            cell.actif = False
        board.changeCellValue(self.getCoord(), None)
        board.changeCellValue(coord, self)
        self.x, self.y = getPosition(coord)

    def getCoord(self):
        coord = chr(ord("a") + self.x - 1)
        coord += str(self.y)
        return(coord)
 
    def getAllowedMoves(self):
        return(self.allowed_moves)

    def setAllowedMoves(self, board):
        self.allowed_moves.append("a1")
        pass

    def print(self):
        print("Piece :", end=" ")
        print(self.color + " " + self.name, end=" ")
        print("Coord : [" + self.getCoord() + "]")
    
    def printMoves(self):
        print("Movements : ", end="")
        for i in self.allowed_moves:
            print(i, end=", ")
        print("")
            
    def display(self, win, offset = 80, size = 80):
        if (self.actif):
            win.blit(self.img, (size * self.x ,size * (9 - self.y)))

    def displayAllowedMoves(self, win, size = 80):
        for i in self.allowed_moves:
            x, y = getPosition(i)
            win.blit(self.dot, (size * x , size * (9 - y)))

class Rook(Piece):
    name = "Rook"
    symbole = "R"
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if (color == "white"):
            self.img = pygame.image.load("white_rook.png")
        if (color == "black"):
            self.img = pygame.image.load("black_rook.png")

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        flag = [True, True, True, True]

        for i in range(1,8):
            for idx, (x, y) in enumerate(self.directions):
                if (validCoord(self.x + x * i, self.y + y * i)):
                    cell = board.getCell(getCoord(self.x + (x * i), self.y + (y * i)))
                    if ((cell == None or (cell != None and cell.color != self.color)) and flag[idx]):
                        self.allowed_moves.append(getCoord(self.x + x * i, self.y + y * i))
                        if (cell != None and cell.color != self.color):
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
        if (color == "white"):
            self.img = pygame.image.load("white_queen.png")
        if (color == "black"):
            self.img = pygame.image.load("black_queen.png")

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        flag = [True, True, True, True, True, True, True, True]

        for i in range(1,8):
            for idx, (x, y) in enumerate(self.directions):
                if (validCoord(self.x + x * i, self.y + y * i)):
                    cell = board.getCell(getCoord(self.x + (x * i), self.y + (y * i)))
                    if ((cell == None or (cell != None and cell.color != self.color)) and flag[idx]):
                        self.allowed_moves.append(getCoord(self.x + x * i, self.y + y * i))
                        if (cell != None and cell.color != self.color):
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
        if (color == "white"):
            self.img = pygame.image.load("white_king.png")
        if (color == "black"):
            self.img = pygame.image.load("black_king.png")

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        for i, j in self.directions:
            if (validCoord(self.x + i, self.y + j)):
                cell = board.getCell(getCoord(self.x + i, self.y + j))
                if (cell == None or (cell != None and cell.color != self.color)):
                    self.allowed_moves.append(getCoord(self.x + i, self.y + j))

class Knight(Piece):
    name = "Knight"
    symbole = "N"
    directions = [(2, 1), (2, -1), (-2, 1), (-2, -1),
                 (1, 2), (1, -2), (-1, 2), (-1, -2)]

    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if (color == "white"):
            self.img = pygame.image.load("white_knight.png")
        if (color == "black"):
            self.img = pygame.image.load("black_knight.png")

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        for i, j in self.directions:
            if (validCoord(self.x + i, self.y + j)):
                cell = board.getCell(getCoord(self.x + i, self.y + j))
                if (cell == None or (cell != None and cell.color != self.color)):
                    self.allowed_moves.append(getCoord(self.x + i, self.y + j))

class Pawn(Piece):
    name = "Pawn"
    symbole = "P"
    directions = [(0, 1), (0, 2), (1, 1), (-1, 1)]

    def __init__(self, color, x, y):
        self.first_turn = True
        Piece.__init__(self, color, x, y)
        if (color == "white"):
            self.directions = [(0, 1), (0, 2), (1, 1), (-1, 1)]
            self.img = pygame.image.load("white_pawn.png")
        if (color == "black"):
            self.directions = [(0, -1), (0, -2), (1, -1), (-1, -1)]
            self.img = pygame.image.load("black_pawn.png")

    def setAllowedMoves(self, board):
        left_cell = None
        right_cell = None
        self.allowed_moves = list()

        if (validCoord(self.x + 1, self.y + 1)):
            right_cell = board.getCell(getCoord(self.x + 1, self.y + 1))
        if (validCoord(self.x - 1, self.y + 1)):
            left_cell = board.getCell(getCoord(self.x - 1, self.y + 1))

        if (validCoord(self.x, self.y + 1)):
            cell = board.getCell(getCoord(self.x, self.y + 1))
            if (cell == None):
                self.allowed_moves.append(getCoord(self.x, self.y + 1))

        if (self.first_turn):
            if (validCoord(self.x, self.y + 2)):
                cell = board.getCell(getCoord(self.x, self.y + 2))
                if (cell == None):
                    self.allowed_moves.append(getCoord(self.x, self.y + 2))

        if (right_cell != None and right_cell.color != self.color):
            self.allowed_moves.append(getCoord(self.x + 1, self.y + 1))
        if (left_cell != None and left_cell.color != self.color):
            self.allowed_moves.append(getCoord(self.x - 1, self.y + 1))

class Bishop(Piece):
    name = "Bishop"
    symbole = "B"
    directions = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    def __init__(self, color, x, y):
        Piece.__init__(self, color, x, y)
        if (color == "white"):
            self.img = pygame.image.load("white_bishop.png")
        if (color == "black"):
            self.img = pygame.image.load("black_bishop.png")

    def setAllowedMoves(self, board):
        self.allowed_moves = list()
        flag = [True, True, True, True]

        for i in range(1,8):
            for idx, (x, y) in enumerate(self.directions):
                if (validCoord(self.x + x * i, self.y + y * i)):
                    cell = board.getCell(getCoord(self.x + (x * i), self.y + (y * i)))
                    if ((cell == None or (cell != None and cell.color != self.color)) and flag[idx]):
                        self.allowed_moves.append(getCoord(self.x + x * i, self.y + y * i))
                        if (cell != None and cell.color != self.color):
                            flag[idx] = False
                    else:
                        flag[idx] = False
