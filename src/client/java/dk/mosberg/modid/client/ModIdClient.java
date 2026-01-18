package dk.mosberg.modid.client;

import net.fabricmc.api.ClientModInitializer;

// NOTE: Yarn names vary; search for TintResourceTypes and register your ID -> codec.
public class ModIdClient implements ClientModInitializer {
	@Override
	public void onInitializeClient() {
		// TintResourceTypes.ID_MAPPER.put(Identifier.of(ModId.MOD_ID, "fluid_from_component"),
		// FluidFromComponentTintSource.CODEC);

		// If your Yarn exposes a different registration method, use that instead.
	}
}
