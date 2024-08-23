import pygame
from sys import exit

pygame.init()
pygame.display.init()
pygame.font.init()

font_select1 = pygame.font.get_fonts()[89]
font = pygame.font.SysFont(font_select1,32,True)


screen = pygame.display.set_mode([500,500])
color = "red"


run = True
clock = pygame.time.Clock()

LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT
UP = pygame.K_UP
DOWN = pygame.K_DOWN

left = 20
top = 20
width = 50
height = 50

line_width = 10

box_color = "blue"
left_color = "black"
top_color = "yellow"
right_color = "purple"
bottom_color = "white"

velocity_message_snail = "Gary is that you?"
velocity_message_slow = "Take your time!"
velocity_message_medium = "Now we're moving..."
velocity_message_superfast = "Woah, woah slow down!"

v_messages = [velocity_message_snail,
              velocity_message_slow,
              velocity_message_medium,
              velocity_message_superfast]

velocity = 5

points = 0
countdown = 0
wait = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    collide_left = left < 0 
    collide_right = left > 450      
    collide_top = top < 0   
    collide_bottom = top > 450

    if collide_left:
        box_color = left_color
        velocity = 3
        points += .05
    
    if collide_right:
        box_color = right_color
        velocity = 5
        points += .1
       
    if collide_top:
        box_color = top_color
        velocity = 1
        points += .005
        
    if collide_bottom:
        box_color = bottom_color
        velocity = 10
        points += .5

    if velocity < 2:
        current_message = v_messages[0]
    if velocity == 3:
        current_message = v_messages[1]
    if velocity == 5:
        current_message = v_messages[2]
    if velocity == 10:
        current_message = v_messages[3]


    keys = pygame.key.get_pressed()
    if keys[LEFT] and not collide_left:
        left -= velocity
    if keys[RIGHT] and not collide_right:
        left += velocity
    if keys[UP] and not collide_top:
        top -= velocity
    if keys[DOWN] and not collide_bottom:
        top += velocity

    screen.fill(color)
    vel_show = font.render(f"velocity = {velocity}", True, "white")
    vel_message = font.render(f"{current_message}",True, "white")
    color_show = font.render(f"color = {box_color}", True, box_color,"lightgray")
    collide_show = font.render(f"points = {int(points)}", True, "white")
    screen.blit(vel_show,[60,60])
    screen.blit(color_show,[60,100])
    screen.blit(collide_show,[60,140])
    screen.blit(vel_message,[60,180])

    pygame.draw.line(screen,left_color,[0,500],[0,0],line_width)
    pygame.draw.line(screen,right_color,[495,0],[495,500],line_width)
    pygame.draw.line(screen,top_color,[0,0],[500,0],line_width)
    pygame.draw.line(screen,bottom_color,[0,500],[500,500],line_width)
    pygame.draw.rect(screen, box_color, [left, top, width, height])
    pygame.display.update()
    clock.tick(60)