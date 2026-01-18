
package dk.mosberg.modid.block.entity;

import dk.mosberg.modid.registry.ModDataComponents;
import net.fabricmc.fabric.api.transfer.v1.fluid.FluidVariant;
import net.fabricmc.fabric.api.transfer.v1.storage.base.SidedStorageBlockEntity;
import net.fabricmc.fabric.api.transfer.v1.storage.base.SingleVariantStorage;
import net.fabricmc.fabric.api.transfer.v1.transaction.TransactionContext;
import net.minecraft.block.BlockState;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.fluid.Fluids;
import net.minecraft.nbt.NbtCompound;
import net.minecraft.registry.Registries;
import net.minecraft.util.Identifier;
import net.minecraft.util.math.Direction;

public abstract class AbstractTankBlockEntity extends BlockEntity
        implements SidedStorageBlockEntity {

    protected final SingleVariantStorage<FluidVariant> tank = new SingleVariantStorage<>() {
        @SuppressWarnings("null")
        @Override
        protected FluidVariant getBlankVariant() {
            return FluidVariant.of(Fluids.EMPTY);
        }

        @Override
        protected long getCapacity(FluidVariant variant) {
            return AbstractTankBlockEntity.this.getCapacity();
        }

        @Override
        protected void onFinalCommit() {
            markDirty();
            if (world != null) {
                world.updateListeners(pos, getCachedState(), getCachedState(), 3);
            }
        }

        @Override
        protected boolean canInsert(FluidVariant variant) {
            return true;
        }

        @Override
        protected boolean canExtract(FluidVariant variant) {
            return true;
        }

        @SuppressWarnings("null")
        @Override
        public long insert(@SuppressWarnings("null") FluidVariant insertedVariant, long maxAmount,
                @SuppressWarnings("null") TransactionContext transaction) {
            // Enforce single-fluid rule: can only contain one fluid type at a time.
            if (!isResourceBlank() && !getResource().equals(insertedVariant))
                return 0;
            return super.insert(insertedVariant, maxAmount, transaction);
        }
    };

    protected AbstractTankBlockEntity(net.minecraft.block.entity.BlockEntityType<?> type,
            net.minecraft.util.math.BlockPos pos, BlockState state) {
        super(type, pos, state);
    }

    public abstract long getCapacity();

    public SingleVariantStorage<FluidVariant> getStorage(Direction side) {
        return tank;
    }

    public ModDataComponents.FluidContent toComponent() {
        if (tank.amount <= 0 || tank.variant.isBlank())
            return ModDataComponents.FluidContent.EMPTY;
        Identifier id = Registries.FLUID.getId(tank.variant.getFluid());
        return new ModDataComponents.FluidContent(id, tank.amount);
    }

    @SuppressWarnings("null")
    public void fromComponent(ModDataComponents.FluidContent content) {
        if (content == null || content.isEmpty()) {
            tank.variant = FluidVariant.of(Fluids.EMPTY);
            tank.amount = 0;
            markDirty();
            return;
        }

        var fluid = Registries.FLUID.get(content.fluidId());
        tank.variant = FluidVariant.of(fluid);
        tank.amount = Math.min(content.amount(), getCapacity());
        markDirty();
    }

    public void writeTankNbt(NbtCompound nbt) {
        ModDataComponents.FluidContent c = toComponent();
        nbt.putString("Fluid", c.fluidId().toString());
        nbt.putLong("Amount", c.amount());
    }

    public void readTankNbt(NbtCompound nbt) {
        String fluidStr = nbt.getString("Fluid").orElse("");
        Identifier id = Identifier.tryParse(fluidStr);
        long amount = nbt.getLong("Amount").orElse(0L);
        if (id == null) {
            fromComponent(ModDataComponents.FluidContent.EMPTY);
        } else {
            fromComponent(new ModDataComponents.FluidContent(id, amount));
        }
    }
}
