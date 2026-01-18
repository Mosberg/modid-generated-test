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
import net.minecraft.util.Identifier;

public final class ModItems {

        // Keep a predictable order for creative tabs.
        public static final Map<String, Item> ITEMS = new LinkedHashMap<>();

        public static final List<Item> BARRELS = new ArrayList<>();
        public static final List<Item> KEGS = new ArrayList<>();
        public static final List<Item> SMALL_FLASKS = new ArrayList<>();
        public static final List<Item> MEDIUM_FLASKS = new ArrayList<>();
        public static final List<Item> BIG_FLASKS = new ArrayList<>();

        // These lists match the IDs in your en_us.json naming scheme.
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
                // Class load triggers static init, which performs the registrations.
                ModId.LOGGER.info("Registered {} items for {}", ITEMS.size(), ModId.MOD_ID);
        }

        public static Item get(String id) {
                Item item = ITEMS.get(id);
                if (item == null) {
                        throw new IllegalArgumentException("Unknown mod item id: " + id);
                }
                return item;
        }

        private static void registerAllBarrels() {
                Item.Settings settings = new Item.Settings().maxCount(1);

                for (String wood : WOODS) {
                        for (String material : BARREL_MATERIALS) {
                                String id = wood + "_" + material + "_barrel";
                                register(id, new BarrelItem(settings), BARRELS);
                        }
                }
        }

        private static void registerAllKegs() {
                Item.Settings settings = new Item.Settings().maxCount(1);

                for (String material : KEG_MATERIALS) {
                        String id = material + "_keg";
                        register(id, new KegItem(settings), KEGS);
                }
        }

        private static void registerAllFlasks() {
                registerFlasksForSize("small", SMALL_FLASKS, (s) -> new SmallFlaskItem(s));
                registerFlasksForSize("medium", MEDIUM_FLASKS, (s) -> new MediumFlaskItem(s));
                registerFlasksForSize("big", BIG_FLASKS, (s) -> new BigFlaskItem(s));
        }

        private static void registerFlasksForSize(String size, List<Item> out,
                        FlaskFactory factory) {
                Item.Settings settings = new Item.Settings().maxCount(16);

                for (String wood : WOODS) {
                        // Plain glass / tinted glass variants.
                        register(size + "_" + wood + "_glass_flask", factory.create(settings), out);
                        register(size + "_" + wood + "_tinted_glass_flask",
                                        factory.create(settings), out);

                        // Stained variants.
                        for (String color : STAINED_COLORS) {
                                String id = size + "_" + wood + "_" + color
                                                + "_stained_glass_flask";
                                register(id, factory.create(settings), out);
                        }
                }
        }

        private static Item register(String id, Item item, List<Item> category) {
                Item registered = Registry.register(Registries.ITEM,
                                Identifier.of(ModId.MOD_ID, id), item);
                ITEMS.put(id, registered);
                category.add(registered);
                return registered;
        }

        @FunctionalInterface
        private interface FlaskFactory {
                Item create(Item.Settings settings);
        }
}
