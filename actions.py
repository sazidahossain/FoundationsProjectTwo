# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.achoo.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for i in stores:
        print("-"+i.name)


def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for i in stores:
        if store_name.lower() == i.name.lower():
            return i
    else:
        return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    userinput = input("Pick a store by typing its name, or type \"checkout\" to pay your bills and say your goodbyes\n")


    if userinput.lower() == "checkout":
        return "checkout"

    elif get_store(userinput) != False:
        return get_store(userinput)

    else:
        print("No store with that name. Please try again.")
        return pick_store()



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to cart.
    """
    # your code goes here!
    print(picked_store.name+":")
    picked_store.print_products()
    checkx=[]
    userinputx=input("Pick the items you would like to add in your cart by typing the product name exactly as it was spelled above. Type \"back\" to go back to the main menu where you could checkout\n" )
    while(userinputx.lower() != "back"):
        for i in picked_store.products:
            checkx.append(i.name.lower())
            if userinputx.lower() == i.name.lower():
                cart.add_to_cart(i)
        if(userinputx.lower()) not in checkx:
            print("Product not available in store.")
            checkx=[]
        userinputx = input()

    return pick_store()

def shop():
    """
    The main shopping functionality
    """

    # your code goes here!
    cartx=Cart()
    l=pick_store()

    while l !="checkout":
        l=pick_products(cartx, l)

    if l=="checkout":
        cartx.checkout()








def thank_you():
    userinput=input("Confirm?(yes/no)\n")
    if(userinput.lower()=="yes"):
        print("Your order has been placed")
        print("Thank you for shopping with us at %s" % site_name)
    elif(userinput.lower()=="no"):
        print("Thank you for shopping with us at %s" % site_name)
    else:
        return thank_you()

