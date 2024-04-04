from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
left = 180
down = 270
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())
            
    def reset_game(self):
        for seg in self.segments:
            seg.goto(600, 600)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        


    def move(self):
        for seg_num in range( len(self.segments)-1, 0, -1):
            new_x = self.segments [seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        '''hasta aqui el bloque 2 se mueve al 1 y el 1 al cero, pero el cero queda en 
        cero, por eso hay que mover el cero en la sigiente linea'''
        self.head.forward(move_distance)
    
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
        else: 
            pass
    
    def down(self):
        if self.head.heading()!= up :            
            self.head.setheading(down)
        else :
            pass
    
    def left(self):
        if self.head.heading()!= right:
            self.head.setheading(left)
        else:
            pass

    def right(self):
        if self.head.heading() != left:            
            self.head.setheading(right) 
        else: 
            pass
