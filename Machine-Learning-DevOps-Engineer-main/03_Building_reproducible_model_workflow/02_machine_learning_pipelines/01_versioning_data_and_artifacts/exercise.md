# Exercise: Versioning Data & Artifacts

In this exercise you will write a script that uploads an artifact to Weights & Biases.

## Set-up
To ensure you can complete the course exercises, make sure you have done the following (see also the introductory lesson for more extensive set-up instructions):

* Make sure you have conda(opens in a new tab) installed locally
* Install MLflow(opens in a new tab)
* Create a free account on Weights & Biases(opens in a new tab). You will also want to install the related CLI tool with Python(opens in a new tab). 
 
Lastly, clone the course exercise repository(opens in a new tab), which contains code for each exercise and related solution. This link will be provided again later in case you need it.

## Steps
1. Modify the script upload_artifact.py. This script receives the following parameters:
    * input_file: the path to an input file that will be uploaded as an artifact
    * artifact_name: the name to be used for the artifact
    * artifact_type: the type of the artifact
    * artifact_desc: a description of the artifact Inside the script, you will find instructions about what to do.

2. Run the script using as input_file the path to the provided zen.txt file, and fill the other parameters reasonably. For example:
```
python upload_artifact.py --input_file zen.txt \
              --artifact_name zen_of_python \
              --artifact_type text_file \
              --artifact_description "20 aphorisms about writing good python code"
```

This artifact will contain the Zen of Python (19 aphorisms about designing Python code), that you can also find by simply writing import this in a python script or terminal.

1. Go to W&B and check that the artifact exists at version v0
2. Open the file zen.txt and change something (anything works)
3. Re-run the script, then go to W&B and check that now the artifact has a version v1 containing the modified version. Notice now how the latest tag has moved to v1.
4. Re-run again the script without changing the file, and then check that W&B recognizes that the artifact did not change and it does NOT create a v2
5. Modify the script use_artifact.py. Instructions are contained within the file.
6. Run the script:

`python use_artifact.py --artifact_name exercise_1/zen_of_python:v1`

You will see the content of the artifact printed on the screen. Play with the versions and check that v0 and v1 differ.

7. Go to W&B, in the Artifacts section, select the artifact exercise_1/zen_of_python and look at the Graph view. You will see your first very simple pipeline.