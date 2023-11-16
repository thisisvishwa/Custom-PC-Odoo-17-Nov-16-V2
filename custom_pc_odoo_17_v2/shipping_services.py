```python
from odoo import api, fields, models

class ShippingService(models.Model):
    _name = 'custom_pc_odoo_17_v2.shipping_service'
    _description = 'Shipping Service'

    name = fields.Char(string='Service Name', required=True)
    cost = fields.Float(string='Cost', required=True)
    delivery_time = fields.Char(string='Estimated Delivery Time', required=True)

    @api.model
    def calculate_shipping(self, order_id):
        order = self.env['custom_pc_odoo_17_v2.order'].browse(order_id)
        weight = sum(line.product_id.weight for line in order.order_line)
        # Here we assume that the shipping cost is proportional to the total weight of the order
        # In a real-world application, the calculation could be more complex and depend on various factors
        return self.cost * weight

    @api.model
    def get_tracking_info(self, tracking_number):
        # This is a placeholder function. In a real-world application, it would integrate with the shipping service's API
        # to retrieve real-time tracking information.
        return 'Tracking information for {}: In transit'.format(tracking_number)
```