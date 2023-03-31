# Musical notes

> You can see the **Project WorkFlow** here.

## Contents

 - [Project Goals](#goals)
 - [Musical notes theory](#musical-notes-theory)
 - [Init the project with Poetry](#init-poetry)
 - [Init the repository with the git tool](#init-git)
 - [Add .gitignore and .editorconfig](#gitignore-editorconfig)
 - [Add LICENSE.md](#license)
 - [Add Pytest and Pytest-Cov ("dev" group)](#pytest-cov)
 - [Add Taskipy](#taskipy)
 - [Add blue (PEP8: code formatter + analyze)](#blue)
 - [Add isort (reorder import library)](#isort)
 - [Add mkdocs-material, mkdocstrings and mkdocstrings-python ("doc" group)](#mkdocs)
 - [Init mkdocs settings (mkdocs new .)](#init-mkdocs)
 - [](#)
 - [](#)
 - [](#)
 - [](#)

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

## Init the project with Poetry

```
poetry new musical-notes
```

To use the environment use:

```
poetry shell
```

---

<div id="init-git"></div>

## Init the repository with the git tool

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

## Adding .gitignore and .editorconfig

Now, let's add [.gitignore](../.gitignore) and [.editorconfig](../.editorconfig) to the project.

---

<div id="license"></div>

## Adding LICENSE.md

Now, let's add a [LICENSE.md](../LICENSE.md) to the project.

---

<div id="pytest-cov"></div>

## Adding Pytest and Pytest-Cov ("dev" group)

Now, let's add Pytest to the project:

```
poetry add --group dev pytest@latest pytest-cov@latest
```

**NOTE**  
See that we group the test libraries in the de "dev" group.

---

<div id="taskipy"></div>

## Adding Taskipy

```
poetry add --group dev taskipy@latest
```

---

<div id="blue"></div>

## Adding blue (PEP8: code formatter + analyze)

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

## Adding mkdocs-material, mkdocstrings and mkdocstrings-python ("doc" group)

```
poetry add --group doc mkdocs-material@latest mkdocstrings@latest mkdocstrings-python@latest
```

---

<div id="init-mkdocs"></div>

## Init mkdocs settings (mkdocs new .)

Now, let's init our mkdocs sources. For it, let's pass the path (root for us):

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

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```







---

<div id=""></div>

##


```

```






---

Ro**drigo** **L**eite da **S**ilva - **drigols**
