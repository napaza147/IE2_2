
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random

doc = ''


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




class Subsession(BaseSubsession):

    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    # Preguntas de test de adición

    adiccion_1 = models.IntegerField(
        label="¿Cuántos minutos pasan entre el momento de levantarse y fumar el primer cigarrillo?",
        choices=[[3, "5 o menos"], [2, "De 6 a 30"], [1, "De 31 a 60"], [0, "Más de 60"]], widget=widgets.RadioSelect)

    adiccion_2 = models.IntegerField(
        label="¿Encuentras dificultad para abstenerte de fumar en lugares dónde está prohibido?",
        choices=[[1, "Sí"], [0, "No"]],widget=widgets.RadioSelect)

    adiccion_3 = models.IntegerField(label="¿Qué cigarrillo te costaría más abandonar?",
                                     choices=[[1, "El primero de la mañana"], [0, "Cualquier otros"]],widget=widgets.RadioSelect)

    adiccion_4 = models.IntegerField(label="¿Cuántos cigarrillos fumas al día?",
                                     choices=[[0, "Menos de 11"], [1, "Entre 11 y 20"], [2, "Entre 21 y 30"],
                                              [3, "Más de 30"]],widget=widgets.RadioSelect)

    adiccion_5 = models.IntegerField(
        label="¿Fumas más durante las primeras horas de la mañana que durante el resto del día?",
        choices=[[1, "Sí"], [0, "No"]],widget=widgets.RadioSelect)

    adiccion_6 = models.IntegerField(label="¿Fumas cuando no te encuentras bien o cuando estás enfermo?",
                                     choices=[[1, "Sí"], [0, "No"]],widget=widgets.RadioSelect)

    #Preguntas de control - Consumidor

    formato_preferido = models.IntegerField(label="¿Qué formato prefiere usualmente?",
                                            choices=[[0, "Cajetilla"], [1, "Suelto"]],widget=widgets.RadioSelect)

    estres = models.IntegerField(label="¿Cómo considera su nivel de estrés actual?",
                                 choices=[[0, "No vivenció"], [1, "No me siento estresado"],
                                          [2, "Me siento poco estresado"], [3, "Me siento muy estresado"]],widget=widgets.RadioSelect)

    entorno = models.IntegerField(label="¿Cómo considera su entorno social?",
                                  choices=[[0, "Ninguno fuma"], [1, "Algunos fuman"], [2, "La mayoría fuma"],
                                           [3, "Todos fuman"]],widget=widgets.RadioSelect)

    alcohol = models.IntegerField(label="¿Consume alcohol regularmente?",
                                  choices=[[0, "No"], [1, "Sí"]], widget=widgets.RadioSelect)

    situacion =  models.IntegerField(label="¿Cuáles eran sus situaciones preferentes de consumo?",
                                     choices=[[1, "Reuniones sociales"], [2, "Entornos sociales entre 2-5 personas"],
                                            [3, "De forma solitaria"]], widget=widgets.RadioSelect)

    marca = models.IntegerField(blank=True, choices=[[1, "Lucky Strike"], [2, "Hamilton"], [3, "Pall Mall"], [4, "Malboro"],
                                                      [5, "Otros"]], widget=widgets.RadioSelect)

    #Preguntas de control - Consumidor

    sexo = models.IntegerField(label="¿A qué género pertenece?", choices=[[0, "Femenino"], [1, "Masculino"]],  widget=widgets.RadioSelect)

    percibido = models.IntegerField(label="De la última caja que compró, ¿Recuerda de qué trataba la imagen disuasoría?",
                                  choices=[[0, "No"], [1, "Sí"]], widget=widgets.RadioSelect)

    talla = models.IntegerField(label="¿Cuál es tu talla actual? (Cm)")

    peso = models.IntegerField(label="¿Cuál es tu peso actual? (Kg)")

    estado_s = models.IntegerField(label="¿Cómo considera su estado de salud actual?",
                                  choices=[[0, "Muy mala"], [1, "Mala"], [2, "Buena"], [3, "Muy buena"]], widget=widgets.RadioSelect)


    # Hidden Field for detecting bots
    quiz_dec_2 = models.LongStringField(blank=True)
