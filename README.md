# ECE143-Project

The aim of this project is to analyse top Machine Learning Conferences and to arrive at conclusions like:-\
a. Most active institutes and authors in Machine Learning\ 
b. Conferences with most relevant publications in Machine Learning\ 
c. Trending topics of research in Machine Learning\ 
d. Provide a recommender system that can provide other closely related research papers for a given paper. 

The libraries used for the project are :- \
a. BeautifulSoup\
b. LXML\
c. Scholarly\
d. Standard third party python packages such as Numpy, Matplotlib, Pandas and Jupyter Notebook.

To run the project, first create a conda environment using the provided conda.yaml file. \
    $`conda env create -f conda.yaml`

Next, activate the conda environment\
    $`conda activate ece143`

Now run the dataset collection codes\
    $`python3 src/iclr.py`\
    $`python3 src/icml.py`\
    $`python3 src/nips.py`\
    $`python3 src/cvpr.py`

After the dataset collection is done, get the citations for the papers using \
    $`python3 src/citation.py`

Finally, we can run the visualisations.ipynb file for the analysis
