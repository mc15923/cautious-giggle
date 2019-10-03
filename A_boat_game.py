import pygame as py
import time
import random

py.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
sky = (184, 228, 234)

gameDisplay = py.display.set_mode ((display_width, display_height))

py.display.set_caption('A Bit Boaty')

clock = py.time.Clock()

carImg = py.image.load ('Boat_art.png')
waveImg = py.image.load ('waves.png')
seagullImg = py.image.load ('seagull.png')
rockImg = py.image.load ('rock.png')
fishImg = py.image.load('fish.png')
goldenfishImg = py.image.load('golden_fish.png')



def fish_caught(count):
    font = py.font.SysFont(None, 25)
    text = font.render ('Fish caught: ' + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

def fish (fishx, fishy):
    gameDisplay.blit (fishImg, (fishx, fishy))


def gfish (gfishx, gfishy):
    gameDisplay.blit (goldenfishImg, (gfishx, gfishy))


def seagull (seagullx, seagully):
    gameDisplay.blit (seagullImg, (seagullx, seagully))

def rock (rockx, rocky):
    gameDisplay.blit (rockImg, (rockx, rocky))

def boat(x, y):
    gameDisplay.blit(carImg, (x,y))

def wave():
    gameDisplay.blit(waveImg, (0*display_width, 0.95*display_height))

def text_objects(text, font):
    textSurface = font.render (text, True, black)
    return textSurface, textSurface.get_rect()

def message_display_lose (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf, TextRect)

    py.display.update()

    time.sleep(2)

def message_display_welcome (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2 - 70))
    gameDisplay.blit (TextSurf, TextRect)

    

def message_display_welcome_two (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2 - 35))
    gameDisplay.blit (TextSurf, TextRect)

def message_display_welcome_three (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf, TextRect)


def message_display_pause (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf, TextRect)

    py.display.update()

def message_display_pause_two (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2 + 35))
    gameDisplay.blit (TextSurf, TextRect)

    py.display.update()

