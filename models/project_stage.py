# Copyright 2023 GUEST.it s.r.l.

from odoo import fields, models


class ProjectStage(models.Model):
    _inherit = "project.project.stage"

    column_limit = fields.Char(string="Column limits")
    strict_column_limit = fields.Char(string="Strict column limits")
