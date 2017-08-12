from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'risk_aversion'
    players_per_group = None
    num_rounds = 1
    num_gambles = 10
    risk_takers_payoff_1 = c(10)
    risk_takers_payoff_2 = c(0.25)
    risk_averse_payoff_1 = c(5)
    risk_averse_payoff_2 = c(4)
    lb = 1
    ub = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):

    gamble_num = models.IntegerField()
    num_drawn = models.IntegerField()
    def get_lot_choices(self):
        choice = getattr(self,
                         "gamble_{}".format(self.gamble_num))
        if not choice:
            lottery_choices = [Constants.risk_takers_payoff_1,
                               Constants.risk_takers_payoff_2]

        else:
            lottery_choices = [Constants.risk_averse_payoff_1,
                               Constants.risk_averse_payoff_2]
        return lottery_choices

    def set_payoffs(self):
        self.gamble_num = random.choice(range(1, Constants.num_gambles+1))
        self.num_drawn = random.choice(range(Constants.lb, Constants.ub + 1))
        if self.num_drawn < self.gamble_num:
            self.payoff = self.get_lot_choices()[0]
        else:
            self.payoff = self.get_lot_choices()[1]


for i in range(1, Constants.num_gambles+1):
    Player.add_to_class("gamble_{}".format(i),
                        models.BooleanField())