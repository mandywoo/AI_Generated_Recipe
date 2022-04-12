import json
from urllib.request import urlopen
import time
import sqlalchemy

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:tfialkow@localhost/AI_generated_recipes')


def getIngredientsAndInstructions(text):
    '''
    Gets both ingredients and instructions from OP. Only will grab them if they follow the formatting rules of the subreddit. They can be found here
        https://www.reddit.com/r/recipes/wiki/index#wiki_how_to_format_a_recipe_post
    Sadly, a lot of the comments are inconsistent but for the most part we can acquire some, just not nearly as much as ourr primary dataset. This function looks
    for the headers Instructions and Ingredients and pulls the information that follows.  
    '''
    ingredients_keyword = 'ingredients' 
    instructions_keyword = 'instructions' # Keywords to find in text

    text = text.encode('utf-8').decode('utf-8').lower() # Some users use 1/n with n being an integer for measurements and it needs to be decoded from unicode.

    before_ingredients, ingredients_keyword, after_ingredients = text.partition(ingredients_keyword) # Logic for parsing ingredients and instructions.
    ingredients, instructions_keyword, instructions = after_ingredients.partition(instructions_keyword)

    if ingredients == '' or instructions == '':
        return False # If the logic above doesn't find anything it returns '', so we fail and return False

    ingredients = 'Ingredients: ' + ingredients.strip() # Formatting..
    instructions = 'Instructions: ' + instructions.strip()
    
    return (ingredients, instructions)

def possibleRecipe(text):
    return ('ingredients' in text and 'instructions' in text)


if __name__ == "__main__":
    '''Get comments'''
    # supports s,m,h,d 
    time_frame = 'd'
    comment_lis = []
    ingredients_and_instructions = []
    recipes = 0
        
    for day in range(1, 3000, 50): # Looking over the span of 3000 days, pulling data from every 50 days as to not overwhelm pushshift
        before = str(day) + time_frame
        after = str(day + 50) + time_frame

        url = f'https://api.pushshift.io/reddit/search/comment/?subreddit=recipes&is_submitter=True&before={before}&after={after}&q=instructions&limit=1000' # q=instructions is looking for comments that mention instructions, these should be what we're after
                                                                                                                                                                # Its not case sensitive
        data = json.load(urlopen(url))['data'] # JSON parsing...
        
        for comment in data:
            if possibleRecipe(comment['body'].lower()):
                comment_lis.append(comment['body'])

        print(f'PULLING Before : {before} | After : {after} | Sleeping...')
        time.sleep(3)

    for comment in comment_lis:
        output = getIngredientsAndInstructions(comment) # See function
        
        if output == False:
            continue # See function getIngredientsAndInstructions()

        recipes += 1 # Keeping track of how many recipes pulled.

        print(f'Pulled output successfully. COUNT : {recipes}')
        ingredients_and_instructions.append(output) # Making list of "neatly" pulled ingredients and instructions

    # SQL Stuff...
    for recipe in ingredients_and_instructions:
        recipe_info = (recipe[0], recipe[1])
        print(recipe_info)
        engine.execute("INSERT INTO Reddit VALUES (%s, %s)", recipe_info)
    