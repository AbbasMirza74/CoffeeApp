class Coffee:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Order:
    def __init__(self):
        self.items=[]
    def add_item(self,coffee):
        self.items.append(coffee)
        print(f"\nadded {coffee.name} to your order.")
    def total(self):
        return sum(item.price for item in self.items)
    def show_order(self):
        if not self.items:
            print("\nNo items ordered")
            return
        print("\nYour order:")
        for i,item in enumerate(self.items,1):
            print(f"{i}.{item.name} - ${item.price} ")
        print(f"Total: ${self.total()}")
    def checkout(self):
        if not self.items:
            print("\nyour cart is empty.")
            return 
        self.show_order()
        confirm=input("proceed to order ?(yes/no): ").strip().lower()
        if confirm=="yes":
            print("\norder confirmed thankyou.")
            self.items.clear()
        else:
            print("checkout cancelled.")
def main():
    menu=[
        Coffee("Espresso",2.5),
        Coffee("Latte",3.5),
        Coffee("Cappuccino",3.0),
        Coffee("Americano",2.0),
    ]
    order=Order()
    while True:
        print("\n--Coffee Menu--\n")
        for i,coffee in enumerate(menu,1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")
        choice=int(input("\nchoose an option:"))
        if choice in [1,2,3,4]:
            order.add_item(menu[choice-1])
        elif choice==5:
            order.show_order()
        elif choice==6:
            order.checkout()
        elif choice==7:
            print("\nThanks for visiting...")
            break
        else:
            print("Invalid choice try again..")
if __name__ == "__main__":
    main()


        
