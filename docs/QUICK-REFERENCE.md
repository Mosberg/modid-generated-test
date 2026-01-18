# Quick Reference: Minecraft 1.21.11 Model System Changes

## Block Model Rotation - Old vs. New

### Old Syntax (Pre-1.21.11)

```json
{
  "rotation": {
    "origin": [8, 8, 8],
    "axis": "y",
    "angle": 45
  }
}
```

**Limitations**:

- One axis only (x, y, or z)
- Angle: 22.5° increments only
- Range: -45 to +45 degrees

### New Syntax (1.21.11+)

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

**Capabilities**:

- All three axes simultaneously
- Any angle value (floats accepted)
- Range: -45 to +45 degrees (no increment restriction)
- Applied in order: X → Y → Z

**Backwards Compatibility**: Both syntaxes work. If both present, old (axis/angle) takes precedence.

---

## Item Model System - Before and After 1.21.4

### Pre-1.21.4: Predicate-Based Overrides

**File Location**: `assets/minecraft/models/item/diamond_sword.json`

```json
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "item/diamond_sword"
  },
  "overrides": [
    {
      "predicate": { "custom_model_data": 1 },
      "model": "item/custom_sword_1"
    },
    {
      "predicate": { "custom_model_data": 2 },
      "model": "item/custom_sword_2"
    }
  ]
}
```

**Usage**:

```
/give @s diamond_sword[custom_model_data=1]
```

### 1.21.4+: Component-Based Selection

**File Structure**:

1. Item Definition: `assets/namespace/items/diamond_sword.json`
2. Model File: `assets/namespace/models/item/custom_sword.json`

**Item Definition File** (`items/diamond_sword.json`):

```json
{
  "model": {
    "type": "minecraft:model",
    "model": "namespace:item/custom_sword"
  }
}
```

**Model File** (`models/item/custom_sword.json`):

```json
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "item/custom_sword"
  }
}
```

**Usage**:

```
/give @s diamond_sword[item_model=namespace:item/custom_sword]
```

---

## Block State Variants - Z-Axis Rotation (NEW)

### Pre-1.21.11: X and Y only

```json
{
  "variants": {
    "facing=north": { "model": "block/example", "x": 0, "y": 0 },
    "facing=east": { "model": "block/example", "x": 0, "y": 90 },
    "facing=south": { "model": "block/example", "x": 0, "y": 180 },
    "facing=west": { "model": "block/example", "x": 0, "y": 270 }
  }
}
```

### 1.21.11+: X, Y, and Z

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

**Z-Axis Details**:

- Integer values only: 0, 90, 180, 270
- Applied after X and Y rotations
- Clamped to 0-360 degree range

---

## Item Predicates (Still Valid in 1.21.11)

These predicates work in data packs and command predicates:

| Predicate           | Item Type                 | Range   | Description             |
| ------------------- | ------------------------- | ------- | ----------------------- |
| `angle`             | Compass                   | 0-1     | Current angle           |
| `blocking`          | Shield                    | 0-1     | 1 = blocking            |
| `broken`            | Durability                | 0-1     | 1 = one durability left |
| `cast`              | Fishing Rod               | 0-1     | 1 = cast                |
| `cooldown`          | Ender Pearl, Chorus Fruit | 0-1     | Remaining cooldown      |
| `damage`            | Durability                | 0-1     | Damage ratio            |
| `damaged`           | Durability                | 0-1     | 1 = damaged             |
| `lefthanded`        | Any                       | N/A     | Left-handed player      |
| `pull`              | Bow, Crossbow             | 0-1     | Pull amount             |
| `pulling`           | Bow, Crossbow             | 0-1     | 1 = pulling             |
| `charged`           | Crossbow                  | 0-1     | 1 = charged             |
| `firework`          | Crossbow                  | 0-1     | 1 = firework            |
| `throwing`          | Trident                   | 0-1     | 1 = ready               |
| `time`              | Clock                     | 0-1     | Current time            |
| `custom_model_data` | Any                       | Integer | Custom data value       |
| `level`             | Light Block               | 0-1     | Light level             |
| `filled`            | Bundle                    | 0-1     | Fill ratio              |
| `tooting`           | Goat Horn                 | 0-1     | 1 = tooting             |
| `trim_type`         | Armor                     | 0-1     | Trim material           |
| `brushing`          | Brush                     | 0-1     | Brush progress          |
| `honey_level`       | Beehive, Bee Nest         | 0-1     | Honey amount            |

---

## Display Positions for Item Models

All positions have **rotation**, **translation**, and **scale**:

| Position                | Use                               |
| ----------------------- | --------------------------------- |
| `thirdperson_righthand` | Held in right hand (third person) |
| `thirdperson_lefthand`  | Held in left hand (third person)  |
| `firstperson_righthand` | Held in right hand (first person) |
| `firstperson_lefthand`  | Held in left hand (first person)  |
| `gui`                   | In inventory/GUI                  |
| `head`                  | Worn on head (armor stands)       |
| `ground`                | Dropped on ground                 |
| `fixed`                 | In item frames                    |

**Constraints**:

- **Translation**: Clamped to ±80
- **Scale**: Max 4.0

---

## Resource Pack Format Versions

| Version | Minecraft     | Key Changes             |
| ------- | ------------- | ----------------------- |
| 72      | 1.20.5-1.21.2 | Earlier resource pack   |
| 73      | 1.21.3        | Minor updates           |
| **74**  | **1.21.11**   | **Current for 1.21.11** |

---

## File Structure Comparison

### Block Models (Unchanged)

```
assets/
├── minecraft/
│   ├── blockstates/
│   │   └── stone.json          (references models)
│   ├── models/
│   │   └── block/
│   │       └── stone.json      (3D model definition)
│   └── textures/
│       └── block/
│           └── stone.png
```

### Item Models (Updated in 1.21.4+)

```
assets/
├── minecraft/
│   ├── items/
│   │   └── diamond_sword.json  (NEW: points to model)
│   ├── models/
│   │   └── item/
│   │       └── diamond_sword.json (actual model)
│   └── textures/
│       └── item/
│           └── diamond_sword.png
```

---

## Migration Checklist for 1.21.11

- [ ] Update `pack.mcmeta` to specify `"pack_format": 74`
- [ ] Review block model rotation (old format still works)
- [ ] If using custom item models, migrate to component system
- [ ] Test both old and new model formats
- [ ] Update documentation/comments
- [ ] Verify Z-axis rotations in block states if needed
- [ ] Check for deprecated item model predicates (none known for 1.21.11)

---

## Key Takeaways

1. **Block Rotation**: Multi-axis support with unlimited angles (backward compatible)
2. **Item Models**: Complete system redesign in 1.21.4 (requires migration)
3. **Block States**: Z-axis rotation now available (optional feature)
4. **Resource Packs**: Use format 74 for 1.21.11
5. **Backwards Compatibility**: Most changes are backward compatible; old formats still work

For detailed information, see the full updated tutorial: `TUTORIAL-MODELS-121.md`
