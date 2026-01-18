// src/main/java/dk/mosberg/modid/registry/ModItems.java
package dk.mosberg.modid.registry;

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

    // Flasks
    public static final Item SMALL_FLASK =
            register("small_flask", new SmallFlaskItem(new Item.Settings().maxCount(16)));
    public static final Item MEDIUM_FLASK =
            register("medium_flask", new MediumFlaskItem(new Item.Settings().maxCount(16)));
    public static final Item BIG_FLASK =
            register("big_flask", new BigFlaskItem(new Item.Settings().maxCount(16)));

    // Containers
    public static final Item KEG = register("keg", new KegItem(new Item.Settings().maxCount(16)));
    public static final Item BARREL =
            register("barrel", new BarrelItem(new Item.Settings().maxCount(16)));

    private ModItems() {}

    public static void registerModItems() {
        // Touching this class triggers static init (item registration).
        ModId.LOGGER.info("Registering items for {}", ModId.MOD_ID);
    }

    private static Item register(String name, Item item) {
        return Registry.register(Registries.ITEM, Identifier.of(ModId.MOD_ID, name), item);
    }
}
