bl_info = {
    "name": "Stacker",
    "description": "A modern revival of Autodesk Slicer for Fusion 360",
    "author": "Tynan Purdy",
    "version": (0,1),
    "blender": (2,80,0), # minimum blender version required (no reference for what it should be so far)
    "support": "TESTING",
    "category": "Object"
}

import bpy

def register():
    print("Hello there")

def unregister():
    print("General Kenobi")


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()