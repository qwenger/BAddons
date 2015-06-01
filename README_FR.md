# BAddons
Collection d'addons pour Blender

*Note: cette documentation est également disponible en [anglais](https://github.com/qwenger/BAddons/blob/master/README.md).
La version anglaise peut être considérée comme faisant référence.*

*Note: le nom de fichier `README_FR` a été choisi à la place de `LISEZMOI` dans un souci d'uniformité.*

## A propos

Le dépôt `BAddons` contient des addons (c.-à-d. des morceaux de scripts conçus pour étendre des fonctionalités) pour le programme de 3D [Blender](https://www.blender.org/).

Ces addons sont libres et open-source (licenciés sous GPL, en version 2+), voir [`LICENSE`](https://github.com/qwenger/BAddons/blob/master/LICENSE) pour plus d'informations.

## Structure du dépôt

Le dépôt est organisé comme suit:

Dossier principal:

- divers fichiers liés au dépôt (`.gitignore`, des `README`, `LICENCE`)
- un fichier [Pickle](https://docs.python.org/3/library/pickle.html), `ADDONS_LIST.pkl`, qui contient une représentation sérialisée de la structure du dépôt; il est utilisé par le fichier suivant:
- un addon Python, [`matpi_addons_collection.py`](https://github.com/qwenger/BAddons/blob/master/matpi_addons_collection.py), qui a pour but de faciliter le maniement des autres (téléchargement, mise à jour, suppression, etc.). Voir ci-dessous.
- divers dossiers, contenant chacun un addon Python. Voir plus bas pour plus d'informations à propos de chaque addon.

## La Collection d'Addons de Matpi (Configurateur)

L'addon `Addons Collection`, parfois appelé *addon maître* ou *addon master*, a été écrit dans le but de fournir aux utilisateurs une gestion simplifiée des addons de ce dépôt dans leur propre configuration de Blender, p.ex. pour garder les addons à jour par rapport à la dernière version sortie.

De ce fait, un utilisateur de ce script ne doit télécharger et installer à la main que celui-ci, qui une fois activé dans Blender affiche des options pour télécharger et installer les autres de manière très simple et rapide.

L'utilisation de cet addon maître est fortement recommandée pour une utilisation optimale des éléments de BAddons. Bien entendu, il est également possible de télécharger chaque addon séparément.

Version courante: [](matpi_addons_collection)1.1[](/)

Lien: [`matpi_addons_collection.py`](https://github.com/qwenger/BAddons/blob/master/matpi_addons_collection.py)

## Description des addons

| Nom     | Description | Version courante |
|---------|-------------|:----------------:|
| [3DView_BorderLines_BMeshEdition](https://github.com/qwenger/BAddons/blob/master/3DView_BorderLines_BMeshEdition/3dview_border_lines_bmesh_edition.py) | Fournit un moyen de surligner les lignes de bord (les arêtes connectées à exactement une face) de maillages Blender pour la vérification de la topologie. | [](3dview_border_lines_bmesh_edition)1.9[](/) |
| [3DView_MeshStatistics](https://github.com/qwenger/BAddons/blob/master/3DView_MeshStatistics/3dview_mesh_statistics.py) | Calcule certaines informations à propos du maillage Blender courant, à savoir le volume, l'aire, la position du centre de masse. | [](3dview_mesh_statistics)1.0[](/) |
| [3DView_SynchronizeViews](https://github.com/qwenger/BAddons/blob/master/3DView_SynchonizeViews/3dview_synchronize_views.py) | Fournit une option pour loquer le point de vue dans une région de vue 3D Blender par rapport à une autre vue 3D. Cet addon est actuellement dans une phase de profonde réécriture. | [](3dview_synchronize_views)1.0[](/) |
| [GameEngine_DecompileRuntime](https://github.com/qwenger/BAddons/blob/master/GameEngine_DecompileRuntime/game_engine_decompile_runtime.py) | Ré-extrait le fichier .blend original à partir d'un fichier BlenderPlayer exécutable; ceci prouve notamment que l'option "save as Game Engine Runtime" est reversible. | [](game_engine_decompile_runtime)1.0[](/) |
| [GameEngine_LegacyStart](https://github.com/qwenger/BAddons/blob/master/GameEngine_LegacyStart/game_engine_legacy_start.py) | Réactive l'option de démarrage du BGE à partir de n'importe quel mode de rendu, supprimée par défaut depuis la version 2.73, en pressant la touche P dans la vue 3D. | [](game_engine_legacy_start)1.1[](/) |
| [Node_LocationPanel](https://github.com/qwenger/BAddons/blob/master/Node_LocationPanel/node_location_panel.py) | Affiche la position exacte d'un noeud dans son espace 2D; ceci est plutôt un addon de démo, probablement inutile pour la plupart des utilisateurs. | [](node_location_panel)1.1[](/) |

