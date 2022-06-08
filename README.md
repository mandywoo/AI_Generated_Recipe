# AI_Generated_Recipe

## How to Run Notebook
NOTE: We are using torch with Cuda in our notebook, so please make sure your environment has access to GPU !

Files Required:
- project.ipynb
- model.bin
- sample_data.csv : contains 100 sample data points.

It is highly recommended to run the notbook using [Our Colab Environment](https://drive.google.com/file/d/1PemuOf8HNM6vT_GSAkMHKehCeJ01a7nb/view?usp=sharing), this will save you the effort of downloading the following dependencies required to run our model.

How to Download Model.bin:

Option 1:
- make sure you have git lfs installed 
- clone the repo and you can use it directly


Instructions:
1. Run **all** the blocks under **"Set Up"**, this includes installing the dependencies at the top. Installing the required dependencies can take around ~1.5 min.
2. **In "Load Data" section, IF you are using your LOCAL ENVIRONMENT**: if you downloaded all the files in the same structure as it is in github, then you DO NOT need to update the file paths in the first block of "Load Data." Else, please update the paths according to the comments in the notebook. And **skip** the second block under "Load Data."
3. **In "Load Data" section, IF you are using GOOGLE COLAB**: please run the mount to mount your Google Drive by running the second block under "Load Data". You will need to update your file paths accordingly.
4. **In "Load Data" section**, Run all remaining blocks (skiping block 2 if you are using local environment instead of Colab)
5. **In "Load Model" section**, run the 1 block that is in this section, this can take around ~1 min to load in the trained model data.
6. **SKIP "Modeling Training" and "Model Saving"**
7. **In "Generation" section**, in the first block, the first line is commented out. If you wish to use a input from the original dataset, then please uncomment that first line and comment out the second line. 
8. **In "Generation" section**, If you want to try our own input, comment out the first line and uncomment the second line, then in the second line, please enter a list of ingredients in the following format : *Ingredients: 1. amount ingredient 2. amount ingredient ...*
9. **In "Generation" section**, after setting the input you want, run the first block.
10. **In "Generation" section**, there are subsections for different temperature values, you can run a specific subsection or all of the subsections.
11. **In "Evaluation" section**, if you wish to perfrom evaluation, in the first block, there is a temperature variable, it is set at 1.5 (optimal), you can change it if you wish. Note that it has to be a positive float. Them run all blocks under "Evaluation" section.

## Notebook Contents:
- recipe1m directory: Contains python code for gathering data from Recipes1M+ database and code from cleaning data
- Project.html: html output of model notebook that contains the output for every cell
- Project.ipynb: Final project notebook, contains dataloading, model training, response generation, and evalution
- comments_dfs.ipynb: Contains code preview reddit post comments
- reddit_comments.py: contains code to extract reddit posts and their comments
- reddit_pushshift_api.py: contains code to set up pushshift to pull data from reddit
- sample_data: contains 100 sample data points
- tables.sql: contains SQL code for generating our table
- visuals.py: contains code for word cloud visual
- model.bin: final GPT2 model data
