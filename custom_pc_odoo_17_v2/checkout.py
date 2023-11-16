```python
from odoo import models, fields, api

class Checkout(models.Model):
    _name = 'custom_pc_odoo_17_v2.checkout'
    _description = 'Checkout Process'

    order_id = fields.Many2one('custom_pc_odoo_17_v2.order', string='Order')
    user_id = fields.Many2one('res.users', string='User')
    payment_method = fields.Selection([
        ('paypal', 'PayPal'),
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('bank_transfer', 'Bank Transfer'),
    ], string='Payment Method', required=True)
    shipping_address = fields.Text(string='Shipping Address', required=True)
    billing_address = fields.Text(string='Billing Address', required=True)

    @api.onchange('user_id')
    def _onchange_user_id(self):
        if self.user_id:
            self.billing_address = self.user_id.partner_id.street
            self.shipping_address = self.user_id.partner_id.street

    def process_checkout(self):
        # Validate the order
        if not self.order_id:
            return {'warning': {'title': 'No Order', 'message': 'Please create an order before checkout.'}}

        # Update the order status
        self.order_id.state = 'done'

        # Send a message to update the checkout
        self.env['bus.bus'].sendone(
            (self._cr.dbname, 'custom_pc_odoo_17_v2.checkout', self.user_id.partner_id.id),
            {'type': 'checkoutUpdateMessage', 'order_id': self.order_id.id}
        )

        return {'type': 'ir.actions.act_window_close'}
```