package dk.mosberg.modid.registry;

import dk.mosberg.modid.ModId;
import dk.mosberg.modid.block.entity.BarrelBlockEntity;
import dk.mosberg.modid.block.entity.KegBlockEntity;
import net.fabricmc.fabric.api.object.builder.v1.block.entity.FabricBlockEntityTypeBuilder;
import net.minecraft.block.Block;
import net.minecraft.block.entity.BlockEntityType;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

public final class ModBlockEntities {
    private ModBlockEntities() {}

    public static BlockEntityType<BarrelBlockEntity> BARREL;
    public static BlockEntityType<KegBlockEntity> KEG;

    @SuppressWarnings("null")
    public static void init() {
        BARREL = Registry.register(Registries.BLOCK_ENTITY_TYPE,
                Identifier.of(ModId.MOD_ID, "barrel"),
                FabricBlockEntityTypeBuilder
                        .create(BarrelBlockEntity::new, ModBlocks.BARRELS.toArray(Block[]::new))
                        .build());

        KEG = Registry.register(Registries.BLOCK_ENTITY_TYPE, Identifier.of(ModId.MOD_ID, "keg"),
                FabricBlockEntityTypeBuilder
                        .create(KegBlockEntity::new, ModBlocks.KEGS.toArray(Block[]::new)).build());

        ModId.LOGGER.info("Registered block entities for {}", ModId.MOD_ID);
    }
}
