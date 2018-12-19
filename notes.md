# My notes

## Recommended environment
- text editor
- ipython shell
- jupyter notebooks

## IPython and Jupyter "Now I know"
- `%run 'filename.py'` executes the script and loads assets into memory in the shell session
- IPython pretty prints data by default
- Run jupyter with `jupyter notebook`
- `shift + Enter` evaluates a line (or block) of code
- tab-autocomplete is super useful and grows with new values and functions in scope (like a good editor)
- `%run -i` instead of `%run` allows the script acces to variables already defined in the interactive ipython namespace.
- `%load` imports a script
- `%paste` pastes text from the clipboard
- `%cpaste` provides a prompt for pasting code
    
## Making random data
```python
import numpy as np

data = {i : np.random.randn() for i in range(7)}
```

## CLI Keyboard shortcuts that work in ipython and jupyter
- ctrl+l to clear screen
- ctrl +b to move cursor back one character
- ctrl + f to move cursor forward one character