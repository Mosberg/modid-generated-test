// src/main/java/dk/mosberg/modid/registry/ModItemGroups.java
package dk.mosberg.modid.registry;

import dk.mosberg.modid.ModId;
import net.fabricmc.fabric.api.itemgroup.v1.FabricItemGroup;
import net.minecraft.item.ItemGroup;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.text.Text;
import net.minecraft.util.Identifier;

public final class ModItemGroups {

    public static final ItemGroup MODID_GROUP =
            Registry.register(Registries.ITEM_GROUP, Identifier.of(ModId.MOD_ID, "modid"),
                    FabricItemGroup.builder().displayName(Text.translatable("itemGroup.modid"))
                            .icon(() -> new ItemStack(ModItems.SMALL_FLASK))
                            .entries((displayContext, entries) -> {
                                entries.add(ModItems.SMALL_FLASK);
                                entries.add(ModItems.MEDIUM_FLASK);
                                entries.add(ModItems.BIG_FLASK);
                                entries.add(ModItems.KEG);
                                entries.add(ModItems.BARREL);
                            }).build());

    private ModItemGroups() {}

    public static void registerItemGroups() {
        // Touching this class triggers static init (item group registration).
        ModId.LOGGER.info("Registering item groups for {}", ModId.MOD_ID);
    }
}
