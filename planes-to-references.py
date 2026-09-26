import bpy

selobjs = [obj for obj in bpy.context.selected_objects if obj.type == 'MESH']

currentcollection = bpy.context.collection

for objmesh in selobjs:
    img = None
    if objmesh.data.materials:
        for mat in objmesh.data.materials:
            if mat and mat.use_nodes:
                for node in mat.node_tree.nodes:
                    if node.type == 'TEX_IMAGE' and node.image:
                        img = node.image
                        break
            if img:
                break
                
    if not img:
        continue

    loc = objmesh.location.copy()
    rot = objmesh.rotation_euler.copy()
    scale = objmesh.scale.copy()
    name = objmesh.name

    objempty = bpy.data.objects.new(name=f"{name}_Reference", object_data=None)
    currentcollection.objects.link(objempty)
    
    objempty.empty_display_type = 'IMAGE'
    objempty.data = img 
    
    objempty.location = loc
    objempty.rotation_euler = rot
    objempty.empty_display_size = max(scale.x, scale.y)
    
    bpy.data.objects.remove(objmesh, do_unlink=True)

bpy.context.view_layer.update()
