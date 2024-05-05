from odoo import fields, models, api


class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Hospital Doctor'

    first_name = fields.Char()
    last_name = fields.Char()
    image = fields.Binary()
