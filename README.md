[![CI_CD](https://github.com/zachary-fennie/Rust-Project-2/actions/workflows/CI_CD.yml/badge.svg)](https://github.com/zachary-fennie/Rust-Project-2/actions/workflows/CI_CD.yml)

# Python and Rust Command Line Tool
## This project satisfies three assignments. First, a python script that connects to a SQLite database is packaged into a command line tool. Next, the Python command line tool is translated to Rust. Successful performance of the Rust translation will also satisfy all project 2 requirements. Additional materials include a user guide for installation and  a Continuous Integration/Continuous Deployment (CI/CD) pipeline that produces a Rust binary as an artifact. Github Copilot was used to assist with Rust errors as I lack the experience necessary to efficiently solve them. 


<img width="463" alt="Screenshot 2024-11-03 at 7 55 33 PM" src="https://github.com/user-attachments/assets/27361169-78fa-4bfa-8f6d-6a3187c8901f">


## Structure Python CLT
The `python_library` directory contains `my_tool.py` which contains all the necessary functions including `load` to transform and load local raw data from a `.csv` to a SQLite database, and `crud_query.py` to perform simple SQL operations. The files serve as a template to be customized for your own data project, and `main.py` is used for testing of the complete operations prior to conversion to a command line tool.

## Successful SQL Operations
<img width="1071" alt="Screenshot 2024-10-20 at 8 30 17 PM" src="https://github.com/user-attachments/assets/165c22af-3ddb-4b20-b66e-7adcd54a13a3">

### Core Files of the Repo:
* `python_library.py`
    - `transform_load.py`
    - `crud_query.py`
    - `requirements.txt`
    - `Makefile`
* `sqlite` rust folder
    - `library.rs`
    - `main.rs`
* `Cargo.toml`
* CI/CD pipeline
* `README.md`

Private Video Link: https://youtu.be/Ikr3W7MdwT0