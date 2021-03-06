# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name( pet_shop ):
    pet_shop_name = pet_shop["name"]
    return pet_shop_name

def get_total_cash( pet_shop ):
    total_cash = pet_shop["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash( pet_shop, cash_amount ):
    current_cash_total = get_total_cash( pet_shop )
    new_cash_total = current_cash_total + cash_amount
    pet_shop["admin"]["total_cash"] = new_cash_total

def get_pets_sold( pet_shop ):
    total_pets_sold = pet_shop["admin"]["pets_sold"]
    return total_pets_sold

def increase_pets_sold( pet_shop, num_pets_sold):
    current_pet_total = get_pets_sold( pet_shop )
    new_pet_total = current_pet_total + num_pets_sold
    pet_shop["admin"]["pets_sold"] = new_pet_total

def get_stock_count( pet_shop ):
    stock_count = len(pet_shop["pets"])
    return stock_count

def get_pets_by_breed( pet_shop, pet_breed ):
    pets_by_breed = []
    for pet in pet_shop["pets"]:
        if pet.get("breed") == pet_breed:
            pets_by_breed.append(pet)
    return pets_by_breed

def find_pet_by_name( pet_shop, pet_name ):
    pet_by_name = {}
    for pet in pet_shop["pets"]:
        if pet.get("name") == pet_name:
            pet_by_name = pet
            return pet_by_name

def remove_pet_by_name( pet_shop, pet_name ):
    pet_exists = find_pet_by_name( pet_shop, pet_name )
    if pet_exists != None:
        pet_shop["pets"].remove(pet_exists)

def add_pet_to_stock( pet_shop, new_pet ):
    pet_shop["pets"].append(new_pet)

def get_customer_cash( customer ):
    customer_cash = customer.get("cash")
    return customer_cash

def remove_customer_cash( customer, cash_amount ):
    customer_cash = get_customer_cash( customer )
    updated_customer_cash = customer_cash - cash_amount
    customer["cash"] = updated_customer_cash

def get_customer_pet_count( customer ):
    cust_pet_count = len(customer["pets"])
    return cust_pet_count

def add_pet_to_customer( customer, new_pet ):
    customer["pets"].append(new_pet)

def customer_can_afford_pet( customer, new_pet ):
    customer_cash = get_customer_cash( customer )
    new_pet_price = new_pet["price"]
    if customer_cash - new_pet_price >= 0:
        return True
    else:
        return False

def sell_pet_to_customer( pet_shop, new_pet, customer ):
    if new_pet != None:                     # check to see if pet available to sell...
        cust_can_afford = customer_can_afford_pet( customer, new_pet ) # check to see if customer can afford pet...
        if cust_can_afford == True:         # If they can afford pet... sell it!     
            pet_price = new_pet["price"]
            remove_customer_cash( customer, pet_price )
            add_or_remove_cash( pet_shop, pet_price )
            add_pet_to_customer( customer, new_pet )
            increase_pets_sold( pet_shop, 1)
            remove_pet_by_name( pet_shop, new_pet )
    