def message_display_pause_three (text):
    largeText = py.font.Font ('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2 + 70))
    gameDisplay.blit (TextSurf, TextRect)

    py.display.update()
    

def score_message (text):
        
    largeText = py.font.Font ('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf, TextRect)

    py.display.update()

def gscore_message (text):
        
    largeText = py.font.Font ('freesansbold.ttf', 60)
    TextSurf, TextRect = text_objects (text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit (TextSurf, TextRect)

    py.display.update()

def welcome_message():
    message_display_welcome ('WELCOME!')
    message_display_welcome_two ('USE ARROW KEYS TO MOVE')
    message_display_welcome_three ("CATCH THE FISH DODGE THE REST")
    
        

def pause ():
    paused = True

    while paused:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

            if event.type == py.KEYDOWN:
                if event.key ==py.K_c:
                    paused = False

                elif event.key == py.K_q:
                    py.quit()
                    quit()

        
        gameDisplay.fill (white)
        message_display_pause ('PAUSED')
        message_display_pause_two ('PRESS C TO CONTINUE OR Q TO QUIT')
        py.display.update()
        clock.tick (5)
        

def start():
    start_game = True
    while start_game:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
                    
                    
            if event.type == py.KEYDOWN:
                if event.key == py.K_c:
                    start_game == False
                    game_loop()
                        
            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    py.quit()
                    quit()
            
        gameDisplay.fill (white)
        welcome_message ()
        message_display_pause_two ("(don't touch the wall)")
        message_display_pause_three ('PRESS C TO CONTINUE OR Q TO QUIT')
        
        py.display.update()
        clock.tick (5)



def crash():
    message_display_lose('You Crashed, You Dickhead!')
    crashed = True

    while crashed:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()

            if event.type == py.KEYDOWN:
                if event.key == py.K_c:
                    crashed == False
                    game_loop()

            if event.type == py.KEYDOWN:
                if event.key == py.K_q:
                    py.quit()
                    quit()

        gameDisplay.fill (white)
        message_display_pause ('LOSER!')
        message_display_pause_two ('PRESS C TO RESTART OR Q TO QUIT')
        py.display.update()
        clock.tick (5)



def game_loop():


    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0

    boat_width = 210

    seagull_width = 61
    seagullx = random.randrange(0, display_width - seagull_width)
    seagully = -600
    seagull_speed = 5
    seagull_width = 61
    seagull_height = 47
    
    
    rock_width = 62
    rockx = random.randrange(0, display_width - rock_width)
    rocky = -600
    rock_speed = 5
    rock_width = 62
    rock_height = 56
    

    fish_width = 62
    fishx = random.randrange(0, display_width- fish_width)
    fishy = -800
    fish_speed = 5
    fish_width = 62
    fish_height = 56

    gfish_width = 62
    gfishx = random.randrange(0, display_width- fish_width)
    gfishy = random.randrange(-4000, -3000)
    gfish_speed = 5
    gfish_width = 62
    gfish_height = 56

    score_block = 10
    gscore_block = 10
    
    caught = 0


    gameExit = False

    while not gameExit:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT:
                    x_change = -6
                elif event.key == py.K_RIGHT:
                    x_change = 6
                elif event.key ==py.K_p:
                    pause()
                    
            if event.type == py.KEYUP:
                if event.key == py.K_LEFT and x_change !=6:
                    x_change = 0
                elif event.key == py.K_RIGHT and x_change !=-6:
                    x_change = 0
    

        
            

        x += x_change
        
        

        for event in py.event.get():
            if event.type == py.KEYUP:
                if event.key == py.K_p:
                    pause()

        
       
        gameDisplay.fill(sky)
        
        seagull(seagullx, seagully)
        seagully += seagull_speed
        gfish (gfishx, gfishy)
        gfishy += gfish_speed
        fish (fishx, fishy)
        fishy += fish_speed
        if caught == 5 or caught > 5:
            rock (rockx, rocky)
            rocky += rock_speed
            
        boat (x, y)
        wave ()
        fish_caught (caught)
        
        
                   
               
        

        

        if x > display_width - boat_width or x < 0:
            crash ()
        if seagully > display_height:
            seagully = 0 - seagull_height
            seagullx = random.randrange (0, display_width - seagull_width)

        if fishy > display_height:
            fishy = 0 - fish_height
            fishx = random.randrange (0, display_width- fish_width)

        if gfishy > display_height:
            gfishy = -3000
            gfishx = random.randrange (0, display_width- fish_width)

        if fishy > 200:
            score_block = 10

        if gfishy > -2800:
            gscore_block = 10

        if y + 91 < fishy + fish_height and y + 86 > fishy :
            if (x > fishx and x < fishx + fish_width) or (x+ boat_width > fishx and x + boat_width < fishx + fish_width) or (x + boat_width/2 > fishx and x + boat_width/2 < fishx + fish_width) or (x + boat_width/4 > fishx and x + boat_width/4 < fishx + fish_width) or (x + boat_width*0.75 > fishx and x + boat_width*0.75 < fishx + fish_width):
               fishx = random.randrange(0, display_width - fish_width)
               fishy = 0-fish_height
               if gscore_block == 10:
                   score_block = 12

               caught += 1
               if caught == 7 or caught >7:
                   rock_speed += 0.1
                   seagull_speed += 0.1

        if y + 91 < gfishy + gfish_height and y + 86 > gfishy :
            if (x > gfishx and x < gfishx + fish_width) or (x+ boat_width > gfishx and x + boat_width < gfishx + fish_width) or (x + boat_width/2 > gfishx and x + boat_width/2 < gfishx + fish_width) or (x + boat_width/4 > gfishx and x + boat_width/4 < gfishx + fish_width) or (x + boat_width*0.75 > gfishx and x + boat_width*0.75 < gfishx + fish_width):
               gfishx = random.randrange(0, display_width- fish_width)
               gfishy = -3000
               score_block = 10
               gscore_block = 12

               caught += 5
                   
        

        if y + 91 < seagully + seagull_height and y + 86 > seagully :

            if (x > seagullx and x < seagullx + seagull_width) or (x+ boat_width > seagullx and x + boat_width < seagullx + seagull_width) or (x + boat_width/2 > seagullx and x + boat_width/2 < seagullx + seagull_width) or (x + boat_width/4 > seagullx and x + boat_width/4 < seagullx + seagull_width) or (x + boat_width*0.75 > seagullx and x + boat_width*0.75 < seagullx + seagull_width):
                score_block = 10
                gscore_block = 10
                crash()
                


        if rocky > display_height:
                rocky = 0 - rock_height
                rockx = random.randrange (0, display_width- rock_width)

        if y + 91 < rocky + rock_height and y + 86 > rocky :

            if (x > rockx and x < rockx + rock_width) or (x+ boat_width > rockx and x + boat_width < rockx + rock_width) or (x + boat_width/2 > rockx and x + boat_width/2 < rockx + rock_width) or (x + boat_width/4 > rockx and x + boat_width/4 < rockx + rock_width) or (x + boat_width*0.75 > rockx and x + boat_width*0.75 < rockx + rock_width):
                score_block = 10
                gscore_block = 10
                crash()

        if score_block == 10:
            fish_score = False
        elif score_block != 10:
            fish_score = True

        if fish_score:
            score_message('FISH!')

        if gscore_block == 10:
            gfish_score = False
        
        if gscore_block != 10 and score_block == 10:
            gfish_score = True

        if gfish_score:
            gscore_message ('GOLDEN FISH!')
        
                    
        
        
        py.display.update()
        clock.tick(60)

start()
game_loop()
py.quit()
quit()
