# ECE143 Project : Top Conferences' Paper Analysis

The aim of this project is to analyse top Machine Learning Conferences and to arrive at conclusions like:-\
a. Most active institutes and authors in Machine Learning <br /> 
b. Conferences with most relevant publications in Machine Learning <br /> 
c. Trending topics of research in Machine Learning <br />
d. Provide a recommender system that can provide other closely related research papers for a given paper. 

The libraries used for the project are :- \
a. BeautifulSoup\
b. LXML\
c. Scholarly\
d. wordcloud \
e. NLTK \
f. bar_chart_race \
g. Standard third party python packages such as Numpy, Matplotlib, Pandas and Jupyter Notebook.

<pre>
Repository Structure

├── data  
    ├── 2020_iclr_manual_data.csv
    ├── ICLR-2017-18-19-20-21.csv
    ├── ICLR-2017-18-19-21.csv 
    ├── cvpr_16-21.csv
    ├── cvpr_citations.csv
    ├── cvpr_data.csv
    ├── icml.csv
    ├── icml_affiliations.csv
    ├── icml_citations.csv
    ├── industry_keywords.csv
    ├── nips_2016-2020.csv
    ├── nips_citations.csv
        
├── notebooks
    ├── ipynb_checkpoints
        ├── analysis_cvpr-checkpoint.ipynb
        ├── final_notebook-checkpoint.ipynb
        ├── visualisation-checkpoint.ipynb
    ├── Final_Visualization_Notebook.ipynb
    
├── src
    ├── ipynb_checkpoints
        ├── visualisation-checkpoint.ipynb  
    ├── citation.py
    ├── cvpr.py   
    ├── iclr.py
    ├── icml.py 
    ├── nips.py
    ├── notebook_combine.py
    
├── Final_Presentation_Report.pdf
├── README.md
├── conda.yaml
├── geckodriver.log

</pre>

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

Finally, we use notebooks in `./notebooks` for the analysis
