import networkx as nx
import matplotlib.pyplot as plt
from random import randint

class Chess_piece:
    def __init__(self, board_coords, board_id, first_vertex, target=None):
        self.board_coords = board_coords  # board_coords taken from the Board class
        self.board_id = board_id  # board_id taken from the Board class
        self.first_vertex = first_vertex
        self.target = target
        self.all_cells = self.make_all_cells()
        self.valid_moves_coords = self.valid_moves()
        self.valid_moves_id = self.indeces_to_id_notation()
        self.edges_by_vertices = self.make_edges_by_vertices()
        self.path_width = self.make_path_with_width()
        self.path_depth = self.make_path_with_depth()
        self.path_random = self.make_path_with_random()
        self.path_to_target_width = self.make_path_to_target_width()
        self.path_to_target_depth = self.make_path_to_target_depth()
        self.path_to_target_random = self.make_path_to_target_random()

    def make_all_cells(self):
        return [(i, j) for i, elem in enumerate(self.board_coords) for j, subelem in enumerate(elem)]
    def valid_moves(self):
        return None
    def indeces_to_id_notation(self):
        return [((self.board_id[elem[0][0]][elem[0][1]]),(self.board_id[elem[1][0]][elem[1][1]])) for elem in self.valid_moves_coords]

    def show_connections(self):
        graph = nx.DiGraph()
        graph.add_edges_from(self.valid_moves_id)
        pos = nx.spring_layout(graph)
        plt.figure(figsize=(14, 12))
        nx.draw(graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold",
                arrows=True, arrowsize=10, arrowstyle="->", edge_color="gray", linewidths=1, alpha=0.9)

        plt.title("Directed Graph of Connections")
        plt.show()
    def make_edges_by_vertices(self):
        edges_by_vertices = []
        for elem in enumerate(self.valid_moves_id):
            current_pos = elem[0]
            current_pos_moves = [elem for elem in self.valid_moves_id if elem[0] == current_pos]
            if current_pos_moves != []:
                edges_by_vertices.append(current_pos_moves)
        return edges_by_vertices
    def show_edges_by_vertices(self):
        print("Edges by vertices:")
        for elem in self.edges_by_vertices:
            print(elem)

    def make_path_with_width(self):
        return self.make_path_with_strategy("width")

    def make_path_with_depth(self):
        return self.make_path_with_strategy("depth")

    def make_path_with_random(self):
        return self.make_path_with_strategy("random")

    def make_path_with_strategy(self, strategy):
        current_edge = self.first_vertex
        path = []
        for elem in self.edges_by_vertices:
            num_of_unvisited_vertices = []
            path.append(current_edge)
            for index, link in enumerate(self.edges_by_vertices[current_edge - 1]):
                to_go = self.edges_by_vertices[current_edge - 1][index][1]
                if to_go not in path:
                    num_of_unvisited_vertices.append(
                        {to_go: len([elem for elem in self.edges_by_vertices[to_go - 1] if elem[1] not in path])})
            if len(num_of_unvisited_vertices):
                min_num_vertices = min(value for item in num_of_unvisited_vertices for value in item.values())
            edge_with_min_num_vertices = self.find_key_by_value(num_of_unvisited_vertices, min_num_vertices, strategy)
            current_edge = edge_with_min_num_vertices
            if current_edge is None:
                return path
        return path
    def make_path_with_strategy_to_target(self, strategy):
        if strategy == "width":
            path = self.path_width
        elif strategy == "depth":
            path = self.path_depth
        elif strategy == "random":
            path = self.path_random
        else:
            return None

        for index, elem in enumerate(path):
            if elem == self.target:
                return path[:index + 1]
        return None

    def make_path_to_target_width(self):
        return self.make_path_with_strategy_to_target("width")

    def make_path_to_target_depth(self):
        return self.make_path_with_strategy_to_target("depth")

    def make_path_to_target_random(self):
        return self.make_path_with_strategy_to_target("random")

    def remove_dicts_with_non_target_value(self, list_of_dicts, target_value):
        legit_options = [] #dicts where the value is a target value
        print(f"options: {list_of_dicts}, target_value: {target_value}")
        for dictionary in list_of_dicts:
            for key, value in dictionary.items():
                if value == target_value:
                    legit_options.append({key: value})
        return legit_options

    def width_method(self, legit_options):
        return list(legit_options[0].keys())[0]

    def depth_method(self, legit_options):
        return list(legit_options[-1].keys())[0]

    def random_method(self, legit_options):
        keys_list = [key for dict in legit_options for key in dict.keys()]
        return keys_list[randint(0, len(keys_list) - 1)]

    def find_key_by_value(self, list_of_dicts, target_value, method):
        legit_options = [] #dicts where the value is a target value
        legit_options = self.remove_dicts_with_non_target_value(list_of_dicts, target_value)
        if (len(legit_options)) > 0:
            if method == "width":
                return self.width_method(legit_options)
            elif method == "depth":
                return self.depth_method(legit_options)
            elif method == "random":
                return self.random_method(legit_options)
        else:
            return None
    def choose_node_cycle(self, strategy):
        if strategy == "width":
            if self.target is not None:
                return self.path_to_target_width
            else:
                return self.path_width
        elif strategy == "depth":
            if self.target is not None:
                return self.path_to_target_depth
            else:
                return self.path_depth
        elif strategy == "random":
            if self.target is not None:
                return self.path_to_target_random
            else:
                return self.path_random
        else:
            raise Exception("Not a valid strategy")

    def visualise_target(self, graph, pos):
        if self.target is not None:
            node_colors = [
                'green' if n == self.target else 'skyblue' for n in graph.nodes
            ]
            nx.draw(
                graph, pos, with_labels=True, node_size=700, node_color=node_colors,
                font_size=10, font_weight="bold", arrows=True, arrowsize=10, arrowstyle="->",
                edge_color="gray", linewidths=1, alpha=0.9
            )
            plt.pause(3)
    def visualise_graph_movement(self, node_cycle, graph, pos):
        visited_nodes = []

        for node in node_cycle:
            node_colors_updated = [
                'red' if n == node and n not in visited_nodes else 'yellow' if n in visited_nodes else "skyblue" for n
                in graph.nodes]

            plt.clf()

            nx.draw(
                graph, pos, with_labels=True, node_size=700, node_color=node_colors_updated,
                font_size=10, font_weight="bold", arrows=True, arrowsize=10, arrowstyle="->",
                edge_color="gray", linewidths=1, alpha=0.9
            )
            plt.title(f"Node {node} in Red, Visited Nodes in Yellow")

            plt.pause(1)

            visited_nodes.append(node)

    def visual_path(self, strategy):
        graph = nx.DiGraph()
        graph.add_edges_from(self.valid_moves_id)

        pos = nx.spring_layout(graph)

        plt.figure(figsize=(14, 12))
        nx.draw(
            graph, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_weight="bold",
            arrows=True, arrowsize=10, arrowstyle="->", edge_color="gray", linewidths=1, alpha=0.9
        )
        plt.title("Directed Graph of Connections")

        plt.ion()
        node_cycle = self.choose_node_cycle(strategy)

        self.visualise_target(graph, pos)

        self.visualise_graph_movement(node_cycle, graph, pos)

        plt.ioff()
        plt.show()

    def visual_path_width(self):
        self.visual_path("width")

    def visual_path_depth(self):
        self.visual_path("depth")

    def visual_path_random(self):
        self.visual_path("random")

    def __str__(self):
        return f"Chess piece:\n" \
               f"all_cells:\n{self.all_cells},\n" \
               f"valid_moves_coords:\n{self.valid_moves_coords}\n" \
               f"valid_moves_id:\n{self.valid_moves_id}\n" \
               f"\n"