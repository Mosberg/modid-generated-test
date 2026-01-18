# Copilot Instructions for Minecraft Java Edition (1.21.11) Fabric Modding

## Project Structure & Technologies

- **Minecraft Version:** 1.21.11
- **Mod Loader:** Fabric (with Yarn mappings)
- **Language:** Java 21
- **Build System:** Gradle (Loom plugin)
- **Source Layout:**
  - Core logic: `src/main/java/dk/mosberg/modid/`
  - Client-only: `src/client/java/dk/mosberg/modid/`
  - Resources: `src/main/resources/assets/modid/`
  - Mod metadata: `src/main/resources/fabric.mod.json`

## Entrypoints & Registration

- **Entrypoints:**
  - Main: `ModId.java` (implements `ModInitializer`)
  - Client: `ModIdClient.java` (implements `ClientModInitializer`)
- **Item Registration:**
  - All custom items: `ModItems.java`
  - Item groups: `ModItemGroups.java`
  - Each item: separate class in `item/` (e.g., `SmallFlaskItem.java`)
- **Block Registration:**
  - All custom blocks: `ModBlocks.java`
- **Resource Files:**
  - Blockstates: `assets/modid/blockstates/`
  - Block/item models: `assets/modid/models/{block,item}/`
  - Textures: `assets/modid/textures/{block,item}/`
  - Language: `assets/modid/lang/`

## Best Practices

- **Follow Standard Fabric Patterns:**
  - Use Yarn mappings for all Minecraft classes.
  - Register all items, blocks, and groups in their respective registry files.
  - Place client-only code/resources in the `client/` source/resource sets.
- **Resource Management:**
  - Add new models, textures, and lang entries for every new item/block.
  - Use correct JSON structure for blockstates and models (see `docs/` for templates and guides).
- **Mod Metadata:**
  - Update `fabric.mod.json` for new entrypoints, dependencies, or metadata changes.
- **Build & Run:**
  - Use Gradle tasks:
    - `./gradlew build` — build the mod jar
    - `./gradlew runClient` — launch Minecraft for testing
  - Java 21 is required (see `build.gradle`).

## Do & Do Not

**Do:**

- Use only Yarn mappings and Fabric API.
- Keep code and resources organized by type and environment (main/client).
- Follow conventions in `README.md` and `docs/` for file placement and JSON structure.
- Use Maven publishing config in `build.gradle` if publishing.

**Do Not:**

- Do not introduce nonstandard build tools, scripts, or mappings.
- Do not place client-only code in the main source set.
- Do not modify files outside the established source/resource structure.
- Do not use mappings other than Yarn.

## Resources & References

- See `docs/MINECRAFT-FABRIC-MODDING-RESOURCES.md` for blockstate/model JSON examples and links to official documentation.
- See `README.md` for directory structure and file locations.
- See `docs/` for JSON templates and quick reference guides.

---

**This file is auto-generated for AI coding agents. Update if project conventions change.**
