import turtle
import random
import time
from pygame import mixer # Load the required library


import turtle
import random
import time
import pygame # Load the required library


pygame.init()
pygame.mixer.music.load("Super Mario Bros Official Theme Song (1).mp3")
pygame.mixer.music.play()

screen=turtle.Screen()
#screen.bgpic("bgpic.gif")
def up():
    x,y = turtle.pos()
    turtle.goto(x,y+10)

turtle.onkeypress(up, "Up")
turtle.listen()


turtle.tracer(1,0)
turtle.ht()
screen=turtle.Screen()
# This helps the turtle move more smoothly
trash_distance =20
mario_distance = 10
SIZE_X = 800
SIZE_Y = 500
LEFT_EDGE = -SIZE_X/2

RIGHT_EDGE = SIZE_X/2
turtle.setup(SIZE_X, SIZE_Y)  # Curious? It's the turtle window
# size.
TIME_STEP= 25
turtle.bgcolor("white")
trash=turtle.Turtle()
'''
turtle.register_shape("trash1.gif") 
trash.shape("trash1.gif")
'''
questions=[]
trash_list=[]
mario = turtle.Turtle()
mario.penup()
mario.left(90)

turtle.register_shape("mario2.gif") 
mario.shape("mario2.gif")
jumping = False
jump_time = 1
falling = False
falling_time = 1
count = 0

graund=turtle.Turtle()
graund.penup()
graund.goto(400,-20)
graund.pendown()
graund.goto(-400,-20)
graund.hideturtle()
trash.hideturtle()
trash.penup()
trash.goto(400,0)
trash.showturtle()
counter=turtle.Turtle()
counter.goto(0,-200)
#for i in range(1000000):
    

def is_in_range(point, lower, upper):
    return point >= lower and point <= upper

def move():
    #print("moving")
    global jumping,falling, jump_time, falling_time, trash_distance, count
    counter.clear()
    count+=1
    counter.ht()
    counter.write(count, font = ("Arial",20,"normal"))
    mx, my = mario.pos()
    tx, ty = trash.pos()

    #print("trash pos",tx,ty)
    if is_in_range(mx, tx-15, tx+15) and is_in_range(my, ty-15, ty+15):
        question_maker()
        quiz()
        jumping = False
        falling = False
        mario.goto(0,0)
        return
        
    if tx <= LEFT_EDGE:        
        trash.hideturtle()
        rand_num = random.randint(1,10)
        #print(rand_num)
        if  rand_num == 1:
            trash_distance=random.randint(20,45)
            trash.goto(RIGHT_EDGE,ty)
            trash.showturtle()
    else:
        trash.goto(tx-trash_distance, ty)
        
    if jumping:
        mario.forward(mario_distance)
        jump_time -= 1
        if jump_time == 0:
            falling = True
            falling_time = 6
            jumping = False
            
    elif falling:
        mario.back(mario_distance)
        falling_time -= 1
        if falling_time == 0:
                falling = False
    def jump():
        global jumping, jump_time
        if not jumping and not falling:
            jump_time = 6
            jumping = True
        


    turtle.onkeypress(jump, 'Up')
    turtle.listen() 

    turtle.ontimer(move,TIME_STEP)
