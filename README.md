Here's a sample `README.md` for your project on generating AST using ANTLR:

---

# AST Generation Using ANTLR

## Description

This project demonstrates how to generate an Abstract Syntax Tree (AST) using ANTLR (ANother Tool for Language Recognition). The grammar rules define a simple language, and the lexer and parser handle tokenization and parsing, respectively. The `test_script.py` runs the parser and generates an AST.

## Prerequisites

- Python 3.x
- ANTLR4 installed
- ANTLR grammar files (`GosuLexer.g4`, `GosuParser.g4`)

## Setup

1. **Install ANTLR**: 
   - Download ANTLR from [official site](https://www.antlr.org/).
   - Add ANTLR to your system's PATH.

2. **Generate Lexer and Parser**: 
   - Use ANTLR tool to generate the lexer and parser classes from `.g4` grammar files.
     ```bash
     antlr4 -Dlanguage=Python3 GosuLexer.g4
     antlr4 -Dlanguage=Python3 GosuParser.g4
     ```

3. **Run the Python script**: 
   - After generating the lexer and parser, you can run the `test_script.py` to parse and generate the AST.
     ```bash
     python3 test_script.py
     ```

## Project Structure

- `GosuLexer.g4`: Defines the lexer rules.
- `GosuParser.g4`: Defines the parser rules.
- `GosuLexer.py`: Python class generated from `GosuLexer.g4`.
- `GosuParser.py`: Python class generated from `GosuParser.g4`.
- `test_script.py`: Contains code to test and generate AST.

## Generating AST

To generate the AST:

1. Run:
   ```bash
   python3 test_script.py
   ```

2. View the generated AST output.

## Issues and Troubleshooting

If you encounter any issues, make sure:
- The grammar rules are correctly defined.
- Lexer and parser classes are correctly generated and imported.
- All dependencies are correctly installed and set up.

---

Let me know if you'd like any additional details or modifications!
