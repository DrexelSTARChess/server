from chessPiece import ChessPiece


class Rook(ChessPiece):
    """docstring for Rook"""

    def __init__(self, color, x, y):
        super(Rook, self).__init__(color, x, y)

    def getPossibleMoves(self, board):
        return [][]