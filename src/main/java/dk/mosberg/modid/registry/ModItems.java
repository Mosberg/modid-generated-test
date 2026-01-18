// src/main/java/dk/mosberg/modid/registry/ModItems.java
package dk.mosberg.modid.registry;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import dk.mosberg.modid.ModId;
import dk.mosberg.modid.item.BarrelItem;
import dk.mosberg.modid.item.BigFlaskItem;
import dk.mosberg.modid.item.KegItem;
import dk.mosberg.modid.item.MediumFlaskItem;
import dk.mosberg.modid.item.SmallFlaskItem;
import net.minecraft.item.Item;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.registry.RegistryKey;
import net.minecraft.registry.RegistryKeys;
import net.minecraft.util.Identifier;

public final class ModItems {

        public static final Map<String, Item> ITEMS = new LinkedHashMap<>();

        public static final List<Item> BARRELS = new ArrayList<>();
        public static final List<Item> KEGS = new ArrayList<>();
        public static final List<Item> SMALL_FLASKS = new ArrayList<>();
        public static final List<Item> MEDIUM_FLASKS = new ArrayList<>();
        public static final List<Item> BIG_FLASKS = new ArrayList<>();

        private static final String[] WOODS = {"acacia", "bamboo", "birch", "cherry", "crimson",
                        "dark_oak", "jungle", "mangrove", "oak", "pale_oak", "spruce", "warped"};

        private static final String[] BARREL_MATERIALS = {"copper", "copper_exposed",
                        "copper_oxidized", "copper_weathered", "gold", "iron", "netherite"};

        private static final String[] KEG_MATERIALS = {"copper_exposed", "copper",
                        "copper_oxidized", "copper_weathered", "gold", "iron", "netherite"};

        private static final String[] STAINED_COLORS = {"black", "blue", "brown", "cyan", "gray",
                        "green", "light_blue", "light_gray", "lime", "magenta", "orange", "pink",
                        "purple", "red", "white", "yellow"};

        private ModItems() {}

        static {
                registerAllBarrels();
                registerAllKegs();
                registerAllFlasks();
        }

        public static void registerModItems() {
                ModId.LOGGER.info("Registered {} items for {}", ITEMS.size(), ModId.MOD_ID);
        }

        public static Item get(String id) {
                Item item = ITEMS.get(id);
                if (item == null)
                        throw new IllegalArgumentException("Unknown mod item id: " + id);
                return item;
        }

        private static void registerAllBarrels() {
                for (String wood : WOODS) {
                        for (String material : BARREL_MATERIALS) {
                                String id = wood + "_" + material + "_barrel";
                                register(id, (s) -> new BarrelItem(s), settingsFor(id).maxCount(1),
                                                BARRELS);
                        }
                }
        }

        private static void registerAllKegs() {
                for (String material : KEG_MATERIALS) {
                        String id = material + "_keg";
                        register(id, (s) -> new KegItem(s), settingsFor(id).maxCount(1), KEGS);
                }
        }

        private static void registerAllFlasks() {
                registerFlasksForSize("small", SMALL_FLASKS, (s) -> new SmallFlaskItem(s));
                registerFlasksForSize("medium", MEDIUM_FLASKS, (s) -> new MediumFlaskItem(s));
                registerFlasksForSize("big", BIG_FLASKS, (s) -> new BigFlaskItem(s));
        }

        private static void registerFlasksForSize(String size, List<Item> out,
                        ItemFactory factory) {
                for (String wood : WOODS) {
                        String glassId = size + "_" + wood + "_glass_flask";
                        register(glassId, factory, settingsFor(glassId).maxCount(16), out);

                        String tintedId = size + "_" + wood + "_tinted_glass_flask";
                        register(tintedId, factory, settingsFor(tintedId).maxCount(16), out);

                        for (String color : STAINED_COLORS) {
                                String stainedId = size + "_" + wood + "_" + color
                                                + "_stained_glass_flask";
                                register(stainedId, factory, settingsFor(stainedId).maxCount(16),
                                                out);
                        }
                }
        }

        private static Item.Settings settingsFor(String id) {
                Identifier identifier = Identifier.of(ModId.MOD_ID, id);
                RegistryKey<Item> key = RegistryKey.of(RegistryKeys.ITEM, identifier);
                return new Item.Settings().registryKey(key);
        }

        private static Item register(String id, ItemFactory factory, Item.Settings settings,
                        List<Item> category) {
                Identifier identifier = Identifier.of(ModId.MOD_ID, id);
                Item item = factory.create(settings);
                Item registered = Registry.register(Registries.ITEM, identifier, item);

                ITEMS.put(id, registered);
                category.add(registered);
                return registered;
        }

        private static void registerAllBarrels() {
                for (String wood : WOODS) {
                        for (String material : BARREL_MATERIALS) {
                                String id = wood + "_" + material + "_barrel";
                                String blockId = wood + "_" + material + "_barrel_block";

                                register(id, (s) -> new BarrelItem(ModBlocks.get(blockId), s),
                                                settingsFor(id).maxCount(1), BARRELS);
                        }
                }
        }

        private static void registerAllKegs() {
                for (String material : KEG_MATERIALS) {
                        String id = material + "_keg";
                        String blockId = material + "_keg_block";

                        register(id, (s) -> new KegItem(ModBlocks.get(blockId), s),
                                        settingsFor(id).maxCount(1), KEGS);
                }
        }

        @FunctionalInterface
        private interface ItemFactory {
                Item create(Item.Settings settings);
        }
}
