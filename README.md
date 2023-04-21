# Crawler Coding Challenge

A console application that displays the most common words used in a portion of a webpage.

## Usage

Use the application with following configurable features:

-> The top number of words to return (default: 10)

-> Words to exclude from search

```bash
python3 main.py

# optional 'number of words'
python3 main.py 15

# optional 'words to exclude'
python3 main.py for
python3 main.py for or and

# optional 'number of words, words to exclude'
python3 main.py 20 the and or
```

## Notes

The following modifications are done while cleaning the data to avoid counting same word multiple times:

1. All text is converted into lower case e.g.: On - 15, on - 12
2. Citations are removed e.g.: BASIC[11] - 8, BASIC - 15
3. Punctuations are removed e.g.: 'employees.' - 3, 'employees' - 22
4. I have also included binary file in GUI folder named ashi,executing it will result the same as code.py