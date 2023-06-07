import pygame
import math
from queue import PriorityQueue
from tkinter import *
from tkinter import messagebox


WIDTH = 800
WINDOW= pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Waze shortest path finder")


# COULEURS

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255 , 255 , 255)
BLACK = (0 , 0 , 0)
PURPLE = (128 , 0 , 128)
ORANGE = (255 , 165 , 0)
GREY = (128 , 128 , 128)
TURQUOISE = (64 , 220 , 208)


class Node:
    """ Classe des cubes init : couleur,coord,voisins ..."""
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    # METHODE DE RECUPERATION
    
    def get_pos(self):
        """Retourne la position (i,j) """
        return self.row , self.col

    def is_closed(self):
        """ On verifie si le node est deja traité"""
        return self.color == RED
    
    def is_open(self):
        """ On verifie si le node est en cours de traitement"""
        return self.color == GREEN

    def is_obstacle(self):
        """ On verifie si le node est un obstacle"""
        return self.color == BLACK
    
    def is_start(self):
        """ On verifie si le node est le départ"""
        return self.color == ORANGE

    def is_end(self):
        """ On verifie si le node est l'arrivée"""
        return self.color == TURQUOISE

    def reset(self):
        """ On reset le node en mettant sa couleur à blanc"""
        self.color = WHITE


    # METHODES D'AFFECTATIONS 

    def make_closed(self):
        """ ON set le node en prochainement à traiter"""
        self.color = RED

    def make_open(self):
        """ On set le node à en cours de traitement"""
        self.color = GREEN

    def make_obstacle(self):
        """ On set le node en obstacle"""
        self.color = BLACK
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_start(self):
        self.color = ORANGE

    def make_path(self):
        self.color = PURPLE

    # METHODE D'AFFICHAGE

    def draw(self , win):
        pygame.draw.rect(win, self.color, (self.x, self.y , self.width, self.width))
    
    def update_neighbords(self, grid):
        """ on regarde en h d b g et on regarde si obstacle et on ajout dans neighbors"""
        self.neighbors = []

        # on regarde en bas
        if self.row < self.total_rows -1 and not grid[self.row + 1][self.col].is_obstacle():
            self.neighbors.append(grid[self.row + 1][self.col])

        # on regarde en haut
        if self.row > 0 and not grid[self.row - 1][self.col].is_obstacle():
            self.neighbors.append(grid[self.row -  1][self.col])
        
        # on regarde à droite
        if self.col < self.total_rows -1 and not grid[self.row][self.col + 1].is_obstacle():
            self.neighbors.append(grid[self.row][self.col + 1])
        
        # on regarde à gauche
        if self.col > 0 and not grid[self.row][self.col - 1].is_obstacle():
            self.neighbors.append(grid[self.row][self.col - 1])



    def __lt__(self, other):
        return False



def h(p1 , p2):
    """ Distance manhattan entre p1 et p2 (le plus petit L)"""
    x1 , y1 = p1
    x2 , y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from , current , draw):
    lenght = 0
    while current in came_from:
        current = came_from[current]
        current.make_path() # change la couleur à violet
        draw()
        lenght += 1
    print(lenght)



def algorithme(draw , grid , start, end , row , width):
    count = 0 
    open_set = PriorityQueue()
    open_set.put((0 , count, start))
    came_from = {} # A vient de B, B vient de C etc ...

    # enregistrement des score G(n) on associe un score à un node
    g_score = {node: float("inf") for row in grid for node in row } # on met tout à l'infini
    g_score[start] = 0 

    # enregistrement des score F(n) on associe un score à un node
    f_score = {node: float("inf") for row in grid for node in row } # on met tout à l'infini
    f_score[start] = h(start.get_pos(), end.get_pos())


    open_set_hash = {start} 

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


        current = open_set.get()[2] # PriorityQueue 
        open_set_hash.remove(current)

        if current == end: # c'est la fin
            reconstruct_path(came_from , end , draw)

            return True

        
        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1 # tout est à 1 de distance 

            if temp_g_score < g_score[neighbor]:
                # find a better way
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos() , end.get_pos())

                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor] , count , neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open() # on change sa couleur pour qu'il soit prochainement traité 

        draw()

        if current != start:
            current.make_closed()

    Tk().wm_withdraw()
    messagebox.showinfo("Probleme" , "Il n'y a pas de solution")


    



def make_grid(rows , width):
    """ Ajoute tous les objets nodes dans un tableau 2D"""
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid



# FONCTIONS D'AFFICHAGE

def draw_grid(win , rows, width):
    """ Trace les lignes horizontale et vertcale de la grid"""
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0 , i * gap), (width, i * gap))
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap , 0), (j * gap , width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)
    
    draw_grid(win, rows, width)
    pygame.display.update()



# GESTION DE LA SOURIS

def get_clicked_pos(pos , rows , width):
    """ Renvoie la position en terme de colonnes et de lignes de l'emplacement de la souris """
    gap = width // rows # taille d'un cube 
    y , x = pos # position en coord de la souris 

    row = y // gap 
    col = x // gap
    return row, col


def main(win , width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None 
    end = None
    
    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                # si l'algo est lancé on ne peut plus rien toucher
                continue

            if pygame.mouse.get_pressed()[0]: # souris gauche
                pos = pygame.mouse.get_pos() # On recup la position en coordonnées
                row, col = get_clicked_pos(pos, ROWS, width) # On recup la position en terme de ligne colonne (comme matrice )
                node = grid[row][col] # On recup le cube / node correspondant

                # Si on clique et qu'on a pas encore associé le start et que là ou on clique cest pas end alors on place direct le start 
                if not start and node != end :
                    start = node
                    start.make_start()

                # Si on clique et que le end n'est pas placé et que le là ou on clique cest pas start alors on place end 
                elif not end and node != start:
                    end = node
                    end.make_end()
                
                # Sinon on met des obstacle en noir
                elif node != end and node!= start:
                    node.make_obstacle()

            # On reset avec le clique droit 
            elif pygame.mouse.get_pressed()[2]: # Right
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                if node == end:
                    end = None
                
            # On lance l algo avec la barre espace 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:

                    # On cherche les voisins de chaque cube 
                    for row in grid:
                        for node in row:
                            node.update_neighbords(grid)


                    algorithme(lambda: draw(win, grid, ROWS, width), grid , start, end , ROWS , width)

                # On reset le plateau / on recreer le plateau 
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)


    pygame.quit()


main(WINDOW, WIDTH)
