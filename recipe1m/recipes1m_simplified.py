import numpy as np
from collections import defaultdict
import pickle

with np.load('simplified-recipes-1M.npz', allow_pickle=True) as data, open('ingredient_recipe_dict.pkl', 'wb') as handle:
    
    recipes = data['recipes']
    ingredients = data['ingredients']

    ingredient_recipe_dict = defaultdict(int)

    print(ingredients[recipes[0]])
    # print(recipes[0])

    for recipe in recipes:
        # print(recipe)
        if len(recipe) == 0: continue
        ingredient_lis = ingredients[recipe]
        for ingredient in ingredient_lis:
            ingredient_recipe_dict[ingredient] += 1

    pickle.dump(ingredient_recipe_dict, handle)

    