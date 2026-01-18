# Tutorial: Models Updated for Minecraft Java Edition 1.21.11

[Tutorial Models Reference](https://minecraft.wiki/w/Tutorial:Models)

## Introduction

**Block models** are used to depict all the blocks in the game, whereas **item models** are used to display the items in the player's hand, on their head (helmets and hats), on the ground, in the inventory, in item frames, and on armor stands. As there are different variants of some blocks, **block states** are used to link these with the corresponding models. Each model and each block state has its own file, which is of the `.json` format. Even the icons used in the inventory are defined in these files.

## File Path

In JSON files of models and block states, the resource location in the form of `namespace:path` (the `minecraft` namespace can be omitted) is used to represent the local file path.

In these files, the path corresponding to the resource location `namespace:path` is `assets/namespace/object_type/path.suffix`, where the path can contain subfolders separated by `/`, such as `namespace:foo/bar/baz` (`foo` and `bar` are folders, `baz` is the real file name).

The object specified by a resource location and its corresponding object type and suffix are as follows:

| Object       | `object_type` substitution | `suffix` substitution |
| ------------ | -------------------------- | --------------------- |
| Block States | `blockstates`              | `json`                |
| Models       | `models`                   | `json`                |
| Textures     | `textures`                 | `png`                 |

## Block States

There are several different variants of some blocks (like doors, which can be open or closed). Each block has its own blockstates definition file, which lists all its existing variants and links them to their corresponding models. Blocks can also be composed of several different models at the same time, called "multipart". The models are then used depending on the block states of the block.

These files are stored in the following folder: `assets/namespace/blockstates`. The files are used directly based on their filename.

### Example: Wall Torch

The wall torch has several variants: It can be placed at a wall facing in four different directions. This example is taken from the file `wall_torch.json`, which can be found at `assets/minecraft/blockstates`.

```json
{
  "variants": {
    "facing=east": { "model": "block/wall_torch" },
    "facing=south": { "model": "block/wall_torch", "y": 90 },
    "facing=west": { "model": "block/wall_torch", "y": 180 },
    "facing=north": { "model": "block/wall_torch", "y": 270 }
  }
}
```

A torch can be placed on all four sides of a block and therefore needs four different variants, one for each side. These are called `facing=east`, `facing=west`, `facing=south`, and `facing=north`. All four variants use `block/wall_torch` as their model, which is rotated by a multiple of 90 degrees around the `y` axis to align with the different sides of the block they are placed on.

### Example: Grass Block

The grass block has two variants, whereby the first one holds four different models. This example is taken from the file `grass_block.json`, which can be found at `assets/minecraft/blockstates`.

```json
{
  "variants": {
    "snowy=false": [
      { "model": "block/grass_block" },
      { "model": "block/grass_block", "y": 90 },
      { "model": "block/grass_block", "y": 180 },
      { "model": "block/grass_block", "y": 270 }
    ],
    "snowy=true": { "model": "block/grass_block_snow" }
  }
}
```

The non-snow-covered grass block (`snowy=false`) holds four models, which all use the same block model, but each one is rotated by a multiple of 90 degrees. As there are four models and the `weight` tag is not used for any of them, each one has a chance of 25% to be used every time a block is placed.

### Example: Oak Fence

The oak fence uses the `multipart` format. This example is taken from `oak_fence.json` in `assets/minecraft/blockstates`.

```json
{
  "multipart": [
    { "apply": { "model": "block/oak_fence_post" } },
    {
      "when": { "north": "true" },
      "apply": { "model": "block/oak_fence_side", "uvlock": true }
    },
    {
      "when": { "east": "true" },
      "apply": { "model": "block/oak_fence_side", "y": 90, "uvlock": true }
    },
    {
      "when": { "south": "true" },
      "apply": { "model": "block/oak_fence_side", "y": 180, "uvlock": true }
    },
    {
      "when": { "west": "true" },
      "apply": { "model": "block/oak_fence_side", "y": 270, "uvlock": true }
    }
  ]
}
```

While the first model, the fence post, is always used, the other models are used only if certain conditions are met. Here the sides of the fence are applied only if there is another adjacent block next to this one. As there is just one model for the post and another one for all the sides of the fence, which then is rotated by increments of 90 degrees, the amount of models needed for all the different possible set-ups of fences can be reduced to two.

### Block State Rotation (NEW in 1.21.11)

As of Minecraft 1.21.11, block state variants can now be rotated around the Z axis in addition to X and Y:

```json
{
  "variants": {
    "facing=north": { "model": "block/example", "x": 0, "y": 0, "z": 0 },
    "facing=east": { "model": "block/example", "x": 0, "y": 0, "z": 90 },
    "facing=south": { "model": "block/example", "x": 0, "y": 0, "z": 180 },
    "facing=west": { "model": "block/example", "x": 0, "y": 0, "z": 270 }
  }
}
```

The `z` field accepts integer values of 0 (default), 90, 180, and 270 degrees. Rotation around Z is applied after X and Y rotations.

## Block Models

The folder `assets/namespace/models/block` holds the model files for all the specified variants. The names of the files can be changed, but must always correspond with the names used in the variant files.

Block models are defined using a JSON structure that supports the following properties:

- **parent**: Loads a different model from the given path. Can be set to `builtin/generated` to use a model created from the specified icon.
- **ambientocclusion**: Whether to use ambient occlusion (`true` - default) or not (`false`).
- **display**: Holds the different places where item models are displayed (thirdperson_righthand, thirdperson_lefthand, firstperson_righthand, firstperson_lefthand, gui, head, ground, fixed).
- **textures**: Holds the textures of the model as resource locations or texture variables.
- **elements**: Contains all the elements (cuboids) of the model.

### Element Structure

Each element in the `elements` array can have:

- **from**: Start point of a cuboid `[x, y, z]` (values -16 to 32)
- **to**: Stop point of a cuboid `[x, y, z]` (values -16 to 32)
- **rotation**: Defines rotation around one or multiple axes (NEW in 1.21.11)
- **shade**: Whether shadows are rendered (default: true)
- **faces**: Contains properties for each face (down, up, north, south, west, east)

### Model Rotation (UPDATED in 1.21.11)

**NEW FORMAT (1.21.11+)**: Minecraft now supports rotation around multiple axes in a single element:

```json
{
  "rotation": {
    "origin": [8, 8, 8],
    "x": 22.5,
    "y": 45.0,
    "z": 0.0
  }
}
```

Where:

- **origin**: Center point of rotation `[x, y, z]`
- **x, y, z**: Rotation angles in degrees (as floats, any value allowed - no longer limited to 22.5 increments)
- **rescale** (optional): Scale on non-rotated axes by 1 + 1/cos(angle) - 1

The rotations are applied in order: X first, then Y, then Z.

**OLD FORMAT (still supported)**:

```json
{
  "rotation": {
    "origin": [8, 8, 8],
    "axis": "y",
    "angle": 45
  }
}
```

If both formats are present, the old format (axis/angle) takes precedence.

### Face Properties

For each face in the `faces` object:

- **uv**: `[x1, y1, x2, y2]` - Defines the area of texture to use (works in percentages of 16)
- **texture**: Specifies the texture as a texture variable (prepended with `#`)
- **cullface**: Prevents rendering when another block is adjacent (down, up, north, south, west, east)
- **rotation**: Rotates texture by 0, 90, 180, or 270 degrees
- **tintindex**: Applies a tint based on hardcoded color indices (-1 for no tint)

### Example: Standing Torch

```json
{
  "ambientocclusion": false,
  "textures": {
    "particle": "#torch"
  },
  "elements": [
    {
      "from": [7, 0, 7],
      "to": [9, 10, 9],
      "shade": false,
      "faces": {
        "down": { "uv": [7, 13, 9, 15], "texture": "#torch" },
        "up": { "uv": [7, 6, 9, 8], "texture": "#torch" }
      }
    },
    {
      "from": [7, 0, 0],
      "to": [9, 16, 16],
      "shade": false,
      "faces": {
        "west": { "uv": [0, 0, 16, 16], "texture": "#torch" },
        "east": { "uv": [0, 0, 16, 16], "texture": "#torch" }
      }
    },
    {
      "from": [0, 0, 7],
      "to": [16, 16, 9],
      "shade": false,
      "faces": {
        "north": { "uv": [0, 0, 16, 16], "texture": "#torch" },
        "south": { "uv": [0, 0, 16, 16], "texture": "#torch" }
      }
    }
  ]
}
```

And the texture assignment:

```json
{
  "parent": "block/template_torch",
  "textures": {
    "torch": "block/torch"
  }
}
```

### Example: Simple Cube

```json
{
  "elements": [
    {
      "from": [0, 0, 0],
      "to": [16, 16, 16],
      "faces": {
        "down": { "texture": "#down", "cullface": "down" },
        "up": { "texture": "#up", "cullface": "up" },
        "north": { "texture": "#north", "cullface": "north" },
        "south": { "texture": "#south", "cullface": "south" },
        "west": { "texture": "#west", "cullface": "west" },
        "east": { "texture": "#east", "cullface": "east" }
      }
    }
  ]
}
```

### Example: Sapling with Rotation

```json
{
  "ambientocclusion": false,
  "textures": {
    "particle": "#cross"
  },
  "elements": [
    {
      "from": [0.8, 0, 8],
      "to": [15.2, 16, 8],
      "rotation": {
        "origin": [8, 8, 8],
        "axis": "y",
        "angle": 45,
        "rescale": true
      },
      "shade": false,
      "faces": {
        "north": { "uv": [0, 0, 16, 16], "texture": "#cross" },
        "south": { "uv": [0, 0, 16, 16], "texture": "#cross" }
      }
    },
    {
      "from": [8, 0, 0.8],
      "to": [8, 16, 15.2],
      "rotation": {
        "origin": [8, 8, 8],
        "axis": "y",
        "angle": 45,
        "rescale": true
      },
      "shade": false,
      "faces": {
        "west": { "uv": [0, 0, 16, 16], "texture": "#cross" },
        "east": { "uv": [0, 0, 16, 16], "texture": "#cross" }
      }
    }
  ]
}
```

## Item Models (MAJOR UPDATE - 1.21.4+)

**IMPORTANT**: Item models underwent a significant system change in version 1.21.4. The override-based system has been replaced with a component-based model selection system.

### New Item Model System (1.21.4+)

Items now have their models defined through the `minecraft:item_model` data component. This is a data-driven approach rather than resource pack predicates.

**File Structure**:

```
assets/namespace/items/itemname.json
```

**File Content**:

```json
{
  "model": {
    "type": "minecraft:model",
    "model": "namespace:item/custom_item"
  }
}
```

The `model` field should point to your item model JSON in the models directory, which follows the standard item model format.

### Item Model JSON Format

Item models use a similar structure to block models:

- **parent**: Can be `item/generated` (for 2D textures) or a custom model path
- **display**: Controls how the item appears in different contexts (thirdperson_righthand, thirdperson_lefthand, firstperson_righthand, firstperson_lefthand, gui, head, ground, fixed)
  - Each position has **rotation**, **translation**, and **scale**
  - Translation values are clamped between -80 and 80
  - Scale values greater than 4 are displayed as 4
- **textures**: Defines texture layers (layer0, layer1, etc.) for generated models, or custom texture variables
- **elements**: Custom 3D model elements (similar to block models)
- **gui_light**: Can be "front" (flat shading) or "side" (block-like shading), defaults to "side"

### Example: 2D Item (Bed)

```json
{
  "parent": "item/generated",
  "textures": {
    "layer0": "item/red_bed"
  }
}
```

### Example: Item with Display Properties (Torch)

```json
{
  "parent": "item/generated",
  "textures": {
    "layer0": "block/torch"
  },
  "display": {
    "thirdperson_righthand": {
      "rotation": [-90, 0, 0],
      "translation": [0, 1, -3],
      "scale": [0.55, 0.55, 0.55]
    },
    "thirdperson_lefthand": {
      "rotation": [-90, 0, 0],
      "translation": [0, 1, -3],
      "scale": [0.55, 0.55, 0.55]
    },
    "firstperson_righthand": {
      "rotation": [0, -135, 25],
      "translation": [0, 4, 2],
      "scale": [1.7, 1.7, 1.7]
    },
    "firstperson_lefthand": {
      "rotation": [0, 135, -25],
      "translation": [0, 4, 2],
      "scale": [1.7, 1.7, 1.7]
    },
    "gui": {
      "rotation": [30, 225, 0],
      "translation": [0, 0, 0],
      "scale": [0.625, 0.625, 0.625]
    }
  }
}
```

### Using Custom Model Data (1.21.4+)

While the old override system is removed, custom model data still works through the item component system:

```json
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "item/custom_sword"
  }
}
```

To use it, provide an item with the `minecraft:custom_model_data` component:

```
/give @s diamond_sword[minecraft:item_model=namespace:item/custom_sword]
```

## Resource Pack Compatibility

Minecraft 1.21.11 uses **Pack Format 74** for resource packs. When creating or updating resource packs, ensure your `pack.mcmeta` file specifies the correct format version:

```json
{
  "pack": {
    "pack_format": 74,
    "description": "Your Pack Description"
  }
}
```

## Summary of Changes for 1.21.11

1. **Block Model Rotation**: Now supports multi-axis rotation (X, Y, Z) with no angle restrictions
2. **Block State Variants**: Can now include Z-axis rotation (90° increments)
3. **Item Models**: Complete system overhaul in 1.21.4 - no longer uses overrides, now component-based
4. **Resource Pack Format**: Updated to pack format 74
5. **Display Properties**: Translation still clamped to ±80, scale still capped at 4

For the most up-to-date information, visit the [Minecraft Wiki Models Tutorial](https://minecraft.wiki/w/Tutorial:Models).
