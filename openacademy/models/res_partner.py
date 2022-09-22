from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean(string='Is Instructor')
    instructor_category = fields.Selection(
        [
            ('t_lvl1', 'Teacher / Level 1'),
            ('t_lvl2', 'Teacher / Level 2'),
        ]
    )
    session_ids = fields.Many2many('openacademy.session')
