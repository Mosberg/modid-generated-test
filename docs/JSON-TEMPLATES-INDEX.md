# Minecraft 1.21.11 JSON Templates Index

Complete set of JSON template files for block states, block models, and item models for Minecraft Java Edition 1.21.11.

## File Structure Overview

```
your-resource-pack/
├── pack.mcmeta                          (Pack metadata - Format 74)
└── assets/
    └── namespace/
        ├── blockstates/                 (Block state definitions)
        ├── models/
        │   ├── block/                   (Block model definitions)
        │   └── item/                    (Item model definitions)
        ├── items/                       (Item definitions - 1.21.4+)
        └── textures/
            ├── block/                   (Block textures)
            └── item/                    (Item textures)
```

---

## Pack Metadata

### `pack.mcmeta` [85]
- **Location**: Root of resource pack
- **Format Version**: 74 (current for 1.21.11)
- **Description**: Pack identifier and format version
- **Usage**: Required for all resource packs

---

## Block State Templates

Block states define how blocks appear based on their properties.

### 1. `blockstate-simple.json` [71]
- **Type**: Simple variants with single property
- **Use Case**: Basic directional blocks (facing north/south/east/west)
- **Rotation**: Y-axis only (90° increments)
- **Example**: Wall torch, directional blocks
- **Compatible**: All versions

### 2. `blockstate-variants-random.json` [72]
- **Type**: Multiple models per variant with random selection
- **Use Case**: Blocks with multiple texture variations
- **Features**: Multiple models with weight-based selection
- **Example**: Grass block (snowy/not snowy)
- **Compatible**: All versions

### 3. `blockstate-multipart.json` [73]
- **Type**: Multipart composition with conditional logic
- **Use Case**: Blocks that combine multiple sub-models
- **Features**: Conditional application based on block properties
- **Example**: Fences, rails, redstone wire
- **Compatible**: All versions

### 4. `blockstate-xyz-rotation.json` [74]
- **Type**: Full XYZ rotation with multiple properties
- **Use Case**: Complex blocks with multiple rotation states
- **Features**: X, Y, Z axis control (1.21.11 feature)
- **Example**: Oriented blocks with power states
- **Compatible**: 1.21.11+ (backward compatible with older versions)

---

## Block Model Templates

Block models define the 3D geometry of blocks.

### 5. `blockmodel-cube.json` [75]
- **Type**: Basic cube with all faces
- **Use Case**: Simple solid blocks
- **Features**: All 6 faces with cullface optimization
- **Example**: Stone, dirt, log blocks
- **Compatible**: All versions

### 6. `blockmodel-cube-textured.json` [76]
- **Type**: Cube with texture inheritance
- **Use Case**: Blocks using parent model inheritance
- **Features**: Texture variable assignment
- **Example**: Most full-cube blocks
- **Compatible**: All versions

### 7. `blockmodel-rotation-old.json` [77]
- **Type**: Single-axis rotation (legacy format)
- **Use Case**: Simple rotational elements
- **Features**: axis/angle format (still supported)
- **Restrictions**: Single axis only, limited angles
- **Example**: Saplings, torches
- **Compatible**: All versions

### 8. `blockmodel-rotation-new.json` [78]
- **Type**: Multi-axis rotation (1.21.11 format)
- **Use Case**: Complex rotational elements
- **Features**: x, y, z independent angles
- **Restrictions**: None - any angle allowed
- **Example**: Custom diagonal/complex shapes
- **Compatible**: 1.21.11+ (recommended for new packs)

### 9. `blockmodel-sapling-cross.json` [79]
- **Type**: Cross-shaped model with rotation
- **Use Case**: Decorative cross-shaped blocks
- **Features**: Rotated planes with rescale
- **Example**: Saplings, flowers, fire
- **Compatible**: All versions

---

## Item Model Templates

Item models define how items appear in inventory, hand, and world.

### 10. `itemmodel-generated-simple.json` [80]
- **Type**: 2D flat generated texture
- **Use Case**: Simple tools, items with single texture layer
- **Features**: Parent inheritance from item/generated
- **Example**: Swords, pickaxes, food
- **Compatible**: All versions

### 11. `itemmodel-generated-multilayer.json` [81]
- **Type**: 2D multi-layer texture composition
- **Use Case**: Items with layered textures
- **Features**: Multiple layer0, layer1, etc. textures
- **Example**: Bow (base + pull states), banners
- **Compatible**: All versions

### 12. `itemmodel-handheld-display.json` [82]
- **Type**: Handheld item with full display transformations
- **Use Case**: Tools and weapons with proper hand positioning
- **Features**: All 8 display positions configured
- **Positions**: thirdperson_righthand/lefthand, firstperson_righthand/lefthand, gui, head, ground, fixed
- **Example**: Swords, axes, pickaxes
- **Compatible**: All versions

### 13. `itemdefinition-component.json` [83]
- **Type**: Item definition (1.21.4+ system)
- **Location**: assets/namespace/items/itemname.json
- **Use Case**: Pointing items to their models (required in 1.21.4+)
- **Features**: Component-based model selection
- **Example**: All 1.21.4+ custom items
- **Compatible**: 1.21.4+ (mandatory for 1.21.4+)

### 14. `itemmodel-custom-3d.json` [84]
- **Type**: Custom 3D model with elements
- **Use Case**: Items with custom 3D geometry
- **Features**: Full element-based model definition
- **Example**: Complex item shapes, special items
- **Compatible**: All versions

---

## Template Usage Guide

### For Block States

