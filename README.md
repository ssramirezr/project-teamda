## First and Follow Set Calculator <br>
This project was created by David Ramírez and Ana Sofía Alfonso.    A Python project to compute the First and Follow sets of a specific grammar.

# Table of Contents
- Introduction
- Espesifications
- Usage
- Examples
- Features

# Introduction
This Python project, developed by David Ramírez and Ana Sofía Alfonso, helps users compute First and Follow sets for context-free grammars. It's handy for students and pros working on compiler design and syntax analysis. It's a great tool for grasping grammars, creating parsing methods, and improving compilers.

# Especifications
- Language: Python 3.10
- IDE: PyCharm 2023.1.4

# Usage
Instructions on how to use the project to compute First and Follow sets.

Run command: python "main.py"

Advertisement:
- When you run more than one grammar, you need to click enter when the last grammar is going to give its output
- e represents epsilon
- $ this symbol is not allow on the input
-  First simbols are nonterminals, right side reprents the productions
- The program only reads nonterminals in uppercase and terminals in lowcase


When prompted, enter the number of cases, the number of nonterminals, and the productions in the following format:

```
1
3
S AB
A aBc  e
B b
```
# Expected output
```
 First(S): {a, b, ε}
 First(A): {a, ε}
 First(B): {b}
 Follow(S): {$}
 Follow(A): {b, c}
 Follow(B): {c, $}
```
# Features

1. Calculate First sets: The project computes First sets for context-free grammars, crucial for predicting symbols in parsing algorithms like LL and LR parsers. It's based on established algorithms, ensuring accurate results.
2. Calculate Follow sets: The project also computes Follow sets, essential for predictive parsing methods such as LL(1) parsing. Follow sets aid in constructing parsing tables and resolving parsing conflicts.
3. Handles epsilon (ε) productions: The implementation effectively manages epsilon productions, ensuring accurate computation of First and Follow sets. It appropriately incorporates epsilon transitions for comprehensive analysis of grammar predictability.


