spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    for item in spicy_foods:
        return(item["name"])



def get_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item["heat_level"] > 5:
            return (item)


def print_spicy_foods(spicy_foods):
    for item in spicy_foods:       
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}")
        
#print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if cuisine == item["cuisine"]:
            print(item)
#get_spicy_food_by_cuisine(spicy_foods, "American")

def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item['heat_level'] > 5:
            print (f"{item['name']} ({item['cuisine']}) | Heat Level: { '🌶' * item['heat_level']}")
          
#print_spiciest_foods(spicy_foods)
def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num = []
    for item in spicy_foods:
        heat_level = item['heat_level'] 
        num.append(heat_level)
    for n in num:
        total_heat_level += n
    return(total_heat_level/len(spicy_foods))

    


#get_average_heat_level(spicy_foods)
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return (spicy_foods) 

#create_spicy_food(spicy_foods, 90)
