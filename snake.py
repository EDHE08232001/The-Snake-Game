from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_body = []
        self._generate_begining_parts()
        self.head = self.snake_body[0]

    def reset(self):
        self.snake_body.clear()
        self._generate_begining_parts()

    def extend(self):
        """add a new segment to the snake"""
        self._add_segment(self.snake_body[-1].position())

    def _generate_begining_parts(self):
        """Generate 3 starting snake body parts and make them to the right positions"""
        for position in STARTING_POSITIONS:
            self._add_segment(position)

    def _add_segment(self, position):
        """Add snake segment"""
        new_part = Turtle('square')
        new_part.color('white')
        new_part.penup()
        self.snake_body.append(new_part)
        new_part.goto(position)

    def move(self):
        """Move the snake"""
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(new_x, new_y)
        self.snake_body[0].forward(20)

    def turn_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def turn_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
