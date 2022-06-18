# See LICENSE file for full copyright and licensing details.

from odoo import api, models,fields


class AccountMove(models.Model):

    _inherit = "account.move"

    hotel_folio_ids = fields.One2many("hotel.folio","hotel_invoice_id")
    @api.model
    def create(self, vals):
        res = super(AccountMove, self).create(vals)
        if self._context.get("folio_id"):
            folio = self.env["hotel.folio"].browse(self._context["folio_id"])
            folio.write({"hotel_invoice_id": res.id, "invoice_status": "invoiced"})
        return res
