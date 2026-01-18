// src/main/java/dk/mosberg/modid/registry/ModItemGroups.java
package dk.mosberg.modid.registry;

import dk.mosberg.modid.ModId;
import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.Item;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

public final class ModItemGroups {

    public static final ItemGroup BARRELS = register("barrels", "itemGroup.modid.barrels",
            ModItems.get("acacia_copper_barrel"), ModItems.BARRELS);

    public static final ItemGroup KEGS =
            register("kegs", "itemGroup.modid.kegs", ModItems.get("copper_keg"), ModItems.KEGS);

    public static final ItemGroup SMALL_FLASKS =
            register("smallflasks", "itemGroup.modid.smallflasks",
                    ModItems.get("small_oak_glass_flask"), ModItems.SMALL_FLASKS);

    public static final ItemGroup MEDIUM_FLASKS =
            register("mediumflasks", "itemGroup.modid.mediumflasks",
                    ModItems.get("medium_oak_glass_flask"), ModItems.MEDIUM_FLASKS);

    public static final ItemGroup BIG_FLASKS = register("bigflasks", "itemGroup.modid.bigflasks",
            ModItems.get("big_oak_glass_flask"), ModItems.BIG_FLASKS);

    private ModItemGroups() {}

    public static void registerItemGroups() {
        // Class load triggers static init, which registers the item groups.
        ModId.LOGGER.info("Registered item groups for {}", ModId.MOD_ID);
    }

    private static ItemGroup register(String groupId, String translationKey, Item icon,
            Iterable<Item> items) {
        return Registry.register(Registries.ITEM_GROUP, Identifier.of(ModId.MOD_ID, groupId),
                FabricItemGroup.builder().displayName(Text.translatable(translationKey))
                        .icon(() -> new ItemStack(icon)).entries((displayContext, entries) -> {
                            for (Item item : items) {
                                entries.add(item);
                            }
                        }).build());
    }
}
