class ChessBoard(object):
    def __init__(self, chess_pieces):
        self.board = list()
        ah = [chr(i) for i in range(ord("a"), ord("h") + 1)]
        for y in range(8, 0, -1):
            line = list()
            for x in ah:
                coord = x + str(y)
                cell = None
                for piece in chess_pieces:
                    if piece.getCoord() == coord:
                        cell = piece
                line.append(cell)
            self.board.insert(0, line)

    def getCell(self, coord):
        x = ord(coord[0]) + 1 - ord("a") - 1
        y = int(coord[1]) - 1
        return(self.board[y][x])

    def changeCellValue(self, coord, value):
        x = ord(coord[0]) + 1 - ord("a") - 1
        y = int(coord[1]) - 1
        self.board[y][x] = value

    def print(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] is not None:
                    print("cell : " + chr(ord("a") + j) + str(i + 1)
                          + " -> " + self.board[i][j].color + " "
                          + self.board[i][j].name)
                else:
                    print("cell : " + chr(ord("a") + j)
                          + str(i + 1) + " -> None")
