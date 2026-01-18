# Complete JSON Template Guide - Minecraft 1.21.11

## Overview

This guide provides 14 production-ready JSON templates covering every aspect of block states, block models, and item models for Minecraft Java Edition 1.21.11. All templates are fully documented with inline comments explaining structure and usage.

---

## Quick Start

### 1. Create Resource Pack Structure
```
my-pack/
├── pack.mcmeta
└── assets/
    └── mymod/
        ├── blockstates/
        ├── models/
        │   ├── block/
        │   └── item/
        ├── items/
        └── textures/
```

### 2. Copy pack.mcmeta
Use `pack.mcmeta` [85] and update the description field.

### 3. Create Your First Block
- Copy `blockstate-simple.json` → `assets/mymod/blockstates/my_block.json`
- Copy `blockmodel-cube-textured.json` → `assets/mymod/models/block/my_block.json`
- Create texture file → `assets/mymod/textures/block/my_block.png`

### 4. Create Your First Item
- Copy `itemmodel-generated-simple.json` → `assets/mymod/models/item/my_item.json`
- Copy `itemdefinition-component.json` → `assets/mymod/items/my_item.json`
- Create texture file → `assets/mymod/textures/item/my_item.png`

---

## Template Categories

### Category 1: Block States (4 Templates)

Block states are located in: `assets/namespace/blockstates/`

#### Template 1.1: Simple Directional Block
**File**: `blockstate-simple.json` [71]

Use when: Block has one main property (facing direction)

```json
{
  "variants": {
    "facing=north": { "model": "namespace:block/example" },
    "facing=south": { "model": "namespace:block/example", "y": 180 },
    "facing=east": { "model": "namespace:block/example", "y": 90 },
    "facing=west": { "model": "namespace:block/example", "y": 270 }
  }
}
```

**Customization Points**:
- Replace `facing` with your property name
- Replace `north/south/east/west` with your values
- Adjust Y rotation values as needed

---

#### Template 1.2: Multi-Variant with Random Selection
**File**: `blockstate-variants-random.json` [72]

Use when: Block has variant types with random texture selection

```json
{
  "variants": {
    "type=variant1": [
      { "model": "namespace:block/example" },
      { "model": "namespace:block/example", "y": 90 },
      { "model": "namespace:block/example", "y": 180 },
      { "model": "namespace:block/example", "y": 270 }
    ],
    "type=variant2": { "model": "namespace:block/example_variant2" }
  }
}
```

**Customization Points**:
- Define multiple variants within property
- Each variant can have single model or array of models
- Array models are randomly selected (each has 25% chance with 4 models)

---

#### Template 1.3: Multipart Conditional
**File**: `blockstate-multipart.json` [73]

Use when: Block combines multiple sub-models based on conditions (fences, rails, redstone)

```json
{
  "multipart": [
    { "apply": { "model": "namespace:block/post" } },
    {
      "when": { "north": "true" },
      "apply": { "model": "namespace:block/side", "uvlock": true }
    }
  ]
}
```

**Customization Points**:
- First model without `when` clause is always applied
- `when` conditions filter which models apply
- `uvlock: true` prevents texture rotation on applied sides

---

#### Template 1.4: Full Rotation with Z-Axis (NEW 1.21.11)
**File**: `blockstate-xyz-rotation.json` [74]

Use when: Block needs full 3D rotation including Z-axis

```json
{
  "variants": {
    "facing=north,power=0": { "model": "...", "x": 0, "y": 0, "z": 0 },
    "facing=north,power=1": { "model": "...", "x": 0, "y": 0, "z": 90 }
  }
}
```

**Customization Points**:
- **x, y**: Integer values (0, 90, 180, 270)
- **z**: Integer values (NEW in 1.21.11)
- Combine multiple property conditions

---

### Category 2: Block Models (5 Templates)

Block models are located in: `assets/namespace/models/block/`

#### Template 2.1: Simple Cube
**File**: `blockmodel-cube.json` [75]

Use when: Standard full-block cube with all 6 faces

```json
{
  "elements": [
    {
      "from": [0, 0, 0],
      "to": [16, 16, 16],
      "faces": {
        "down": { "texture": "#bottom", "cullface": "down" },
        ...
      }
    }
  ]
}
```

