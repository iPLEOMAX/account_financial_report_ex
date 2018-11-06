# -*- coding: utf-8 -*-

from odoo import _, models, fields, api

# Inherit the original GeneralLedgerXslx class
class GeneralLedgerXslx(models.AbstractModel):
    _inherit = 'report.a_f_r.report_general_ledger_xlsx'

    # Override the method
    def _get_report_columns(self, report):
        res = super(GeneralLedgerXslx, self)._get_report_columns(report)

        # Replace the label field with custom analytic field
        res[6]['field'] = 'label_with_analytic'

        return res