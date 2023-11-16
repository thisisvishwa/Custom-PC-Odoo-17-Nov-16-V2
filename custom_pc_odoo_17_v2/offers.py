```python
from datetime import datetime
from .database_management import DatabaseManager
from .product_comparison import ProductComparison

class Offer:
    def __init__(self, offer_id, product_ids, discount, start_date, end_date):
        self.offer_id = offer_id
        self.product_ids = product_ids
        self.discount = discount
        self.start_date = start_date
        self.end_date = end_date

    def is_valid(self):
        current_date = datetime.now()
        return self.start_date <= current_date <= self.end_date

class OfferManager:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.product_comparison = ProductComparison()

    def get_offers(self):
        offers_data = self.db_manager.get_data('offers')
        offers = [Offer(**offer) for offer in offers_data]
        return offers

    def apply_offer(self, offer_id, product_ids):
        offers = self.get_offers()
        valid_offer = next((offer for offer in offers if offer.offer_id == offer_id and offer.is_valid()), None)
        if valid_offer:
            product_comparison = self.product_comparison.compare_products(product_ids)
            total_price = product_comparison.get_total_price()
            discount_price = total_price * (valid_offer.discount / 100)
            return total_price - discount_price
        else:
            return None

    def get_bundle_offers(self, product_ids):
        offers = self.get_offers()
        bundle_offers = [offer for offer in offers if set(offer.product_ids).issubset(set(product_ids)) and offer.is_valid()]
        return bundle_offers
```