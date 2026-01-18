package dk.mosberg.modid.item;

import net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants;

public class SmallFlaskItem extends AbstractFluidContainerItem {
    public SmallFlaskItem(Settings settings) {
        super(settings);
    }

    @Override
    protected long getCapacity() {
        return FluidConstants.BOTTLE;
    }
}
