# Musical notes

> You can see the **Project WorkFlow** here.

## Contents

 - [Project Goals](#goals)
 - [Musical notes theory](#musical-notes-theory)
 - [Start the project with Poetry](#init-poetry)
 - [Start the repository with the git tool](#init-git)
 - [Add .gitignore and .editorconfig](#gitignore-editorconfig)
 - [Add LICENSE.md](#license)
 - [Add Pytest and Pytest-Cov ("dev" group)](#pytest-cov)
 - [Add Taskipy](#taskipy)
 - [Add blue (PEP8: code formatter + analyze)](#blue)
 - [Add isort (reorder import library)](#isort)
 - [Add mkdocs-material, mkdocstrings and mkdocstrings-python ("doc" group)](#mkdocs)
 - [Start mkdocs settings (mkdocs new .)](#init-mkdocs)
 - [Start Pytest settings](#start-pytest)
 - [Testing Blue (PEP8: code formatter + analyze)](#testing-blue)
 - [Add tasks](#add-tasks)
 - [Planning and Implementing the scales.py](#planning-implementing-scale-py)
 - [Create a mkdocs to our scales.py function](#mkdocs-scales-py)
 - [Intro to AAA (3A or A3) tests](#intro-to-aaa)
 - [Add test for our function to work with lowercase notes](#test-lowercase-notes)
 - [Add test when pass note (argument) does not exist](#test-pass-note-does-not-exist)

---

<div id="goals"></div>

## Project Goals

To start, let's get started with the **Project Goals**.

> Help music student study ***Musical Theory***.

 - Assist (ajudar) in understanding musical scales.
 - Chord formation (formação de acordes).
 - Assist in the understanding of harmonic fields (campos harmônicos).
 - Help with harmonic progressions

---

<div id="musical-notes-theory"></div>

## Musical notes theory

To create this project we need to know what's Musical notes. For example:

|                |                   |                   |                       |                   |                     |                     |                     |
| -------------- | ----------------- |-------------------|-----------------------|-------------------|---------------------|---------------------|---------------------|
| **English**    | C                 | D                 | E                     | F                 | G                   | A                   | B                   |
| **Portuguese** | Dó e acorde de dó | Ré e acorde de ré | E - Mi e acorde de mi | Fá e acorde de fá | Sol e acorde de sol | Lá e acorde de lá   | Si e acorde de si   |

Between each note above we have some **"accidental" (sharp # / sustenidos )** notes:

|                |   |    |   |    |   |   |    |   |    |   |    |   |
| -------------- | --|----|---|----|---|---|----|---|----|---|----|---|
| **English**    | C | C# | D | D# | E | F | F# | G | G# | A | A# | B |

For example, see the clock analogy below:

![img](images/analogy01.png)  

> **Ok, we know the basics of musical notes, but what's a *"scale"*?**
> - [EN] - "Scales is a formula to find notes that combine between."
> - [PT] - "Escalas é uma fórmula para encontrar notas que combinam entre si."

For example, see the clock analogy below:

![img](images/analogy02.png)  

See that all notes listed above have a relation - That's, C (dó), D (ré), E (mí), F (fá), G (sol), A (lá), B (sí).

> **Ok, but and the space between these notes?**  
> These are `"intervals (intervalos)"`.

However, we have two types of intervals:

![img](images/analogy03.png)  

 - **TOM (ENG: Tone):**
   - Distance between two notes: C (dó), D (ré), E (mí), F (fá), G (sol), A (lá), B (sí).
 - **SEMITOM (ENG: Semitone):**
   - Distance between a note and a note sharp (#) or vice-versa.

---

<div id="init-poetry"></div>

## Start the project with Poetry

```
poetry new musical-notes
```

To use the environment use:

```
poetry shell
```

---

<div id="init-git"></div>

## Start the repository with the git tool

```
git init .
```

**NOTE**  
Now, let's create our repository on the cloud (GitHub):

```
gh repo create
```

**NOTE:**  
He will ask some questions to create the repository. Answer and create the repository.

---

<div id="gitignore-editorconfig"></div>

## Add .gitignore and .editorconfig

Now, let's add [.gitignore](../.gitignore) and [.editorconfig](../.editorconfig) to the project.

---

<div id="license"></div>

## Add LICENSE.md

Now, let's add a [LICENSE.md](../LICENSE.md) to the project.

---

<div id="pytest-cov"></div>

## Add Pytest and Pytest-Cov ("dev" group)

Now, let's add Pytest to the project:

```
poetry add --group dev pytest@latest pytest-cov@latest
```

**NOTE**  
See that we group the test libraries in the de "dev" group.

---

<div id="taskipy"></div>

## Add Taskipy

```
poetry add --group dev taskipy@latest
```

---

<div id="blue"></div>

## Add blue (PEP8: code formatter + analyze)

```
poetry add --group dev blue@latest
```

---

<div id="isort"></div>

## Adding isort (reorder import library)

```
poetry add --group dev isort@latest
```

---

<div id="mkdocs"></div>

## Add mkdocs-material, mkdocstrings and mkdocstrings-python ("doc" group)

```
poetry add --group doc mkdocs-material@latest mkdocstrings@latest mkdocstrings-python@latest
```

---

<div id="init-mkdocs"></div>

## Start mkdocs settings (mkdocs new .)

Now, let's start our mkdocs settings. For it, let's pass the path (root for us):

```
mkdocs new .
```

**OUTPUT:**  
```
INFO     -  Writing config file: ./mkdocs.yml
INFO     -  Writing initial docs: ./docs/index.md
```

To test we can se mkdocs serve:

```
mkdocs serve
```

**OUTPUT:**  
```
INFO     -  Building documentation...
INFO     -  Cleaning site directory
INFO     -  Documentation built in 0.04 seconds
INFO     -  [08:52:04] Watching paths for changes: 'docs', 'mkdocs.yml'
INFO     -  [08:52:04] Serving on http://127.0.0.1:8000/
```

> **NOTE:**  
> To test open the server address to test: **http://127.0.0.1:8000/**

Now, let's apply some settings. For it, open the generated [mkdocs.yml](../mkdocs.yml):

[mkdocs.yml](../mkdocs.yml)
```
site_name: Musical Notes
repo_url: https://github.com/drigols/musical-notes
repo_name: drigols/musical-notes
edit_uri: tree/master/docs

theme:
  name: material
  language: en
  logo: assets/logo.png
  favicon: assets/logo.png
  palette:
    primary: black

markdown_extensions:
  - attr_list # Allow apply styles ![](){width=xxx .center}.

extra_css:
  - stylesheets/extra.css
```

To edit the main content open the [index.md](../docs/index.md):

[index.md](../docs/index.md)
```
![project-logo](assets/logo.png){width=300 .center}
# Musical Notes
```

Now, let's see how to apply stylesheet on our docs:

[extra.css](../docs/stylesheets/extra.css)
```
.center {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
```

---

<div id="start-pytest"></div>

## Start Pytest settings

To settings our Pytest first we need to define it in [pyproject.toml](../pyproject.toml):

[pyproject.toml](../pyproject.toml)
```py
[tool.pytest.ini_options]
pythonpath = "."
addopts = "--doctest-modules"
```

---

<div id="testing-blue"></div>

## Testing Blue (PEP8: code formatter + analyze)

Imagine we have the following **Python** file:

[musical_notes/test.py](../musical_notes/test.py)
```
name = "Rodrigo"
```

 - **If we just run *"blue ."*, he will format the code automatically, we don't know what was modified**.
 - We can also use two different approaches to know what needs to change:
   - `blue --check .`
     - Tells you if you have any issues to fix, but not what they are.
   - `blue --check --diff .`
     - Tells you if you have any issues to fix, and what they are.

For example, if we run:

```
blue --check --diff .
```

**OUTPUT:**
```
--- musical_notes/test.py       2023-03-31 16:46:45.855618 +0000
+++ musical_notes/test.py       2023-03-31 16:52:29.974415 +0000
@@ -1 +1 @@
-name = "Rodrigo"
+name = 'Rodrigo'
would reformat musical_notes/test.py
```

Now, we just need to solve that.

---

<div id="add-tasks"></div>

## Add tasks

Now, let's add some tasks to the project:

[pyproject.toml](../pyproject.toml)
```python
[tool.taskipy.tasks]
lint = "blue --check --diff . && isort --check --diff ."
docs = "mkdocs serve"
pre_test = "task lint" # Pre test.
test = "pytest -s -x --cov=musical_notes -vv"
post_test = "coverage html" # Post test.
```

---

<div id="planning-implementing-scale-py"></div>

## Planning and Implementing the scales.py

Now, let's planning and implementing the [scale.py](../musical_notes/scale.py). Let's start from docstring and from it implement the function. For example, which parameter does the function have?

[scales.py](../musical_notes/scales.py)
```python
def scales():
    """
    >>> scales('C', 'major')
    """
    ...
```

**OUTPUT:**  
```
TypeError: scales() takes 0 positional arguments but 2 were given
```

> **NOTE:**  
> See that the function should have two parameters, but doesn't have any.

Ok, let's implement these parameters:

[scales.py](../musical_notes/scales.py)
```python
def scales(note, key):
    """
    >>> scales('C', 'major')
    """
    ...
```

**RUNG TASK:**  
```
task test
```

**OUTPUT:**  
```
1 passed in 0.11s
```

> **Ok, but what output should the function have?**

Let's, implement in the docstring an output example:

[scales.py](../musical_notes/scales.py)
```python
def scales(note, key):
    """
    >>> scales('C', 'major')
    {'notes': ['C, 'D', 'E', 'F', 'G', 'A', 'B'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    ...
```

**RUNG TASK:**  
```
task test
```

**OUTPUT:**  
```
>>> scales('C', 'major')
Expected:
    {'notes': ['C, 'D', 'E', 'F', 'G', 'A', 'B'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
Got nothing
```

Well, we have to implement this output now:

[scales.py](../musical_notes/scales.py)
```python
NOTES = 'C C# D D# E F F# G G# A A# B'.split()
ESCALES = {'major': (0, 2, 4, 5, 7, 9, 11)}


def scale(note: str, key: str) -> dict[str, list[str]]:
    """
    Generate a scale from a note and a tone (key).

    Parameters:
        note: The note that will be the tonic of the scale.
        key: Scale tone (key).

    Returns:
        A dictionary with the scale notes and degree. Inside of the dictionary, the key is a string (str) and a value is a list of strings.

    Examples:
        >>> scale('C', 'major')
        {'notes': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}

        >>> scale('a', 'major')
        {'notes': ['A', 'B', 'C#', 'D', 'E', 'F#', 'G#'], 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
    """
    note = note.upper()
    intervals = ESCALES[key]
    key_post = NOTES.index(note)
    temp = []

    for interval in intervals:
        note = (key_post + interval) % 12
        temp.append(NOTES[note])

    return {'notes': temp, 'key': ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']}
```

**RUN TASK:**  
```
task test
```

**OUTPUT:**  
```
1 passed in 0.10s
```

---

<div id="mkdocs-scales-py"></div>

## Create a mkdocs to our scales.py function

Now, let's create a mkdocs API to our [scales.py](../musical_notes/scales.py).

 - First create a folder in **docs/api**, next, create **scales.md**.

Inside [docs/api/scales.md](../docs/api/scales.md) add:

[docs/api/scales.md](../docs/api/scales.md)
```
::: scales
```

Now, let's add a plugin to our mkdocs settings:

[mkdocs.yml](../mkdocs.yml)
```python
plugins:
- mkdocstrings:
    handlers:
      python:
        paths: [musical_notes]
```

Finally, run **"task docs"** to testin.

---

<div id="intro-to-aaa"></div>

## Intro to AAA (3A or A3) tests

For our tests we will use AAA (3A or A3) Approach, which means:

 - **Arrange**
   - PT-BR = Arrumar
 - **Act**
   - PT-BR = Agir
 - **Assert**
   - PT-BR = Garantir

---

<div id="test-lowercase-notes"></div>

## Add test for our function to work with lowercase notes

Now, let's add a test to check if our **"scale"** function works with lowercase notes *(following AAA approach)*:

[test_scales.py](../tests/test_scales.py)
```python
def test_scale_must_work_with_lowercase_notes():
    # Arrange
    note = 'c'
    key = 'major'

    # Act
    result = scale(note, key)

    # Assert
    assert result
```

**RUN TASK:**  
```
task test
```

**OUTPUT:**  
```
2 passed in 0.11s
```

---

<div id="test-pass-note-does-not-exist"></div>

## Add test when pass note (argument) does not exist

Now, let's add a test to check when a invalid note is passed:

[scales.py](../musical_notes/scales.py)
```python
#.............

    """
    .....................

    Raises:
        ValueError: When passing a non-existent note.

    .....................
    """

    try:
        key_post = NOTES.index(note)
    except ValueError:
        raise ValueError(f'That note does not exist, try {NOTES}')

#............
```

[test_scales.py](../tests/test_scales.py)
```python
from pytest import raises

def test_scale_must_return_an_error_saying_that_the_note_not_exists():
    # Arrange
    note = 'X'
    key = 'major'
    error_message = f'That note does not exist, try {NOTES}'

    # Act
    with raises(ValueError) as error:
        scale(note, key)

    # Assert
    assert error_message == error.value.args[0]
```

**RUN TASK:**  
```
task test
```

**OUTPUT:**  
```
3 passed in 0.07s
```

---

Ro**drigo** **L**eite da **S**ilva - **drigols**

[](../)
```python

```

**RUN TASK:**  
```
task test
```

**OUTPUT:**  
```

```