1. **Start with**: `blockstate-simple.json` for basic directional blocks
2. **Upgrade to**: `blockstate-variants-random.json` for texture variation
3. **Use**: `blockstate-multipart.json` for connected/conditional blocks
4. **Add**: `blockstate-xyz-rotation.json` for 1.21.11 advanced features

### For Block Models

1. **Standard blocks**: Use `blockmodel-cube-textured.json` with parent inheritance
2. **Rotated elements**: Use `blockmodel-rotation-old.json` for compatibility
3. **Advanced rotation**: Use `blockmodel-rotation-new.json` for 1.21.11+ features
4. **Cross-shaped**: Use `blockmodel-sapling-cross.json` for plants/decorations

### For Item Models

1. **2D items**: Use `itemmodel-generated-simple.json`
2. **Layered items**: Use `itemmodel-generated-multilayer.json`
3. **Handheld tools**: Use `itemmodel-handheld-display.json`
4. **Custom 3D**: Use `itemmodel-custom-3d.json`
5. **Item definition**: Use `itemdefinition-component.json` for 1.21.4+

---

## Version Compatibility

| Template | 1.20.5-1.21.2 | 1.21.3 | 1.21.11 |
|----------|--------------|--------|---------|
| blockstate-simple | ✓ | ✓ | ✓ |
| blockstate-variants-random | ✓ | ✓ | ✓ |
| blockstate-multipart | ✓ | ✓ | ✓ |
| blockstate-xyz-rotation | ✓* | ✓* | ✓ |
| blockmodel-cube | ✓ | ✓ | ✓ |
| blockmodel-cube-textured | ✓ | ✓ | ✓ |
| blockmodel-rotation-old | ✓ | ✓ | ✓ |
| blockmodel-rotation-new | ✗ | ✗ | ✓ |
| blockmodel-sapling-cross | ✓ | ✓ | ✓ |
| itemmodel-generated-simple | ✓ | ✓ | ✓ |
| itemmodel-generated-multilayer | ✓ | ✓ | ✓ |
| itemmodel-handheld-display | ✓ | ✓ | ✓ |
| itemdefinition-component | ✗ | ✗ | ✓ |
| itemmodel-custom-3d | ✓ | ✓ | ✓ |

**Notes**:
- `*` = Works but Z-axis rotation not available
- `✓` = Full support
- `✗` = Not supported in this version

---

## Key 1.21.11 Changes

### New Features
- **Multi-axis block element rotation** (blockmodel-rotation-new.json)
- **Z-axis block state rotation** (blockstate-xyz-rotation.json)
- **Component-based item definitions** (itemdefinition-component.json)

### Modified Systems
- Item model system completely redesigned
- Block state format supports Z-axis rotation
- Block model rotation supports arbitrary angles

### Pack Format
- Current: **74** (specified in pack.mcmeta)

---

## Creating New Files

### Step 1: Start with Pack Metadata
```
Copy: pack.mcmeta
Edit: description field to match your pack
```

### Step 2: Create Block States
```
Copy: appropriate blockstate-*.json template
Rename: example_block → your_blockname
Update: model paths to match your namespace
```

### Step 3: Create Block Models
```
Copy: appropriate blockmodel-*.json template
Rename: example_block → your_blockname
Update: texture references (#variable names)
```

### Step 4: Create Item Models
```
Copy: appropriate itemmodel-*.json template
Rename: example_item → your_itemname
Update: texture and parent references
```

### Step 5: Create Item Definitions (1.21.4+)
```
Copy: itemdefinition-component.json
Rename: example_sword → your_itemname
Update: model path to point to your model
```

---

## Common Customization Points

### Block States
- **"facing=direction"** → Change direction property
- **"snowy=true/false"** → Change variant conditions
- **"north": "true"** → Change multipart conditions
- **"y": 90** → Adjust rotation values (0, 90, 180, 270)
- **"z": 90** → NEW in 1.21.11 (Z-axis rotation)

### Block Models
- **"origin": [8, 8, 8]** → Rotation center point
- **"x", "y", "z" angles** → Rotation values (NEW format)
- **"axis": "y", "angle": 45** → Rotation values (OLD format)
- **"from" / "to"** → Cuboid dimensions [x, y, z]
- **"texture": "#variable"** → Texture references

### Item Models
- **"rotation": [x, y, z]** → Display rotation
- **"translation": [x, y, z]** → Display position (±80 clamped)
- **"scale": [x, y, z]** → Display size (max 4.0)
- **"layer0", "layer1"** → Texture layers

---

## File Size Reference

- **Block State**: ~500 bytes - 2 KB (depending on complexity)
- **Block Model**: ~1-5 KB (depending on elements)
- **Item Model**: ~500 bytes - 3 KB (depending on features)
- **Item Definition**: ~150 bytes
- **pack.mcmeta**: ~100 bytes

---

## Validation Checklist

- [ ] All JSON files are valid (no syntax errors)
- [ ] pack.mcmeta specifies format 74
- [ ] All texture paths exist and are correctly referenced
- [ ] All parent model paths exist
- [ ] Block state variants match defined block properties
- [ ] Rotation values are in valid ranges
- [ ] Display positions use correct coordinate values
- [ ] Translation values are within ±80 range
- [ ] Scale values are within 0-4 range

---

## References

- [Full Tutorial](TUTORIAL-MODELS-121.md)
- [Quick Reference](QUICK-REFERENCE.md)
- [Analysis Document](ANALYSIS-UPDATES.md)
- [Minecraft Wiki](https://minecraft.wiki/w/Tutorial:Models)

---

**Generated for Minecraft Java Edition 1.21.11**  
**Pack Format: 74**  
**Last Updated: January 18, 2026**
