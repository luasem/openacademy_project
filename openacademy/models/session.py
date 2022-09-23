from dateutil.relativedelta import relativedelta

from odoo import _, api, exceptions, fields, models


class Session(models.Model):
    _name = "openacademy.session"
    _description = 'Open Academy Session'

    name = fields.Char()
    start_date = fields.Date(default=fields.Date.today())
    duration = fields.Integer(default=1)
    end_date = fields.Date(default=fields.Date.today())
    seats = fields.Integer('Number of Seats', default=1)
    instructor_id = fields.Many2one(
        'res.partner',
        string='Instructor',
        domain="['|', ('instructor', '=', 'True'), ('instructor_category', 'in', ['t_lvl1', 't_lvl2'])]",
    )
    course_id = fields.Many2one('openacademy.course', 'Course')
    attendee_ids = fields.Many2many('res.partner', string='Attendees')
    active = fields.Boolean(default=True)
    taken_seats = fields.Float(compute='_compute_taken_seats')

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            num_attendees = len(record.attendee_ids)
            record.taken_seats = 100 * (num_attendees / record.seats)

    @api.onchange('start_date', 'duration')
    def _onchange_end_date(self):
        for record in self:
            record.end_date = record.start_date + relativedelta(days=record.duration)

    @api.onchange('seats')
    def _onchange_seats(self):
        if self.seats <= 0:
            raise exceptions.UserError(_('The ammount of seats must be a positive number bigger than 0!'))

    @api.onchange('attendee_ids')
    def _onchange_attendee_ids(self):
        if len(self.attendee_ids) > self.seats:
            raise exceptions.UserError(_('You\'ve exceeded the amount of  available seats for this session!'))

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_validity(self):
        for record in self:
            if record.instructor_id in record.attendee_ids:
                raise exceptions.ValidationError(_('The instructor can\'t also be an attendee!'))

    @api.constrains('duration')
    def _check_valid_duration(self):
        for record in self:
            if record.duration < 1:
                raise exceptions.ValidationError(_('The session\'s duration must be at least 1 day!'))
