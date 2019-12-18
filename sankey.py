# a function that converts pandas dataframe into a sankey

import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt


def draw_sankey(df):

    # flatten sankey
    flat = []
    for i in range(len(df.columns) - 2):
        subdf = df[[df.columns[i], df.columns[i + 1], 'amount']]
        subdf = subdf.rename(columns={df.columns[i]: 'source',
                                      df.columns[i + 1]: 'target'})
        subdf['start_node'] = df[df.columns[0]]
        flat.append(subdf)
    flat = pd.concat(flat)

    nodes = list(flat['source']) + list(flat['target'])
    nodes = dict.fromkeys(nodes)
    c = 0
    for node in nodes.keys():
        nodes[node] = c
        c += 1

    cmap = plt.cm.get_cmap('viridis')
    color_map = dict()
    start_nodes = list(flat['start_node'].drop_duplicates())
    step = 1 / len(start_nodes)
    node_colors = []
    for i in range(len(start_nodes)):
        rgba = cmap(i * step)
        rgba = tuple(int((255 * x)) for x in rgba[0:3]) + (0.3,)
        rgba = 'rgba' + str(rgba)
        color_map[start_nodes[i]] = rgba
        node_colors.append(rgba)

    sources = []
    targets = []
    values = []
    colors = []
    for index, row in flat.iterrows():
        sources.append(nodes[row['source']])
        targets.append(nodes[row['target']])
        values.append(row['amount'])
        colors.append(color_map[row['start_node']])

    fig = go.Figure(data=[go.Sankey(
                          # Define nodes
                          node=dict(pad=15,
                                    thickness=15,
                                    line=dict(color="black", width=0.01),
                                    label=list(nodes.keys()),
                                    color=node_colors
                                    ),
                          # Add links
                          link=dict(source=sources,
                                    target=targets,
                                    value=values,
                                    color=colors
                                    # label=[]
                                    ))])

    fig.update_layout(title_text="Sankey Diagram", font_size=10)
    fig.show()


# test_sankey = pd.read_excel('results/testsankey.xlsx')
# test_sankey = test_sankey.groupby(['activity_group_name', 'status', 'VerwerkingsMethode'], as_index=False)['amount'].sum()
# draw_sankey(test_sankey)