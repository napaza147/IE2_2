
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

doc = 'Cuestionario de preguntas de control'


class Constants(BaseConstants):
    """
    Description:
        Inherits oTree Class BaseConstants. Defines constants for
        the experiment these will remain unchanged
    """

    players_per_group = None
    num_rounds = 1
    timer = 20
    payment_per_answer = c(0.2)


    instructions_template = 'Quiz_2/InstruccionesB.html'
    instructions_button = "Quiz_2/Instructions_Button.html"
    contact_template = "Quiz_2/Contactenos.html"

    name_in_url = 'Cigarettes_experiment_4'  # name in webbrowser

 # Write here your possible choices as [number, string_with_choice]
    brand_choices = [[1, 'Lucky Strike'],
                  [2, 'Hamilton'],
                  [3, 'Marlboro'],
                  [4, 'Winston'],
                  [5, 'Kent'],
                  [6, 'Pall Mall'],
                  [7, 'Otros']]

 # To randomize the order in which the answers are presented
    random.SystemRandom().shuffle(brand_choices)

class Subsession(BaseSubsession):

    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Preguntas de test de adición

    addiction_1 = models.IntegerField(
        label="¿Cuántos minutos pasan entre el momento de levantarse y fumar el primer cigarrillo?",
        choices=[[3, "5 o menos"], [2, "De 6 a 30"], [1, "De 31 a 60"], [0, "Más de 60"]], widget=widgets.RadioSelect)

    addiction_2 = models.IntegerField(
        label="¿Encuentra dificultad para abstenerte de fumar en lugares dónde está prohibido?",
        choices=[[1, "Sí"], [0, "No"]],widget=widgets.RadioSelect)

    addiction_3 = models.IntegerField(label="¿Qué cigarrillo le costaría más abandonar?",
                                     choices=[[1, "El primero de la mañana"], [0, "Cualquier otro"]],widget=widgets.RadioSelect)

    addiction_4 = models.IntegerField(label="¿Cuántos cigarrillos fuma al día?",
                                     choices=[[0, "Menos de 11"], [1, "Entre 11 y 20"], [2, "Entre 21 y 30"],
                                              [3, "Más de 30"]],widget=widgets.RadioSelect)

    addiction_5 = models.IntegerField(
        label="¿Fuma más durante las primeras horas de la mañana o durante el resto del día?",
        choices=[[1, "Primeras horas de la mañana"], [0, "Resto del día"]],widget=widgets.RadioSelect)

    addiction_6 = models.IntegerField(label="¿Fuma cuando no se encuentra bien o cuando está enfermo?",
                                     choices=[[1, "Sí"], [0, "No"]],widget=widgets.RadioSelect)

    #Preguntas de control - Consumidor

    stress = models.IntegerField(label="¿Cómo considera su nivel de estrés habitual?",
                                 choices=[[0, "Muy bajo"], [1, "Bajo"], [2, "Alto"], [3, "Muy alto"]],widget=widgets.RadioSelect)

    environment = models.IntegerField(label="Considera que en su entorno social",
                                  choices=[[0, "Ninguno fuma"], [1, "Algunos fuman"], [2, "La mayoría fuma"],
                                           [3, "Todos fuman"]],widget=widgets.RadioSelect)

    alcohol = models.IntegerField(label="¿Consume bebidas alcohólicas regularmente (al menos 1 vez cada 14 días)?",
                                  choices=[[0, "No"], [1, "Sí"]], widget=widgets.RadioSelect)

    context =  models.IntegerField(label="¿En cuál de los siguientes contextos solía consumir más cigarrillos?",
                                     choices=[[1, "Reuniones sociales"], [2, "Entornos sociales entre 2-5 personas"],
                                            [3, "De forma solitaria"]], widget=widgets.RadioSelect)

    brand = models.IntegerField(label="¿Cuáles es su marca favorita de cigarrillos?", widget=widgets.RadioSelect,
                                              choices=Constants.brand_choices)
    #Preguntas de control - Consumidor

    sex = models.IntegerField(label="¿A qué género pertenece?", choices=[[0, "Femenino"], [1, "Masculino"], [2, "Prefiero no decir"]],  widget=widgets.RadioSelect)

    perception = models.IntegerField(label="De la última cajetilla que compró, ¿Recuerda de qué trataba la imagen disuasoria?",
                                  choices=[[0, "No"], [1, "Sí"]], widget=widgets.RadioSelect)

    height = models.IntegerField(label="¿Cuál es tu talla actual? (Cm)", min=0)

    weight = models.IntegerField(label="¿Cuál es tu peso actual? (Kg)", min=0)

    health_state = models.IntegerField(label="¿Cómo considera su estado de salud actual?",
                                  choices=[[0, "Muy malo"], [1, "Malo"], [2, "Bueno"], [3, "Muy bueno"]], widget=widgets.RadioSelect)

    # Hidden Field for detecting bots
    quiz_dec_2 = models.LongStringField(blank=True)
