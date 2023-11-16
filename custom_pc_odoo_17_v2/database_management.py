```python
from odoo import models, fields

class ProductSchema(models.Model):
    _name = 'product.schema'
    name = fields.Char('Name', required=True)
    category = fields.Selection([
        ('gaming_pc', 'Gaming PC'),
        ('laptop', 'Laptop'),
        ('pc_component', 'PC Component'),
        ('gaming_console', 'Gaming Console'),
        ('accessory', 'Accessory'),
    ], string='Category', required=True)
    specifications = fields.Text('Specifications')

class ComponentSchema(models.Model):
    _name = 'component.schema'
    name = fields.Char('Name', required=True)
    product_id = fields.Many2one('product.schema', string='Product')
    specifications = fields.Text('Specifications')

class DatabaseManagement(models.Model):
    _name = 'database.management'

    def manageDatabase(self):
        # Update product and component schemas
        self.env['product.schema'].search([]).write({'updated_at': fields.Datetime.now()})
        self.env['component.schema'].search([]).write({'updated_at': fields.Datetime.now()})

        # Notify frontend about the update
        self.env['bus.bus'].sendone(
            'databaseUpdateMessage',
            {'message': 'Database updated successfully'}
        )

    def createProduct(self, name, category, specifications):
        self.env['product.schema'].create({
            'name': name,
            'category': category,
            'specifications': specifications
        })

    def createComponent(self, name, product_id, specifications):
        self.env['component.schema'].create({
            'name': name,
            'product_id': product_id,
            'specifications': specifications
        })
```