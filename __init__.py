from .addons.umayuru import register as addon_register, unregister as addon_unregister

bl_info = {
    "name": 'Umayuru',
    "blender": (3, 6, 0),
    "category": "URA",
    "tracker_url": 'https://github.com/voyager-py/umayuru'
}

def register():
    addon_register()

def unregister():
    addon_unregister()

    