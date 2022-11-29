### For start a project
`git clone https://github.com/sei666/test_csv.git`

### Install venv
`python -m venv env`
### Run venv
##### For Linux
`source env/bin/activate`
##### For Windows
`.\env\Scripts\activate`
### Install requirements
`pip install -r requirements.txt`
### Add 50 archives
`python generator_archives.py`
### Process archives and get csv
`python multi_csv_archive_handler.py`