# Tutorial

If you have made it this far, it means that you want to learn more about `musical-notes`.

The goal of this project is to help music students or professionals to easily access `scales`, `chord formations`, and `harmonic fields`. Each of these commands is distributed in a subcommand of our **CLI**.

{% include "templates/installation.md" %}


## The commands

The `musical-notes` distributes each function in a *subcommand* and you can execute each of them to test now. The purpose of this tutorial is to explain the basics of how the *command-line (CLI)* application works.

The subcommands are divided into three functions so far: `scale`, `chord`, and `harmonic-field`.

Let's understand what each of them aims to do now.

### Scales

The `scale` subcommand helps us to easily access the formation of music scales.

If it is invoked without any parameters, it will return the `C major` scale:

```bash
{{ commands.run }} scale
```

This will provide a table in the terminal showing the scale:

**OUTPUT:**  
```bash
| I | II | III | IV | V | VI | VII |
| - | -- | --- | -- | - | -- | --- |
| C | D  | E   | F  | G | A  | B   |
```

---

### Chords

The chords subcommand is based on showing in which degrees they are related within the major scale. It allows you to input a chord and it will show the notes contained in that chord and their corresponding degrees.

For example, chord `Dm+`:

```bash
{{ commands.run }} chord Dm+
```

**OUTPUT:**  
```bash
| I | III- | V+ |
| - | ---- | -- |
| D | F    | A# |
```

Points to note regarding this response:

 - The `"-"` symbolizes one semitone less. That is, for the chord to be major, it would require `F` to be an `F#`.
 - The `"+"` symbolizes one semitone more. That is, for the chord to be major, it would require `A#` to be an `A`.

!!! warning "About chords"
	It is possible that the chords you are looking for have not yet been implemented. At the time of writing this tutorial, only triad chords have been implemented. Therefore, you can use major, minor, augmented, and diminished chords.

---

### Harmonic Field

Harmonic fields are representations of the scale using chords. Its subcommand has the same use as the `scale` subcommand. However, its call varies to `harmonic-field`:

```bash
{{ commands.run }} harmonic-field [TONIC] [KEY]
```

#### Basic use

If the command is called without any `tonic note`, it will return the harmonic field of `C major`:

```bash
{{ commands.run }} harmonic-field
```

Obtaining, thus, a table with all the corresponding chords for this field:

**OUTPUT:**  
```bash
| I | ii | iii | VI | V | vi | vii° |
| - | -- | --- | -- | - | -- | ---- |
| C | Dm | Em  | F  | G | Am | B°   |
```

---
