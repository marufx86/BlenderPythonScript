# Blender Python Scripts

This repository contains a collection of Python scripts to automate and optimize tasks in Blender. These scripts are designed to enhance efficiency when working with objects, materials, and transformations.

## Scripts Overview

1.  **Rename Objects by Material**
    *   Renames selected mesh objects based on their assigned materials.  If an object has more than one material, it will be renamed to "Z\_ErrorMaterial".  If it has only one material, it will be renamed to the material's name.

2.  **Delete Unused Materials**
    *   Safely deletes materials not used by any object in the scene.

3.  **Ungroup, Unparent, and Clear History**
    *   Ungroups all objects, clears parenting, and applies transformations (location, rotation, scale).

4.  **Delete Empty Groups**
    *   Deletes all empty parent objects (groups) in the scene. An empty group is an empty object with no children.

5. **Assign New Material Based on Object Name**
   * For each selected mesh, this function creates (or reuses) a material with a name derived from the mesh's name.  It replaces `SM_` with `M_` or, if the object name doesn't start with `SM_`, it prefixes the object name with `M_`.  The new material is then assigned to the first material slot of the mesh. If no material slot exists, a new one is created.

## Usage

1.  Open the Blender Python Console or Script Editor.
2.  Copy and paste the desired script into the editor.
3.  Run the script to execute the functionality.  For some scripts, you need to select the relevant object in the viewport before running the script.
