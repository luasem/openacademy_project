from odoo import api, fields, models


class Session(models.Model):
    _name = "openacademy.session"
    _description = 'Open Academy Session'

    name = fields.Char()
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Float()
    seats = fields.Integer('Number of Seats')
    instructor_id = fields.Many2one(
        'res.partner',
        string='Instructor',
        domain="['|', ('instructor', '=', 'True'), ('instructor_category', 'in', ['t_lvl1', 't_lvl2'])]",
    )
    course_id = fields.Many2one('openacademy.course', 'Course')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    active = fields.Boolean(default=True)
    occupancy = fields.Float(compute='_compute_occupancy')

    @api.depends('seats', 'attendee_ids')
    def _compute_occupancy(self):
        for record in self:
            num_attendees = len(record.attendee_ids)
            record.occupancy = 100 * (num_attendees / record.seats)
