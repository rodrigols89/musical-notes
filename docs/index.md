![project-logo](assets/logo.png){ width="300" .center }
# Musical Notes

Musical Notes is a **CLI** tool to assist in the formation of **scales**, **chords**, and **harmonic fields**.

The entire application is based on a command called **"musical-notes"**. This command has a subcommand related to each action that the application can perform, such as **scales**, **chords**, and **harmonic fields**.

{% include "templates/cards.html" %}

{% include "templates/installation.md" %}

<div id="how-to-install"></div>

## How to use?

### Scales

You can call the **scales** via the command line. For example:


```bash
{{ commands.run }} scale
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
{{ commands.run }} scale F#
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
{{ commands.run }} scale D# major

┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ G   │ G# │ A# │ C  │ D   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

---

## Chords

Basic use:

```bash
{{ commands.run }} chord
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

### Chord variations (Portuguese=Variações na cifra)

```bash
{{ commands.run }} chord C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

---

## Harmonic Field

You can call the **Harmonic Fields** via the subcommand `harmonic-field`. For example:

```bash
{{ commands.run }} harmonic-field

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
{{ commands.run }} harmonic-field [TONIC] [KEY]
```

#### Change in the tonic of the field

An example with the harmonic field of `E`:

```bash
{{ commands.run }} harmonic-field E

┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ vii° ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#°  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Change in the tonality of the field

An example using the harmonic field of `E` in the `minor` tonality:


```bash
{{ commands.run }} harmonic-field E minor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ ii° ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#° │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## More information about the CLI

To discover other options, you can use the `--help` flag:

```bash
{{ commands.run }} --help
                                                                       
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

### More information about subcommands

Information about subcommands can be accessed by using the `--help` flag after the parameter name. An example of using `help` on the harmonic fields:

```bash
{{ commands.run }} harmonic-field --help
                                                                       
 Usage: musical-notes harmonic-field [OPTIONS] [TONIC] [KEY]

╭─ Arguments ──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│   tonic      [TONIC]  Harmonic field tonic note [default: c]                                                                                                                         │
│   key        [KEY]    Harmonic field key (PT-BR=tonalidade) [default: major]                                                                                                         │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```
