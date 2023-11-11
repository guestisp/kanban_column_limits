# Copyright 2023 GUEST.it s.r.l.

from odoo import fields, models


class ProjectProjectStage(models.Model):
    _inherit = "project.project.stage"

    column_limit = fields.Integer(string="Column limits")
    strict_column_limit = fields.Boolean(string="Strict column limits")
