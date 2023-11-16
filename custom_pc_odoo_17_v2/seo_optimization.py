```python
from flask import Flask, url_for
from flask_seo import Seo

app = Flask(__name__)
seo = Seo()

# Define SEO tags for each page
seo.init_app(app)

def optimizeSEO():
    seo_tags = {
        "title": "Custom PC Builder",
        "description": "Build your custom PC with our interactive catalog. Choose from a wide range of components.",
        "author": "Custom PC Builder Team",
        "keywords": "Custom PC, Gaming PC, PC Components, CPU, GPU, Motherboard, RAM, Storage, Cooling Systems, Cases, Gaming Consoles, Accessories",
        "url": url_for('index', _external=True),
        "image": url_for('static', filename='images/logo.png', _external=True)
    }

    seo.set_tags(seo_tags)

@app.route('/')
def index():
    optimizeSEO()
    return "Homepage"

@app.route('/product/<product_id>')
def product_page(product_id):
    product = productCatalog.get(product_id)
    seo_tags = {
        "title": product['name'],
        "description": product['description'],
        "author": "Custom PC Builder Team",
        "keywords": ", ".join(product['tags']),
        "url": url_for('product_page', product_id=product_id, _external=True),
        "image": url_for('static', filename='images/products/{}.png'.format(product_id), _external=True)
    }

    seo.set_tags(seo_tags)
    return "Product Page: {}".format(product['name'])

if __name__ == "__main__":
    app.run(debug=True)
```