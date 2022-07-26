# LomandoCrawler
This project initially started to parse the choice based creepy pasta style webgame [Lomando](https://lomando.com/) into a graph representation. It can now do the same for the visual novel game Tsukihme which was built with the NScripter Engine.

Future plans include building a gui to interact with this graph representation. Currently pyvis and networkx are used for visualization.

Adittionally now any choice based youtube storyline can be parsed and if the network.json file rendered is placed in the root of the Node-UI directory and a node.js server started a dynamic graph chart will be displayed on localhost:3000.

## Dependencies
### Python:
* networkx
* matplotlib
* pyvix
* numpy
* requests
* bs4
### Tsukihime (to be placed in Tsukihime/):
* nscript.dat from Tsukihime game files
* [NSDec](http://nscripter.insani.org/sdk.html) decompiler for the nscript.dat
### Node UI
* node.js
* express
* fs
* path
* vis-network
### Electron UI
* node.js
* react.js
* electron.js

## References and docs

[NScriptr API](http://nscripter.insani.org/reference/)
[Creating an Electron App](https://www.section.io/engineering-education/desktop-application-with-react/)
