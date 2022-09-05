from odoo import fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'
    _rec_name = 'title'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('openacademy.session', 'course_id')
