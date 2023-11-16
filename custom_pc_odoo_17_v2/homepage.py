```python
from flask import Flask, render_template
from .database_management import get_best_selling_products, get_deals, get_categories

app = Flask(__name__)

@app.route('/')
def homepage():
    best_selling_products = get_best_selling_products()
    deals = get_deals()
    categories = get_categories()

    return render_template('homepage.html', 
                           best_selling_products=best_selling_products, 
                           deals=deals, 
                           categories=categories)

def updateHomepage():
    with app.app_context():
        best_selling_products = get_best_selling_products()
        deals = get_deals()
        categories = get_categories()

        return render_template('homepage.html', 
                               best_selling_products=best_selling_products, 
                               deals=deals, 
                               categories=categories)

if __name__ == '__main__':
    app.run(debug=True)
```