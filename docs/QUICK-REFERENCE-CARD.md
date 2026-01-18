# JSON Templates Quick Reference Card

## All 14 Templates at a Glance

### BLOCK STATES (4) - `assets/namespace/blockstates/`

| File | Purpose | Best For |
|------|---------|----------|
| [71] blockstate-simple | Y-axis rotation | Directional blocks |
| [72] blockstate-variants-random | Multiple models | Random textures |
| [73] blockstate-multipart | Conditional logic | Fences, rails |
| [74] blockstate-xyz-rotation | Full 3D rotation | Complex blocks (1.21.11) |

### BLOCK MODELS (5) - `assets/namespace/models/block/`

| File | Purpose | Best For |
|------|---------|----------|
| [75] blockmodel-cube | Full solid cube | Standard blocks |
| [76] blockmodel-cube-textured | Parent inheritance | Textured blocks |
| [77] blockmodel-rotation-old | Single axis | Legacy compatibility |
| [78] blockmodel-rotation-new | Multi-axis | Advanced (1.21.11) |
| [79] blockmodel-sapling-cross | Cross shape | Plants, flowers |

### ITEM MODELS (5) - `assets/namespace/models/item/` + `assets/namespace/items/`

| File | Purpose | Best For |
|------|---------|----------|
| [80] itemmodel-generated-simple | 2D flat | Tools, items |
| [81] itemmodel-generated-multilayer | 2D layered | Complex 2D |
| [82] itemmodel-handheld-display | Hand positioning | Swords, tools |
| [83] itemdefinition-component | Model selector | 1.21.4+ items |
| [84] itemmodel-custom-3d | 3D geometry | Custom shapes |

### CONFIGURATION (1)

| File | Purpose |
|------|---------|
| [85] pack.mcmeta | Pack metadata (Format 74) |

---

## File Structure Template

```
your-pack/
├── pack.mcmeta [85]
└── assets/
    └── namespace/
        ├── blockstates/
        │   ├── [71-74] *.json
        ├── models/
        │   ├── block/
        │   │   └── [75-79] *.json
        │   └── item/
        │       └── [80-84] *.json
        ├── items/
        │   └── [83-84] *.json
        └── textures/
            ├── block/ (*.png)
            └── item/  (*.png)
```

---

## Quick Selection Guide

### "I'm making a..."

**Directional block** (furnace, repeater)
→ [71] blockstate-simple + [76] blockmodel-cube-textured

**Textured block** (stone, dirt, wood)
→ [71] blockstate-simple + [76] blockmodel-cube-textured

**Random-texture block** (grass, stone)
→ [72] blockstate-variants-random + [76] blockmodel-cube-textured

**Connected block** (fence, rail, redstone)
→ [73] blockstate-multipart + [75-79] blockmodels

**Plant/Flower** (sapling, flower)
→ [71] blockstate-simple + [79] blockmodel-sapling-cross

**Complex rotated block** (1.21.11)
→ [74] blockstate-xyz-rotation + [78] blockmodel-rotation-new

**Simple 2D item** (food, simple tool)
→ [80] itemmodel-generated-simple + [83] itemdefinition-component

**Sword/Pickaxe** (handheld tool)
→ [82] itemmodel-handheld-display + [83] itemdefinition-component

**Layered item** (banner, enchanted item)
→ [81] itemmodel-generated-multilayer + [83] itemdefinition-component

**Custom 3D item**
→ [84] itemmodel-custom-3d + [83] itemdefinition-component

---

## Key Values Reference

### Rotations in Block States
```json
"y": 0    // North
"y": 90   // East
"y": 180  // South
"y": 270  // West
```

### New Z-Rotation (1.21.11)
```json
"z": 0    // Normal
"z": 90   // Rotated 90° clockwise
"z": 180  // Rotated 180° (inverted)
"z": 270  // Rotated 270° clockwise
```

### Display Positions
```json
"thirdperson_righthand"  // 3rd person right
"thirdperson_lefthand"   // 3rd person left
"firstperson_righthand"  // 1st person right
"firstperson_lefthand"   // 1st person left
"gui"                    // Inventory
"head"                   // Armor stand/head
"ground"                 // Dropped item
"fixed"                  // Item frame
```

### Display Constraints
```
Translation: -80 to +80 (clamped)
Scale:       0 to 4.0 (max 4.0)
Rotation:    Any values [x, y, z]
```

### Element Coordinates
```
from/to: [x, y, z]
Typical range: -16 to 32
Relative to block space (0-16)
```

---

## Customization Checklist

