Rendering
=====================

### maya_batch_render.sh
This script will simply render a maya scene to specified path.
Can be useful for queuing multiple scenes on the same machine.

### maya_render_passes.py
Running the script will create a render layer and a number of render passes and contribution maps, already connected with each other.

The name of the render layer created can be changed by modifying the variable which holds it: **renderLayerName**. 

All of the render passes are contained in the list called **passesNames**, so you can add  your own by just modifying the values in that list.

Check [this video](https://vimeo.com/68691232) for further infos.
