import time
import turtle
from abc import ABC, abstractmethod
import pygame



pygame.init
screen = pygame.display.set_mode((480, 480))
pygame.display.set_caption('board')
game_end = False


def main(white_first:bool):
    board_make()
    print("board made")
    board_set()
    print("board set")
    piece_update()
    
    while not(game_end):
        time.sleep(2)
        test= move_reader(white_first)
        print("move Made")
        if test:
            white_first = not(white_first)

def legal_check(move_input,color):
    return (columns[move_input%10][int(move_input/10)]).in_square.color != color


        
class piece(ABC):         #defines basic movement for all pieces, NEED TO ADD COLLUSION DETECTION AND ATTACKING
        def __init__(self,space,color:bool, life:bool):
            self.space = space
            self.color = color
            self.life = life  
        @abstractmethod
        def pos_update(self,X,Y):
            pass
        @abstractmethod
        def get_spot(self):
            pass
        def move(self,move_to):
            pass
    
class knight(piece):
        # def __init__(self,space,color, life):
        #     self.space = space
        #     self.color = color
        #     self.life = life              
        def move(self,move_to):
            return(move_to - self.space)%11 ==0 or (move_to - self.space)%9 ==0
        def pos_update(self,X,Y):
            if self.color:
                screen.blit(pygame.image.load("Chess_nlt60.png"),(X,Y))
            else:
                screen.blit(pygame.image.load("Chess_ndt60.png"),(X,Y))
        def get_spot(self):
            return self.space
class bishop(piece):
        # def __init__(self,space,color, life):
        #     self.space = space
        #     self.color = color
        #     self.life = life              
        def move(self,move_to):
            return(((self.space%10-(int(self.space/10)))==((move_to%10-(int(move_to/10))))) or ((self.space%10+(int(self.space/10)))==((move_to%10+(int(move_to/10)))))) and legal_check(move_to,self.color)
            # return(move_to - self.space)%11 ==0 and (move_to - self.space)/11 <=7 or (move_to - self.space)%9 ==0 and (move_to - self.space)/9 <=7
        def pos_update(self,X,Y):
            if self.color:
                screen.blit(pygame.image.load("Chess_blt60.png"),(X,Y))
            else:
                screen.blit(pygame.image.load("Chess_bdt60.png"),(X,Y))
        def get_spot(self):
            return self.space
        
class rook(piece):
        # def __init__(self,space,color, life):
        #     self.space = space
        #     self.color = color
        #     self.life = life
        def move(self,move_to):
            return(move_to%10 == self.space%10) or int(move_to/10) == int(self.space/10)
        def pos_update(self,X,Y):
            if self.color:
                screen.blit(pygame.image.load("Chess_rlt60.png"),(X,Y))
            else:
                screen.blit(pygame.image.load("Chess_rdt60.png"),(X,Y))
        def get_spot(self):
            return self.space
class queen(piece):
        # def __init__(self,space,color, life):
        #     self.space = space
        #     self.color = color
        #     self.life = life
        def move(self,move_to):
            return((self.space%10-(int(self.space/10)))==((move_to%10-(int(move_to/10))))) or ((self.space%10+(int(self.space/10)))==((move_to%10+(int(move_to/10))))) or (move_to%10 == self.space%10) or int(move_to/10) == int(self.space/10)
        def pos_update(self,X,Y):
            if self.color:
                screen.blit(pygame.image.load("Chess_qlt60.png"),(X,Y))
            else:
                screen.blit(pygame.image.load("Chess_qdt60.png"),(X,Y))
        def get_spot(self):
            return self.space
class king(piece):
        # def __init__(self,space,color, life):
        #     self.space = space
        #     self.color = color
        #     self.life = life
        def move(self,move_to):
            return abs(move_to-self.space) == 11 or abs(move_to-self.space) == 10 or abs(move_to-self.space) == 9 or abs(move_to-self.space) == 1
        def pos_update(self,X,Y):
            if self.color:
                screen.blit(pygame.image.load("Chess_klt60.png"),(X,Y))
            else:
                screen.blit(pygame.image.load("Chess_kdt60.png"),(X,Y))
        def get_spot(self):
            return self.space
class pawn(piece):
        # def __init__(self,space,color, life):
        #     self.space = space
        #     self.color = color
        #     self.life = life
        def move(self,move_to):
            return move_to== self.space+10 or move_to== self.space+9 and columns[int((self.space+9)/10)][(self.space+9)%10].in_square.color== self.color or move_to== self.space+11 and columns[int((self.space+11)/10)][(self.space+11)%10].in_square.color== self.color
        def pos_update(self,X,Y):
            if self.color:
                screen.blit(pygame.image.load("Chess_plt60.png"),(X,Y))
            else:
                screen.blit(pygame.image.load("Chess_pdt60.png"),(X,Y))
        def get_spot(self):
            return self.space
