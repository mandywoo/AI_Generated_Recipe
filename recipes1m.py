import ijson

import csv
# with open(<path to output_csv>, "wb") as csv_file:
#         writer = csv.writer(csv_file, delimiter=',')
#         for line in data:
#             writer.writerow(line)

with open('recipe1M_layers/layer1.json', "r") as f, open('recipes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['id','title','ingredients','instructions'])

    for record in ijson.items(f, "item"):
        recipe_id = record['id']
        title = record['title']
        ingredients_lis = record['ingredients'] # list of ingredients [[{'text': '6 ounces penne'}, ...]
        instructions_lis = record['instructions']   # list of steps [{'text': 'Preheat the oven to 350 F. Butter or oil an 8-inch baking dish.'}, {'text': ...]

        ingredients = 'Ingredients: '
        for i, ingredient_dict in enumerate(ingredients_lis, 1):
            ingredient = ingredient_dict['text']
            ingredient_str = str(i) + '. ' + ingredient + ' '
            ingredients += ingredient_str
        
        # print(ingredients)


        instructions = 'Instructions: '
        for i, instructions_dict in enumerate(instructions_lis, 1):
            instruction = instructions_dict['text']
            instruction_str = str(i) + '. ' + instruction + ' '
            instructions += instruction_str

        # print(instructions)

        line = [recipe_id, title, ingredients, instructions]
        writer.writerow(line)

        print(i)
        # break


# with open('recipes.csv', 'r') as csv_file:
#     for line in csv_file:
#         print(line)