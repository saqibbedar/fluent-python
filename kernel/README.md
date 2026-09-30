# Kernel

The purpose of `kernel` directory is that this accumulates frequently used libraries list and also few gists, as written below. It helps me to just install dependencies in single directory and when working with notebook files, I just select the *this directories virtual environment so its single yet powerful directory that fuel my development process and helps me to avoid installation for each directory separately. 

Think like its a backbone of repo or a centralized directory dedicated for working with notebook files and conduct any tests.


# Gists

### Run files using poethepoet

> First you need to install the poethepoet dependency using `uv add --dev poethepoet` to make the following commands to work properly.

```bash
uv run poe task1
uv run poe task2
```

### Run files using Justfile

> Note: You need to install the just first. On Linux/Ubuntu run `sudo apt update && sudo apt install just` to install the just.

Make a [Justfile](./Justfile) and run these commands

```bash
just task1
```