import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('ingredient_recipe_dict.pkl', 'rb') as handle1, open('unique_ingredients_set.pkl', 'rb') as handle2:
    ingredient_recipe_dict = pickle.load(handle1)
    unique_ingredients_set = pickle.load(handle2)

    print(ingredient_recipe_dict['salt'])
    print(len(unique_ingredients_set))

    # word cloud
    ingredient_text = ' '.join(unique_ingredients_set)
    word_cloud = WordCloud(collations=False, background_color='white').generate(ingredient_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()