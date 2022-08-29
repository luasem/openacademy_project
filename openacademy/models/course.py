from odoo import fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'

    title = fields.Char(required=True)
    description = fields.Text()
