from airtest.core.api import *
from airtest.cli.parser import cli_setup
from base.base import BaseElement
from page.game_page import GamePage


class GameVictory(BaseElement):

    def tube_position(self, position):
        self.image_click(position)
        self.sleep_time(1.5)
        return self

    def level_two(self):
        first_tube = [240, 1118]
        second_tube = [574, 1211]
        third_tube = [950, 1186]
        ((((((self.tube_position(first_tube).tube_position(third_tube).
              tube_position(second_tube).tube_position(first_tube)).
             tube_position(second_tube).tube_position(third_tube)).
            tube_position(first_tube).tube_position(second_tube)).
           tube_position(first_tube).tube_position(third_tube)).
          tube_position(second_tube).tube_position(first_tube)).
         tube_position(second_tube).tube_position(third_tube))
        self.sleep_time()
        return GamePage

    def level_three(self):
        first_tube = [84, 1156]
        second_tube = [295, 1173]
        third_tube = [620, 1186]
        fourth_tube = [823, 1156]
        fifth_tube = [1114, 1165]
        (((((((((self.tube_position(first_tube).tube_position(fourth_tube).
                 tube_position(second_tube).tube_position(fourth_tube)).
                tube_position(first_tube).tube_position(fifth_tube)).
               tube_position(second_tube).tube_position(fifth_tube)).
              tube_position(third_tube).tube_position(fifth_tube)).
             tube_position(third_tube).tube_position(first_tube)).
            tube_position(second_tube).tube_position(first_tube)).
           tube_position(second_tube).tube_position(fourth_tube)).
          tube_position(third_tube).tube_position(fourth_tube)).
         tube_position(third_tube).tube_position(fifth_tube))
        self.sleep_time()
        return GamePage

    def level_four(self):
        first_tube = [84, 1156]
        second_tube = [295, 1173]
        third_tube = [620, 1186]
        fourth_tube = [823, 1156]
        fifth_tube = [1114, 1165]
        (((((((((self.tube_position(first_tube).tube_position(fourth_tube).
                 tube_position(third_tube).tube_position(fourth_tube)).
                tube_position(first_tube).tube_position(fifth_tube)).
               tube_position(second_tube).tube_position(fifth_tube)).
              tube_position(third_tube).tube_position(fifth_tube)).
             tube_position(first_tube).tube_position(third_tube)).
            tube_position(second_tube).tube_position(third_tube)).
           tube_position(second_tube).tube_position(fifth_tube)).
          tube_position(first_tube).tube_position(fourth_tube)).
         tube_position(second_tube).tube_position(third_tube))
        self.sleep_time()
        return GamePage

    def level_five(self):
        first_tube = [29, 1051]
        second_tube = [232, 1114]
        third_tube = [380, 1216]
        fourth_tube = [540, 1097]
        fifth_tube = [743, 1114]
        sixth_tube = [950, 1152]
        seventh_tube = [1131, 1085]
        (((((((((((((((((self.tube_position(first_tube).tube_position(sixth_tube).
                         tube_position(fourth_tube).tube_position(sixth_tube)).
                        tube_position(first_tube).tube_position(seventh_tube)).
                       tube_position(third_tube).tube_position(seventh_tube)).
                      tube_position(fourth_tube).tube_position(seventh_tube)).
                     tube_position(fifth_tube).tube_position(seventh_tube)).
                    tube_position(second_tube).tube_position(third_tube)).
                   tube_position(second_tube).tube_position(first_tube)).
                  tube_position(third_tube).tube_position(second_tube)).
                 tube_position(third_tube).tube_position(fourth_tube)).
                tube_position(fourth_tube).tube_position(third_tube)).
               tube_position(first_tube).tube_position(fourth_tube)).
              tube_position(first_tube).tube_position(third_tube)).
             tube_position(second_tube).tube_position(first_tube)).
            tube_position(fifth_tube).tube_position(first_tube)).
           tube_position(second_tube).tube_position(sixth_tube)).
          tube_position(fifth_tube).tube_position(sixth_tube)).
         tube_position(fifth_tube).tube_position(fourth_tube))
        self.sleep_time()
        return GamePage


if __name__ == "__main__":
    if not cli_setup():
        auto_setup(__file__, logdir=True, devices=[
            "ios:///http://127.0.0.1:8300", ])
        GameVictory().level_five()
