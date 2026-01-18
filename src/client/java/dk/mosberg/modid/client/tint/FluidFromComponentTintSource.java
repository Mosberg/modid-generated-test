package dk.mosberg.modid.client.tint;

import com.mojang.serialization.MapCodec;
import dk.mosberg.modid.registry.ModDataComponents;
import net.fabricmc.fabric.api.client.render.fluid.v1.FluidRenderHandlerRegistry;
import net.minecraft.fluid.Fluid;
import net.minecraft.fluid.Fluids;
import net.minecraft.item.ItemStack;
import net.minecraft.registry.Registries;

// NOTE: Class/interface names here are Yarn-dependent in 1.21.11.
// In Yarn, search for "TintSource" and "TintResourceTypes" and adjust imports accordingly.
public final class FluidFromComponentTintSource /* implements TintSource */ {
    public static final MapCodec<FluidFromComponentTintSource> CODEC =
            MapCodec.unit(new FluidFromComponentTintSource());

    private FluidFromComponentTintSource() {}

    // Signature is Yarn-dependent; adapt to the actual TintSource method.
    public int getTint(ItemStack stack, int tintIndex) {
        if (tintIndex != 1)
            return 0xFFFFFFFF;

        var content = stack.getOrDefault(ModDataComponents.FLUID_CONTENT,
                ModDataComponents.FluidContent.EMPTY);
        if (content.isEmpty())
            return 0xFFFFFFFF;

        Fluid fluid = Registries.FLUID.get(content.fluidId());
        if (fluid == null || fluid == Fluids.EMPTY)
            return 0xFFFFFFFF;

        var handler = FluidRenderHandlerRegistry.INSTANCE.get(fluid);
        if (handler == null)
            return 0xFFFFFFFF;

        // No world/pos context for items (same limitation described in the wiki).
        int rgb = handler.getFluidColor(null, null, fluid.getDefaultState());
        return 0xFF000000 | (rgb & 0x00FFFFFF);
    }

    // Signature is Yarn-dependent; adapt to actual API (usually a "codec()" accessor).
    public MapCodec<FluidFromComponentTintSource> codec() {
        return CODEC;
    }
}
