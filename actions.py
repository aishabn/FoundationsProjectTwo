# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "www.departmentstore.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for i in stores:
        print ("- %s" % i.name)
    

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for i in stores:
        if i.name.lower() == store_name.lower():
            return i
        
    return False



def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    print ('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.\n')
    name = input()

    while name.lower() not in stores:

        if name.lower() == "checkout":
            return "checkout"

        elif get_store(name):
            store = get_store(name)
            break

        else:
            print ("No store with that name. Please try again")
            name = input()

    return store



def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    inpt = input()

    while inpt.lower() != "back":

        for i in picked_store.products:
            if inpt.lower() == i.name.lower():
                cart.add_to_cart(i)
        inpt = input()

        if inpt.lower() == "back":
            pick_store()

    return inpt

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    var = ""
    while var.lower() != "checkout":
        var = ""
        store = pick_store()
        if store == "checkout":
            break

        store.print_products()

        print("Pick the items you'd like to add in your cart by typing the product name exactly as it was spelled above.")
        print('Type "back" to go back to the main menu where you can checkout.')

        var = pick_products(cart, store)

    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
