package dk.mosberg.modid.item;

import java.util.List;
import dk.mosberg.modid.registry.ModDataComponents;
import net.minecraft.item.Item;
import net.minecraft.item.ItemStack;
import net.minecraft.item.tooltip.TooltipType;
import net.minecraft.text.Text;

public abstract class AbstractFluidContainerItem extends Item {
    protected AbstractFluidContainerItem(Settings settings) {
        super(settings);
    }

    protected abstract long getCapacity();

    public void appendTooltip(ItemStack stack, TooltipContext context, List<Text> tooltip,
            TooltipType type) {
        ModDataComponents.FluidContent c = stack.getOrDefault(ModDataComponents.FLUID_CONTENT,
                ModDataComponents.FluidContent.EMPTY);
        if (c.isEmpty()) {
            tooltip.add(Text.translatable("tooltip.modid.fluid.empty"));
        } else {
            tooltip.add(Text.literal("Fluid: " + c.fluidId()));
            tooltip.add(Text.literal("Amount: " + c.amount() + " / " + getCapacity()));
        }
    }
}
