package dk.mosberg.modid.item;

import net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants;

public class BigFlaskItem extends AbstractFluidContainerItem {
    public BigFlaskItem(Settings settings) {
        super(settings);
    }

    @Override
    protected long getCapacity() {
        return FluidConstants.BOTTLE * 4;
    }
}
