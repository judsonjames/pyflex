# pyflex

## How to Run
- Clone Repository
  ```bash
  # This repository uses a submodule called pytils, so the clone needs
  # to be recursive
  git clone --recurse-submodules https://github.com/judsonjames/pyflex
  ```
- Ensure that you have Pipenv and Python3.7 installed on your machine
  ```bash
  # Installs pipenv to your Pip
  pip3 install pipenv

  # Creates a virtual environment for your machine and install needed packages
  pipenv lock
  pipenv sync

  # Execute this program
  pipenv run python3 main.py <pyflex_file>
  
  # Execute this program
  pipenv run python3 generated_code.py <input_files>
  ```
