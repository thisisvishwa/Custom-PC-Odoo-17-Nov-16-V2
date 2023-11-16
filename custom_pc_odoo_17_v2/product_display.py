```python
from odoo import models, fields

class ProductDisplay(models.Model):
    _name = 'product.display'
    _description = 'Product Display'

    productGridView = fields.Boolean('Grid View', default=True)
    productListView = fields.Boolean('List View', default=False)
    productImages = fields.One2many('product.image', 'product_id', string='Product Images')
    quickViewOptions = fields.Boolean('Quick View Options', default=True)

    def displayProduct(self):
        if self.productGridView:
            # Code to display products in grid view
            pass
        elif self.productListView:
            # Code to display products in list view
            pass

    def toggleView(self):
        self.productGridView = not self.productGridView
        self.productListView = not self.productListView
        self.displayProduct()

    def loadQuickView(self, product_id):
        if self.quickViewOptions:
            # Code to load quick view of a product
            pass

class ProductImage(models.Model):
    _name = 'product.image'
    _description = 'Product Image'

    product_id = fields.Many2one('product.display', string='Related Product')
    image = fields.Binary('Image', attachment=True)
    image_url = fields.Char('Image URL')
    alt_text = fields.Char('Alt Text')
```
This Python code defines two Odoo models for managing product display. The `ProductDisplay` model has fields for grid view, list view, product images, and quick view options. It also has methods for displaying products, toggling the view mode, and loading the quick view of a product.

The `ProductImage` model is used to manage images of products. It has fields for the related product, the image file, the image URL, and the alt text for the image.