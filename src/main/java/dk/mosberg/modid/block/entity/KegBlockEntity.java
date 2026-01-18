package dk.mosberg.modid.block.entity;

import dk.mosberg.modid.registry.ModBlockEntities;
import net.minecraft.block.BlockState;
import net.minecraft.util.math.BlockPos;

public class KegBlockEntity extends AbstractTankBlockEntity {
    public static final long CAPACITY =
            net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants.BUCKET * 8;

    public KegBlockEntity(BlockPos pos, BlockState state) {
        super(ModBlockEntities.KEG, pos, state);
    }

    @Override
    public long getCapacity() {
        return CAPACITY;
    }
}
