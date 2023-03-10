import math
import unreal

# Get a reference to Unreal Engine's Editor Utility Library
editor_util = unreal.EditorUtilityLibrary()

# Get a list of selected assets in the editor
selected_assets = editor_util.get_selected_assets()

# Count how many assets were selected
num_assets = len(selected_assets)

# Count how many textures with non-power-of-two dimensions were found
not_pow = 0

# Loop over each selected asset
for assets in selected_assets:

    # Get the name and path of the asset
    asset_name = assets.get_fname()
    asset_path = assets.get_path_name()

    try:
        # Get the dimensions of the texture
        x_size = assets.blueprint_get_size_x()
        y_size = assets.blueprint_get_size_y()

        # Check if both dimensions are power of two
        is_x_valid = math.log(x_size, 2).is_integer()
        is_y_valid = math.log(y_size, 2).is_integer()

        if not is_x_valid or not is_y_valid:

            # Log a warning message if dimensions are not power of two
            unreal.log('{} is not power of two ({}, {})'.format(asset_name, x_size, y_size))
            unreal.log('Its path is {}'.format(asset_path))
            not_pow += 1
    except Exception as err:

        # Log an error message if the asset is not a texture
        unreal.log('{} is not a Texture - {}'.format(asset_name, err))

# Log a summary message with the number of assets checked and the number of problematic textures found
unreal.log('{} checked, {} textures found problematic'.format(num_assets, not_pow))