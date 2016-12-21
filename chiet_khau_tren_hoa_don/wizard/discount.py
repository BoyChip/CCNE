# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.tools.safe_eval import safe_eval
from odoo.exceptions import UserError

class SaleDiscountWizard(models.TransientModel):
    _name = "sale.discount.wizard"


    luachon = fields.Selection([('theo_phan_tram','Theo %'),('theo_gia','Theo gia tri')], string='Chiet khau',default='theo_phan_tram', required=True)
    giatri  = fields.Float(string='Nhap gia tri', required=True)

    @api.multi
    def submit(self):
        self.ensure_one()
        order = self.env['sale.order'].browse(self._context.get('active_id'))
        value = 0
        if self.luachon == 'theo_phan_tram':
            value = order.amount_total * self.giatri / 100.0
        else:
            value = self.giatri

        product = self.env.ref('chiet_khau_tren_hoa_don.sp_giam_gia')
        self.env['sale.order.line'].create({
            'order_id':         order.id,
            'name':             product.name, 
            'product_id':       product.id, 
            'product_uom_qty':  1, 
            'product_uom':      product.uom_id.id, 
            'price_unit':       -value,
        })

