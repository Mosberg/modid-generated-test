// src/main/java/dk/mosberg/modid/ModId.java
package dk.mosberg.modid;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import dk.mosberg.modid.registry.ModBlockEntities;
import dk.mosberg.modid.registry.ModBlocks;
import dk.mosberg.modid.registry.ModDataComponents;
import dk.mosberg.modid.registry.ModFluidStorages;
import dk.mosberg.modid.registry.ModItemGroups;
import dk.mosberg.modid.registry.ModItems;
import net.fabricmc.api.ModInitializer;

public class ModId implements ModInitializer {

	public static final String MOD_ID = "modid";
	public static final Logger LOGGER = LoggerFactory.getLogger(MOD_ID);

	@Override
	public void onInitialize() {
		ModItems.registerModItems();
		ModBlocks.registerModBlocks();
		ModItemGroups.registerItemGroups();

		ModDataComponents.init();
		ModBlockEntities.init();
		ModFluidStorages.init();

		LOGGER.info("Initialized {}", MOD_ID);
	}
}
