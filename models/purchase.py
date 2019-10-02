# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    supplier_phone = fields.Char("Phone", related = "partner_id.phone")
    supplier_email = fields.Char("Email", related = "partner_id.email")
    contact_person = fields.Many2one("res.users",string = "Contact Person",default= lambda self: self.env.user)
    duration = fields.Float("duration", compute = "compute_duration")

    def compute_duration(self):
        if not self.date_planned:
            self.date_planned = fields.Date.today()
        od = fields.Date.from_string(self.date_order)
        ed = fields.Date.from_string(self.date_planned)
        dur = ed - od
        self.duration = dur.days

    @api.multi
    def action_view_related_product(self):
        return {
        "view_type": "form",
        "view_mode": "tree",
        "res_model": "purchase.order",
        "target": "current",
        "res_id": "purchase.purchase_order_tree",
        "type": "ir.actions.act_window",
        "name" : "Related Product"
    }


