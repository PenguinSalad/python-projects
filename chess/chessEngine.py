"""
Aquesta classe serveix per guardar tota la informacio sobre el estat del joc, per poder determinar els moviments. Tambe podra servir per guardar un log dels moviments.
"""

class GameState():
    def __init__(self):

        #board representa el tauler de 8x8
        #La primera lletra representa el color de la pesa (white or black)
        #La segona lletra representa el tipo de pesa (Rook, Knight, Bishop, Queen, King, pawn)
        #"--" representa un espai en blanc.

        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
        ]