**Key Concepts**:
- **from/to**: 3D coordinates defining cuboid volume
- **cullface**: Prevents rendering when adjacent block exists
- **texture**: References texture variable (prepended with #)

---

#### Template 2.2: Cube with Texture Inheritance
**File**: `blockmodel-cube-textured.json` [76]

Use when: Using parent model with texture variables

```json
{
  "parent": "block/cube",
  "textures": {
    "particle": "namespace:block/example",
    "bottom": "namespace:block/example_bottom",
    ...
  }
}
```

**Key Concepts**:
- **parent**: Inherits structure from parent model
- **textures**: Defines texture variables used in parent
- **particle**: Texture for breaking particles

---

#### Template 2.3: Single-Axis Rotation (Legacy)
**File**: `blockmodel-rotation-old.json` [77]

Use when: Simple rotation around one axis (still fully supported)

```json
{
  "rotation": {
    "origin": [8, 8, 8],
    "axis": "y",
    "angle": 45,
    "rescale": true
  }
}
```

**Limitations**:
- Single axis only (x, y, or z)
- Angles typically in 22.5° increments
- Still supported in 1.21.11 for compatibility

---

#### Template 2.4: Multi-Axis Rotation (NEW 1.21.11)
**File**: `blockmodel-rotation-new.json` [78]

Use when: Complex rotations requiring multiple axes

```json
{
  "rotation": {
    "origin": [8, 8, 8],
    "x": 22.5,
    "y": 45.0,
    "z": 33.75
  }
}
```

**Features**:
- **x, y, z**: Independent angles (any value -45 to +45)
- Applied in order: X → Y → Z
- No restriction on increments
- Recommended for new packs

---

#### Template 2.5: Cross-Shaped (Saplings/Plants)
**File**: `blockmodel-sapling-cross.json` [79]

Use when: Cross-shaped decorative blocks

```json
{
  "ambientocclusion": false,
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
      "faces": {
        "north": { "uv": [0, 0, 16, 16], "texture": "#cross" }
      }
    }
  ]
}
```

**Key Features**:
- **ambientocclusion: false**: No AO on transparent blocks
- Two perpendicular planes with 45° rotation
- **rescale: true**: Compensates for rotation scaling

---

### Category 3: Item Models (5 Templates)

Item models are located in:
- **Models**: `assets/namespace/models/item/`
- **Definitions**: `assets/namespace/items/` (1.21.4+)

#### Template 3.1: Simple 2D Item
**File**: `itemmodel-generated-simple.json` [80]

Use when: Basic 2D items (tools, food, etc.)

```json
{
  "parent": "item/generated",
  "textures": {
    "layer0": "namespace:item/my_item"
  }
}
```

**Key Concepts**:
- **parent: "item/generated"**: Flat 2D texture model
- **layer0**: Single texture layer
- Simplest item model type

---

#### Template 3.2: Multi-Layer 2D Item
**File**: `itemmodel-generated-multilayer.json` [81]

Use when: 2D items with multiple texture layers

```json
{
  "parent": "item/generated",
  "textures": {
    "layer0": "namespace:item/base",
    "layer1": "namespace:item/overlay"
  }
}
```

**Usage**:
- layer0: Base/main texture
- layer1: Overlay/decoration texture
- Supports layer0-layer2 (limited by hardcoded limits)

---

#### Template 3.3: Handheld with Display
**File**: `itemmodel-handheld-display.json` [82]

Use when: Tools/weapons with proper hand positioning

```json
{
  "parent": "item/handheld",
  "textures": { "layer0": "..." },
  "display": {
    "thirdperson_righthand": {
      "rotation": [0, 180, 0],
      "translation": [0, 0, 0],
      "scale": [0.85, 0.85, 0.85]
    },
    ...
  }
}
```

**Display Positions**:
1. **thirdperson_righthand**: Third-person right hand
2. **thirdperson_lefthand**: Third-person left hand
3. **firstperson_righthand**: First-person right hand
4. **firstperson_lefthand**: First-person left hand
5. **gui**: Inventory/GUI display
6. **head**: Worn on head (armor stands)
7. **ground**: Dropped on ground
8. **fixed**: Item frames

**Constraints**:
- Translation: -80 to +80 (clamped)
- Scale: 0 to 4.0 (values > 4 displayed as 4)
- Rotation: Any values [x, y, z]

---

#### Template 3.4: Item Definition (1.21.4+)
**File**: `itemdefinition-component.json` [83]

Use when: Defining item models in 1.21.4+ (REQUIRED)

```json
{
  "model": {
    "type": "minecraft:model",
    "model": "namespace:item/my_item"
  }
}
```

**Location**: `assets/namespace/items/itemname.json`

**Critical**: Required in 1.21.4+ to use custom item models!

---

#### Template 3.5: Custom 3D Item Model
**File**: `itemmodel-custom-3d.json` [84]

Use when: Items with custom 3D geometry (not flat)

```json
{
  "textures": { "particle": "#main" },
  "elements": [
    {
      "from": [4, 0, 4],
      "to": [12, 8, 12],
      "faces": { ... }
    }
  ],
  "display": { ... }
}
```

**Similarities to Block Models**:
- Uses same element structure
- Same face definition format
- Same texture variable system

**Differences**:
- Display transformations control appearance
- No parent: "builtin/entity" for items
- Limited to elements (no multipart)

---

## Important Changes in 1.21.11

### 1. Block Model Rotation
**Old**: Single axis, limited angles
```json
"rotation": { "axis": "y", "angle": 45 }
```

**New**: Multiple axes, unlimited angles
```json
"rotation": { "x": 22.5, "y": 45.0, "z": 33.75 }
```

### 2. Block State Z Rotation
**New in 1.21.11**: Z-axis rotation in block state variants
```json
"variants": {
  "facing=north": { "model": "...", "z": 0 },
  "facing=east": { "model": "...", "z": 90 }
}
```

### 3. Item Model System
**Old (Pre-1.21.4)**: Overrides in model file
```json
{
  "overrides": [
    { "predicate": { "custom_model_data": 1 }, "model": "..." }
  ]
}
```

**New (1.21.4+)**: Component-based definitions
```
assets/namespace/items/itemname.json
assets/namespace/models/item/itemname.json
```

---

## Practical Examples

### Example 1: Custom Directional Block

**Block State**:
```json
{
  "variants": {
    "facing=north": { "model": "mymod:block/custom" },
    "facing=south": { "model": "mymod:block/custom", "y": 180 },
    "facing=east": { "model": "mymod:block/custom", "y": 90 },
    "facing=west": { "model": "mymod:block/custom", "y": 270 }
  }
}
```

**Block Model**:
```json
{
  "parent": "block/cube",
  "textures": {
    "all": "mymod:block/custom"
  }
}
```

**Files Needed**:
- `assets/mymod/blockstates/custom.json`
- `assets/mymod/models/block/custom.json`
- `assets/mymod/textures/block/custom.png`

---

### Example 2: Custom Tool Item (1.21.11)

**Item Definition**:
```json
{
  "model": {
    "type": "minecraft:model",
    "model": "mymod:item/custom_sword"
  }
}
```

**Item Model**:
```json
{
  "parent": "item/handheld",
  "textures": { "layer0": "mymod:item/custom_sword" },
  "display": {
    "thirdperson_righthand": { ... },
    "firstperson_righthand": { ... },
    "gui": { ... }
  }
}
```

**Files Needed**:
- `assets/mymod/items/custom_sword.json`
- `assets/mymod/models/item/custom_sword.json`
- `assets/mymod/textures/item/custom_sword.png`

---

### Example 3: Fence-like Block

**Block State**:
```json
{
  "multipart": [
    { "apply": { "model": "mymod:block/custom_fence_post" } },
    {
      "when": { "north": "true" },
      "apply": { "model": "mymod:block/custom_fence_side", "uvlock": true }
    },
    ...
  ]
}
```

**Models Needed**:
- `mymod:block/custom_fence_post`
- `mymod:block/custom_fence_side` (rotated for each direction)

---

## Validation & Testing

### JSON Validation
1. No trailing commas
2. All strings in double quotes
3. All braces/brackets properly closed
4. No comments in actual JSON (only in templates)

### Model Validation
1. Textures exist and are referenced correctly
2. Parents exist if used
3. Element coordinates are within -16 to 32
4. Rotation values are within -180 to 180
5. File structure matches standard

### Testing in Game
1. Place/use item in creative
2. Verify textures render correctly
3. Check rotations/transformations
4. Verify no error messages in logs

---

## File Naming Conventions

Follow Minecraft conventions:

| Type | Convention | Example |
|------|-----------|---------|
| Block State | `blockname.json` | `stone_stairs.json` |
| Block Model | `blockname.json` | `stone_stairs.json` |
| Item Model | `itemname.json` | `custom_sword.json` |
| Item Definition | `itemname.json` | `custom_sword.json` |
| Texture | `blockname.png` / `itemname.png` | `stone_stairs.png` |

---

## Performance Tips

1. **Use parent models**: Inherit from `block/cube` instead of redefining
2. **Optimize multipart**: Use conditional logic efficiently
3. **Minimal elements**: Use fewest cuboids needed
4. **Texture atlasing**: Combine multiple textures into single file
5. **Cullface optimization**: Prevent rendering hidden faces

---

## Troubleshooting

### Issue: Texture not showing
- Check texture path is correct
- Verify texture file exists
- Check namespace matches
- Verify texture variable is defined in textures object

### Issue: Block rotates wrong way
- Check Y rotation values (90° increments for block states)
- Verify rotation origin is [8, 8, 8] for center
- Check new vs. old rotation format usage

### Issue: Item displays wrong in hand
- Check all 8 display positions are configured
- Verify translation values are within ±80
- Check scale values don't exceed 4.0
- Test in both first and third person

### Issue: Multipart not working
- Verify `when` conditions match block property names
- Check all property values are lowercase
- Ensure first part without `when` is always applied
- Test with simpler multipart first

---

## Summary Table

| Feature | Template | Compatibility | Notes |
|---------|----------|---------------|-------|
| Simple Block | blockstate-simple + blockmodel-cube-textured | All | Best for starting |
| Rotation (Old) | blockmodel-rotation-old | All | Use for compatibility |
| Rotation (New) | blockmodel-rotation-new | 1.21.11+ | Recommended |
| Z-Axis Rotation | blockstate-xyz-rotation | 1.21.11+ | NEW feature |
| Multipart | blockstate-multipart | All | For fences/rails |
| 2D Item | itemmodel-generated-simple | All | Simple items |
| 3D Item | itemmodel-custom-3d | All | Complex items |
| Item Definition | itemdefinition-component | 1.21.4+ | REQUIRED for 1.21.4+ |

---

**Total Templates**: 14
**Total Files Generated**: 16 (including index)
**Pack Format**: 74 (1.21.11)
**Compatibility**: Ranges from All Versions to 1.21.11+ specific

For complete details, see `JSON-TEMPLATES-INDEX.md` and refer to individual template files.
