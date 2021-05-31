"""
Funcio principal.
"""

import pygame as p
import chessEngine

p.init()
WIDTH = HEIGHT = 512 #400 tambe va be (mes gran perd qualitat)
DIMENSION = 8 #La dimensio del tauler
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #Per futures animacions
IMAGES = {}

'''
Creem un diccionari amb les images de totes les peces
'''

def loadImages():
    pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    #Amb aixo, podem accedir a una imatge posant, 'IMAGES['wp']'

def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("White"))
    gs = chessEngine.GameState()
    loadImages()
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsable de la part grafica del joc
'''

def drawGameState(screen, gs):
    drawBoard(screen) #Dibuixa la quadricula
    drawPieces(screen, gs.board) #Dibuixa les peces sobra la quadricula


'''
Dibuixa la quadricula
'''

def drawBoard(screen):
    colors = [p.Color(235, 235, 208), p.Color(119, 148, 85)]

    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r+c) % 2]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


'''
Dibuixa les peces sobra la quadricula
'''

def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #No esta buit      
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
                

if __name__ == "__main__":
    main()