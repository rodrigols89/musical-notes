<img src="https://musical-notes.readthedocs.io/en/latest/assets/logo.png" width="200">

# Musical Notes

[![Documentation Status](https://readthedocs.org/projects/musical-notes/badge/?version=latest)](https://musical-notes.readthedocs.io/en/latest/)
[![CI](https://github.com/drigols/musical-notes/actions/workflows/pipeline.yaml/badge.svg)](https://github.com/drigols/musical-notes/actions/workflows/pipeline.yaml)
[![codecov](https://codecov.io/gh/drigols/musical-notes/branch/master/graph/badge.svg?token=QYMBUYB4HF)](https://app.codecov.io/gh/drigols/musical-notes)

Musical Notes is a **CLI** tool to assist in the formation of **scales**, **chords**, and **harmonic fields**.

The entire application is based on a command called **"musical-notes"**. This command has a subcommand related to each action that the application can perform, such as **scales**, **chords**, and **harmonic fields**.

## Contents

 - [How to Install the Project](#how-to-install)
 - [How to use?](#how-to-use)
 - [Tech Stack](#tech-stack)
 - [Credits](#credits)

---

<div id="how-to-install"></div>

## How to Install the Project

To install the project's CLI, we recommend using `pipx` for this installation:

```bash
pipx install musical-notes
```

Although this is only a recommendation! You can also install the project with your preferred package manager, such as `pip`:
```bash
pip install musical-notes
```

---

<div id="how-to-use"></div>

## How to use?

### Scales

You can call the **scales** via the command line. For example:

```bash
musical-notes scale
```

Returning the **degrees** and **notes** corresponding to this scale:

```
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Changing the scale tonic

The first parameter of the **CLI** is the `tonic` of the scale you wish to display. This way, you can change the returned scale. For example, the `F#` *scale*:"

```bash
musical-notes scale F#
```

Result in:

```
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Changing the key (PT-BR=tonalidade) of the scale

You can also change the **key (PT-BR=tonalidade)** of the scale! This is the second parameter of the command line. For example, the scale of `D# major`:"

```bash
musical-notes scale D# major

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

---

### Chords

Basic use:

```bash
musical-notes chord
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Chord variations (Portuguese=Variações na cifra)

```bash
musical-notes chord C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

---

### Harmonic Field

You can call the **Harmonic Fields** via the subcommand `harmonic-field`. For example:

```bash
musical-notes harmonic-field

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ vii° ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ B°   │
└───┴────┴─────┴────┴───┴────┴──────┘
```

**NOTE:**  
By default, the parameters used are the tonic of `C` and the `major` harmonic field.

#### Changes in the harmonic fields

You can change the parameters of the `tonic note` and `key (tonality)`.

```bash
musical-notes harmonic-field [TONIC] [KEY]
```

#### Change in the tonic of the field

An example with the harmonic field of `E`:

```bash
musical-notes harmonic-field E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Change in the tonality of the field

An example using the harmonic field of `E` in the `minor` tonality:


```bash
musical-notes harmonic-field E minor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

---

### More information about the CLI

To discover other options, you can use the `--help` flag:

```bash
musical-notes --help
                                                                       
 Usage: musical-notes [OPTIONS] COMMAND [ARGS]...

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified shell. [default: None]                               │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell, to copy it or customize the installation.        │
│                                                              [default: None]                                                                           │
│ --help                                                       Show this message and exit.                                                               │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ chord                                                                                                                                                  │
│ harmonic-field                                                                                                                                         │
│ scale                                                                                                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

#### More information about subcommands

Information about subcommands can be accessed by using the `--help` flag after the parameter name. An example of using `help` on the harmonic fields:

```bash
musical-notes harmonic-field --help
                                                                       
 Usage: musical-notes harmonic-field [OPTIONS] [TONIC] [KEY]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonic      [TONIC]  Harmonic field tonic note [default: c]                                                                                                                         │
│   key        [KEY]    Harmonic field key (PT-BR=tonalidade) [default: major]                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

**NOTE:**  
You can also use the [main documentation](https://musical-notes.readthedocs.io/en/latest/) to learn more about the project.

---

<div id="tech-stack"></div>

## Tech Stack

 - **Programming Languages:**
   - Python
 - **CLI:**
   - Typer
   - Rich
 - **Test:**
   - Pytest
   - Pytest-cov
 - **Linters:**
   - blue
   - isort
 - **Project management:**
   - VSCode
     - .editorconfig extension
   - Poetry
   - taskipy
   - Git
   - GitHub Actions
 - **Documentation:**
   - [The Read Docs](https://readthedocs.org/)
   - mkdocs-material
   - mkdocstrings
   - mkdocstrings-python
   - mkdocs-macros-plugin
   - jinja2

---

<div id="credits"></div>

## Credits

The project credits are to [Eduardo Mendes](https://www.youtube.com/@Dunossauro) Youtube channel. I followed the ["Construindo um pacote Python do zero #CodaComigo"](https://www.youtube.com/playlist?list=PLOQgLBuj2-3LiHhK1upnjpHiFzcJ472QS) playlist to develop this project. However, I translated all the project to English.
