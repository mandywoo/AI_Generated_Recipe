import json
from urllib.request import urlopen

'''Get categories'''
developer_test_key = 1
url = 'https://www.themealdb.com/api/json/v1/{}/categories.php'.format(developer_test_key)
data = json.load(urlopen(url))

categories_lis = []
for category_info in data['categories']:
    categories_lis.append(category_info['strCategory'])

print(categories_lis)

'''Get meal ids'''
url = 'https://www.themealdb.com/api/json/v1/{}/filter.php?c='.format(developer_test_key)

meal_id_lis = []
for category in categories_lis:
    full_url = url + category
    data = json.load(urlopen(full_url))

    for meal_info in data['meals']:
        meal_id_lis.append(meal_info['idMeal'])
print(meal_id_lis)

'''Get meals'''
url = 'https://www.themealdb.com/api/json/v1/{}/lookup.php?i='.format(developer_test_key)

meal_lis = []
for meal_id in meal_id_lis:
    full_url = url + meal_id
    data = json.load(urlopen(full_url))

    meal_info =  data['meals'][0]
    meal_dict = {'instructions': meal_info['strInstructions'].replace('\r', '')}

    # there seems to only be 20 ingredients max
    ingredient_and_amounts_str = ''
    for i in range(1, 21):
        ingredient = meal_info['strIngredient' + str(i)]
        amount = meal_info['strMeasure' + str(i)]
        if ingredient and amount:
            ingredient_and_amounts_str += amount + ' ' + ingredient + '\n'
    
    meal_dict['ingredients'] = ingredient_and_amounts_str
    meal_lis.append(meal_dict)
print(meal_lis)
