package dk.mosberg.modid.block.entity;

import dk.mosberg.modid.registry.ModBlockEntities;
import net.minecraft.block.BlockState;
import net.minecraft.util.math.BlockPos;

public class BarrelBlockEntity extends AbstractTankBlockEntity {
    public static final long CAPACITY =
            net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BUCKET * 4;

    public BarrelBlockEntity(BlockPos pos, BlockState state) {
        super(ModBlockEntities.BARREL, pos, state);
    }

    @Override
    public long getCapacity() {
        return CAPACITY;
    }
}
