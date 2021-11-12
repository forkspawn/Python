import pygame
import random
import math
import sys

from pygame import mixer


#intialize the pygame
#pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

#create the screnn
screen=pygame.display.set_mode((800,600))

#background image
background=pygame.image.load('background.jpg')

#game entry image
entry_image=pygame.image.load('game_entry.jpg')

#background  music
mixer.music.load('entry.mp3')
mixer.music.play()
#title and icon
pygame.display.set_caption("Into The Space")
icon=pygame.image.load('aircraft.png')
pygame.display.set_icon(icon)
 
#player
playerImg=pygame.image.load('spaceship.png')
playerX = 370
playerY = 530

playerX_change=0
playerY_change=0

#enemy  
enemyImg = [] 
enemyX = []
enemyY = []
enemyX_change=[]
enemyY_change=[]
num_of_enemies=6
 
for i in range(num_of_enemies): 
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.30)
    enemyY_change.append(30)

#bullet
# ready - you cant see the bullet on the screen
# fire - the bullet is currently moving
bulletImg = pygame.image.load('laser.png')
bulletX = 0
bulletY = 510
bulletX_change= 0
bulletY_change= 10
bullet_state="Ready"

#score
score=0
font = pygame.font.Font('freesansbold.ttf',32)
gameover_font=pygame.font.Font('freesansbold.ttf',32)
entry_font=pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def show_score(x,y):
    score_value = font.render("Score : " + str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))

def player(X,Y):
    screen.blit(playerImg,(X,Y))

def enemy(X,Y,i):
    screen.blit(enemyImg[i],(X,Y))

def fire_bullet(X,Y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg,(X+16,Y+5))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

def game_over_text():
    gameover = gameover_font.render("GAME OVER",True,(255,255,255))
    screen.blit(gameover,(200,250))

def game_entry_text():
    entry = entry_font.render("Press Enter to Play",True,(255,255,255))
    entry2=font.render("Press Esc to Exit",True,(255,255,255))
    screen.blit(entry,(200,230))
    screen.blit(entry2,(200,260))

starting = True
running = False

def start():
    global starting
    global running
    while starting:
        screen.fill((128,128,128)) #rgb
        screen.blit(entry_image,(0,0)) #background
        game_entry_text()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                if event.key == pygame.K_RETURN:
                    starting = False
                    running = True
            pygame.display.update()

start()
while running:
    screen.fill((128,128,128)) #rgb
    screen.blit(background,(0,0)) #background
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #checking keystrokes
        if event.type == pygame.KEYDOWN:
           # print("Keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -4  #without background -0.35
            if event.key == pygame.K_RIGHT:
                playerX_change = 4  #0.35
            if event.key == pygame.K_SPACE and bullet_state =="Ready":
                bulletX = playerX #get the current coordinate of the player
                bullet_sound=mixer.Sound('bullet.wav')
                bullet_sound.play()
                fire_bullet(playerX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX+=playerX_change #this is for moving the image in the x axis
    
    #cheking for boundaries

    if playerX <=0:  #if the image moves to the right it comes back to the left
        playerX=736
    elif playerX >=736: #if the image moves to the left it comes back to the right
        playerX=0

    #enemy movement
    for i in range(num_of_enemies):
        #game over
        if enemyY[i] > 500:
           # for j in range(num_of_enemies):
           enemyY[i]=2000
           game_over_text()
           break

        enemyX[i]+=enemyX_change[i] #this is for moving the enemy image in the x asix
        if enemyX[i] <=0:  #if the image moves to the right it comes back to the left
            enemyX_change[i]=0.3
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >736: #if the image moves to the left it comes back to the right
            enemyX_change[i]=-0.3
            enemyY[i]+=enemyY_change[i]

        #collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 510
            bullet_state="Ready"
            score+=1
            print(score)
            enemyX[i]=random.randint(0,700)
            enemyY[i]=enemyY[i]+random.randint(0,20)

        enemy(enemyX[i],enemyY[i],i)

    #bullet movement
    if bulletY<=0:
        bulletY=510
        bullet_state= "Ready"
    if bullet_state == "Fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()


