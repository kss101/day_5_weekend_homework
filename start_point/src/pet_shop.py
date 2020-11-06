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
