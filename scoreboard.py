from turtle import Turtle
import json

ALIGNMENT = "center"

FONT = ("Arial", 24, "normal")

file_name = "high_score.json"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            self._load_score()
        except FileNotFoundError:
            self._dump_score(0)
        else:
            pass
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self._update_scoreboard()

    def increase_score(self):
        self.score += 1
        self._update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

    def reset(self):
        current_high = self._current_high()
        if self.score > current_high:
            self._dump_score(self.score)
        self.score = 0
        self._update_scoreboard()

    def _update_scoreboard(self):
        self.clear()
        score = self._load_score()
        self.write(f"Score: {self.score}; Highest Score: {score}",
                   align=ALIGNMENT,
                   font=FONT)

    def _current_high(self):
        with open(file_name) as file_object:
            current_high = json.load(file_object)
        return current_high

    def _dump_score(self, dumped_object):
        with open(file_name, 'w') as file_object:
            json.dump(dumped_object, file_object)

    def _load_score(self):
        with open(file_name) as file_object:
            score = json.load(file_object)
        return score
