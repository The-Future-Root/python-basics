# Python Basics

A beginner's course in Python, the programming language used for everything from websites and data analysis to automation and AI. You'll learn by reading short lessons and writing small programs, and every exercise comes with tests that tell you when your code works.

No experience needed. If you can use a keyboard and a text editor, you can do this.

## What you'll be able to do

By the end you'll write programs that store and calculate values, make decisions, repeat work, organise code into functions, work with lists and dictionaries, read and write files, handle errors without crashing, and you'll have built a complete command-line expense tracker.

## What you need

- **Python 3.10 or newer.** Download it from [python.org](https://www.python.org/downloads/). On Windows, tick **Add python.exe to PATH** in the installer.
- **A text editor.** VS Code is a popular free choice, with its Python extension. Any editor that saves plain text works.
- **A terminal.** Terminal on macOS and Linux, PowerShell or Command Prompt on Windows.

Check that Python is installed:

```bash
python3 --version
```

You should see something like `Python 3.12.4`. On Windows the command is usually `python` instead of `python3`, and that's true for every command in this course.

## Lessons

Work through them in order. Each one builds on the last.

| # | Lesson | You'll learn |
|---|---|---|
| 1 | [Variables](./01-variables/) | Storing values and giving them names |
| 2 | [Data types](./02-data-types/) | Numbers, text, true/false, and converting between them |
| 3 | [Input and output](./03-input-and-output/) | Printing nicely formatted output and reading what the user types |
| 4 | [Conditionals](./04-conditionals/) | Making decisions with `if`, `elif` and `else` |
| 5 | [Loops](./05-loops/) | Repeating work with `for` and `while` |
| 6 | [Functions](./06-functions/) | Packaging code into reusable, testable pieces |
| 7 | [Lists and dictionaries](./07-lists-and-dictionaries/) | Storing collections of data |
| 8 | [Files](./08-files/) | Reading and writing text, CSV and JSON files |
| 9 | [Errors and exceptions](./09-errors-and-exceptions/) | Handling problems instead of crashing |
| 10 | [Project: expense tracker](./10-project-expense-tracker/) | Putting it all together in one real program |

## How the exercises work

Every lesson ends with an exercise in its folder:

- `exercise.py` is where you write your code. It has comments telling you what to do.
- `test_exercise.py` checks your code. Don't edit it.

To check your work, go into the lesson's folder and run the tests:

```bash
cd 01-variables
python3 -m unittest -v
```

Each test prints `ok` or `FAIL`. A failing test tells you what it expected and what it got. Keep going until they all pass:

```
Ran 5 tests in 0.002s

OK
```

The tests use `unittest`, which is built into Python, so there's nothing to install.

If you're stuck, there's a hint section at the end of each exercise, and full solutions in [solutions/](./solutions/). Try properly first: getting stuck and working it out is how the learning happens.

## Running Python code

There are two ways to run Python, and you'll use both.

**Run a file.** Write your code in a file ending in `.py`, then run it from the terminal:

```bash
python3 hello.py
```

**Try things out interactively.** Type `python3` on its own to start the Python shell. You'll see a `>>>` prompt. Type a line of Python, press Enter, and you get the answer straight away. It's great for quick experiments. Type `exit()` to leave.

```
>>> 3 * 4
12
>>> "coffee".upper()
'COFFEE'
```

## License

The code in this repository is released under the [MIT License](./LICENSE). The lesson text and diagrams are released under [Creative Commons Attribution 4.0](./LICENSE-CONTENT) (CC BY 4.0): you may share and adapt them, including for your own teaching, as long as you credit The Future Root.
