from .contact import Contact

class Supplier(Contact):
    '''
    A Subclass of the Contact - it inherits the attributes and the methos of the Contact class 
    Acts just like the Contact but has an additional method order that accepts the Order object
    '''
    def order(self, order: str):
        print(f"If this were a real system we would send {order} order to {self.name}")