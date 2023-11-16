```python
from odoo import models, fields

class InventoryManagement(models.Model):
    _name = 'custom_pc_odoo_17_v2.inventory_management'
    _description = 'Inventory Management'

    product_id = fields.Many2one('custom_pc_odoo_17_v2.product', string='Product')
    quantity_on_hand = fields.Integer(string='Quantity On Hand')
    forecasted_quantity = fields.Integer(string='Forecasted Quantity')

    def manageInventory(self):
        for record in self:
            if record.quantity_on_hand <= 0:
                return {
                    'warning': {
                        'title': "Out of Stock",
                        'message': "The selected product is out of stock.",
                    },
                }
            else:
                record.quantity_on_hand -= 1
                record.forecasted_quantity -= 1
                return {
                    'success': {
                        'title': "Inventory Updated",
                        'message': "The inventory has been updated successfully.",
                    },
                }

    def inventoryStatus(self, product_id):
        product = self.search([('product_id', '=', product_id)])
        if product:
            return {
                'quantity_on_hand': product.quantity_on_hand,
                'forecasted_quantity': product.forecasted_quantity,
            }
        else:
            return {
                'error': {
                    'title': "Product Not Found",
                    'message': "The requested product was not found in the inventory.",
                },
            }
```
