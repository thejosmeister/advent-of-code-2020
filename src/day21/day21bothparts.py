"""
Both parts of day 21

Unknowingly solved part 2 in my soln to part 1
"""


# Something to store our ingredient and allergen lists for each food.
class Food:
    def __init__(self, ingredients: str, allergens: str):
        self.ingredients = ingredients.split(' ')
        self.allergens = allergens.split(', ')


list_of_foods = []

f = open("day21input.txt", "r")
for file_line in f:
    list_of_foods.append(Food(file_line.rstrip().split(' (')[0], file_line.rstrip().split('(contains ')[1].split(')')[0]))
f.close()

# Create a set of allergens and ingredients
set_of_allergens = set([allergen for allergens in [f.allergens for f in list_of_foods] for allergen in allergens])
set_of_ingredients = set([ingredient for ingredients in [f.ingredients for f in list_of_foods] for ingredient in ingredients])

# The ingredients that appear everytime a certain allergen is listed.
always_present_with_allergen = {}

for al in set_of_allergens:
    foods_present_all_times_allergen_is_listed = []
    first_time = 0
    for food in list_of_foods:
        if al in food.allergens:
            if first_time == 0:
                foods_present_all_times_allergen_is_listed = food.ingredients
                first_time = 1
            else:
                foods_present_all_times_allergen_is_listed = list(set(food.ingredients) & set(foods_present_all_times_allergen_is_listed))

    always_present_with_allergen[al] = foods_present_all_times_allergen_is_listed

# Inspecting always_present_with_allergen we can see that one allergen only has one ingredient always present so we
# know that must be the ingredient containg the allergen. We create a map for the 'allergen, food' pairs and begin the
# process of elimination.

allergen_to_food = {}
i = 0
while i < 10:
    ingreds_to_remove = []
    for al in set_of_allergens:
        if len(always_present_with_allergen[al]) == 1:
            allergen_to_food[al] = always_present_with_allergen[al][0]
            ingreds_to_remove.append(always_present_with_allergen[al][0])

    for al in set_of_allergens:
        for ingred_to_remove in ingreds_to_remove:
            if ingred_to_remove in always_present_with_allergen[al]:
                always_present_with_allergen[al].remove(ingred_to_remove)

    i += 1

# Now we want to remove the ingredients in allergen_to_food from the set of all ingredients
inert_ingredients = list(set_of_ingredients)
for al in set_of_allergens:
    inert_ingredients.remove(allergen_to_food[al])

# Count how many times the 'inert' ingredients are present
out = 0
for ing in inert_ingredients:
    for food in list_of_foods:
        out += food.ingredients.count(ing)

print('Number of inert ingredients: ' + str(out))

# Need to sort the ingredients containing allergens alphabetically by allergen name.
sorted_allergen_names = sorted(allergen_to_food.keys(), key=lambda x:x.lower())

a_list = []
for key in sorted_allergen_names:
    a_list.append(allergen_to_food[key])

print('Part 2 output: ' + ','.join(a_list))
