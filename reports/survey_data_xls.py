from odoo import models

class PartnerXlsx(models.AbstractModel):
    _name = 'report.survey.survey_data_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        print(partners)
        # for obj in partners:
        #     report_name = obj.name
        #     # One sheet by partner
        #     sheet = workbook.add_worksheet(report_name[:31])
        #     bold = workbook.add_format({'bold': True})
        #     sheet.write(0, 0, obj.name, bold)