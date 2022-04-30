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
        'cm', 'inches', 'inch', 'slc', 'sq', 'liter', 'liters', 'squeeze', 'clv', 'gm', 'pkt', 'cansof', 'scant', 
        'kilograms', 'cap', 'caps', 'gr', 'pk', 'squeeze', 'squeezes', 'handful', 'handfuls', 
        'pt', 'ltr', 'bowl', 'ct', 'glass', 'half glass', 'sets', 'pcs', 'pch', 'tspn', 'fl', 'env', 'pk', 'qts', 'tps', 
        'lb.', 'lbs.', 'tbs.', 'oz.', 'tsp.', 'c.', 'tbsp.', 'pc', 'bit', 'sqr', 'tab', 'bot', 'gm', 'slc', 
        'ozs', 'sol', 'lt', 'tbp', 'stk', 'pce', 'veg', 'wedge', 'b', 'pen', 'ea', 'psc', 'u', 'dsh', 'l', 'ts',
        'a', 'grn', 'spg', 'bow', 'fu', 'th', 't', 'twp', 'pd', 'shot', 'kl', 'pks', 'mr', 'mrs', 'ms', 'cl', 'tb', 'tbl', 'k',
        'pcz', 't.s', 'dz.', 'dz', 'red', 'yellow', 'orange', 'green', 'purple', 'pink', 'blue', 'gray', 'black', 'white']

    size = ['large', 'small', 'medium', 'whole', 'sm.', 'lrg', 'inchlong', 'med', 'sm', 'lg', 'lg.', 'whl', 'size', 'big', 'md.', 'md', 
    'med.']

    process = ['quartered', 'chilled', 'chopped', 'cubed',  'boiling', 'thin', 'pounded', 'heart-shaped', 
    'hulled', 'roasted', 'chopped', 'shredded', 'diced', 'crushed', 'smashed', 'divided', 'packed', 'diced', 
    'grated', 'grate', 'seeded', 'grnd', 'minced', 'mince', 'mashed', 'devined', 'peeled', 'peel', 'devine', 
    'drained', 'drain', 'sliced', 'cube', 'ground', 'wedge', 'rolled', 'cored', 'beaten', 'strips', 'granulated', 
    'snip', 'snipped', 'coursely', 'thinly', 'frzn', 'imported', 'cold', 'boiled', 'crumbly', 'sliced']

    miscellaneous = ['for', 'thru', 'firmly', 'finely', 'fresh', 'optional', 'garnishing', 'garnish', 
    'of', 'freshly', 'ready', 'a', 'good', 'cracking', 'in', 'few', 'to serve', 'topping', 'frying', 'extra', 'slightly',
    'at room temperature', 'copyright', 'television', 'food', 'network', 'each', 'to', 'such', 'as', 'as needed', 'taste', 'additional',
    'storebought', 'deep', 'frying', 'individual', 'extra', 'to', 
    'per', 'serving', 'possibly', 'plump', 'slim', 'sheet of reynolds wrap heavy duty aluminum foil', 'thick', 
    'flat', 'beater', 'dough hook', 'by inch  baking pan', 'baking stone', 'topping', 'matchstick', 'quality', 'very', 
    'see', 'enough', 'spoon', 'use', 'much', 'you', 'like', 'authentic', 'store', 'bought', 'about', 'by', 
    'your', 'favorite', 'decorative', 'mason', 'lightly', 'regular', 'if', 'available', 'required', 'safeway', 'taste', 
    'plus' ,'any', 'choice', 'best', 'other', 'empty', 'sterilized', 'glass', 'hand', 'equal', 'into', 'mm', 'less', 'more',
    'if', 'needed', 'roughly', 'fine', 'using', 'own', 'taste', 'by', 'wax', 'paper', 'generous', 'any', 'you\'ll', 'need', 
    'at', 'least', 'either', 'just', 'meaure', 'total', 'simply', 'etc', 'an', 'raw']
    
    
    tokens_new = []
    token_units = []
    for t in tokens:
        t = t.strip()
        if t not in size and t not in process and t not in miscellaneous:
            tokens_new.append(t)
        if t in units:
            token_units.append(t)

    ingredient = ' '.join(tokens_new)

    ingredient_wo_unit_and_amount = ' '.join(tokens_new)
    for unit in token_units:    
        ingredient_wo_unit_and_amount = ingredient_wo_unit_and_amount.replace(unit, '')
    ingredient_wo_unit_and_amount = re.sub('[0-9 .\/-]+', '', ingredient_wo_unit_and_amount)
    if ingredient_wo_unit_and_amount == '':
        return ''

    # remove everything after first period 
    ingredient_split = ingredient.split('.')
    ingredient_split = list(filter(len, ingredient_split))
    if len(ingredient_split) == 0:
        return ''
    if len(ingredient_split) == 1:
        ingredient = ingredient_split[0]
    else:
        ingredient = [ingredient_split[0]]
        for i, split in enumerate(ingredient_split[1:], 1):
            # if the last split ends with a unit meaning it split a unit ending with a period ex: lbs.
            # print(original_string, ingredient_split, ingredient_split[i-1])
            if ingredient_split[i-1] != ' ' and \
                (re.sub('[^a-zA-Z]+', '', ingredient_split[i-1].split()[-1]).strip() in units \
                or len(re.sub('[^a-zA-Z]+', '', ingredient_split[i-1].split()[-1])) == 0):
                ingredient.append(split)
        ingredient = '.'.join(ingredient)
    # remove everything after first asterisk 
    ingredient = ingredient.split('*')[0]
    # remove everything after first semicolon 
    ingredient = ingredient.split(';')[0]
    # remove everything after first comma
    # ingredient = ingredient.split(',')[0].strip()
    ingredient_split = ingredient.split(',')
    ingredient_split = list(filter(len, ingredient_split))
    if len(ingredient_split) == 0:
        return ''
    if len(ingredient_split) == 1:
        ingredient = ingredient_split[0]
    else:
        ingredient = [ingredient_split[0]]
        for i, split in enumerate(ingredient_split[1:], 1):
            # if the last split ends with a unit meaning it split a unit ending with a period ex: c,
            # print(original_string, ingredient_split, ingredient_split[i-1])
            if ingredient_split[i-1] != ' ' and (re.sub('[^a-zA-Z]+', '', ingredient_split[i-1].split()[-1]).strip() in units or len(re.sub('[^a-zA-Z]+', '', ingredient_split[i-1].split()[-1])) == 0):
                ingredient.append(split)
        ingredient = ','.join(ingredient)


    return ingredient.strip()
    
def cleanup_ingredient(ingredient):
    original_ingredient = ingredient.lower()

    # gets rid of parentheses and anything in parentheses
    ingredient = "".join(re.split("\(|\)|\[|\]", ingredient)[::2]) 
    if len(ingredient) == 0:
        return ''

    if ingredient.strip().startswith('*'):
        return ''
    

    # replace number words with numbers
    ingredient_list = []
    for word in ingredient.split():
        try:
            ingredient_list.append(str(w2n.word_to_num(word)))
        except ValueError:
            ingredient_list.append(word)
    
    ingredient = ' '.join(ingredient_list)

    # gets rid of non alpha characters and units
    ingredient = replace_units(re.sub('[^0-9a-zA-Z\'&.*;,]+', ' ', ingredient.lower()).strip(), original_ingredient)

    return ingredient


def cleanup_instruction(instruction):
    return "".join(re.split("\(|\)|\[|\]", instruction)[::2])



