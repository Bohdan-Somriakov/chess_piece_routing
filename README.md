# NetworkX, Matplotlib, and NumPy Libraries

## Overview

These libraries are essential tools in the Python scientific computing ecosystem, offering capabilities for network analysis, data visualization, and numerical computations.

- **NetworkX**: A powerful library for creating, manipulating, and studying complex networks or graphs. It provides various algorithms for network analysis and graph visualization.
- **Matplotlib**: A cornerstone library for generating static, animated, and interactive visualizations in Python. It offers a wide range of plot types and customization options.
- **NumPy**: A fundamental foundation for scientific computing in Python. It provides efficient multidimensional arrays and mathematical functions, enabling high-performance numerical operations.

# Description

## Introduction
The algorithm constructs a path through a graph representation of a chessboard. This path demonstrates the legal movements of a specified chess piece, ensuring that each square is visited at most once.

![image](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/intro/5x5_chess_board.png)

The graph depicts the legal connections between squares on a chessboard. A knight's movement follows a specific pattern: it traverses either two squares vertically and one square horizontally, or vice versa, forming an "L".

![image](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/intro/5x5_knight.png)

The bishop chess piece moves in any direction diagonally. Chess rules state that there is no limit to the number of squares a bishop can travel on the chessboard, as long as there is not another piece obstructing its path.

![image](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/intro/5x5_bishop.png)

## Traversing the entire graph without revisiting any node
Many rules can be activated and placed in the working list of rules during each cycle. In addition, the results of activating rules from previous cycles remain in the working list of rules, unless these rules are deactivated due to the fact that their left-hand sides are no longer satisfied. Thus, during program execution, the number of activated rules in the working list of rules changes.

Depending on the program, previously activated rules may always remain in the working list of rules, but never be selected for execution. Similarly, some rules may never become activated. In such cases, it is worth re-checking the purpose of these rules, since either such rules are not needed at all, or their antecedents are incorrectly designed.

### Depth strategy
Depth strategy - implementation of the data novelty strategy in relation to rules of the same class. Rules chosen based on data included in working memory relatively recently are positioned earlier in this list than rules chosen using older data.

Thus, priority is given to the depth-first search principle in the problem state space, meaning that rules resulting from more recent changes in system state have a higher priority. In this case, the last activated rule is chosen from the conflict set.

|  |  |
|---------|---------|
| ![1](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/depth_knight/1.png) | ![3](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/depth_knight/2.png) |
| ![2](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/depth_knight/3.png) | ![4](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/depth_knight/4.png) |

PATH: [1, 12, 21, 18, 25, 14, 5, 8, 19, 22, 11, 2, 9, 20, 23, 16, 7, 4, 15, 24, 17, 6, 13, 10, 3]

### Breadth strategy
In the src code called width strategy.

Breadth Strategy (breadth) - opposite to the depth strategy and is designed to implement a breadth-first search in the problem state space. The rules selected to the list based on the data that were included in the working memory relatively long time ago are located earlier in this list than the rules that were selected using more recent data. In this case, the first activated rule from the conflict set is chosen.

|  |  |
|---------|---------|
| ![1](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/bredth_knight/1.jpg) | ![3](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/bredth_knight/2.jpg) |
| ![2](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/bredth_knight/3.jpg) | ![4](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/bredth_knight/4.jpg) |

PATH: [1, 8, 5, 14, 25, 18, 21, 12, 3, 6, 17, 24, 15, 4, 7, 16, 23, 20, 9, 2, 11, 22, 13, 10, 19]

### Random strategy
Pretty self-explanatory

|  |  |
|---------|---------|
| ![1](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/random_knight/1.jpg) | ![3](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/random_knight/2.jpg) |
| ![2](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/random_knight/3.jpg) | ![4](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/random_knight/4.jpg) |

PATH: [1, 8, 5, 14, 25, 18, 21, 12, 9, 2, 11, 22, 19, 10, 3, 6, 17, 24, 15, 4, 7, 16, 13, 20, 23]

### Example 
This algorithm exhibits the capability of being applied to any chess piece, irrespective of the dimensions of the chessboard. An illustrative example is provided for a 10x10 board.

![10x10_width_knight](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/entire_graph/more_examples/knight_10x10_width.png)

