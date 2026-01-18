package dk.mosberg.modid.block;

import com.mojang.serialization.MapCodec;
import dk.mosberg.modid.block.entity.AbstractTankBlockEntity;
import dk.mosberg.modid.block.entity.BarrelBlockEntity;
import dk.mosberg.modid.registry.ModDataComponents;
import net.minecraft.block.Block;
import net.minecraft.block.BlockRenderType;
import net.minecraft.block.BlockState;
import net.minecraft.block.BlockWithEntity;
import net.minecraft.block.entity.BlockEntity;
import net.minecraft.entity.LivingEntity;
import net.minecraft.item.ItemPlacementContext;
import net.minecraft.item.ItemStack;
import net.minecraft.state.StateManager;
import net.minecraft.state.property.Properties;
import net.minecraft.util.math.BlockPos;
import net.minecraft.util.math.Direction;
import net.minecraft.world.World;

public class BarrelBlock extends BlockWithEntity {
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

    @Override
    public BlockEntity createBlockEntity(BlockPos pos, BlockState state) {
        return new BarrelBlockEntity(pos, state);
    }

    @Override
    public BlockRenderType getRenderType(BlockState state) {
        return BlockRenderType.MODEL;
    }

    @Override
    public void onPlaced(World world, BlockPos pos, BlockState state, LivingEntity placer,
            ItemStack stack) {
        super.onPlaced(world, pos, state, placer, stack);
        if (world.isClient)
            return;

        BlockEntity be = world.getBlockEntity(pos);
        if (be instanceof AbstractTankBlockEntity tankBe) {
            ModDataComponents.FluidContent content = stack.getOrDefault(
                    ModDataComponents.FLUID_CONTENT, ModDataComponents.FluidContent.EMPTY);
            tankBe.fromComponent(content);
        }
    }

    @Override
    public void onStateReplaced(BlockState state, World world, BlockPos pos, BlockState newState,
            boolean moved) {
        if (!state.isOf(newState.getBlock())) {
            BlockEntity be = world.getBlockEntity(pos);
            if (!world.isClient && be instanceof AbstractTankBlockEntity tankBe) {
                ItemStack drop = new ItemStack(this.asItem());
                drop.set(ModDataComponents.FLUID_CONTENT, tankBe.toComponent());
                Block.dropStack(world, pos, drop);
            }
        }
        super.onStateReplaced(state, world, pos, newState, moved);
    }
}
