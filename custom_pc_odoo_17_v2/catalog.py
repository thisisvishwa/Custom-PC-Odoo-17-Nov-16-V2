```python
from odoo import models, fields

class ProductCatalog(models.Model):
    _name = 'product.catalog'
    _description = 'Product Catalog'

    name = fields.Char('Name', required=True)
    category_id = fields.Many2one('product.category', 'Category')
    brand = fields.Char('Brand')
    price = fields.Float('Price')
    specifications = fields.Text('Specifications')
    image = fields.Binary('Image')

class ProductCategory(models.Model):
    _name = 'product.category'
    _description = 'Product Category'

    name = fields.Char('Name', required=True)
    product_ids = fields.One2many('product.catalog', 'category_id', 'Products')

class ProductFilter(models.Model):
    _name = 'product.filter'
    _description = 'Product Filter'

    name = fields.Char('Name', required=True)
    category_id = fields.Many2one('product.category', 'Category')
    brand = fields.Char('Brand')
    price_range = fields.Char('Price Range')
    specifications = fields.Text('Specifications')

    def filterCatalog(self):
        domain = []
        if self.category_id:
            domain.append(('category_id', '=', self.category_id.id))
        if self.brand:
            domain.append(('brand', 'ilike', self.brand))
        if self.price_range:
            min_price, max_price = map(float, self.price_range.split('-'))
            domain.append(('price', '>=', min_price))
            domain.append(('price', '<=', max_price))
        if self.specifications:
            domain.append(('specifications', 'ilike', self.specifications))
        return self.env['product.catalog'].search(domain)
```