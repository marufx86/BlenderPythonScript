import bpy

def rename_objects_by_material():
    """Renames selected meshes based on their materials."""

    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            material_count = len(obj.material_slots)

            if material_count > 1:
                obj.name = "Z_ErrorMaterial"
            elif material_count == 1:
                material_name = obj.material_slots[0].material.name
                obj.name = material_name

    print("Renamed selected meshes based on material count.")

# Call the function to rename objects
rename_objects_by_material()

################################################################################

import bpy

def delete_unused_materials():
    """Safely deletes unused materials from the scene."""

    # Get a list of all materials in the scene
    materials_to_delete = []

    for material in bpy.data.materials:
        # Check if the material is used by any objects
        is_used = False
        for obj in bpy.context.scene.objects:
            if obj.type == 'MESH':
                for slot in obj.material_slots:
                    # Check if the material is assigned to the slot
                    if slot.material == material:
                        is_used = True
                        break  # No need to check other slots in the object

            if is_used:
                break  # No need to check other objects

        # If the material is unused, add it to the list for deletion
        if not is_used:
            materials_to_delete.append(material)

    # Delete the unused materials
    for material in materials_to_delete:
        try:
            bpy.data.materials.remove(material)
        except:
            # Handle potential errors during deletion
            print(f"Error deleting material: {material.name}")

    print("Unused materials deleted (if any).")

# Call the function to delete unused materials
delete_unused_materials() 

#############################################################################################################################


## Ungroups, unparents, and clears history for all objects in the scene
import bpy

def ungroup_unparent_clear_history():
    """Ungroups, unparents, and clears history for all objects in the scene."""

    # Switch to object mode if not already
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Get all objects in the scene
    objects = bpy.context.scene.objects

    # Ungroup (Clear Parent and Keep Transformation)
    for obj in objects:
        if obj.parent and obj.parent_type == 'OBJECT':
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')

    print("Ungrouped all objects.")

    # Unparent (Clear Parent)
    for obj in objects:
        if obj.parent:
            bpy.ops.object.parent_clear(type='CLEAR')

    print("Unparented all objects.")

    # Clear object history 
    for obj in objects:
        bpy.ops.object.select_all(action='DESELECT')  # Deselect all
        obj.select_set(True)  # Select the current object
        bpy.ops.object.transform_apply(location=True, rotation=True, scale=True) 

    print("Cleared transformation history for all objects.")

# Run the function
ungroup_unparent_clear_history() 

#############################################################################################################

import bpy

def delete_empty_groups():
    """Deletes all empty groups (empty parent objects) in the scene."""

    # Switch to object mode if not already
    if bpy.context.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')

    # Get all objects in the scene
    objects = bpy.context.scene.objects

    # Delete empty groups
    for obj in objects:
        if obj.type == 'EMPTY' and not obj.children:  # Check if empty and has no children
            bpy.data.objects.remove(obj, do_unlink=True)  # Remove the empty object

    print("Deleted all empty groups.")


##########################################################################################################

import bpy

def assign_new_material_based_on_object_name():
    """
    For each selected mesh, this function creates (or reuses) a material with a name
    derived from the mesh's name by replacing 'SM_' with 'M_' and assigns it to the mesh.
    """
    for obj in bpy.context.selected_objects:
        if obj.type == 'MESH':
            # Determine the new material name based on the object's name
            if obj.name.startswith("SM_"):
                new_mat_name = "M_" + obj.name[3:]
            else:
                new_mat_name = "M_" + obj.name  # Fallback if not following the 'SM_' pattern
            
            # Try to get an existing material with the new name, or create a new one
            mat = bpy.data.materials.get(new_mat_name)
            if not mat:
                mat = bpy.data.materials.new(name=new_mat_name)
                print(f"Created new material: {new_mat_name}")
            else:
                print(f"Using existing material: {new_mat_name}")
            
            # Assign the material to the mesh
            # If the object already has material slots, replace the first one;
            # otherwise, create a new material slot.
            if obj.data.materials:
                obj.data.materials[0] = mat
            else:
                obj.data.materials.append(mat)
                
    print("Assigned new materials to all selected meshes.")

# Run the function
assign_new_material_based_on_object_name()


# Run the function
delete_empty_groups() 
