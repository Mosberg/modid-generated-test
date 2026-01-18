// src/main/java/dk/mosberg/modid/block/BarrelBlock.java
package dk.mosberg.modid.block;

import com.mojang.serialization.MapCodec;
import net.minecraft.block.Block;
import net.minecraft.block.BlockState;
import net.minecraft.block.HorizontalFacingBlock;
import net.minecraft.item.ItemPlacementContext;
import net.minecraft.state.StateManager;
import net.minecraft.state.property.Properties;
import net.minecraft.util.math.Direction;

public class BarrelBlock extends HorizontalFacingBlock {

    public static final MapCodec<BarrelBlock> CODEC = Block.createCodec(BarrelBlock::new);

    public BarrelBlock(Settings settings) {
        super(settings);
        this.setDefaultState(
                this.getDefaultState().with(Properties.HORIZONTAL_FACING, Direction.NORTH));
    }

    @Override
    protected MapCodec<? extends BarrelBlock> getCodec() {
        return CODEC;
    }

    @Override
    protected void appendProperties(StateManager.Builder<Block, BlockState> builder) {
        builder.add(Properties.HORIZONTAL_FACING);
    }

    @Override
    public BlockState getPlacementState(ItemPlacementContext ctx) {
        return this.getDefaultState().with(Properties.HORIZONTAL_FACING,
                ctx.getHorizontalPlayerFacing().getOpposite());
    }
}
