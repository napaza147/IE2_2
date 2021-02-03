
from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player, Group


class Adiccion(Page):

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['adiccion_1', 'adiccion_2', 'adiccion_3', 'adiccion_4', 'adiccion_5', 'adiccion_6']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False

    timeout_seconds = 300

class General_fum(Page):

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['formato_preferido', 'estres', 'entorno', 'alcohol', 'situacion', 'marca']

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False

    timeout_seconds = 480

class General_soc(Page):

    # Variables que se utilizarán en esta sección
    form_model = 'player'
    form_fields = ['sexo', 'percibido', 'talla', 'peso', 'estado_s' ]

    def vars_for_template(self):
        return dict(participant_id=self.participant.label)

    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False

    timeout_seconds = 480

class Pagos(Page):
    form_model = 'player'
    form_fields = ['quiz_dec_2']

    def vars_for_template(self):
        return {'participant_id': self.participant.label,
                'quiz_earnings': self.participant.vars['quiz_earnings'],
                'numero': self.participant.vars['quiz_questions_correct'],
                'ea1': self.participant.vars['ea1'],
                'ea2': self.participant.vars['ea2'],
                'ea3': self.participant.vars['ea3'],
                'ea4': self.participant.vars['ea4'],
                'pago_final': self.participant.vars['quiz_earnings'] + 5
                }


    # def is_displayed(self):
    #     if self.participant.vars['MobilePhones'] is False:
    #         return True
    #     else:
    #         return False



# Orden en que se mostrarán las páginas
page_sequence = [Adiccion,
                 General_fum,
                 General_soc,
                 Pagos]