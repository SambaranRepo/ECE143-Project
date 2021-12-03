import nbformat
import os
import copy

notebook_path = '../notebooks/'
files = os.listdir(notebook_path)


first_notebook = nbformat.read(notebook_path + files[0],4)
def read_ipynb(notebook_path):
    nb = nbformat.read(notebook_path, 4)
    return nb.cells
    


final_notebook = nbformat.v4.new_notebook(metadata=first_notebook.metadata)
temp = copy.deepcopy(notebook_path + files[0])

for file in files:
    if file == '.ipynb_checkpoints':
        continue
    final_notebook.cells = final_notebook.cells + read_ipynb(notebook_path + file)
    
nbformat.write(final_notebook, '../notebooks/final_notebook.ipynb')    
        