PATH: [1, 13, 5, 17, 9, 30, 18, 10, 29, 8, 20, 39, 60, 79, 100, 88, 80, 99, 87, 95, 83, 91, 72, 51, 32, 11, 3, 22, 41, 62, 81, 93, 74, 82, 61, 53, 34, 15, 7, 19, 40, 28, 16, 4, 12, 24, 36, 48, 27, 6, 14, 2, 21, 42, 23, 31, 43, 35, 47, 26, 38, 50, 69, 90, 98, 86, 94, 73, 92, 71, 52, 33, 25, 44, 63, 55, 67, 59, 78, 70, 49, 37, 45, 57, 65, 46, 54, 66, 58, 77, 85, 64, 56, 75, 96, 84, 76, 68, 89, 97]

## Traversing to a specific vertex

The mechanism of backward logical inference consists of verifying the validity of a certain hypothesis (judgment or fact) that is put forward by the user and verified by the ES [expert system]. In doing so, the truth of the right parts of the productions, rather than the left parts, is checked, and the question is formulated as follows: "What is necessary for the right part of the production rule to be valid (true), and are there necessary judgments in working memory?"

When implementing this mechanism, new facts are not added to the working memory; instead, only the presence of the necessary judgments at the next step of the algorithm is checked. In some production systems, the working memory is replenished with new facts.

![10x10_width_knight](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/theory/table_with_ifs.png)

The presented algorithm executes until it successfully locates the designated vertex.

### Strategies comparison

Analysis of Knight Maneuvers on a Chessboard: Exploring Various Approaches to Reach Square "9".

| depth | breadth | random |
|---------|---------|---------|
| ![1](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/knight_depth_to_9.png) | ![2](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/knight_width_to_9.png) | ![3](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/knight_random_to_9.png)
|---------|---------|---------|
|[1, 12, 21, 18, 25, 14, 5, 8, 19, 22, 11, 2, 9]|[1, 8, 5, 14, 25, 18, 21, 12, 3, 6, 17, 24, 15, 4, 7, 16, 23, 20, 9]|[1, 12, 21, 18, 25, 14, 5, 8, 11, 2, 9]|


Analysis of Bishop Maneuvers on a Chessboard: Exploring Various Approaches to Reach Square "9".

| depth | breadth | random |
|---------|---------|---------|
| ![1](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/bishop_depth_to_9.png) | ![2](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/bishop_width_to_9.png) | ![3](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/bishop_random_to_9.png)
|---------|---------|---------|
|[1, 25, 19, 23, 15, 3, 11, 7, 13, 21, 17, 9]|[1, 25, 7, 3, 11, 23, 15, 19, 13, 5, 9]|[1, 25, 7, 11, 3, 15, 23, 19, 13, 5, 17, 21, 9]|

### Example

This algorithm exhibits the capability of being applied to any chess piece, irrespective of the dimensions of the chessboard. An illustrative example is provided for a 15x15 board. The algorithm utilized is breadth-first search. The objective is to reach a target value of 100, starting from the initial point of 1.

![knight_15x15_width](https://github.com/Bohdan-Somriakov/chess_piece_routing/blob/main/assets/to_given_node/examples/knight_15x15_width.png)

PATH: [1, 18, 5, 22, 9, 26, 13, 30, 59, 90, 119, 150, 179, 210, 223, 194, 225, 208, 195, 224, 207, 220, 203, 216, 199, 212, 181, 152, 121, 92, 61, 32, 3, 16, 47, 76, 63, 46, 17, 4, 21, 34, 51, 20, 7, 38, 25, 8, 39, 10, 23, 6, 19, 2, 31, 48, 35, 52, 65, 36, 49, 62, 33, 50, 37, 24, 11, 28, 15, 44, 75, 88, 105, 74, 45, 14, 27, 40, 57, 70, 53, 66, 79, 96, 67, 54, 41, 12, 29, 42, 55, 68, 81, 64, 77, 106, 93, 80, 97, 84, 71, 58, 87, 56, 43, 60, 73, 104, 135, 164, 133, 120, 89, 72, 85, 102, 115, 86, 69, 98, 111, 82, 99, 116, 103, 134, 165, 148, 117, 100]