class NA(piece):
    def move(self,move_to):
        return
    def pos_update(self,X,Y):
        return
    def get_spot(self):
            print("nah fam")
class space:
    def __init__(self, in_square:piece ,color):
        self.in_square = in_square
        self.color = color #False =  dark True = light 

empty = NA(00,False,False)
blank = space(empty,False)


column1 = [blank,blank,blank,blank,blank,blank,blank,blank]
column2 = [blank,blank,blank,blank,blank,blank,blank,blank]
column3 = [blank,blank,blank,blank,blank,blank,blank,blank]
column4 = [blank,blank,blank,blank,blank,blank,blank,blank]
column5 = [blank,blank,blank,blank,blank,blank,blank,blank]
column6 = [blank,blank,blank,blank,blank,blank,blank,blank]
column7 = [blank,blank,blank,blank,blank,blank,blank,blank]
column8 = [blank,blank,blank,blank,blank,blank,blank,blank]
columns = [column1,column2,column3,column4,column5,column6,column7,column8]



    
def board_make():
    print("making")
    color_count = 1
    for y in range (8):
        for x in range (8):
            if color_count%2 == 0:
                pygame.draw.rect(screen, "brown", (x*60, y*60 , 60, 60))
            else:
                pygame.draw.rect(screen, "white", (x*60, y*60 , 60, 60))
            color_count = color_count+1
        color_count = color_count+1
    print("done making")
    return 
   
    
    

def board_set():
    color_count = 0
    for i in range (8): #create empty board
        for k in range (8):
            dspace = space(empty,False)
            lspace = space(empty,True)
            if color_count%2 ==0:
                columns[i][k] = dspace
            else:
                columns[i][k] = lspace
            color_count = color_count+1
        color_count = color_count+1
            
    for i in range (8): #places pawns
        columns[i][1].in_square = pawn((10+i),True,True)
        columns[i][6].in_square = pawn((70+i),False,True)
    
    #placing bishops
    columns[2][0].in_square = bishop(2,True,True)
    columns[5][0].in_square = bishop(5,True,True)
    columns[2][7].in_square = bishop(72,False,True)
    columns[5][7].in_square = bishop(75,False,True)
    
    #placing rooks
    columns[0][0].in_square = rook(00,True,True)
    columns[0][7].in_square = rook(70,False,True)
    columns[7][0].in_square = rook(7,True,True)
    columns[7][7].in_square = rook(77,False,True)
    
    #placing knights
    columns[1][0].in_square = knight(1,True,True)
    columns[6][0].in_square = knight(6,True,True)
    columns[1][7].in_square = knight(71,False,True)
    columns[6][7].in_square = knight(76,False,True)

    #placing kings and queens
    columns[3][0].in_square = queen(3,True,True)
    columns[3][7].in_square = queen(73,False,True)
    columns[4][0].in_square = king(4,True,True)
    columns[4][7].in_square = king(74,False,True)

    return
    
    
def piece_update():       
    
    for i in range (8):
        for k in range (8):
            columns[i][k].in_square.pos_update(i*60,420-k*60)
    pygame.display.update()
    pygame.display.flip()
    return
    
    
def move_lister(spot:space):
    
    for x in range (8):
        for y in range (8):
            if spot.in_square.move((y*10)+x):
                screen.blit(pygame.image.load("good move marker.png"),(x*60,420-y*60))
                pygame.display.update()
                
    pygame.display.flip()


def board_update():
    print("UPDATE?")
    screen.fill((0,0,0))
    pygame.display.flip()
    pygame.display.update()    
    color_count = 1
    for y in range (8):
        for x in range (8):
            if color_count%2 == 0:
                pygame.draw.rect(screen, "brown", (x*60, y*60 , 60, 60))
            else:
                pygame.draw.rect(screen, "white", (x*60, y*60 , 60, 60))
            color_count = color_count+1
        color_count = color_count+1
    piece_update()
    print("done making")
    pygame.display.flip()
    return

def move_reader(white_check:bool):
    action = input("What do you want to do? ")
    if action == "move":
        print("yes")
        piece_input = input("What piece")
        move_input= input("where to? ")
        current_spot = (columns[int(piece_input[1:2])][int(piece_input[0:1])])
        future_spot = (columns[int(move_input[1:2])][int(move_input[0:1])])
        current_piece = current_spot.in_square
        test= input(current_piece.move(int(move_input)) == True and current_piece.color == white_check)
        
        if current_piece.move(int(move_input)) == True and current_piece.color == white_check:
            print("MOVING")
            future_spot.in_square = current_piece
            current_spot.in_square =  empty
            board_update()
            
            return True
        else: return False
    if action == "list":
        list_input= input("what piece? ")
        move_lister(columns[int(list_input[1:2])][int(list_input[0:1])])
        return False
    if action == "?":
        print("best move")
        return False
        

