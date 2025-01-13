# Enigma TUI (Terminal User Interface)

![Enigma TUI](img/enigmatui.png)

**Enigma TUI** is a **T**erminal **U**ser **I**nterface for Enigma machines, allowing you to simulate different Enigma machine models from the terminal.

Built with Python, it employs [**enigmapython**](https://pypi.org/project/enigmapython/) as Enigma engine and [**textual**](https://pypi.org/project/textual/) to render the interface.

## Prerequisites

- Python 3.11
- Clone this repo, checkout the desired branch/tag and install requirements (`pip install -r requirements.txt`) or directly from PyPI using `pip install enigmatui`

## How to run Enigma TUI

Use Python to run Enigma TUI's package

```console
$ python -m enigmatui
```

## Enigma TUI online version

An online version of Enigma TUI exists thanks to the [Render](https://render.com)'s free plan. If you'd like to test Enigma TUI before installing it locally, please refer to https://enigma-tui.onrender.com/


## How it works

Reading the usage instructions is more difficult than using the application itself. 

Enigma TUI has a fairy simple user interface with a couple of screens to let you configure an Enigma machine (among the supported models) and encrypt/decrypt messages, plus seeing in realtime the machine internals (rotors positions, wirings) and how a single letter is scrambled from the keyboard to rotors, through reflector and back up to lamp.

Please refer to the following flowchart to navigate the app.

```mermaid
flowchart TD
%% Nodes
    A("Splash screen")
    B("Main screen")
    C("Configure screen")
    D("De/Encrypt screen")


%% Edge connections between nodes
    Start([Start]) --> A
    A -- Go to app --> B 
    C -- Save and exit --> B
    B -- Configure --> C
    B -- De/Encrypt --> D
    D -- Back --> B
    A -- Quit --> End([Stop])
    B -- Quit --> End([Stop])
    C -- Quit --> End([Stop])
    D -- Quit --> End([Stop])
    
```

Anytime you can press `ctrl-q` to quit the application.

> **Note**
> This version of Enigma TUI does not support the plugboard (a.k.a. Steckerbrett)


## Run Enigma TUI in development mode

By following this procedure, you leverage [**pytest-watch**](https://pypi.org/project/pytest-watch/) to live reloading the application upon Python code change. 
In addition, thanks to the `textual run` command with its `--dev` flag, changing the stylesheets reflects to the interface instantly.

```console
$ pip install -r requirements-dev.txt
$ cd src/tui
$ ptw --runner "textual run --dev  enigmatui/__main__.py"      
```

The above commands are valid provided that you cloned the [**enigma-tui**](https://github.com/denismaggior8/enigma-tui) repository from GitHub and your terminal is in the repository's root directory.

## Enigma references

If you want more details about how an Enigma machine works, especially to understand the difference between the machine models, rotors types ans so on, I can not suggest you a better reference than [Crypto Musem](https://www.cryptomuseum.com/crypto/enigma/index.htm) 