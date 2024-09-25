# Introduction

In this lesson we will review git and then delve into Data Version Control (DVC) and the concepts of data provenance.

DVC provides us a way to easily store and track both our data and models, even when they go beyond the size limits of a typical code repositories. We will also learn DVC's functionality for creating pipelines and tracking experiments.

* Data Provenance
* Review of Git
* Data Version Control (DVC)
* Remote Storage with DVC
* Pipelines with DVC
* Experiment Tracking with DVC

# Overview of Data Provenance

Data provenance is the complete origin, movement, and manipulation of data.

Origin can include not just where the data was retrieved from but also how the data set was generated, e.g. Census data retrieved from their API and that data was gathered by the American Community Survey in a particular year.

Movement may not always apply, but when it does it would encompass data that you or your team received from someone else. In other words, it's the origin plus any other jumps the data has made, e.g. data pulled from an API and moved to a company's S3 bucket for storage only to later be moved to HDFS for analysis.

Lastly is manipulation. Data may come to you completely raw, and then the manipulation will be any transforms or alterations you do on the data. Alternatively, data may come to you in a baked form and the various transformations will ideally be documented. A common example in NLP is documentation on how a data set is processed such as by changing the case or removing numbers or punctuation.

## Further Reading
Wikipedia's page on data lineage(opens in a new tab) https://en.wikipedia.org/wiki/Data_lineage provides a nice background on the above concepts.

# Use Cases of Data Provenance

Having well documented data provenance is generally useful to provide accountability for any product derived from the data. Just as a home-builder would want to know about the wood used to build a house, we want to know about the data used to build our models. Depending on the sector, this can become crucially important if there is regulation compliance or audits to be mindful of.

Furthermore, essentially no data is perfect. Understanding the origin and manipulation can help us understand the imperfections which can help in building models and in conveying efficacy and limitations to stakeholders.

## Optional Readings:
* List of Provenance Tools(opens in a new tab) https://projects.iq.harvard.edu/provenance-at-harvard/tools (Source: Provenance@Harvard)
* Provenance Use Cases(opens in a new tab) https://confluence.csiro.au/public/PROMS/provenance-use-cases (Source: CSIRO)

# Review of Git Commands

Git is software used to track changes to files, manage multiple versions of files/directories and using branches, and is well-suited for both solo and collaborative work. Git at its simplest is a CLI program but is often used in conjunction with platforms such as GitHub and GitLab which provide additional features such as project hosting, collaboration tools, GUIs, and CI/CD (see the next lesson for more).

Git has a rich and occasionally complex set of commands, but to get started we only need a few:

* `git init` to initiate a new Git repository.
* `git add` to add files to your repository.
* `git commit` once a file is added you must commit. Include a brief and descriptive commit message, collaborates and your past self will thank you.
* `git push` and `git pull` to send or receive changes from your remote repository.
* `git branch` and `git checkout` to create a new branch and to switch to it.

Lastly, `git status` can be a lifesaver when something invariably goes wrong.

## Further Reading
Git's documentation(opens in a new tab) https://git-scm.com/docs is thorough, but the vast majority of time GitHub's own cheat sheet(opens in a new tab) https://education.github.com/git-cheat-sheet-education.pdf/docs will cover your needs.

# Introduction to Data Version Control (DVC)

Data Version Control (DVC) is a complete solution for managing data, models, and the process of going from data to the model. All the while, it integrates nicely with tools that we already use (or intend to use) such as git and Continuous Integration/Continuous Deployment (CI/CD).

DVC's name is a bit of a misnomer in that it goes well beyond versioning data, and technically it does not even version data at all! Instead, it uses git for the actual versioning. DVC leverages a remote storage to hold the data but then tracks a record file using git (e.g. data.csv.dvc).

Beyond data versioning, DVC is a full experiment management system through its pipeline functionality. In DVC you can define a reusable pipeline (which is also version controlled). These pipelines can be used to build a reproducible model workflow and can be written so experiments can be logged and compared to help choose the best deployment model.

## Further Reading
The DVC docs(opens in a new tab) https://dvc.org/doc/start are very well written and a great resource for all your needs.

# Analogies Between Git and DVC Commands

DVC's commands are designed to be very similar to Git's.

Assuming you have installed `dvc` (see dvc installation page(opens in a new tab)), you can initialize a project using `git init` or `dvc init`.

To add code or data use `git add` or `dvc add`, respectively. Typically, after a `dvc add` it will then prompt you to `git commit` the corresponding `.dvc` file that has been generated. There is a `dvc commit` but it is not used in the same way as with `git commit`.

Lastly, there is `git push` and `git pull` and their equivalents of `dvc push` and `dvc pull`. DVC's push and pull are for uploading and downloading data from your remote store specified in in the dvc configuration, whereas git is for sending changes to your remote repository or bringing in any changes.

# Tracking Data with DVC

To get comfortable with DVC we will start by creating the seemingly paradoxical local remote. This is a remote store in that its not in our main development folder, but it resides elsewhere on our machine, hence local.

To create it, simply make the folder and tell DVC it is your remote:

```bash
mkdir /local/remote
dvc remote add -d localremote /local/remote
```

This will then create a change to DVC's configuration file located at .dvc/config that must be tracked using Git.

To send data to our local remote use `dvc push`. Since this remote is local it is trivial to then explore the structure of how DVC stores the data using your trusty command line tools.

To view available remotes use `dvc remote list`. If you want to make changes or rename a remote then use `dvc remote modify` and `dvc remote rename`, respectively.

## Tracking Data Demo

# Remote Storage with DVC

DVC can be used entirely locally, and that's a great way to learn it! But the true power of DVC is unlocked when you set up remote storage for your project.

Remote storage enables you to use the same data/models regardless of what machine you are working on and allows you to easily share data and models with others. In other words, it makes sharing code/models as easy as it is to `git clone` a repository.

DVC conveniently provides a multitude of ways to retrieve remotely tracked data/models. This enables one to pull in data while working outside of a DVC project, or to easily pull data into the environment where a model may be deployed such as Heroku.

## Further Reading
DVC's docs(opens in a new tab) https://dvc.org/doc/start/data-and-model-access on data and model access.

Go here(opens in a new tab) https://dvc.org/doc/command-reference/remote/add#supported-storage-types in the DVC docs to see a full list of supported storage types.

# Experiment Tracking with DVC

Now that we have a robust and reproducible pipeline built with DVC we are almost ready to use it to track experiments. But first we need to add metrics to our pipeline so that we have something to compare across experiments.

For example:

```bash
dvc exp run -n evaluate \
            -d validate.py -d model.pkl \
            -M validation.json \
            python validate.py model.pkl validation.json
```

where we have now included a metric in our stage. A similar process can be used to include plots as part of a stage.

We are now ready to set up experiments. Simply use `dvc exp run` and specify the relevant parameters to run an experiment. Experiments can be compared using `dvc exp diff` or `dvc exp show`. Each experiment is given a unique name that can be used for management and, ultimately, choosing which experiment to keep as we prepare our model for deployment. Don't forget to commit to the best experiment!

# Lesson Recap

In this lesson we covered the principles of data provenance and a few use cases. Then we moved full steam into versioning data and models using Data Version Control. We learned that DVC's commands are very analogous to those we already know from Git. DVC, despite the name, goes well beyond versioning our data. It can also be used to create reproducible pipelines and those pipelines can be used to create experiments that can be tracked so we can best determine the model for deployment.

* Data Provenance
* Review of Git
* Data Version Control (DVC)
* Remote Storage with DVC
* Pipelines with DVC
* Experiment Tracking with DVC

