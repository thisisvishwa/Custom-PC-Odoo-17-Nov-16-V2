```python
from odoo import models, fields, api

class PaymentGateway(models.Model):
    _name = 'custom_pc_odoo_17_v2.payment_gateways'
    _description = 'Payment Gateways'

    name = fields.Char(string='Gateway Name', required=True)
    provider = fields.Char(string='Provider', required=True)
    transaction_fee = fields.Float(string='Transaction Fee (%)')
    is_active = fields.Boolean(string='Active', default=True)

    @api.model
    def integratePaymentGateway(self, gateway_name, provider, transaction_fee):
        """
        Function to integrate a new payment gateway
        """
        self.create({
            'name': gateway_name,
            'provider': provider,
            'transaction_fee': transaction_fee,
        })

    @api.multi
    def paymentGatewayUpdateMessage(self):
        """
        Function to send a message when a payment gateway is updated
        """
        self.message_post(body="Payment Gateway Updated")

    @api.multi
    def deactivateGateway(self):
        """
        Function to deactivate a payment gateway
        """
        self.write({
            'is_active': False,
        })
        self.paymentGatewayUpdateMessage()
```
