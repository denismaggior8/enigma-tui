# Enigma TUI (Terminal User Interface)

**Enigma TUI** is a **T**erminal **U**ser **I**nterface for Enigma machines, allowing you to simulate different Enigma machine models from the  terminal.

Built with Python, it leverages [**enigmapython**](https://pypi.org/project/enigmapython/) as Enigma engine and [**textual**](https://pypi.org/project/textual/) to render the interface.

## Run in development mode

By following this procedure, you leverage [**pytest-watch**](https://pypi.org/project/pytest-watch/) to live reloading the application upon Python code change. 

```console
$ pip install -r requirements-dev.txt
$ cd src/tui
$ ptw --runner "textual run --dev  enigmatui/__main__.py"      
```

Be aware that, in this case, to terminate the application you have to use CTRL+C (instead of any other shortcut configured in the app)