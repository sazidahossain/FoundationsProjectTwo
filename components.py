# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        if product not in self.products:
            self.products.append(product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        for i in self.products:
            print ("Product Name: "+i.name+"\nDescription: "+i.description+"\nPrice: "+str((i.price))+"\n")


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name=name
        self.description=description
        self.price=price


    def __str__(self):
        # your code goes here!
        return str(self.name, self.description, self.price)




class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here!
        self.cartprod=[]

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.cartprod.append(product)


    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for m in self.cartprod:
            total = total+m.price
        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        for i in self.cartprod:
            print ("Product Name: "+i.name+"\nDescription: "+i.description+"\nPrice: "+str(i.price)+"\n")

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        print("Your total price is: " + str(self.get_total_price()) + " KWD")
