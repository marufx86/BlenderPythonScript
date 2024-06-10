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
