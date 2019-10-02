from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = "stock.picking"

    #confirm_date = fields.Date("Confirmed Date")
    #confirm_user = fields.Many2one("res.user", string = "Confirmed By")
    pass