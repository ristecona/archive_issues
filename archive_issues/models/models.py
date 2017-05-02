# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ArchiveIssuesLine(models.TransientModel):

    _name = 'base.issue.archive.line'
    _order = 'min_id asc'

    wizard_id = fields.Many2one('base.issue.archive.automatic.wizard', 'Wizard')

class ArchiveIssues(models.TransientModel):

    _name = 'base.issue.archive.automatic.wizard'
    _description = 'Archive Issues'

    @api.model
    def default_get(self, fields):
        res = super(ArchiveIssues, self).default_get(fields)
        active_ids = self.env.context.get('active_ids')
        if self.env.context.get('active_model') == 'project.issue' and active_ids:
            #res['state'] = 'selection'
            res['issue_ids'] = active_ids
        return res

    issue_ids = fields.Many2many('project.issue', 'archive_issues_rel', 'archive_id', 'issue_id', string='Issues')



    @api.multi

    def action_archive(self):
        self.issue_ids.write({'active': False})
        return True
