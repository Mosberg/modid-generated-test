# Minecraft Java Edition (1.21.11) Fabric Modding Resources

## Blockstates

- [Blockstates Documentation](https://docs.fabricmc.net/develop/blocks/blockstates)

### assets/${modid}/blockstates/\*.json

Blockstate JSON files define the different states a block can have and how those states correspond to models. Each block can have multiple properties (like "facing", "powered", etc.) that determine its appearance and behavior.

#### Example Blockstate JSON

**File Path:** `assets/${modid}/blockstates/iron_keg_block.json`

- This blockstate file defines a block called "iron_keg_block" that can face four different directions: north, east, south, and west. Each direction corresponds to a specific rotation of the model.

```json
{
  "variants": {
    "facing=north": {
      "model": "${modid}:block/iron_keg_block",
      "y": 0
    },
    "facing=east": {
      "model": "${modid}:block/iron_keg_block",
      "y": 90
    },
    "facing=south": {
      "model": "${modid}:block/iron_keg_block",
      "y": 180
    },
    "facing=west": {
      "model": "${modid}:block/iron_keg_block",
      "y": 270
    }
  }
}
```

**File Path:** `assets/${modid}/blockstates/oak_iron_barrel.json`

- This blockstate file defines a block called "oak_iron_barrel" that can face four different directions and can be either open or closed. Each combination of facing direction and open state corresponds to a specific model and rotation.

```json
{
  "variants": {
    "normal": { "model": "${modid}:block/oak_iron_barrel" },
    "facing=north,open=false": {
      "model": "${modid}:block/oak_iron_barrel",
      "y": 0
    },
    "facing=east,open=false": {
      "model": "${modid}:block/oak_iron_barrel",
      "y": 90
    },
    "facing=south,open=false": {
      "model": "${modid}:block/oak_iron_barrel",
      "y": 180
    },
    "facing=west,open=false": {
      "model": "${modid}:block/oak_iron_barrel",
      "y": 270
    },
    "facing=north,open=true": {
      "model": "${modid}:block/oak_iron_barrel_open",
      "y": 0
    },
    "facing=east,open=true": {
      "model": "${modid}:block/oak_iron_barrel_open",
      "y": 90
    },
    "facing=south,open=true": {
      "model": "${modid}:block/oak_iron_barrel_open",
      "y": 180
    },
    "facing=west,open=true": {
      "model": "${modid}:block/oak_iron_barrel_open",
      "y": 270
    }
  }
}
```
