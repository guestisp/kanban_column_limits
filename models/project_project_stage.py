# Copyright 2023 GUEST.it s.r.l.

from odoo import fields, models


class ProjectStage(models.Model):
    _inherit = "project.stage"

    column_limits = fields.Integer(string="Column limits")
    strict_column_limits = fields.Boolean(string="Strict column limits", default=False)
