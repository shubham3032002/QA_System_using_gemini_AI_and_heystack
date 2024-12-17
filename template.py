import os
from pathlib import Path

project_name ="QA_system"

file_list =[
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py"
    f"{project_name}/ingestion.py",
    f"/{project_name}/retrivelangenerator.py",
    f"{project_name}/utils.py",
    "data/",
    "notebook/research.ipynb",
    "requirements.txt",
    "README.md",
    "setup.py"
    
]


for filepath in file_list:
    filepath =Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if( not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath, "w") as f:
            pass
        
    else:
        print(f"file path:{filepath} already exists")    
            