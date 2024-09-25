Introduction to YAML
You can skip this section if you are already familiar with YAML.

YAML is a cross-language data format meant to store data structures in a human-readable way. It is similar to JSON, but it has fewer boilerplate characters and it is easier to read. YAML has many features (including references, multi-document files, and other advanced features). In this class however we will only use basic data structures such as lists and key-value mappings ("dictionaries" in Python language), so let's look at how to write those in YAML.

In YAML, just like in python, the document structure is an integral part of the definition of the data structures. Therefore, spaces are important and indentation is used to open and close data structures. Note that tabs are not allowed in YAML documents, only spaces are.

Let's look at how to write in YAML simple data structures.

Lists
A simple list
This is how you define a list in Python:

```python
my_list = ['a word', 'b', 1, 3.5]
```

And this is how the same is represented in a YAML file:

```yaml
- "a word"
- b
- 1
- 3.5
```

A nested list:
Of course, in Python you can define lists containing other lists:

```python
my_list = ['a word', [1, 2, 'a'], 1, 3.5]
```

This is how that data structure is represented in YAML:

```yaml
- a word
- - 1
    - 2
    - a
- 1
- 3.5
```

Note how the indentation at line 3 signifies the continuation of the list that started at line 2, and how going back to the upper indentation level signifies the end of the inner list and the continuation of the outer list.

A key-value mapping (a dictionary)
This is how you define a dictionary in Python:

```python
d = {'key_1': 1, 'key_2': "a string", 'another_key': 2.5}
```

In YAML, this is represented simply as:

```yaml
key_1: 1
key_2: a string
another_key: 2.5
```

(note that order might not be preserved when reading the file)

A nested dictionary
In Python you can of course define nested dictionaries, i.e., dictionaries containing other dictionaries:

```python
d = {
  "a": "a value",
  "b": {
    "c": 1.2,
    "d": 1,
    "e": "a string"
  },
  "c": 5
}
```

In YAML this is represented as:

```yaml
a: a value
b:
  c: 1.2
  d: 1
  e: a string
c: 5
```

Note that the quotes are optional in YAML, although they are usually a good idea if you are using characters beyond letters, numbers, and spaces.

Mixing dictionaries and lists
You can of course mix lists and dictionaries in Python:

```python
d = {
  "a": "a value",
  "b": {
    "c": 1.2,
    "d": 1,
    "e": "a string"
  },
  "c": [1, 2, "another string"]
}
```

Such a data structure is represented in YAML as:

```yaml
a: a value
b:
  c: 1.2
  d: 1
  e: a string
c:
  - 1
  - 2
  - another string
```

The YAML of conda.yml and MLproject
Let's now look back at the conda.yml file and the MLproject file. We can read these files using pyyaml, the python parser for YAML that can be installed with pip. For example, this conda.yml file:

```yaml
name: download_data
channels:
  - conda-forge
  - defaults
dependencies:
  - requests=2.24.0
  - pip=20.3.3
  - pip:
        - wandb==0.10.21
```

can be read in Python:

```python
import yaml

with open("conda.yml") as fp:
    d = yaml.safe_load(fp)

print(d)
```

which gives:

```python
{
    "name": "download_data",
    "channels": [
        "conda-forge",
        "defaults"
    ],
    "dependencies": [
        "requests=2.24.0",
        "pip=20.3.3",
        {
            "pip": [
                "wandb==0.10.21"
            ]
        }
    ]
}
```

and this MLproject:

```yaml
name: download_data
conda_env: conda.yml

entry_points:
  main:
    parameters:
      file_url:
        description: URL of the file to download
        type: uri
      artifact_name:
        description: Name for the W&B artifact that will be created
        type: str
      artifact_type:
        description: Type of the artifact to create
        type: str
        default: raw_data
      artifact_description:
        description: Description for the artifact
        type: str

    command: >-
      python download_data.py --file_url {file_url} \
                              --artifact_name {artifact_name} \
                              --artifact_type {artifact_type} \
                              --artifact_description {artifact_description}
```

can be read as:

```python
import yaml
with open("MLproject") as fp:
  d = yaml.safe_load(fp)
print(d)
```

which gives:

```
{
    "name": "download_data",
    "conda_env": "conda.yml",
    "entry_points": {
        "main": {
            "parameters": {
                "file_url": {
                    "description": "URL of the file to download",
                    "type": "uri"
                },
                "artifact_name": {
                    "description": "Name for the W&B artifact that will be created",
                    "type": "str"
                },
                "artifact_type": {
                    "description": "Type of the artifact to create",
                    "type": "str",
                    "default": "raw_data"
                },
                "artifact_description": {
                    "description": "Description for the artifact",
                    "type": "str"
                }
            },
            "command": "python download_data.py --file_url {file_url} 
                                                --artifact_name {artifact_name}
                                                --artifact_type {artifact_type} 
                                                --artifact_description {artifact_description}"
        }
    }
}
```