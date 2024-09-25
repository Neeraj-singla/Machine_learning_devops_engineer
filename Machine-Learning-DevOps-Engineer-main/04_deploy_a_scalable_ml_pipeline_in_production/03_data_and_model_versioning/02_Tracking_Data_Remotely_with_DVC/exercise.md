In this exercise we will track data remotely using Google Drive.

## Set up
Use the same folder with DVC and Git from the previous exercise. Additionally you need to install the needed dependencies for using DVC with Google Drive: `conda install -c conda-forge dvc-gdrive`

## Create Remote
Create a folder in Google Drive and get its unique identifier, e.g. if the URL is https://drive.google.com/drive/u/0/folders/0AIac4JZqHhKmUk9PDA(opens in a new tab) than the unique identifier is 0AIac4JZqHhKmUk9PDA.

## Track files in DVC
Add the Google Drive folder as a remote and push the csv of identifiers from the previous demo. On your first push you'll need to authenticate with Google Drive.

# Pipelines with DVC

Since version 2.0, DVC has used a new command line to run pipelines(opens in a new tab) https://dvc.org/doc/user-guide/pipelines/running-pipelines. Instead of using `dvc run`, we now use `dvc exp run`.

Despite the name, DVC is more than just a way to version control data. DVC provides functionality to define pipelines.

To create pipelines, use `dvc exp run` to create stages. In each stage, you can define dependencies,/inputs, and outputs and specify the run command. By specifying the output of one stage as the input of another stage, it creates a directed acyclic graph (DAG). This can create a comprehensive pipeline that takes us from raw data to a fully trained machine-learning model.

An example of a `dvc exp run` command: we specify a name, a parameter, two dependencies (the code we intend to run as well as some data), the output, and then give the final command.

```bash
dvc exp run -n clean_data \
            -p param \
            -d clean.py -d data/data.csv \
            -o data/clean_data.csv \
            python clean.py data/data.csv
```

-n specifies the stage name (as defined in the dvc.yaml)
-p specifies the parameters (as defined in the params.yaml)
-d provides the required files for this stage to run
-o specifies the output directory when the stage is completed

The parameters we define get stored in param.yaml and the specification of the pipeline is stored in dvc.yaml Both can be version-controlled using Git, thus enabling reproducibility of current and past results.

## Further Reading
DVC documentation on creating pipelines(opens in a new tab) https://dvc.org/doc/start/data-pipelines and on running pipelines(opens in a new tab) https://dvc.org/doc/command-reference/run.