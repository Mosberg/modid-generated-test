# Analysis: Tutorial Models Updates for Minecraft Java Edition 1.21.11

## Executive Summary

The provided TUTORIAL-MODELS.md file required significant updates to be current with Minecraft Java Edition 1.21.11. Two major system overhauls were identified and corrected: (1) **Block Model Rotation System** - expanded to support multi-axis rotation with unlimited angle values, and (2) **Item Model System** - completely redesigned in version 1.21.4 to use component-based model selection instead of predicate overrides.

---

## Critical Updates Required

### 1. Block Model Rotation System (MAJOR CHANGE)

**Status in Original File**: ❌ Outdated

**What Changed**:

- Minecraft 1.21.11 (Snapshot 25w46a) introduced revolutionary changes to block model rotation
- **Old System**: Single-axis rotation with 22.5-degree increment restriction
- **New System**: Multi-axis rotation with arbitrary angle support

**Original Limitation**:

```json
{
  "rotation": {
    "origin": [8, 8, 8],
    "axis": "y",
    "angle": 45
  }
}
```

- Only one axis (x, y, or z)
- Angles limited to 22.5-degree increments
- Angles constrained to [-45, 45] degrees

**Updated Format (1.21.11)**:

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

- All three axes supported simultaneously
- **Any angle value now allowed** (not just 22.5 increments)
- Rotations applied in order: X → Y → Z
- Old format still supported but takes precedence if both exist

**Impact**: This fundamentally changes how modelers can create custom blocks. Previously impossible designs (like diagonal rotations or custom angles) are now possible. The restriction was a deliberate design choice to maintain Minecraft's cubic aesthetic, but this change provides flexibility when needed.

### 2. Item Model System Overhaul (CRITICAL CHANGE)

**Status in Original File**: ⚠️ Contains critical warning but inadequate explanation

**The Problem**:
The original file contains this warning at the Item Models section:

```
{{needs update|section=1|1.21.4 completely changed how these work}}
```

However, the document still describes the old system with predicates and overrides, which no longer works.

**What Changed** (Minecraft 1.21.4):
The entire item model selection system was redesigned from predicate-based to component-based.

**Old System (Pre-1.21.4)**:

- Item models used `overrides` array with predicates
- Predicates matched item properties (damage, custom_model_data, etc.)
- Model selected based on predicate matching
- Stored in `models/item/itemname.json`

```json
{
  "overrides": [
    {
      "predicate": { "custom_model_data": 1 },
      "model": "item/custom_model_1"
    }
  ]
}
```

**New System (1.21.4+)**:

- Item models selected via `minecraft:item_model` data component
- Stored separately in `assets/namespace/items/itemname.json`
- Format points to the actual model to use
- More flexible and data-driven

```json
{
  "model": {
    "type": "minecraft:model",
    "model": "namespace:item/custom_sword"
  }
}
```

**Usage Change**:

- **Old**: `/give @s diamond_sword[custom_model_data=1]` with override predicates
- **New**: `/give @s diamond_sword[item_model=namespace:item/custom_sword]`

**Fabric API Impact**:
The Fabric documentation confirms this change, stating: "Model predicate providers are removed since 1.21.4. Since 1.21.4, please use items model definition instead."

### 3. Block State Variant Z-Rotation (NEW FEATURE)

**Status in Original File**: ❌ Not mentioned

**What's New**:
Block state variants can now include Z-axis rotation, completing the rotation support.

```json
{
  "variants": {
    "facing=north": { "model": "block/example", "z": 0 },
    "facing=east": { "model": "block/example", "z": 90 },
    "facing=south": { "model": "block/example", "z": 180 },
    "facing=west": { "model": "block/example", "z": 270 }
  }
}
```

- Z-axis rotation: Integer values only (0, 90, 180, 270)
- Applied AFTER X and Y rotations
- Enables more complex block orientation scenarios

### 4. Display Properties Validation

**Status in Original File**: ✅ Accurate

The original file correctly states translation clamping and scale limits:

- Translation: Clamped between -80 and 80 ✓
- Scale: Values > 4 displayed as 4 ✓

These specifications remain unchanged in 1.21.11.

### 5. Element Properties

**Status in Original File**: Partially accurate

The section on element rotation angles needs updating:

- **Old statement**: "Can be 45 through -45 degrees in 22.5 degree increments"
- **New reality**: Any angle between -45 and +45 is now allowed (no increment restriction)

---

## File Structure and Path Specifications

### Block States

| Property | Value                          | Status    |
| -------- | ------------------------------ | --------- |
| Folder   | `assets/namespace/blockstates` | ✓ Current |
| Filename | `blockname.json`               | ✓ Current |
| Format   | Variants or Multipart          | ✓ Current |

### Block Models

| Property | Value                           | Status                           |
| -------- | ------------------------------- | -------------------------------- |
| Folder   | `assets/namespace/models/block` | ✓ Current                        |
| Filename | `modelname.json`                | ✓ Current                        |
| Format   | JSON with elements              | ✓ Current (but rotation updated) |

### Item Models (CHANGED)

| Property            | Value                          | Status                          |
| ------------------- | ------------------------------ | ------------------------------- |
| **Old Path**        | `assets/namespace/models/item` | ❌ Still used for actual models |
| **New Path**        | `assets/namespace/items`       | ✓ Item definitions go here      |
| **Definition File** | `itemname.json`                | ✓ New in 1.21.4+                |
| **Model Reference** | Points to models/ folder       | ✓ Current                       |

---

## Resource Pack Format

**Current Pack Format for 1.21.11**: 74

Updated from previous versions. This affects:

- How resources are loaded
- Which features are available
- Backwards compatibility with older packs

The original file doesn't specify pack format, which should be included in `pack.mcmeta`.

---

## Breaking Changes Summary

| Feature            | Pre-1.21.11                   | 1.21.11+                  | Migration                               |
| ------------------ | ----------------------------- | ------------------------- | --------------------------------------- |
| Block Rotation     | Single axis, 22.5° increments | Multi-axis, any angle     | Both formats work; new takes precedence |
| Item Models        | Predicate-based overrides     | Component-based selection | Complete rewrite needed                 |
| Block State Z-Axis | Not supported                 | 90° increments            | New feature, optional                   |
| Element Angles     | 22.5° increments [-45,45]     | Any angle [-45,45]        | More flexible                           |
| Pack Format        | Previous versions             | Format 74                 | Update pack.mcmeta                      |

---

## Recommendations for Resource Pack Authors

1. **For Block Models**: Migrate to new rotation format while maintaining backwards compatibility (old format still works)
2. **For Item Models**: If using custom_model_data, migrate to the new item_model component system
3. **Pack Metadata**: Ensure pack.mcmeta specifies format 74
4. **Testing**: Verify both old and new formats work in intended versions

---

## Verification Sources

- **Snapshot 25w46a** (included in 1.21.11): Block rotation multi-axis feature
- **Snapshot 25w16a** (25w02a): Block rotation angle restriction removal
- **Minecraft 1.21.4 Release Notes**: Item model system overhaul
- **Fabric Wiki**: Model predicate provider removal confirmation
- **Multiple 1.21.4+ Tutorials**: Item model component usage

---

## Conclusion

The provided TUTORIAL-MODELS.md file required substantial updates to reflect Minecraft 1.21.11 specifications. The two most critical changes are:

1. **Block model rotation capabilities** have been dramatically expanded
2. **Item model selection system** has been completely redesigned

An updated version has been created (`TUTORIAL-MODELS-121.md`) that reflects these changes and provides accurate guidance for both new and migrating resource pack authors.
