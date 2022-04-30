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
        'cm', 'inches', 'inch', 'slc', 'sq', 'liter', 'liters', 'squeeze', 'clv', 'gm', 'pkt', 'sht', 'cansof', 'scant', 'kilograms', 'cap', 'caps', 'gr', 'pk', 'squeeze', 'squeezes', 'handful', 'handfuls', 
        'pt', 'ltr', 'bowl', 'ct', 'glass', 'half glass', 'sets', 'pcs', 'pch', 'tspn', 'fl', 'env', 'pk', 'qts', 'tps', 
        'lb.', 'lbs.', 'tbs.', 'oz.', 'tsp.', 'c.', 'tbsp.']

    size = ['large', 'small', 'medium', 'whole', 'sm.', 'lrg', 'inchlong', 'med', 'sm', 'lg', 'lg.', 'whl', 'size', 'big']

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
    'at', 'least', 'either', 'just', 'meaure', 'total', 'simply', 'etc', 'an']


    
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

        amount = re.findall('[0-9 .\/-]+', ingredient[:ingredient.index(token_unit)])
    else:
        token_unit = ''
        amount = re.findall('[0-9 .\/-]+', ingredient)

    if len(amount) == 0:
        amount = ''
    else:
        amount = amount[0].strip()
        if not has_numbers(amount):
            amount = ''


    ingredient = ' '.join(tokens_new)
    # if multiple token units in ingredient, get slice before second token unit
    if len(token_units) > 1 and token_units[1] in ingredient: 
        ingredient = ingredient[:ingredient.index(token_units[1])].strip()
  
    # remove everything after first period 
    ingredient = ingredient.split('.')[0]  
    # remove everything after first asterisk 
    ingredient = ingredient.split('*')[0]
    # remove everything after first semicolon 
    ingredient = ingredient.split(';')[0]
    # remove everything after first comma
    ingredient = ingredient.split(',')[0].strip()


    ingredient_lis = []
    if len(amount) != 0:
        ingredient_lis.append(amount)
    if len(token_unit) != 0:
        ingredient_lis.append(token_unit)
    if len(ingredient) == 0:
        final_ingredient = ''
    else:
        ingredient_lis.append(ingredient)
        final_ingredient = ' '.join(ingredient_lis).strip()
        
    return amount, token_unit, ingredient, final_ingredient
    
def cleanup_ingredient(ingredient):
    original_ingredient = ingredient.lower()

    # gets rid of parentheses and anything in parentheses
    ingredient = "".join(re.split("\(|\)|\[|\]", ingredient)[::2]) 
    if len(ingredient) == 0:
        return '', ''

    if ingredient.strip().startswith('*'):
        return '', ''
    

    # replace number words with numbers
    ingredient_list = []
    for word in ingredient.split():
        try:
            ingredient_list.append(str(w2n.word_to_num(word)))
        except ValueError:
            ingredient_list.append(word)
    
    ingredient = ' '.join(ingredient_list)

    # gets rid of non alpha characters and units
    amount, unit, ingredient, final_ingredient = replace_units(re.sub('[^a-zA-Z\'&.*;,]+', ' ', ingredient.lower()).strip(), original_ingredient)

    return ingredient, final_ingredient


def cleanup_instruction(instruction):
    return "".join(re.split("\(|\)|\[|\]", instruction)[::2])



