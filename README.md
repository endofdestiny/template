# TTT



### Project Structure

```
.
├── LICENSE
├── Makefile
├── README.md
├── config
│   ├── config.json
│   ├── env_check.py
│   └── setup.py
├── data
├── environment.yml
├── logs
├── notebooks
└── src
    ├── TTT
    └── tests
```


### Commands

make 
 - check  
    - Test conda environment is correctly setup
 - clean
    - Delete all compiled Python files
 - create
    - Create environment from environment.yml file
 - install
    - Install Python project locally
 - lint
    - Lint using flake8 and mypy
 - update
    - Update and export environment.yml
