from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from django.forms import Field
from django.utils.translation import ugettext_lazy
from .models import Constants
from django import forms
from django.forms import Field
from django.utils.translation import ugettext_lazy


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class Instruction(Page):
    pass

class Instruction2(Page):
    pass

class Decisions(Page):
    form_model = models.Player
    form_fields = ['gamble_{}'.format(i)
                   for i in range(1, Constants.num_gambles + 1)]

    def vars_for_template(self):
        smth = self.get_form()
        fields_to_show = self.form_fields
        leftcol = []
        rightcol = []
        maxlen = len(fields_to_show) + 1
        for i, f in enumerate(fields_to_show):
            str1 = ', '.join(str(e) for e in [_ for _ in range(1, i+2)])
            str2 = ', '.join(str(e) for e in [_ for _ in range(i+2, maxlen )])
            leftcol.append(str1)
            rightcol.append(str2)

        return {'abclist': zip(smth, leftcol, rightcol), }

    def before_next_page(self):
        self.player.set_payoffs()


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results2(Page):
    def vars_for_template(self):
        choice = getattr(self.player,
                         "gamble_{}".format(self.player.gamble_num))
        maxlen = Constants.num_gambles + 1
        str1 = ', '.join(str(e) for e in [_ for _ in range(1, self.player.gamble_num+1)])
        str2 = ', '.join(str(e) for e in [_ for _ in range(self.player.gamble_num+1, maxlen)])
        return {'chosen_gamble_choice': choice,
                'str1': str1,
                'str2': str2,
                }
        pass


page_sequence = [
    Introduction,
    Instruction,
    Instruction2,
    Decisions,
    Results2
    # DecisionsA,
    # DecisionsB
]