package dk.mosberg.modid.registry;

import dk.mosberg.modid.ModId;
import dk.mosberg.modid.block.entity.AbstractTankBlockEntity;
import net.fabricmc.fabric.api.transfer.v1.fluid.FluidStorage;
import net.fabricmc.fabric.api.transfer.v1.fluid.FluidVariant;
import net.fabricmc.fabric.api.transfer.v1.storage.Storage;
import net.fabricmc.fabric.api.transfer.v1.storage.base.SingleVariantStorage;
import net.fabricmc.fabric.api.transfer.v1.transaction.TransactionContext;
import net.minecraft.fluid.Fluids;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;

public final class ModFluidStorages {
    private ModFluidStorages() {}

    private static Storage<FluidVariant> stackTank(ItemStack stack, long capacity) {
        return new SingleVariantStorage<>() {
            @Override
            protected FluidVariant getBlankVariant() {
                return FluidVariant.of(Fluids.EMPTY);
            }

            @Override
            protected long getCapacity(FluidVariant variant) {
                return capacity;
            }

            @Override
            protected void onFinalCommit() {
                ModDataComponents.FluidContent content;
                if (amount <= 0 || variant.isBlank()) {
                    content = ModDataComponents.FluidContent.EMPTY;
                } else {
                    content = new ModDataComponents.FluidContent(
                            net.minecraft.registry.Registries.FLUID.getId(variant.getFluid()),
                            amount);
                }
                stack.set(ModDataComponents.FLUID_CONTENT, content);
            }

            @Override
            public long insert(FluidVariant insertedVariant, long maxAmount,
                    TransactionContext transaction) {
                if (!isResourceBlank() && !getResource().equals(insertedVariant))
                    return 0;
                return super.insert(insertedVariant, maxAmount, transaction);
            }

            {
                // init from component
                ModDataComponents.FluidContent c = stack.getOrDefault(
                        ModDataComponents.FLUID_CONTENT, ModDataComponents.FluidContent.EMPTY);
                if (c.isEmpty()) {
                    variant = FluidVariant.of(Fluids.EMPTY);
                    amount = 0;
                } else {
                    variant = FluidVariant
                            .of(net.minecraft.registry.Registries.FLUID.get(c.fluidId()));
                    amount = Math.min(c.amount(), capacity);
                }
            }
        };
    }

    public static void init() {
        // Expose storages for placed blocks (block entities).
        FluidStorage.SIDED.registerForBlockEntity(
                (be, side) -> ((AbstractTankBlockEntity) be).getStorage(side),
                ModBlockEntities.BARREL);
        FluidStorage.SIDED.registerForBlockEntity(
                (be, side) -> ((AbstractTankBlockEntity) be).getStorage(side),
                ModBlockEntities.KEG);

        // Barrel/Keg item (as an item container as well)
        FluidStorage.ITEM.registerForItems(
                (stack, ctx) -> stackTank(stack,
                        net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BUCKET * 4),
                ModItems.BARRELS.toArray(Item[]::new));

        FluidStorage.ITEM.registerForItems(
                (stack, ctx) -> stackTank(stack,
                        net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BUCKET * 8),
                ModItems.KEGS.toArray(Item[]::new));

        // Flasks
        FluidStorage.ITEM.registerForItems(
                (stack, ctx) -> stackTank(stack,
                        net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BOTTLE),
                ModItems.SMALL_FLASKS.toArray(Item[]::new));
        FluidStorage.ITEM.registerForItems(
                (stack, ctx) -> stackTank(stack,
                        net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BOTTLE * 2),
                ModItems.MEDIUM_FLASKS.toArray(Item[]::new));
        FluidStorage.ITEM.registerForItems(
                (stack, ctx) -> stackTank(stack,
                        net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BOTTLE * 4),
                ModItems.BIG_FLASKS.toArray(Item[]::new));

        ModId.LOGGER.info("Registered fluid storages for {}", ModId.MOD_ID);
    }
}
