# Copilot Instructions for modid (Fabric Minecraft Mod)

## Project Overview

- This is a Minecraft mod for Fabric, written in Java 21, using the Fabric API and Yarn mappings.
- The project uses Gradle (with Loom) for builds and dependency management.
- Source code is organized into `src/main/java/dk/mosberg/modid/` (core mod logic) and `src/client/java/dk/mosberg/modid/` (client-only logic).
- Resources (assets, models, textures, lang files) are under `src/main/resources/assets/modid/`.

## Key Conventions

- **Entrypoints:**
  - Main mod initializer: `ModId.java` (implements `ModInitializer`)
  - Client initializer: `ModIdClient.java` (implements `ClientModInitializer`)
- **Item and Group Registration:**
  - All custom items are registered in `ModItems.java`.
  - Item groups are registered in `ModItemGroups.java`.
  - Each custom item has its own class in `item/` (e.g., `SmallFlaskItem.java`).
- **Resource Files:**
  - Item models: `src/main/resources/assets/modid/models/item/`
  - Textures: `src/main/resources/assets/modid/textures/item/`
  - Language: `src/main/resources/assets/modid/lang/`
- **Mod Metadata:**
  - `fabric.mod.json` defines mod id, entrypoints, dependencies, and metadata.

## Build & Run

- Use Gradle tasks for all build operations:
  - `./gradlew build` — builds the mod jar
  - `./gradlew runClient` — launches Minecraft with the mod for testing
- Java 21 is required (set in `build.gradle`).
- No custom scripts or nonstandard build/test workflows are present.

## Coding Guidelines

- Follow standard Fabric modding patterns for registration and initialization.
- Place new items in `item/` and register them in `ModItems.java`.
- Add new item models and textures to the appropriate resource folders.
- Update `fabric.mod.json` for new entrypoints or dependencies.
- Keep client-only code in the `client/` source/resource folders.
- Use Yarn mappings for all Minecraft class references.

## Integration Points

- No custom APIs or external integrations beyond Fabric API and Yarn.
- Publishing configuration is present in `build.gradle` (Maven).

## Do Not

- Do not introduce nonstandard build tools or scripts.
- Do not place client-only code in the main source set.
- Do not modify files outside the established source/resource structure.
- Do not use mappings other than Yarn.

## Additional Notes

- The `README.md` is primarily a directory listing; all conventions are discoverable from code and standard Fabric practices.
- No hidden workflows, scripts, or nonstandard conventions are present.

---

This file is auto-generated for AI coding agents. Update if project conventions change.