### Essential Changes
- [ ] Replace "namespace" with yours (e.g., "mymod")
- [ ] Replace "example_block"/"example_item" with your names
- [ ] Update texture paths to your textures
- [ ] Verify all files in correct folders

### Block State Specific
- [ ] Match variant properties to block's actual properties
- [ ] Verify property values (e.g., facing directions)
- [ ] Check Y/Z rotation values are 0, 90, 180, or 270

### Block Model Specific
- [ ] Update texture variable references
- [ ] If using parent, verify parent exists
- [ ] Check rotation origin [8, 8, 8] for center rotation

### Item Model Specific
- [ ] Adjust display positions for your item
- [ ] Verify scale stays within 0-4.0
- [ ] Check translation is within ±80
- [ ] Test in all 8 display positions

### Item Definition (1.21.4+)
- [ ] Must be in `assets/namespace/items/` folder
- [ ] Model path must point to actual model file
- [ ] Required for 1.21.4+ custom items

---

## Common Patterns

### Direction Property
```json
{
  "facing=north": { "model": "..." },
  "facing=south": { "model": "...", "y": 180 },
  "facing=east": { "model": "...", "y": 90 },
  "facing=west": { "model": "...", "y": 270 }
}
```

### Power/State Property
```json
{
  "powered=false": { "model": "..." },
  "powered=true": { "model": "...", "z": 90 }
}
```

### Multipart Always + Conditional
```json
"multipart": [
  { "apply": { "model": "..." } },  // Always
  {
    "when": { "north": "true" },
    "apply": { "model": "..." }
  }
]
```

### Full Display Properties
```json
"display": {
  "thirdperson_righthand": { "rotation": [...], "translation": [...], "scale": [...] },
  "thirdperson_lefthand": { ... },
  "firstperson_righthand": { ... },
  "firstperson_lefthand": { ... },
  "gui": { ... },
  "head": { ... },
  "ground": { ... },
  "fixed": { ... }
}
```

---

## Version Compatibility Matrix

| Feature | 1.20.5+ | 1.21.3 | 1.21.11 |
|---------|---------|--------|---------|
| Block states (variants) | ✓ | ✓ | ✓ |
| Block states (multipart) | ✓ | ✓ | ✓ |
| Block rotation (axis/angle) | ✓ | ✓ | ✓ |
| Block rotation (x/y/z) | ✗ | ✗ | ✓ |
| Z-axis in variants | ✗ | ✗ | ✓ |
| Item models (generated) | ✓ | ✓ | ✓ |
| Item models (custom) | ✓ | ✓ | ✓ |
| Item definitions | ✗ | ✗ | ✓ |
| Pack format 74 | ✗ | ✗ | ✓ |

---

## Troubleshooting Quick Tips

| Problem | Check |
|---------|-------|
| Texture missing | Texture file exists? Path correct? Variable defined? |
| Model error | Parent exists? Element from/to valid? |
| Wrong rotation | Using 0/90/180/270? Origin correct? |
| Item wrong position | Display position configured? Constraints met? |
| Multipart broken | Condition logic correct? Property names match? |
| Z-rotation ignored | 1.21.11 client? Pack format 74? |

---

## File Reference by Artifact Number

| ID | File | Type |
|----|------|------|
| 71 | blockstate-simple | Block State |
| 72 | blockstate-variants-random | Block State |
| 73 | blockstate-multipart | Block State |
| 74 | blockstate-xyz-rotation | Block State |
| 75 | blockmodel-cube | Block Model |
| 76 | blockmodel-cube-textured | Block Model |
| 77 | blockmodel-rotation-old | Block Model |
| 78 | blockmodel-rotation-new | Block Model |
| 79 | blockmodel-sapling-cross | Block Model |
| 80 | itemmodel-generated-simple | Item Model |
| 81 | itemmodel-generated-multilayer | Item Model |
| 82 | itemmodel-handheld-display | Item Model |
| 83 | itemdefinition-component | Item Definition |
| 84 | itemmodel-custom-3d | Item Model |
| 85 | pack.mcmeta | Configuration |
| 86 | JSON-TEMPLATES-INDEX | Documentation |
| 87 | COMPLETE-JSON-GUIDE | Documentation |
| 88 | TEMPLATES-SUMMARY | Documentation |

---

## Start Here

1. **First time?** → Read COMPLETE-JSON-GUIDE.md [87]
2. **Need specific template?** → Check JSON-TEMPLATES-INDEX.md [86]
3. **Lost?** → This quick reference card
4. **Copy templates** → Use appropriate [##] file
5. **Need help?** → See TEMPLATES-SUMMARY.md [88]

---

**Minecraft Java Edition 1.21.11 | Pack Format 74 | All templates production-ready**
