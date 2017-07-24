# Python packages

# We don't usually store all of our files in our computer in the same location.
# We use a well-organized hierarchy of directories for easier access.

# Similar files are kept in the same directory, for example, we may keep all the songs in the "music" directory.
# Analogous to this, Python has packages for directories and modules for files.

# As our application program grows larger in size with a lot of modules, we place similar modules in
# one package and different modules in different packages.
# This makes a project (program) easy to manage and conceptually clear.

# Similar, as a directory can contain sub-directories and files, a Python package can have sub-packages and modules.

# A directory must contain a file named __init__.py in order for Python to consider it as a package.
# This file can be left empty but we generally place the initialization code for that package in this file.

#                           Game
#                         [Package]
#         |-------------------|--------------------|
#         |                   |                    |
#         |                   |                    |
#         V                   V                    V
#     __init.py__           Sound                Engine
#                         [Package]             [Package]
#                          |-> pause.py           |-> injector.py
#                          |-> play.py            |-> renderer.py

# importing a module from a package

# We can import modules from packages using the dot (.) operator.
# For example, if want to import the start module in the above example, it is done as follows.

# import Game.Sound.injector => equal usage: from Game.Sound import injector
# Let's import draw_monster() function from renderer.py
# from Game.Engine.renderer import draw_monster
