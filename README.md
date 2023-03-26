# Gisa

Gisa is a Python package that converts numbers into Malagasy words. It provides a function `number_to_word` that takes a numeric input and returns its corresponding Malagasy word representation.

## Installation

You can install gisa.manisa using pip:

```bash
pip install gisa
```


## Usage

To use gisa, you need to import it first:

```python
from gisa.manisa import number_to_word
```

Then, you can call the number_to_word function to convert a number to its Malagasy word representation:

```python
word = number_to_word(586)
print(word)  # outputs "enina ambiny valopolo sy dimanjato"

```

## Limitations

While Gisa is able to convert whole numbers to their Malagasy word representations, it may have limitations when it comes to converting decimal numbers. Also, the package currently only supports the Malagasy language.

## License

This package is licensed under the MIT License. See the LICENSE file for more information.

