package dk.mosberg.modid.item;

import net.fabricmc.fabric.api.transfer.v1.fluid.FluidConstants;

public class MediumFlaskItem extends AbstractFluidContainerItem {
    public MediumFlaskItem(Settings settings) {
        super(settings);
    }

    @Override
    protected long getCapacity() {
        return FluidConstants.BOTTLE * 2;
    }
}
