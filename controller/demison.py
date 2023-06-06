import json
import logging
import werkzeug

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from odoo import fields, http, SUPERUSER_ID, _
from odoo.addons.base.models.ir_ui_view import keep_query
from odoo.exceptions import UserError
from odoo.http import request, content_disposition
from odoo.osv import expression
from odoo.tools import format_datetime, format_date, is_html_empty

_logger = logging.getLogger(__name__)

class Demison(http.Controller):

    @http.route(['/demison'], type='http', auth="public", website=True)
    def monthly_request_webform(self):
        return request.render("survey_update.demison_model")
