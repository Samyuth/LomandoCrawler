# Renpy Parsers

2 Parsers with example parses of the popular renpy game doki doki literature club a popular renpy game

## More Connections Parser
- Handles implicit flows (this is when execution of some label has no jump call statement to get to a new label getting to the next label is through the flow of the code
- Handles return statements using call stack
- Almost everynode will have some type of connection (edge) although there might be no way for a choice you can make to reach that node
- Graph has less meaningfull connections (note this is only for implicit flow) as sometimes the implicit flow or return connections are not useful
- Might be more difficult to view due to all the extra connections than accurate connections parser
- Plotted using plotly however there is another choice to graph with using pyplot (Plotly is recomended very clean easy to navigate network graph)
- Folder containg parser contains graph with example parse of doki doki literature club (png of the graph)
## Accurate Connections Parser
- Does not handle implicit flows
- Handles return statements using call stack
- Likely many nodes will have no connection if the game script has implicit flows or is not fully choice based game (a node with no connection means there is no way to reach with a choice some different game logic is being used) 
- Graph has many less edges than if it were to be parsed with more connection parser but connections made are more meaningfull
- Nodes with no connection are easily understandable as no choice can be made to reach them
- Might be easier to view due to less edges (node amount remains the same)
- Plotted using plotly however there is another choice to graph with using pyplot (Plotly is recomended very clean easy to navigate network graph)
- Folder containg parser contains graph with example parse of doki doki literature club (png of the graph)
## Parser Guide
- Download folder containing parser of your choice
- Put all of your rpy files into a folder (note usually it will just be one file however some games like doki doki use multiple files)
- Change the line in the code rpy_files_path to contain the path to the folder containing the rpy files (use the absolute path of the folder as usually no errors with finding the folder)
- Choose to plot with pyplot or with plotly #parser.plot_graph(G) (pyplot) #parser.plot_graph_with_plotly(G) (plotly) comment out whichever plotting function you dont want and leave the other uncommented (Plotly highly recommended)
- Done a network graph of the parsed game will open in your browser

## Development Plans
- Continue development for doki doki parse as it seems to be one of the more advanced renpy games
- Handle implicit flows more properly (that is when they actually make a meaninfull connection)
- Try to account for random logic for a node which doki doki uses
- Look at different ways to plot plotly is very nice but pyplot is not as nice for graphs with many nodes like doki doki
- Possibly look into pulling images from the game and using those to represent choices as the nodes
For now those are the next major development steps
