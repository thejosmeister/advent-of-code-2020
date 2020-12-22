class Food:
    def __init__(self, ingredients: str, allergens: str):
        self.ingredients = ingredients.split(' ')
        self.allergens = allergens.split(', ')


list_of_foods = []

f = open("day21input.txt", "r")
for file_line in f:
    list_of_foods.append(Food(file_line.rstrip().split(' (')[0], file_line.rstrip().split('(contains ')[1].split(')')[0]))
f.close()

# Create a set of allergens
allergens = set([allergen for allergens in [f.allergens for f in list_of_foods] for allergen in allergens])
ingredients = set([ingredient for ingredients in [f.ingredients for f in list_of_foods] for ingredient in ingredients])

associated_with_allergen = {}
allergen_to_food = {}

for al in allergens:
    foods_present_all_times_allergen_is_listed = []
    first_time = 0
    for food in list_of_foods:
        if al in food.allergens:
            if first_time == 0:
                foods_present_all_times_allergen_is_listed = food.ingredients
                first_time = 1
            else:
                foods_present_all_times_allergen_is_listed = list(set(food.ingredients) & set(foods_present_all_times_allergen_is_listed))

    associated_with_allergen[al] = foods_present_all_times_allergen_is_listed

print(associated_with_allergen)

i = 0
while i < 10:
    ingreds_to_remove = []
    for al in allergens:
        if len(associated_with_allergen[al]) == 1:
            allergen_to_food[al] = associated_with_allergen[al][0]
            ingreds_to_remove.append(associated_with_allergen[al][0])

    for al in allergens:
        for ingred_to_remove in ingreds_to_remove:
            if ingred_to_remove in associated_with_allergen[al]:
                associated_with_allergen[al].remove(ingred_to_remove)

    i += 1

print(allergen_to_food)

final_list = list(ingredients)

for al in allergens:
    final_list.remove(allergen_to_food[al])

out = 0

for ing in final_list:
    for food in list_of_foods:
        out += food.ingredients.count(ing)

print(out)

sortednames =sorted(allergen_to_food.keys(), key=lambda x:x.lower())

a_list = []
for key in sortednames:
    a_list.append(allergen_to_food[key])

print(','.join(a_list))
