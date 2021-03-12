
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group

class Introduction_Part3(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)
    pass

class Addiction(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['addiction_1', 'addiction_2', 'addiction_3', 'addiction_4', 'addiction_5', 'addiction_6']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False

class General_smoke(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['stress', 'environment', 'alcohol', 'context', 'brand']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False

class General_soc(Page):

    def is_displayed(self):
        return self.participant.vars['non_smoker'] != True

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['sex', 'perception', 'height', 'weight', 'health_state' ]

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False

# Orden en que se mostrarán las páginas
page_sequence = [Introduction_Part3,
                 Addiction,
                 General_smoke,
                 General_soc,
                 ]