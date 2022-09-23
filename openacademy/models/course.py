from odoo import _, fields, models


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Open Academy Course'
    _rec_name = 'title'

    title = fields.Char(required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('openacademy.session', 'course_id')

    _sql_constraints = [
        (
            'different_title_and_descritpion',
            'CHECK(title != description)',
            'The description has to be different from the title!',
        ),
        ('unique_title', 'UNIQUE(title)', 'The title name must be uinique!'),
    ]

    def copy(self, default=None):
        default = dict(default or {})
        default.update(title=_("Copy of %s") % self.title)
        return super().copy(default)
