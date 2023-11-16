```python
from .components import productComponents
from .database_management import ProductSchema

class ProductComparison:
    def __init__(self):
        self.comparisonTable = []

    def add_to_comparison(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.comparisonTable.append(product)
            self.update_comparison_table()
        else:
            print("Product not found.")

    def remove_from_comparison(self, product_id):
        product = self.get_product_by_id(product_id)
        if product in self.comparisonTable:
            self.comparisonTable.remove(product)
            self.update_comparison_table()
        else:
            print("Product not in comparison table.")

    def get_product_by_id(self, product_id):
        for category in productComponents:
            for product in productComponents[category]:
                if product['id'] == product_id:
                    return product
        return None

    def update_comparison_table(self):
        comparisonUpdateMessage = "Comparison table updated."
        print(comparisonUpdateMessage)

    def compare_products(self):
        if len(self.comparisonTable) < 2:
            print("Add more products to compare.")
            return

        comparison_data = []
        for product in self.comparisonTable:
            product_data = ProductSchema.dump(product)
            comparison_data.append(product_data)

        return comparison_data
```