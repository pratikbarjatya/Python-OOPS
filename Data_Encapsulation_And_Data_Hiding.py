class Product:

    def __init__(self):
        self.__product_name = ''
        self.__product_price = ''
        self.__product_model = ''

    def update_product(self, name, price, model):
        self.__product_name = name
        self.__product_model = model
        self.__product_price = price

    def show_product(self):
        print(f"Product Name : {self.__product_name}\nProduct Price : {self.__product_price}\nProduct Model : {self.__product_model}\n")


obj1 = Product()
obj1.update_product('Sony', 56000, 'SoNY123A56')
obj1.show_product()
print(f"after updating price value of the product by directly accessing the private memeber of the class through  \
    object of the class : \n")

# obj1.__product_price = 70000
obj1.show_product()
print(f"after updating the price of the product by accessing the private member through defined method in the class \
    through object of the class.\n")
obj1.update_product('Sony', 70000, 'SoNY123A56')
obj1.show_product()

print(obj1.__product_price)
print(obj1.__product_model)
print(obj1.__product_name)
