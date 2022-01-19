from item import Item

## child class which inherite the names from parent class
## to prevent duplicate attributes and methods, one way is to use key arguments
class Keyboard(Item):
    ## constructor: self:instance, name: instance attribute etc)
    def __init__(self, name:str, price:float, quantity=0):
        # call to super function to have access to all attributes/methods
        super().__init__(
            name,price,quantity
        )
        