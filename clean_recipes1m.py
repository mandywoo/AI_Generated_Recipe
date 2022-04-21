from string import ascii_lowercase
import re
from word2number import w2n

def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

def replace_units(processed_ingredient, ingredient):
    original_string = processed_ingredient
    
    tokens = processed_ingredient.split()
    units = ['ounce', 'ounces', 'cups', 'cup', 'teaspoon', 'tablespoon', 'tablespoons', 'teaspoons', 
        'c', 'g', 'v', 't', 'tbsp', 'kg', 'x', 'ml', 'lb', 'tbs', 'oz', 'pkg', 'tsp', 'grams', 'quarts', 'lbs', 'can', 
        'cans', 'pieces', 'piece', 'pound', 'pounds', 'gram', 'bunch', 'pinch', 'pkg.', 'pkg', 'quart', 'package', 
        'packages', 'bottle', 'cc', 'box', 'fillet', 'fillets', 'loaf', 'container', 'jar', 'slice', 'slices', 
        'sprigs', 'stick', 'tsps', 'pack', 'splash', 'knob', 'sht', 'sheets', 'sheet', 'gal', 'stk', 'doz', 'dash', 
        'bag', 'bags', 'drop', 'qt', 'bar', 'blades', 'blade', 'drops', 'containers', 'pint', 'loaf', 'loafs', 'tub', 
        'dashed', 'splash', 'splashes', 'ears', 'ear', 'pack', 'packs', 'pts', 'serving', 'servings', 'milliliters', 'ml',
        'pinch', 'pinches', 'head', 'bottles', 'slc', 'bunch', 'bunches', 'envelope', 'envelopes', 'gallon', 'packet',
        'sheet', 'sheets', 'drizzle', 'carton', 'head', 'link', 'links', 'sprg', 'tub', 'tubs', 'pouch', 'pouches', 'pack',
        'cm', 'inches', 'inch', 'slc', 'sq', 'liter', 'liters', 'squeeze', 'clv', 'gm', 'pkt', 'sht', 'envelopes',
        'envelope']

    size = ['large', 'small', 'medium', 'whole', 'sm.', 'lrg', 'inchlong', 'med', 'sm', 'lg', 'lg.', 'whl', 'size']

    process = ['quartered', 'chilled', 'chopped', 'cubed',  'boiling', 'thin', 'pounded', 'heart-shaped', 
    'hulled', 'roasted', 'chopped', 'shredded', 'diced', 'crushed', 'smashed', 'divided', 'packed', 'diced', 
    'grated', 'grate', 'seeded', 'grnd', 'minced', 'mince', 'mashed', 'devined', 'peeled', 'peel', 'devine', 
    'drained', 'drain', 'sliced', 'cube', 'ground', 'wedge', 'rolled', 'cored', 'beaten', 'strips', 'granulated', 
    'snip', 'snipped', 'coursely', 'thinly']

    miscellaneous = ['and', 'for', 'thru', 'firmly', 'finely', 'fresh', 'or', 'optional', 'garnishing', 'garnish', 
    'of', 'freshly', 'ready', 'a', 'good', 'cracking', 'in', 'few', 'to serve', 'topping', 'frying', 'extra', 'slightly',
    'at room temperature', 'copyright', 'television', 'food', 'network', 'each', 'to', 'such', 'as', 'as needed', 'taste'
    'special equpment kitchen string large  rimmed baking sheet large heavy roasting pan instantread thermometer',
    'additional required ingredients specified on the gravy and stuffing package instructions', 'additional',
    'storebought', 'deep frying', 'individual', 'all other ingredients are the same as recipe below', 'extra', 'to', 
    'per', 'serving', 'possibly', 'plump', 'slim', 'sheet of reynolds wrap heavy duty aluminum foil', 'thick', 
    'flat beater', 'dough hook', 'by inch  baking pan', 'baking stone', 'topping', 'matchstick', 'quality', 'very']



    with open('error.txt', 'a') as the_file:
    
        tokens_new = []
        token_units = []
        for t in tokens:
            t = t.strip()
            if t not in units and t not in size and t not in process and t not in miscellaneous:
                tokens_new.append(t)
            elif t in units:
                token_units.append(t)
        if len(token_units) > 0:
            token_unit = token_units[0] # get first unit in ingredients
            print(ingredient, token_unit)
            amount = re.findall('[0-9 \/-]+', ingredient[:ingredient.index(token_unit)])
            # amount = max(re.findall('[0-9 \/-]+', amount) , key = len).strip()  # get amount with longest len
        else:
            token_unit = ''
            amount = re.findall('[0-9 \/-]+', ingredient)

        if len(amount) == 0:
            amount = ''
        else:
            # amount = max(amount, key = len).strip()
            amount = amount[0].strip()
            if not has_numbers(amount):
                amount = ''
    
                
        print(original_string, '--->', ' '.join(tokens_new))
        the_file.write(original_string +  '--->' + ' '.join(tokens_new) + '\n')


        ingredient_lis = []
        if len(amount) != 0:
            ingredient_lis.append(amount)
        if len(token_unit) != 0:
            ingredient_lis.append(token_unit)

        ingredient_lis += tokens_new
        ingredient = ' '.join(ingredient_lis)
        
    return amount, token_unit, ingredient
    
def cleanup_ingredient(ingredient):
    # with open('error.txt', 'a+') as the_file:
    #     the_file.write('INGREDIENT:' + ingredient + '\n')

    original_ingredient = ingredient.lower()

    # gets rid of parentheses and anything in parentheses
    ingredient = "".join(re.split("\(|\)|\[|\]", ingredient)[::2]) 
    if len(ingredient) == 0:
        return ''

    # remove everything after first comma
    ingredient = ingredient.split(',')[0] 

    # replace number words with numbers
    ingredient_list = []
    for word in ingredient.split():
        try:
            ingredient_list.append(str(w2n.word_to_num(word)))
        except ValueError:
            ingredient_list.append(word)
    
    ingredient = ' '.join(ingredient_list)

    # gets rid of non alpha characters and units
    # ingredient = replace_units(''.join([char for char in ingredient.lower().strip() if char in ascii_lowercase + ' ']).strip())
    amount, unit, ingredient = replace_units(re.sub('[^a-zA-Z\'&]+', ' ', ingredient.lower()).strip(), original_ingredient)

    return ingredient

clean_ingredients = ["1/2 lb. (225 g) extra-lean ground beef King Sooper's 1 lb For $3.99 thru 02/09", 
"2 14 teaspoons dry yeast (Can decrease to 1/2t if baking next day.)",
"15 ounces, weight Canned Black Beans, Rinsed And Drained"]

clean_ingredients = ['1 egg - beaten']

print(re.findall('[0-9 \/-]+', '1  1/2 egg - beaten'))

# for ingredient in clean_ingredients:
#     clean_ingredient = cleanup_ingredient(ingredient)
#     print(clean_ingredient)

# ingredient = '1/2 hi-lo hi'
# # ingredient = replace_units(''.join([char for char in ingredient.lower().strip() if char in ascii_lowercase + ' ']).strip())
# ingredient = re.sub('[^a-zA-Z]+', ' ', ingredient)

# print(ingredient.strip())