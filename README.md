# The umamusume armature refiner, useless bone deleter and rigifier 3-in-1 super blender 3.6 addon 3000!
# Codename: Umayuru

Fork of [Blender-Uma-Addon](https://github.com/XiaoVonline/Blender-Uma-Addon) with Blender 3.6 LTS support

This SHOULD be compatible with newer versions as the Blender 3.6 fallbacks are defined as other functions in respective files.

# Requires:

### Blender MMD Tools

**[Repository](https://github.com/MMD-Blender/blender_mmd_tools)**

Recommended version: **[2.10.3](https://github.com/MMD-Blender/blender_mmd_tools/releases/download/v2.10.3/mmd_tools-v2.10.3.zip)**

### Miku Miku Rig

**[Repository](https://github.com/XiaoFFGe/MikuMikuRig)**

Recommended version: **[2.58 LTS](https://github.com/XiaoFFGe/MikuMikuRig/releases/download/MikuMikuRig-2.58-LTS/MikuMikuRig.3.6-2.58.LTS.zip)**

# Tutorial on how to use:

https://www.youtube.com/watch?v=q690uRBSCww

(not an ad by the way)

# If you can do it reading instead of watching:

0. Make sure to install Umayuru, MMD Tools and MMR
1. Export your umamusume from [UmaViewer](https://github.com/katboi01/UmaViewer) 
2. Go to Blender and import your umamusume
3. Select your umamusume's armature
4. Click 'Set Bone Collections', then 'Refine Structure' and then click 'Del' (make sure before clicking Del 'handle', 'face', 'others' are highlighted). Make sure no errors appear after each substep, if something went wrong try to fix it yourself or open an issue.

#### Optional:

5. Select your umamusume's mesh and click Shading
5.1. Shading creates a Geometry node in your umamusume's mesh named Uma Outlines. This step is optional, but you can hide it.

6. Select your umamusume's armature and go to MMR
7. Click "Generate controller for umamusume"

# This is what you should get:

<img width="623" height="655" alt="result" src="https://github.com/user-attachments/assets/3fdb7044-1cbf-4974-a43a-35c4d08704d9" />