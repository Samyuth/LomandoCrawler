# LomandoCrawler
This project initially started to parse the choice based creepy pasta style webgame [Lomando](https://lomando.com/) into a graph representation. It can now do the same for the visual novel game Tsukihme which was built with the NScripter Engine and the youtube game Markiplier in Space.

Future plans include building a gui to interact with this graph representation (in progresss). Currently an Electron app is being developed to visualize the network and interact with the choice tree.

Adittionally any choice based youtube storyline can be parsed and if the network.json file rendered is placed in the root of the Node-UI directory and a node.js server started a dynamic graph chart will be displayed on localhost:3000.

Discord Server: https://discord.gg/yy8bkXBv

## Contributing to the project

To contribute to this project create a fork and open a pull request including any features or bugfixes. The main items right now are creating parsers for different types of visual novel scripts, updating the current parsers and work on the Electron UI. Additionally as mentioned in Issue #10 directory reorginization is needed to combine the different parsers. As it stand right now to create a parser for a different script type simply create a different directory.

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
* flask

## References and documentation
* [NScriptr API](http://nscripter.insani.org/reference/)
* [Creating an Electron App](https://www.section.io/engineering-education/desktop-application-with-react/)
* [Electron Guide](https://medium.com/folkdevelopers/the-ultimate-guide-to-electron-with-react-8df8d73f4c97)
