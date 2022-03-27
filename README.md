# LomandoCrawler
This project initially started to parse the choice based creepy pasta style webgame [Lomando](https://lomando.com/) into a graph representation. It can now do the same for the visual novel game Tsukihme which was built with the NScripter Engine.

Future plans include building a gui to interact with this graph representation. Currently pyvis and networkx are used for visualization.

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
