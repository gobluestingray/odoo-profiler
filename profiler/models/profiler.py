# -*- coding: utf-8 -*-
from openerp import api, fields, models, _


class ProfilerProfiler(models.TransientModel):
    _name = "profiler.profiler"
    _description = "Profiler"

    datetime_begin = fields.Datetime(string="Begin Date")
    datetime_end = fields.Datetime(string="End Date")
    user_id = fields.Many2one("res.users", string="User")

    _sql_constraints = [("profiler_user_unique", "unique(user_id)", "A user can only have one profiler.")]
