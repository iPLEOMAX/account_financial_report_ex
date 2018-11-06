# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Inherit the original GeneralLedgerReportMoveLine class
class GeneralLedgerReportMoveLine(models.TransientModel):
    _inherit = 'report_general_ledger_move_line'

    # Add a new label field that computes analytic info
    label_with_analytic = fields.Char(compute='compute_label_with_analytic', store=False)

    @api.multi
    def compute_label_with_analytic(self):
        for record in self:
            if record.move_line_id.analytic_account_id:
                record.label_with_analytic = record.move_line_id.analytic_account_id.name

                tags = []
                for tag in record.move_line_id.analytic_tag_ids:
                    tags.append(tag.display_name)

                if(len(tags)):
                    record.label_with_analytic += ' (' + ','.join(tags) + ')'

                record.label_with_analytic += ' - ' + record.label

            else:
                record.label_with_analytic = record.label