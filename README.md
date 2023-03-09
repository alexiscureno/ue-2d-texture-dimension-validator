# Unreal Texture Power of Two Checker
# ue-2d-texture-dimension-validator
This script checks whether the selected textures in Unreal Engine have dimensions that are power of two.

# Requirements
* Unreal Engine 4.26 or later
* Python 3.7 or later installed


# Usage
1. Select the textures you want to check in the Content Browser.
2. Go to **File > Execute Python Script** 
3. The script will log any texture that is not power of two and its file path.

# Notes
* This script only works with textures. If you select other asset types, it will ignore them.
* The script only fechs the fist mip level of the texture.
* The script assumes that the X and Y dimensions are the same.
