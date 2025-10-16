from odoo import models, fields

class HospitalBanner(models.Model):
    _name = 'hospital.banner'
    _description = 'Hospital Banner'

    name = fields.Char("Banner Title", required=True)
    image = fields.Binary("Banner Image", attachment=True)
    sequence = fields.Integer("Sequence", default=10)
    active = fields.Boolean("Active", default=True)
