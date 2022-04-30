import ijson
import csv
from clean_recipes1m_ver2 import cleanup_ingredient, cleanup_instruction
from collections import Counter
import re

# if these words are in ingredients, skip
skip_words = ['note', 'variation', 'equipment', 'equpment', 'foil', 'skillet', 'fishmonger', 'kitchen', 'i', 'ingredient',
'chef', 'ingredients', 'com', 'cook', 'recipe', 'saucepan', 'cast', 'iron', 'don\'t', 'dont', 'my', 'i\'ve', 'suggestion', 
'i\'m', 'they\'re', 'they', 'recipes']

with open('recipe1M_layers/layer1.json', "r") as f, open('recipes.csv', 'w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(['id','title','ingredients','instructions'])

    ingredient_lis = [] 

    for record in ijson.items(f, "item"):
        recipe_id = record['id']
        title = record['title']
        ingredients_lis = record['ingredients'] # list of ingredients [[{'text': '6 ounces penne'}, ...]
        instructions_lis = record['instructions']   # list of steps [{'text': 'Preheat the oven to 350 F. Butter or oil an 8-inch baking dish.'}, {'text': ...]

        # skip if recipe only has one ingredient (usually an error with scraping and they combine all ingredients into one)
        if len(ingredients_lis)==1: continue

        ingredients = 'Ingredients: '
        ingredient_num = 1
        for ingredient_dict in ingredients_lis:
            ingredient = ingredient_dict['text']

            orig_ingredient = ingredient_dict['text']
            ingredient = cleanup_ingredient(ingredient)
            # if '1 4 ' == ingredient:
            #     print(orig_ingredient)
            #     exit()
            # if '1 red' == ingredient:
            #     print(orig_ingredient)
            #     exit()

            # if the ingredient has 2 or less characters
            if len(ingredient) <= 2 or len(re.sub('[^a-zA-Z]+', '', ingredient)) < 3:
                continue

            # if ingredient has skip_word
            skip_word_exists = False
            for skip_word in skip_words:
                if skip_word in ingredient.lower().split():
                    skip_word_exists = True
                    break
            if skip_word_exists:
                continue

            ingredient_lis.append(ingredient)
            
            ingredient_str = str(ingredient_num) + '. ' + ingredient + ' '
            ingredients += ingredient_str

            ingredient_num += 1
      

        instructions = 'Instructions: '
        for i, instructions_dict in enumerate(instructions_lis, 1):
            instruction = instructions_dict['text']
            instruction = cleanup_instruction(instruction)
            if len(instruction) == 0 or 'note' in instruction.lower() or 'suggestion' in instruction.lower():
                continue

            instruction_str = str(i) + '. ' + instruction + ' '
            instructions += instruction_str


        line = [recipe_id, title, ingredients, instructions]
        writer.writerow(line)


    with open('ingredient_counts_ver2.txt', 'w+') as f:
        ingredient_counter = Counter(ingredient_lis)
        sorted_ingredient_counter = sorted(ingredient_counter.items(), key = lambda x:(x[1], -len(x[0])) , reverse=True)
        for ingredient, count in sorted_ingredient_counter:
            f.write(f'{ingredient}: {count}\n')

    with open('ingredient_len_ver2.txt', 'w+') as f:
        ingredient_counter = Counter(ingredient_lis)
        sorted_ingredient_counter = sorted(ingredient_counter.items(), key = lambda x:(len(x[0]), x[1]))
        for ingredient, count in sorted_ingredient_counter:
            f.write(f'{ingredient}: {count}\n')
       