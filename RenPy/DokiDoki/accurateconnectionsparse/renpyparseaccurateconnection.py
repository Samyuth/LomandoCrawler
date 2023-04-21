import os
import re
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from pyvis.network import Network

class RpyNode:
    def __init__(self, text, file_name):
        self.text = text
        self.file_name = file_name
        self.nodes = {}
        self.call_stack = []

    def parse_text(self):
        lines = self.text.split("\n")
        label = None
        line_number = 0

        while line_number < len(lines):
            line = lines[line_number].strip()

            if re.match(r"label (\w+):", line):
                label = re.findall(r"label (\w+):", line)[0]
                if label not in self.nodes:
                    self.nodes[label] = {"file": self.file_name, "connections": []}

            elif label is not None:
                if re.match(r"jump (\w+)", line):
                    jump_label = re.findall(r"jump (\w+)", line)[0]
                    if label in self.nodes:
                        self.nodes[label]["connections"].append(jump_label)

                elif re.match(r"call (\w+)", line):
                    call_label = re.findall(r"call (\w+)", line)[0]
                    if label in self.nodes:
                        self.nodes[label]["connections"].append(call_label)
                        self.call_stack.append((label, line_number))

                elif re.match(r"return", line):
                    if self.call_stack:
                        return_label, return_line_number = self.call_stack.pop()
                        if label in self.nodes and return_label in self.nodes:
                            self.nodes[label]["connections"].append(return_label)
                        label = return_label
                        line_number = return_line_number


                elif re.match(r"menu:", line):
                    menu_start_index = line_number
                    for i in range(menu_start_index + 1, len(lines)):
                        option_line = lines[i].strip()
                        if re.match(r'"[^"]*":', option_line):
                            if i + 1 < len(lines):
                                jump_label_search = re.findall(r'jump (\w+)', lines[i + 1].strip())
                                call_label_search = re.findall(r'call (\w+)', lines[i + 1].strip())
                                if jump_label_search:
                                    jump_label = jump_label_search[0]
                                    self.nodes[label]["connections"].append(jump_label)
                                elif call_label_search:
                                    call_label = call_label_search[0]
                                    self.nodes[label]["connections"].append(call_label)
                                    self.call_stack.append((label, line_number))
                            else:
                                continue
                        elif option_line == "":
                            break

            line_number += 1


class NscriptParser:
    def __init__(self, file_list):
        self.file_list = file_list
        self.nodes = {}

    def parse_file(self):
        for file_name in self.file_list:
            with open(file_name, 'r', encoding='utf-8') as f:
                data = f.read()
                rpy_node = RpyNode(data, file_name)
                rpy_node.parse_text()
                self.nodes.update(rpy_node.nodes)

    def build_graph(self):
        G = nx.DiGraph()
        for label, node in self.nodes.items():
            G.add_node(label, file=node["file"])
            for connection in node["connections"]:
                G.add_edge(label, connection)
        return G

    def plot_graph(self, G):
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", node_shape="s", font_size=10, font_weight="bold", alpha=0.5, linewidths=40)
        plt.show()

    def plot_graph_with_plotly(self, G):
        pos = nx.spring_layout(G, k=0.2)

        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines')

        node_x = [pos[node][0] for node in G.nodes()]
        node_y = [pos[node][1] for node in G.nodes()]

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers',
            hoverinfo='text',
            marker=dict(
                showscale=True,
                colorscale='YlGnBu',
                reversescale=True,
                color=[],
                size=10,
                colorbar=dict(
                    thickness=15,
                    title='Node Connections',
                    xanchor='left',
                    titleside='right'
                ),
                line_width=2))

        node_adjacencies = []
        node_text = []
        for node, adjacencies in enumerate(G.adjacency()):
            node_adjacencies.append(len(adjacencies[1]))
            node_text.append(f'{adjacencies[0]} - # of connections: {len(adjacencies[1])}')

        node_trace.marker.color = node_adjacencies
        node_trace.text = node_text

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            title='Network Graph',
                            titlefont_size=16,
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                        )

        fig.show()


def get_rpy_files(directory):
    file_list = []
    for filename in os.listdir(directory):
        if filename.endswith('.rpy'):
            file_list.append(os.path.join(directory, filename))
    return file_list


if __name__ == "__main__":
    rpy_files_path = "C:\\Users\\cstec\\Desktop\\Stuff\\craweler\\rpy_files"
    file_list = get_rpy_files(rpy_files_path)
    parser = NscriptParser(file_list)
    parser.parse_file()
    G = parser.build_graph()
   # parser.plot_graph(G)
    parser.plot_graph_with_plotly(G)
   # parser.plot_pretty()
   # net = Network()
  #  net.from_nx(G)
  #  net.show("visual.html")
    print("Total nodes:", len(G.nodes), "Total edges:", len(G.edges))
