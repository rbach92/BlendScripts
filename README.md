# BlendScripts

***All of these were created for use in Blender 2.79b. Haven't tested in 2.8 yet.***

Various Python scripts I created to speed up my workflow

Snap Origin to Selected - used in edit mode, this script quickly moves the object's origin to the selected face/vert/edge. Reduces about four manual actions to a hotkey, if you choose to set one.

Duplicate Faces - duplicates selected faces/edges/verts and then separates them into their own mesh. 

Mixamo Rename - just gets rid of the "mixamorig: " prefix that Mixamo attaches to joints. Useful if you want to use Blender's animation retargeting addon or just to clean up the outliner for additional edits to the rig.

Custom menu - a bunch of functions I frequently use. Just wanted them on a hotkey.

Action Cleaner - iterates thru objects and deletes any animations that have no users. Useful for cleaning up a file that makes heavy use of Mixamo animations & the NLA editor. Save a backup as this refreshes the file to release the data blocks.
