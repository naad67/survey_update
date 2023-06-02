from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.survey.survey_data_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        data = {}
        for obj in partners:
            for questions in obj.question_and_page_ids:
                user_input_ids = obj.env['survey.user_input.line'].sudo().search([
                    ('question_id', '=', questions.id),
                    ])
                for value in user_input_ids:
                    if value.value_text_box:
                        if questions.title not in data:
                            data[questions.title] = [value.value_text_box]
                        else:
                            data[questions.title].append(value.value_text_box)
            report_name = "Survey Data"
            sheet = workbook.add_worksheet(report_name[:31])
            for i,j in enumerate(data):
                print(i,data[j])
                # Name of table
                sheet.write(0, 0, "TIME")
                sheet.write(0, 1, "Согласие на обработку данных(ответов) опроса")
                sheet.write(0, 2, "Ваша должность")
                sheet.write(0, i + 3, j)
                # value of table
                for index,ans in enumerate(data[j]):
                    sheet.write(index+1, 0, "###")
                    sheet.write(index+1, 1, "Я согласен/согласна")
                    sheet.write(index+1, 2, "Сотрудник")
                    sheet.write(index + 1, i + 3, ans)