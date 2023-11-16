```python
from odoo import models, fields

class ComponentSchema(models.Model):
    _name = 'product.component'
    _description = 'Product Component'

    name = fields.Char('Component Name', required=True)
    category = fields.Selection([
        ('gaming_pc', 'Gaming PC'),
        ('laptop', 'Laptop'),
        ('cpu', 'CPU'),
        ('gpu', 'GPU'),
        ('motherboard', 'Motherboard'),
        ('ram', 'RAM'),
        ('storage', 'Storage'),
        ('cooling_system', 'Cooling System'),
        ('case', 'Case'),
        ('gaming_console', 'Gaming Console'),
        ('accessory', 'Accessory'),
    ], string='Category', required=True)
    brand = fields.Char('Brand')
    price = fields.Float('Price')
    specifications = fields.Text('Specifications')

    def get_component_details(self):
        return {
            'name': self.name,
            'category': self.category,
            'brand': self.brand,
            'price': self.price,
            'specifications': self.specifications,
        }

class ProductComponents(models.Model):
    _name = 'product.components'
    _description = 'Product Components'

    component_id = fields.Many2one('product.component', string='Component', required=True)
    quantity = fields.Integer('Quantity', default=1)

    def get_product_components(self):
        return {
            'component': self.component_id.get_component_details(),
            'quantity': self.quantity,
        }
```