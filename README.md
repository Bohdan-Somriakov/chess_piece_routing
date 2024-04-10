# NetworkX, Matplotlib, and NumPy Libraries

## Overview

These libraries are essential tools in the Python scientific computing ecosystem, offering capabilities for network analysis, data visualization, and numerical computations.

- **NetworkX**: A powerful library for creating, manipulating, and studying complex networks or graphs. It provides various algorithms for network analysis and graph visualization.
- **Matplotlib**: A cornerstone library for generating static, animated, and interactive visualizations in Python. It offers a wide range of plot types and customization options.
- **NumPy**: A fundamental foundation for scientific computing in Python. It provides efficient multidimensional arrays and mathematical functions, enabling high-performance numerical operations.

# Description

## Introduction
The algorithm constructs a path through a graph representation of a chessboard. This path demonstrates the legal movements of a specified chess piece, ensuring that each square is visited at most once.

![image](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assetss/intro/5x5_chess_board.png)

The graph depicts the legal connections between squares on a chessboard. A knight's movement follows a specific pattern: it traverses either two squares vertically and one square horizontally, or vice versa, forming an "L" shape.https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assetss/intro/5x5_bishop.png

!(image]https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assetss/intro/5x5_knight.png)

The bishop chess piece moves in any direction diagonally. Chess rules state that there is no limit to the number of squares a bishop can travel on the chessboard, as long as there is not another piece obstructing its path.

!(image]https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assetss/intro/5x5_bishop.png)

## Traversing the entire graph without revisiting any node
Many rules can be activated and placed in the working list of rules during each cycle. In addition, the results of activating rules from previous cycles remain in the working list of rules, unless these rules are deactivated due to the fact that their left-hand sides are no longer satisfied. Thus, during program execution, the number of activated rules in the working list of rules changes.

Depending on the program, previously activated rules may always remain in the working list of rules, but never be selected for execution. Similarly, some rules may never become activated. In such cases, it is worth re-checking the purpose of these rules, since either such rules are not needed at all, or their antecedents are incorrectly designed.

### Depth strategy
Depth strategy - implementation of the data novelty strategy in relation to rules of the same class. Rules chosen based on data included in working memory relatively recently are positioned earlier in this list than rules chosen using older data.

Thus, priority is given to the depth-first search principle in the problem state space, meaning that rules resulting from more recent changes in system state have a higher priority. In this case, the last activated rule is chosen from the conflict set.

### Breadth strategy
In the src code called width strategy.

Breadth Strategy (breadth) - opposite to the depth strategy and is designed to implement a breadth-first search in the problem state space. The rules selected to the list based on the data that were included in the working memory relatively long time ago are located earlier in this list than the rules that were selected using more recent data. In this case, the first activated rule from the conflict set is chosen.

### Random strategy
Pretty self-explanatory
