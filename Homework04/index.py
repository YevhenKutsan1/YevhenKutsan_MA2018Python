﻿# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

def spawn_ball(direction):
    
    global ball_pos, ball_vel
    
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == LEFT:
        ball_vel = [-random.randrange(2, 4), random.randrange(1, 3)]
    else:
        ball_vel = [random.randrange(2, 4), -random.randrange(1, 3)]
    
def new_game():
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    
    score1 = 0
    score2 = 0
    
    paddle1_vel = 0
    paddle2_vel = 0
    
    paddle1_pos = HEIGHT / 2 - HALF_PAD_HEIGHT + paddle1_vel
    paddle2_pos = HEIGHT / 2 - HALF_PAD_HEIGHT + paddle2_vel
    
    spawn_ball(LEFT)

def draw(canvas):
    
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
         
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    paddle1_pos = paddle1_pos + paddle1_vel
    if paddle1_pos < 0:
        paddle1_pos = 0
    if paddle1_pos > (HEIGHT - PAD_HEIGHT):
        paddle1_pos = HEIGHT - PAD_HEIGHT
        
    paddle2_pos = paddle2_pos + paddle2_vel
    if paddle2_pos < 0:
        paddle2_pos = 0
    if paddle2_pos > (HEIGHT - PAD_HEIGHT):
        paddle2_pos = HEIGHT - PAD_HEIGHT 
    
    # left paddle
    p1 = [0, paddle1_pos]
    p2 = [PAD_WIDTH, paddle1_pos]
    p3 = [PAD_WIDTH, paddle1_pos + PAD_HEIGHT]
    p4 = [0, paddle1_pos + PAD_HEIGHT]
    canvas.draw_polygon([p1, p2, p3, p4], 2, "Green")
    
    # right paddle
    p1 = [WIDTH, paddle2_pos]
    p2 = [WIDTH - PAD_WIDTH, paddle2_pos]
    p3 = [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]
    p4 = [WIDTH, paddle2_pos + PAD_HEIGHT]
    canvas.draw_polygon([p1, p2, p3, p4], 2, "Green")    
    
    # determine whether paddle and ball collide    
     
    update_speed = False
    update_y = True
    
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if (ball_pos[1] >= paddle1_pos) and (ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
            update_speed = True
            if ball_vel[0] > 0: 
                ball_vel[0] = -(ball_vel[0] + ball_vel[0]*0.1)
            else:
                ball_vel[0] = -(ball_vel[0] - ball_vel[0]*0.1)
        else:
            score2 += 1
            update_y = False
            spawn_ball(RIGHT)
            
    if ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if (ball_pos[1] >= paddle2_pos) and (ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
            update_speed = True
            if ball_vel[0] > 0: 
                ball_vel[0] = -(ball_vel[0] + ball_vel[0]*0.1)
            else:
                ball_vel[0] = -(ball_vel[0] - ball_vel[0]*0.1)
        else:
            score1 += 1
            update_y = False
            spawn_ball(LEFT)
            
    if ((ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= HEIGHT - BALL_RADIUS)) and update_y:
        if update_speed:
            if ball_vel[1] > 0: 
                ball_vel[1] = -(ball_vel[1] + ball_vel[1]*0.1)
            else:
                ball_vel[1] = -(ball_vel[1] - ball_vel[1]*0.1)
        else:
            ball_vel[1] = -ball_vel[1]    
    
    # draw scores
    canvas.draw_text(str(score1), [20, 25], 30, "Red")
    canvas.draw_text(str(score2), [560, 25], 30, "Red")    
        
def keydown(key):
    
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 2
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 2            
   
def keyup(key):
    
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0    
        
def restart():
    
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button('Restart', restart)

# start frame
new_game()
frame.start()
