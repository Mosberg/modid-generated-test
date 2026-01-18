package dk.mosberg.modid.item;

import java.util.List;
import dk.mosberg.modid.registry.ModDataComponents;
import net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants;
import net.minecraft.block.Block;
import net.minecraft.item.BlockItem;
import net.minecraft.item.ItemStack;
import net.minecraft.item.tooltip.TooltipType;
import net.minecraft.text.Text;

public class KegItem extends BlockItem {
    private static final long CAPACITY = FluidConstants.BUCKET * 8;

    public KegItem(Block block, Settings settings) {
        super(block, settings);
    }

    public void appendTooltip(ItemStack stack, TooltipContext context, List<Text> tooltip,
            TooltipType type) {
        ModDataComponents.FluidContent c = stack.getOrDefault(ModDataComponents.FLUID_CONTENT,
                ModDataComponents.FluidContent.EMPTY);
        if (c.isEmpty()) {
            tooltip.add(Text.translatable("tooltip.modid.fluid.empty"));
        } else {
            tooltip.add(Text.literal("Fluid: " + c.fluidId()));
            tooltip.add(Text.literal("Amount: " + c.amount() + " / " + CAPACITY));
        }
    }
}
