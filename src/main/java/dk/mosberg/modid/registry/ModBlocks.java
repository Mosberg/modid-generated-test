// src/main/java/dk/mosberg/modid/registry/ModBlocks.java
package dk.mosberg.modid.registry;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import dk.mosberg.modid.ModId;
import dk.mosberg.modid.block.BarrelBlock;
import dk.mosberg.modid.block.KegBlock;
import net.minecraft.block.AbstractBlock;
import net.minecraft.block.Block;
import net.minecraft.block.Blocks;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.util.Identifier;

public final class ModBlocks {

    public static final Map<String, Block> BLOCKS = new LinkedHashMap<>();

    public static final List<Block> BARRELS = new ArrayList<>();
    public static final List<Block> KEGS = new ArrayList<>();

    private static final String[] WOODS = {"acacia", "bamboo", "birch", "cherry", "crimson",
            "dark_oak", "jungle", "mangrove", "oak", "pale_oak", "spruce", "warped"};

    private static final String[] BARREL_MATERIALS = {"copper", "copper_exposed", "copper_oxidized",
            "copper_weathered", "gold", "iron", "netherite"};

    private static final String[] KEG_MATERIALS = {"copper_exposed", "copper", "copper_oxidized",
            "copper_weathered", "gold", "iron", "netherite"};

    private ModBlocks() {}

    static {
        registerAllBarrels();
        registerAllKegs();
    }

    public static void registerModBlocks() {
        ModId.LOGGER.info("Registered {} blocks for {}", BLOCKS.size(), ModId.MOD_ID);
    }

    public static Block get(String id) {
        Block block = BLOCKS.get(id);
        if (block == null)
            throw new IllegalArgumentException("Unknown mod block id: " + id);
        return block;
    }

    private static void registerAllBarrels() {
        for (String wood : WOODS) {
            for (String material : BARREL_MATERIALS) {
                String id = wood + "_" + material + "_barrel_block";
                register(id, new BarrelBlock(settingsFor(id)), BARRELS);
            }
        }
    }

    private static void registerAllKegs() {
        for (String material : KEG_MATERIALS) {
            String id = material + "_keg_block";
            register(id, new KegBlock(settingsFor(id)), KEGS);
        }
    }

    private static AbstractBlock.Settings settingsFor(String id) {
        Identifier identifier = Identifier.of(ModId.MOD_ID, id);
        RegistryKey<Block> key = RegistryKey.of(RegistryKeys.BLOCK, identifier);

        // Copy vanilla barrel-ish properties (strength/sounds), but keep it simple for now.
        return AbstractBlock.Settings.copy(Blocks.BARREL).registryKey(key);
    }

    private static Block register(String id, Block block, List<Block> category) {
        Identifier identifier = Identifier.of(ModId.MOD_ID, id);
        Block registered = Registry.register(Registries.BLOCK, identifier, block);
        BLOCKS.put(id, registered);
        category.add(registered);
        return registered;
    }
}
