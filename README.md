# python-solution

python-solution is a CLI based python program that analyses data given in CSV format and generates the SQL and JSON files in an output folder. The files are called `output/sql_insert_queries.txt` and `output/sandbox.json`.

## Installation


```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py data/sandbox-installs.csv
```

## Running in Docker Container

* Build Docker container using the Dockerfile contained in the project
```bash
docker build . --no-cache
```
* The above command should output the docker image id, Now you can run the docker image using the following commands:
```bash
docker run --rm -it -v /tmp:/app/output 088cb78ace16 data/sandbox-installs.csv 
```
* Since, we are volume mounting `/tmp` of the host in `/app/output` of the docker container, it creates the  `/tmp/sql_insert_queries.txt` and `/tmp/sandbox.json`
