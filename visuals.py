import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open('ingredient_recipe_dict.pkl', 'rb') as handle:
    ingredient_recipe_dict = pickle.load(handle)

    print(ingredient_recipe_dict['salt'])

    # word cloud
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(ingredient_recipe_dict)
    plt.figure(figsize=(18,12), frameon=False)
    plt.imshow(wordcloud)
    plt.savefig('foo.png')
