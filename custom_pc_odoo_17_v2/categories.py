```python
from odoo import models, fields

class ProductCategory(models.Model):
    _name = 'product.category'
    _description = 'Product Category'

    name = fields.Char('Category Name', required=True)
    description = fields.Text('Description')

class ProductComponent(models.Model):
    _name = 'product.component'
    _description = 'Product Component'

    name = fields.Char('Component Name', required=True)
    description = fields.Text('Description')
    category_id = fields.Many2one('product.category', 'Category', ondelete='cascade')
    specifications = fields.Text('Specifications')

class GamingPC(models.Model):
    _name = 'gaming.pc'
    _inherit = 'product.component'

class Laptop(models.Model):
    _name = 'laptop'
    _inherit = 'product.component'

class PCComponent(models.Model):
    _name = 'pc.component'
    _inherit = 'product.component'

class GamingConsole(models.Model):
    _name = 'gaming.console'
    _inherit = 'product.component'

class Accessory(models.Model):
    _name = 'accessory'
    _inherit = 'product.component'
```