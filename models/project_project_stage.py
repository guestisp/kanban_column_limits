from odoo import fields, models


class ProjectProjectStage(models.Model):
    _inherit = "project.project.stage"

    column_limits = fields.Integer(string="Column limits")
    strict_column_limits = fields.Boolean(string="Strict column limits", default=False)
