from customer import Customer
from coffee import Coffee

class Order:
    orders = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price     
        Order.orders.append(self)

    @property
    def customer(self):
        return self._customer
    
    #ensuring it only accepts a customer instance
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError('customer must be an instance of Customer')
        else:
            self._customer = customer
            
    @property
    def coffee(self):
        return self._coffee
    
    #ensuring it only accepts a coffee instance
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError('coffee must be an instance of Coffee')
        else:
            self._coffee = coffee
            
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        #making the name immutable once initialized
        if self._name is not None:
            raise AttributeError("Price is immutable and cannot be changed.")
        if not isinstance(price, float):
            raise TypeError('Price mus be a float')
        else:
            if 1.0 <= price <= 10.0:
                self._price = price
                
    @classmethod
    def customer(cls):
        return cls.customer
    
    @classmethod
    def coffee(cls):
        return cls.coffee
    