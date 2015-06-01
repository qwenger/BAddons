# BAddons
Blender addons collection

*Note: throughout this documentation, the syntax* "addon" *is being used.*

## About

The `BAddons` repository contains addons (i.e. script snippets meant to extend functionality) for the 3D software [Blender](https://www.blender.org/).

These addons are free and open-source (GPL-licensed, in version 2+), see [`LICENCE`](https://github.com/qwenger/BAddons/blob/master/LICENSE) for more information.

## Structure of the repository

The repository is organized as follows:

Main folder:

- general repository files (`.gitignore`, `README`'s, `LICENCE`)
- a [Pickle](https://docs.python.org/3/library/pickle.html) file, `ADDONS_LIST.pkl`, which contains a serialized representation of the repo's structure; it is used by the next file:
- a Python addon, [`matpi_addons_collection.py`](https://github.com/qwenger/BAddons/blob/master/matpi_addons_collection.py), which is intended to facilitate handling of others (dowloading, updating, deletion, etc.). See below.
- various folders, containing each a Python addon. See below for more information about each addon.

## Matpi's Addons Collection (Configurator)

The `Addons Collection` addon, sometimes refered to as *addon master*, has been written with the goal of providing to users a simplified way to manage addons of this repository within their own Blender configuration, f.ex. to keep them updated against latest released version.

Thus, a user taking advantage of this script only needs to download and install that one per hand, which will once enabled in Blender display options to download and install others very quickly and easily.

Usage of this addon master is strongly recommended for a ultimate experience with BAddons items.

## Description of the addons

| Name    | Description | Current version |
|---------|-------------|-----------------|
| 3DView_BorderLines_BMeshEdition | Provides a way to highlight border lines (edges connected to exactly one face) of Blender meshes to help checking topology. | 1.9 |
| 3DView_MeshStatistics | Computes some information about current Blender mesh, i.e. volume, area, position of the center of mass. | 1.0 |
| 3DView_SynchronizeViews | Provides an option to lock viewpoint in a Blender 3D view region to the one of another view region. | 1.0 |
| GameEngine_DecompileRuntime | Re-extracts the original .blend file out of a runtime executable BlenderPlayer file; this i.e. proves that the "save as Game Engine Runtime" option is reversible. | 1.0 |
| GameEngine_LegacyStart | Re-enables the 2.73-deleted option of starting the BGE from any rendering mode by pressing the P-Key in the 3D view. | 1.1 |
| Node_LocationPanel | Displays the exact position of a node in its 2D space; this is more of a demo addon, probably useless to most of the users. | 1.1 |

