#  empty dictionary
shoppingCart = {}

#  new product to the shopping cart
def addProduct():
    num_items = int(input("Enter the number of items to be added in the shopping cart: "))
    for i in range(num_items):
        productName = input("Enter an item: ")
        brandName = input("Enter the brand name: ")
        shoppingCart[productName] = brandName
    print("You added the following items to the cart:\n{}".format(shoppingCart))

#  to search  a product 
def searchProduct():
    productName = input("Enter the item to be searched: ")
    if productName in shoppingCart:
        print("{}: {}".format(productName, shoppingCart[productName]))
    else:
        print("No item exists with this name")

# To  delete a product 
def deleteProduct():
    productName = input("Enter the item to be deleted: ")
    if productName in shoppingCart:
        del shoppingCart[productName]
        print("The item has been deleted from the cart")
    else:
        print("No item exists with this name")
    
# Main 
while True:
    print("\nWELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")
    choice = input("Enter your choice: ")

    if choice == '1':
        addProduct()
    elif choice == '2':
        searchProduct()
    elif choice == '3':
        deleteProduct()
    elif choice == '4':
        break
    else:
        print("Wrong option entered.")
