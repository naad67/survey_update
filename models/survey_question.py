from odoo import models, fields, api


class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection([
        ('text_box', 'Multiple Lines Text Box'),
        ('char_box', 'Single Line Text Box'),
        ('numerical_box', 'Numerical Value'),
        ('date', 'Date'),
        ('datetime', 'Datetime'),
        ('simple_choice', 'Multiple choice: only one answer'),
        ('multiple_choice', 'Multiple choice: multiple answers allowed'),
        ('matrix', 'Matrix'),
        ('scale', 'Scale')], string='Question Type',
        compute='_compute_question_type', readonly=False, store=True)

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    denison_model = fields.Boolean(string="Denison Model")

    def action_denison(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/demison'
        }


    def render_denison(self):
        # загружаем файлы
        import pandas as pd
        import io
        df = pd.read_excel(io.BytesIO(['Print to XLSX (21).xlsx']))  # напишите имя файла
        # высчитываем среднее значение по столбцу и по сектору

        Strategic_q = df.iloc[:, 3:7].astype(float).mean()
        Strategic_mean = int(round(Strategic_q.mean() * 10, 0))

        Goals_q = df.iloc[:, 7:11].astype(float).mean()
        Goals_mean = int(round(Goals_q.mean() * 10, 0))

        Vision_q = df.iloc[:, 11:15].astype(float).mean()
        Vision_mean = int(round(Vision_q.mean() * 10, 0))

        Core_q = df.iloc[:, 15:19].astype(float).mean()
        Core_mean = int(round(Core_q.mean() * 10, 0))

        Agreement_q = df.iloc[:, 19:23].astype(float).mean()
        Agreement_mean = int(round(Agreement_q.mean() * 10, 0))

        Coordination_q = df.iloc[:, 23:27].astype(float).mean()
        Coordination_mean = int(round(Coordination_q.mean() * 10, 0))

        Empowerment_q = df.iloc[:, 27:31].astype(float).mean()
        Empowerment_mean = int(round(Empowerment_q.mean() * 10, 0))

        Team_q = df.iloc[:, 31:35].astype(float).mean()
        Team_mean = int(round(Team_q.mean() * 10, 0))

        Capability_q = df.iloc[:, 35:39].astype(float).mean()
        Capability_mean = int(round(Capability_q.mean() * 10, 0))

        Creating_q = df.iloc[:, 39:43].astype(float).mean()
        Creating_mean = int(round(Creating_q.mean() * 10, 0))

        Customer_q = df.iloc[:, 43:47].astype(float).mean()
        Customer_mean = int(round(Customer_q.mean() * 10, 0))

        Organizational_q = df.iloc[:, 47:51].astype(float).mean()
        Organizational_mean = int(round(Organizational_q.mean() * 10, 0))

        data_mean = [Vision_mean, Goals_mean, Strategic_mean, Organizational_mean, Customer_mean, Creating_mean,
                     Empowerment_mean, Team_mean, Capability_mean, Core_mean, Agreement_mean, Coordination_mean]
        # создаем модель Денисона

        import matplotlib.pyplot as plt
        import matplotlib.patches as mpatches
        import numpy as np

        # регулятор размеров
        a = 8
        sector_radii = []
        x = []
        sector_radii = data_mean[:]
        x = data_mean[:]

        for i in range(len(sector_radii)):
            if 0 <= sector_radii[i] <= 25:
                sector_radii[i] = 2 * a
            elif 26 <= sector_radii[i] <= 50:
                sector_radii[i] = 3 * a
            elif 51 <= sector_radii[i] <= 75:
                sector_radii[i] = 4 * a
            elif 76 <= sector_radii[i] <= 100:
                sector_radii[i] = 5 * a

        # Цвета секторов
        sector_colors = ['#CF402C', '#CF402C', '#CF402C', '#4682B4', '#4682B4', '#4682B4', '#69964B', '#69964B',
                         '#69964B', '#F2D43D', '#F2D43D', '#F2D43D']

        # Угол секторов
        angle = 30

        # Радиус окружности
        radius = 6 * a

        # Создание фигуры
        fig, ax = plt.subplots(figsize=(a, a))

        # Создание окружностей
        circle7 = plt.Circle((0, 0), 6 * a, color='#F4F6F8', fill=True, linewidth=1)
        ax.add_artist(circle7)
        circle51 = plt.Circle((0, 0), 3 * a, color='white', fill=True, linewidth=1)
        ax.add_artist(circle51)

        # углы секторов
        angles = np.linspace(0, 2 * np.pi, 13)[:-1]

        # Создание закрашенных секторов
        start_angle = 0
        for i in range(len(sector_radii)):
            end_angle = start_angle + angle
            ax.add_patch(
                mpatches.Wedge((0, 0), sector_radii[i], start_angle, end_angle, color=sector_colors[i], linewidth=1))
            start_angle += angle

        # Создание окружностей
        circle6 = plt.Circle((0, 0), 6 * a, color='black', fill=False, linewidth=1)
        ax.add_artist(circle6)
        circle5 = plt.Circle((0, 0), 5 * a, color='black', fill=False, linewidth=1)
        ax.add_artist(circle5)
        circle4 = plt.Circle((0, 0), 4 * a, color='black', fill=False, linewidth=1)
        ax.add_artist(circle4)
        circle3 = plt.Circle((0, 0), 3 * a, color='black', fill=False, linewidth=1)
        ax.add_artist(circle3)
        circle2 = plt.Circle((0, 0), 2 * a, color='black', fill=False, linewidth=1)
        ax.add_artist(circle2)

        # Создание линий для секторов
        start_angle = 0
        for i in range(12):
            end_angle = start_angle + angle
            ax.add_patch(mpatches.Wedge((0, 0), 6 * a, start_angle, end_angle, color='black', fill=False, linewidth=1))
            start_angle += angle

        # Создание окружностей
        circle1 = plt.Circle((0, 0), a, color='#6E6E72', fill=True, linewidth=1)
        ax.add_artist(circle1)
        circle1 = plt.Circle((0, 0), a, color='#F4F6F8', fill=False, linewidth=1)
        ax.add_artist(circle1)

        # Текст
        ax.text(0, -(a / 5), 'BELIEFS & \n ASSUMPTIONS', fontsize=a, color='#F4F6F8', ha='center')
        ax.text(0, 19 * a / 3, 'External Focus', fontsize=7 * a / 5, color='black', ha='center')
        ax.text(0, -20 * a / 3, 'Internal Focus', fontsize=7 * a / 5, color='black', ha='center')
        ax.text(-21 * a / 3, 0, 'Flexible', fontsize=7 * a / 5, color='black', ha='center')
        ax.text(21 * a / 3, 0, 'Stable', fontsize=7 * a / 5, color='black', ha='center')

        ax.text(9 * a / 2, (11.5 * a) / 3, 'MISSION', fontsize=9 * a / 5, color='red', ha='center', rotation=-45)
        ax.text(-(9.3 * a) / 2, (10 * a) / 3, 'ADAPTABILITY', fontsize=9 * a / 5, color='blue', ha='center',
                rotation=45)
        ax.text(-(9.5 * a) / 2, -(17 * a) / 3, 'INVOLVEMENT', fontsize=9 * a / 5, color='green', ha='center',
                rotation=-45)
        ax.text((9.5 * a) / 2, -(17 * a) / 3, 'CONSISTENCY', fontsize=9 * a / 5, color='#C87900', ha='center',
                rotation=45)

        ax.text(-16 * a / 3, 2 * a / 3, 'Creating\nchange', fontsize=7 * a / 5, color='#4F4F4F', ha='center',
                rotation=75)
        ax.text(-11.3 * a / 3, 8.6 * a / 3, 'Customer focus', fontsize=7 * a / 5, color='#4F4F4F', ha='center',
                rotation=45)
        ax.text(-4 * a / 3, 14 * a / 3, 'Organizational\nLearning', fontsize=7 * a / 5, color='#4F4F4F', ha='center',
                rotation=15)
        ax.text(-16 * a / 3, -8 * a / 3, 'Empowerment', fontsize=7 * a / 5, color='#4F4F4F', ha='center', rotation=-75)
        ax.text(-11.6 * a / 3, -14.3 * a / 3, 'Team\nOrientation', fontsize=7 * a / 5, color='#4F4F4F', ha='center',
                rotation=-45)
        ax.text(-4 * a / 3, -17.5 * a / 3, 'Capability\nDevelopment', fontsize=7 * a / 5, color='#4F4F4F', ha='center',
                rotation=-15)
        ax.text(4.3 * a / 3, -17 * a / 3, 'Core Values', fontsize=7 * a / 5, color='#4F4F4F', ha='center', rotation=15)
        ax.text(11.7 * a / 3, -13.6 * a / 3, 'Agreement', fontsize=7 * a / 5, color='#4F4F4F', ha='center', rotation=45)
        ax.text(15.8 * a / 3, -7.5 * a / 3, 'Coordination\n& Integration', fontsize=7 * a / 5, color='#4F4F4F',
                ha='center', rotation=75)
        ax.text(4.3 * a / 3, 14 * a / 3, 'Strategic Direction\n& Intent', fontsize=6 * a / 5, color='#4F4F4F',
                ha='center', rotation=-15)
        ax.text(12 * a / 3, 9 * a / 3, 'Goals &\nObjectives', fontsize=7 * a / 5, color='#4F4F4F', ha='center',
                rotation=-45)
        ax.text(15.6 * a / 3, 2.8 * a / 3, 'Vision', fontsize=8 * a / 5, color='#4F4F4F', ha='center', rotation=-75)

        # цифры на графике
        ax.text(sector_radii[0] - 0.16 * sector_radii[0], sector_radii[0] - 0.8 * sector_radii[0], x[0],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(sector_radii[1] - 0.4 * sector_radii[1], sector_radii[1] - 0.4 * sector_radii[1], x[1],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(sector_radii[2] - 0.8 * sector_radii[2], sector_radii[2] - 0.2 * sector_radii[2], x[2],
                fontsize=10 * a / 5, color='#213154', ha='center')

        ax.text(-sector_radii[3] + 0.8 * sector_radii[3], sector_radii[3] - 0.2 * sector_radii[3], x[3],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(-sector_radii[4] + 0.4 * sector_radii[4], sector_radii[4] - 0.4 * sector_radii[4], x[4],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(-sector_radii[5] + 0.16 * sector_radii[5], sector_radii[5] - 0.8 * sector_radii[5], x[5],
                fontsize=10 * a / 5, color='#213154', ha='center')

        ax.text(-sector_radii[6] + 0.16 * sector_radii[6], -sector_radii[6] + 0.8 * sector_radii[6], x[6],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(-sector_radii[7] + 0.4 * sector_radii[7], -sector_radii[7] + 0.4 * sector_radii[7], x[7],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(-sector_radii[8] + 0.8 * sector_radii[8], -sector_radii[8] + 0.16 * sector_radii[8], x[8],
                fontsize=10 * a / 5, color='#213154', ha='center')

        ax.text(sector_radii[9] - 0.8 * sector_radii[9], -sector_radii[9] + 0.2 * sector_radii[9], x[9],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(sector_radii[10] - 0.35 * sector_radii[10], -sector_radii[10] + 0.35 * sector_radii[10], x[10],
                fontsize=10 * a / 5, color='#213154', ha='center')
        ax.text(sector_radii[11] - 0.16 * sector_radii[11], -sector_radii[11] + 0.8 * sector_radii[11], x[11],
                fontsize=10 * a / 5, color='#213154', ha='center')

        # Содание графика
        ax.set_aspect('equal')
        plt.xlim(-radius - 5, radius + 5)
        plt.ylim(-radius - 5, radius + 5)
        plt.axis('off')
        plt.show()


class SurveyDemison(models.Model):
    _name = 'survey.demison'

    gaf = fields.Char("String")