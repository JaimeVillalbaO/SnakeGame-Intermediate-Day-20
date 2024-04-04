from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_Score.txt', ) as file:
            self.high_score = int(file.read())                 
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_sroreboard()
        self.hideturtle()

    def encrease_score(self):
        self.score += 1
        self.update_sroreboard()


    def update_sroreboard (self):
        self.clear()    
        self.write(arg= f'Score {self.score}  High score {self.high_score}', align = 'center', font= ('Arial', 18, 'normal'))

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open('high_Score.txt', mode='w' ) as file:
            file.write(f'{self.high_score}')
        self.update_sroreboard()

    # def finish(self):
    #     self.goto(0, 0)
    #     self.write(arg= f'Game Over. Your Score  is {self.score}', align = 'center', font= ('Arial', 14, 'normal'))
       