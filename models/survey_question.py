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
        data = {}
        for rec in self:
            for questions in rec.question_and_page_ids:
                user_input_ids = rec.env['survey.user_input.line'].sudo().search([
                    ('question_id', '=', questions.id),
                    ])
                for value in user_input_ids:
                    if questions.title not in data:
                        data[questions.title] = value.value_text_box
                    else:
                        data[questions.title].append(value.value_text_box)
        return self.env.ref('survey_update.survey_survey_xlsx').report_action(data)