'''

def question_maker():
    global question,choices,answers,explination
    question=["Q:How many square kilometers of trash is in the Pacific Ocean?"]
    question.append("Q: What is the most air polluted city in the world?")
    question.append("Q: What natural Australian landmark will no longer exist due to climate change?")
    question.append("Q: This country produces the most trash in the Middle East.")
    question.append("Q: What is the only country in the world that has not signed the Paris climate agreement?")


    choices=["a.200,000km sq\nb.700,000km sq\nc.50,000km sq\nd.1.6 million km sq"]
    choices.append("a.Beijing China\nb.Kanpur India\nc.Sao Paulo Brazil\nd.Dehli India")
    choices.append("a.Great Barrier Reef\nb.The Outback\nc.Uluru\nd.Whitsundays Tropical Islands") 
    choices.append("a.Iran\nb.Iraq\nc.Saudi Arabia\nd.Lebanon")
    choices.append("a.United States\nb.Nicaragua\nc.Syria\nd.China")

    answers= ["Dd","Bb","Aa","Cc","Aa"]

    explination=["D.The size of the Great Pacific Garbage Patch is 1.6 million km sq, \nan area twice the size of Texas or three times the size of France."]
    explination.append("B. Kanpur, India is the most air polluted city in the world as of 2018. \nResidents there breath air 173 times worse than the requirements of the \nAir Quality Guideline (AQG) according to the World Health Organization.")
    explination.append("A. The Great Barrier Reef will have faced severe and irreversible coral loss\n by 2050 due to warming ocean temperatures as a result of human co2 emissions. \nSorry Mate.")
    explination.append("C.Saudi Arabia produces the most trash annually in the Middle East.\n The Arabian monarchy produces 15 million tons of garbage each year. \nThat's 1.3 kilograms of waste per person every day!!!")
    explination.append("A- Syria signed the Paris agreement in November of 2017 \nleaving the United States the only\n U.N member state to not sign the agreement. The agreement was drafted in 2015 as a joint cooperation between nations to limit co2 emissions to prevent climate change.MERICA!")


def quiz():
    turtle.pu()
    turtle.goto(40,50)
    counter=random.randint(0,4)
    name= turtle.textinput("Question",question[counter]+"\n"+choices[counter])
    #print("input:",type(name))
    if name == "" or name == None:
        name = "zz"
    isCorrect = name in answers[counter]
    if isCorrect:
        turtle.clear()
        turtle.goto(-200,200)
        turtle.write("correct" + explination[counter])
        trash.goto(-400, 0)
        move()
    else:
        turtle.clear()
        turtle.goto(-200,200)
        turtle.write("incorrect"+explination[counter])
        print("You hit the trash! Game over!")
        screen.bgpic('game over.gif')
        mario.ht()
        trash.ht()
        turtle.ht()
        graund.ht()
        screen.update()
        time.sleep(5)
        quit()


def jump():
    global jumping, jump_time
    if not jumping and not falling:
        jump_time = 10
        jumping = True

        
turtle.onkeypress(jump, 'Up')
turtle.listen() 
    
move()
screen=turtle.Screen()
#screen.bgpic("bgpic.gif")
def up():
    x,y = turtle.pos()
    turtle.goto(x,y+10)

turtle.onkeypress(up, "Up")
turtle.listen()


turtle.tracer(1,0)
turtle.ht()
screen=turtle.Screen()
# This helps the turtle move more smoothly
trash_distance =20
mario_distance = 10
SIZE_X = 800
SIZE_Y = 500
LEFT_EDGE = -SIZE_X/2

RIGHT_EDGE = SIZE_X/2
turtle.setup(SIZE_X, SIZE_Y)  # Curious? It's the turtle window
# size.
TIME_STEP= 25
turtle.bgcolor("white")
'''
trash=turtle.Turtle()
turtle.register_shape("trash1.gif") 
trash.shape("trash1.gif")
'''
questions=[]
trash_list=[]
mario = turtle.Turtle()
mario.penup()
mario.left(90)
turtle.register_shape("mario2.gif") 
mario.shape("mario2.gif")
jumping = False
jump_time = 1
falling = False
falling_time = 1
count = 0

graund=turtle.Turtle()
graund.penup()
graund.goto(400,-20)
graund.pendown()
graund.goto(-400,-20)
graund.hideturtle()
trash.hideturtle()
trash.penup()
trash.goto(400,0)
trash.showturtle()
counter=turtle.Turtle()
counter.goto(0,-200)
#for i in range(1000000):
    

def is_in_range(point, lower, upper):
    return point >= lower and point <= upper

def move():
    #print("moving")
    global jumping,falling, jump_time, falling_time, trash_distance, count
    counter.clear()
    count+=1
    counter.ht()
    counter.write(count, font = ("Arial",20,"normal"))
    mx, my = mario.pos()
    tx, ty = trash.pos()

    #print("trash pos",tx,ty)
    if is_in_range(mx, tx-15, tx+15) and is_in_range(my, ty-15, ty+15):
        question_maker()
        quiz()
        jumping = False
        falling = False
        mario.goto(0,0)
        return
        
    if tx <= LEFT_EDGE:        
        trash.hideturtle()
        rand_num = random.randint(1,10)
        #print(rand_num)
        if  rand_num == 1:
            trash_distance=random.randint(20,45)
            trash.goto(RIGHT_EDGE,ty)
            trash.showturtle()
    else:
        trash.goto(tx-trash_distance, ty)
        
    if jumping:
        mario.forward(mario_distance)
        jump_time -= 1
        if jump_time == 0:
            falling = True
            falling_time = 6
            jumping = False
            
    elif falling:
        mario.back(mario_distance)
        falling_time -= 1
        if falling_time == 0:
                falling = False
    def jump():
        global jumping, jump_time
        if not jumping and not falling:
            jump_time = 6
            jumping = True
        


    turtle.onkeypress(jump, 'Up')
    turtle.listen() 

    turtle.ontimer(move,TIME_STEP)

'''
def question_maker():
    global question,choices,answers,explination
    question=["Q:How many square kilometers of trash is in the Pacific Ocean?"]
    question.append("Q: What is the most air polluted city in the world?")
    question.append("Q: What natural Australian landmark will no longer exist due to climate change?")
    question.append("Q: This country produces the most trash in the Middle East.")
    question.append("Q: What is the only country in the world that has not signed the Paris climate agreement?")


    choices=["a.200,000km sq\nb.700,000km sq\nc.50,000km sq\nd.1.6 million km sq"]
    choices.append("a.Beijing China\nb.Kanpur India\nc.Sao Paulo Brazil\nd.Dehli India")
    choices.append("a.Great Barrier Reef\nb.The Outback\nc.Uluru\nd.Whitsundays Tropical Islands") 
    choices.append("a.Iran\nb.Iraq\nc.Saudi Arabia\nd.Lebanon")
    choices.append("a.United States\nb.Nicaragua\nc.Syria\nd.China")

    answers= ["Dd","Bb","Aa","Cc","Aa"]

    explination=["D.The size of the Great Pacific Garbage Patch is 1.6 million km sq, \nan area twice the size of Texas or three times the size of France."]
    explination.append("B. Kanpur, India is the most air polluted city in the world as of 2018. \nResidents there breath air 173 times worse than the requirements of the \nAir Quality Guideline (AQG) according to the World Health Organization.")
    explination.append("A. The Great Barrier Reef will have faced severe and irreversible coral loss\n by 2050 due to warming ocean temperatures as a result of human co2 emissions. \nSorry Mate.")
    explination.append("C.Saudi Arabia produces the most trash annually in the Middle East.\n The Arabian monarchy produces 15 million tons of garbage each year. \nThat's 1.3 kilograms of waste per person every day!!!")
    explination.append("A- Syria signed the Paris agreement in November of 2017 \nleaving the United States the only\n U.N member state to not sign the agreement. The agreement was drafted in 2015 as a joint cooperation between nations to limit co2 emissions to prevent climate change.MERICA!")

'''
def quiz():
    turtle.pu()
    turtle.goto(40,50)
    counter=random.randint(0,4)
   # name= turtle.textinput("Question",question[counter]+"\n"+choices[counter])
    #print("input:",type(name))
   # if name == "" or name == None:
       # name = "zz"
   # isCorrect = name in answers[counter]
    '''
    if isCorrect:
        turtle.clear()
        turtle.goto(-200,200)
        turtle.write("correct" + explination[counter])
        trash.goto(-400, 0)
        move()
    else:
        turtle.clear()
        turtle.goto(-200,200)
        turtle.write("incorrect"+explination[counter])
        print("You hit the trash! Game over!")
        #screen.bgpic('game over.gif')
        '''
        #mario.ht()
        
        turtle.ht()
        graund.ht()
        screen.update()
        time.sleep(5)
        quit()


def jump():
    global jumping, jump_time
    if not jumping and not falling:
        jump_time = 10
        jumping = True

        
turtle.onkeypress(jump, 'Up')
turtle.listen() 
    
move()




turtle.mainloop()