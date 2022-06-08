# AI_Generated_Recipe

## How to Run Notebook
Files Required:
- project.ipynb
- model.bin
- sample_data.csv : contains 100 sample data points.

Instructions:
1. Run **all** the blocks under **"Set Up"**, this includes installing the dependencies at the top. Installing the required dependencies can take around ~1.5 min.
2. **In "Load Data" section, IF you are using your LOCAL ENVIRONMENT**: if you downloaded all the files in the same structure as it is in github, then you DO NOT need to update the file paths in the first block of "Load Data." Else, please update the paths according to the comments in the notebook. And **skip** the second block under "Load Data."
3. **In "Load Data" section, IF you are using GOOGLE COLAB**: please run the mount to mount your Google Drive by running the second block under "Load Data". You will need to update your file paths accordingly.
4. **In "Load Data" section**, Run all remaining blocks (skiping block 2 if you are using local environment instead of Colab)
5. **In "Load Model" section**, run the 1 block that is in this section, this can take around ~1 min to load in the trained model data.
6. **SKIP "Modeling Training" and "Model Saving"
7. **In "Generation" section**, in the first block, the first line is commented out. If you wish to use a input from the original dataset, then please uncomment that first line and comment out the second line. If you want to try our own input, in the second line, please enter a list of ingredients in the following format : *Ingredients: 1. amount ingredient 2. amount ingredient ...*
8. **In "Generation" section**, after setting the input you want, run all blocks under "Generation" section.
9. **In "Evaluation" section**, if you wish to perfrom evaluation, run all blocks under "Evaluation" section.

