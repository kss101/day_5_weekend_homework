# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name( pet_shop ):
    pet_shop_name = pet_shop["name"]
    return pet_shop_name

def get_total_cash( pet_shop ):
    total_cash = pet_shop["admin"]["total_cash"]
    return total_cash

def add_or_remove_cash( pet_shop, cash_amount ):
    current_total_cash = get_total_cash( pet_shop )
    new_total_cash = current_total_cash + cash_amount
    pet_shop["admin"]["total_cash"] = new_total_cash

