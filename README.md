# PDF Page Widener

A simple Python utility to add top and bottom margins to PDF pages.

## Installation

```bash
pip install -e .
```

## Usage

Run the script from the command line:

```bash
python main.py input.pdf
```

By default, this adds a 1-inch margin to both top and bottom of each page.

### Options

- `--top`: Size of top margin in points (default: 72, which is 1 inch)
- `--bottom`: Size of bottom margin in points (default: 72, which is 1 inch)

Example with custom margins:

```bash
python main.py input.pdf --top 36 --bottom 108
```

This adds a 0.5-inch margin to the top and a 1.5-inch margin to the bottom of each page.

## Output

The tool creates a new PDF file with the filename pattern `{original_filename}_elongated.pdf` in the same directory as the input file.