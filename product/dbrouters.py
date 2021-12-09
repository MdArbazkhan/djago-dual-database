from .models import Product

# refer this code https://stackoverflow.com/questions/57676143/using-multiple-databases-with-django

class ProductDBRouter:
    def db_for_read (self, model, **hints):
        if (model == Product):
            # your model name as in settings.py/DATABASES
            return 'product'
        return None
    
    def db_for_write (self, model, **hints):
        if (model == Product):
            # your model name as in settings.py/DATABASES
            return 'product'
        return None