```
modid
├─ build.gradle
├─ gradle
│  └─ wrapper
│     ├─ gradle-wrapper.jar
│     └─ gradle-wrapper.properties
├─ gradle.properties
├─ gradlew
├─ gradlew.bat
├─ LICENSE
├─ README.md
├─ settings.gradle
└─ src
   ├─ client
   │  ├─ java
   │  │  └─ dk
   │  │     └─ mosberg
   │  │        └─ modid
   │  │           └─ ModIdClient.java
   │  └─ resources
   └─ main
      ├─ java
      │  └─ dk
      │     └─ mosberg
      │        └─ modid
      │           ├─ block
      │           │  ├─ BarrelBlock.java        # Block class for barrels (currently empty)
      │           │  └─ KegBlock.java           # Block class for kegs (currently empty)
      │           ├─ item
      │           │  ├─ BarrelItem.java         # Item class for barrels
      │           │  ├─ BigFlaskItem.java       # Item class for big flasks
      │           │  ├─ KegItem.java            # Item class for kegs
      │           │  ├─ MediumFlaskItem.java    # Item class for medium flasks
      │           │  └─ SmallFlaskItem.java     # Item class for small flasks
      │           ├─ ModId.java                 # Main mod class
      │           └─ registry
      │              ├─ ModBlocks.java          # Block registration (currently empty)
      │              ├─ ModItemGroups.java      # Item group registration
      │              └─ ModItems.java           # Item registration
      └─ resources
         ├─ assets
         │  └─ modid
         │     ├─ blockstates
         │     │  ├─ acacia_copper_barrel_block.json
         │     │  ├─ acacia_copper_exposed_barrel_block.json
         │     │  ├─ acacia_copper_oxidized_barrel_block.json
         │     │  ├─ acacia_copper_weathered_barrel_block.json
         │     │  ├─ acacia_gold_barrel_block.json
         │     │  ├─ acacia_iron_barrel_block.json
         │     │  ├─ acacia_netherite_barrel_block.json
         │     │  ├─ bamboo_copper_barrel_block.json
         │     │  ├─ bamboo_copper_exposed_barrel_block.json
         │     │  ├─ bamboo_copper_oxidized_barrel_block.json
         │     │  ├─ bamboo_copper_weathered_barrel_block.json
         │     │  ├─ bamboo_gold_barrel_block.json
         │     │  ├─ bamboo_iron_barrel_block.json
         │     │  ├─ bamboo_netherite_barrel_block.json
         │     │  ├─ birch_copper_barrel_block.json
         │     │  ├─ birch_copper_exposed_barrel_block.json
         │     │  ├─ birch_copper_oxidized_barrel_block.json
         │     │  ├─ birch_copper_weathered_barrel_block.json
         │     │  ├─ birch_gold_barrel_block.json
         │     │  ├─ birch_iron_barrel_block.json
         │     │  ├─ birch_netherite_barrel_block.json
         │     │  ├─ cherry_copper_barrel_block.json
         │     │  ├─ cherry_copper_exposed_barrel_block.json
         │     │  ├─ cherry_copper_oxidized_barrel_block.json
         │     │  ├─ cherry_copper_weathered_barrel_block.json
         │     │  ├─ cherry_gold_barrel_block.json
         │     │  ├─ cherry_iron_barrel_block.json
         │     │  ├─ cherry_netherite_barrel_block.json
         │     │  ├─ copper_exposed_keg_block.json
         │     │  ├─ copper_keg_block.json
         │     │  ├─ copper_oxidized_keg_block.json
         │     │  ├─ copper_weathered_keg_block.json
         │     │  ├─ crimson_copper_barrel_block.json
         │     │  ├─ crimson_copper_exposed_barrel_block.json
         │     │  ├─ crimson_copper_oxidized_barrel_block.json
         │     │  ├─ crimson_copper_weathered_barrel_block.json
         │     │  ├─ crimson_gold_barrel_block.json
         │     │  ├─ crimson_iron_barrel_block.json
         │     │  ├─ crimson_netherite_barrel_block.json
         │     │  ├─ dark_oak_copper_barrel_block.json
         │     │  ├─ dark_oak_copper_exposed_barrel_block.json
         │     │  ├─ dark_oak_copper_oxidized_barrel_block.json
         │     │  ├─ dark_oak_copper_weathered_barrel_block.json
         │     │  ├─ dark_oak_gold_barrel_block.json
         │     │  ├─ dark_oak_iron_barrel_block.json
         │     │  ├─ dark_oak_netherite_barrel_block.json
         │     │  ├─ gold_keg_block.json
         │     │  ├─ iron_keg.json
         │     │  ├─ iron_keg_block.json
         │     │  ├─ jungle_copper_barrel_block.json
         │     │  ├─ jungle_copper_exposed_barrel_block.json
         │     │  ├─ jungle_copper_oxidized_barrel_block.json
         │     │  ├─ jungle_copper_weathered_barrel_block.json
         │     │  ├─ jungle_gold_barrel_block.json
         │     │  ├─ jungle_iron_barrel_block.json
         │     │  ├─ jungle_netherite_barrel_block.json
         │     │  ├─ mangrove_copper_barrel_block.json
         │     │  ├─ mangrove_copper_exposed_barrel_block.json
         │     │  ├─ mangrove_copper_oxidized_barrel_block.json
         │     │  ├─ mangrove_copper_weathered_barrel_block.json
         │     │  ├─ mangrove_gold_barrel_block.json
         │     │  ├─ mangrove_iron_barrel_block.json
         │     │  ├─ mangrove_netherite_barrel_block.json
         │     │  ├─ netherite_keg_block.json
         │     │  ├─ oak_copper_barrel_block.json
         │     │  ├─ oak_copper_exposed_barrel_block.json
         │     │  ├─ oak_copper_oxidized_barrel_block.json
         │     │  ├─ oak_copper_weathered_barrel_block.json
         │     │  ├─ oak_gold_barrel_block.json
         │     │  ├─ oak_iron_barrel.json
         │     │  ├─ oak_iron_barrel_block.json
         │     │  ├─ oak_netherite_barrel_block.json
         │     │  ├─ pale_oak_copper_barrel_block.json
         │     │  ├─ pale_oak_copper_exposed_barrel_block.json
         │     │  ├─ pale_oak_copper_oxidized_barrel_block.json
         │     │  ├─ pale_oak_copper_weathered_barrel_block.json
         │     │  ├─ pale_oak_gold_barrel_block.json
         │     │  ├─ pale_oak_iron_barrel_block.json
         │     │  ├─ pale_oak_netherite_barrel_block.json
         │     │  ├─ spruce_copper_barrel_block.json
         │     │  ├─ spruce_copper_exposed_barrel_block.json
         │     │  ├─ spruce_copper_oxidized_barrel_block.json
         │     │  ├─ spruce_copper_weathered_barrel_block.json
         │     │  ├─ spruce_gold_barrel_block.json
         │     │  ├─ spruce_iron_barrel_block.json
         │     │  ├─ spruce_netherite_barrel_block.json
         │     │  ├─ warped_copper_barrel_block.json
         │     │  ├─ warped_copper_exposed_barrel_block.json
         │     │  ├─ warped_copper_oxidized_barrel_block.json
         │     │  ├─ warped_copper_weathered_barrel_block.json
         │     │  ├─ warped_gold_barrel_block.json
         │     │  ├─ warped_iron_barrel_block.json
         │     │  └─ warped_netherite_barrel_block.json
         │     ├─ icon.png
         │     ├─ items
         │     │  ├─ acacia_copper_barrel.json
         │     │  ├─ acacia_copper_barrel_block.json
         │     │  ├─ acacia_copper_exposed_barrel.json
         │     │  ├─ acacia_copper_exposed_barrel_block.json
         │     │  ├─ acacia_copper_oxidized_barrel.json
         │     │  ├─ acacia_copper_oxidized_barrel_block.json
         │     │  ├─ acacia_copper_weathered_barrel.json
         │     │  ├─ acacia_copper_weathered_barrel_block.json
         │     │  ├─ acacia_gold_barrel.json
         │     │  ├─ acacia_gold_barrel_block.json
         │     │  ├─ acacia_iron_barrel.json
         │     │  ├─ acacia_iron_barrel_block.json
         │     │  ├─ acacia_netherite_barrel.json
         │     │  ├─ acacia_netherite_barrel_block.json
         │     │  ├─ bamboo_copper_barrel.json
         │     │  ├─ bamboo_copper_barrel_block.json
         │     │  ├─ bamboo_copper_exposed_barrel.json
         │     │  ├─ bamboo_copper_exposed_barrel_block.json
         │     │  ├─ bamboo_copper_oxidized_barrel.json
         │     │  ├─ bamboo_copper_oxidized_barrel_block.json
         │     │  ├─ bamboo_copper_weathered_barrel.json
         │     │  ├─ bamboo_copper_weathered_barrel_block.json
         │     │  ├─ bamboo_gold_barrel.json
         │     │  ├─ bamboo_gold_barrel_block.json
         │     │  ├─ bamboo_iron_barrel.json
         │     │  ├─ bamboo_iron_barrel_block.json
         │     │  ├─ bamboo_netherite_barrel.json
         │     │  ├─ bamboo_netherite_barrel_block.json
         │     │  ├─ big_acacia_black_stained_glass_flask.json
         │     │  ├─ big_acacia_blue_stained_glass_flask.json
         │     │  ├─ big_acacia_brown_stained_glass_flask.json
         │     │  ├─ big_acacia_cyan_stained_glass_flask.json
         │     │  ├─ big_acacia_glass_flask.json
         │     │  ├─ big_acacia_gray_stained_glass_flask.json
         │     │  ├─ big_acacia_green_stained_glass_flask.json
         │     │  ├─ big_acacia_light_blue_stained_glass_flask.json
         │     │  ├─ big_acacia_light_gray_stained_glass_flask.json
         │     │  ├─ big_acacia_lime_stained_glass_flask.json
         │     │  ├─ big_acacia_magenta_stained_glass_flask.json
         │     │  ├─ big_acacia_orange_stained_glass_flask.json
         │     │  ├─ big_acacia_pink_stained_glass_flask.json
         │     │  ├─ big_acacia_purple_stained_glass_flask.json
         │     │  ├─ big_acacia_red_stained_glass_flask.json
         │     │  ├─ big_acacia_tinted_glass_flask.json
         │     │  ├─ big_acacia_white_stained_glass_flask.json
         │     │  ├─ big_acacia_yellow_stained_glass_flask.json
         │     │  ├─ big_bamboo_black_stained_glass_flask.json
         │     │  ├─ big_bamboo_blue_stained_glass_flask.json
         │     │  ├─ big_bamboo_brown_stained_glass_flask.json
         │     │  ├─ big_bamboo_cyan_stained_glass_flask.json
         │     │  ├─ big_bamboo_glass_flask.json
         │     │  ├─ big_bamboo_gray_stained_glass_flask.json
         │     │  ├─ big_bamboo_green_stained_glass_flask.json
         │     │  ├─ big_bamboo_light_blue_stained_glass_flask.json
         │     │  ├─ big_bamboo_light_gray_stained_glass_flask.json
         │     │  ├─ big_bamboo_lime_stained_glass_flask.json
         │     │  ├─ big_bamboo_magenta_stained_glass_flask.json
         │     │  ├─ big_bamboo_orange_stained_glass_flask.json
         │     │  ├─ big_bamboo_pink_stained_glass_flask.json
         │     │  ├─ big_bamboo_purple_stained_glass_flask.json
         │     │  ├─ big_bamboo_red_stained_glass_flask.json
         │     │  ├─ big_bamboo_tinted_glass_flask.json
         │     │  ├─ big_bamboo_white_stained_glass_flask.json
         │     │  ├─ big_bamboo_yellow_stained_glass_flask.json
         │     │  ├─ big_birch_black_stained_glass_flask.json
         │     │  ├─ big_birch_blue_stained_glass_flask.json
         │     │  ├─ big_birch_brown_stained_glass_flask.json
         │     │  ├─ big_birch_cyan_stained_glass_flask.json
         │     │  ├─ big_birch_glass_flask.json
         │     │  ├─ big_birch_gray_stained_glass_flask.json
         │     │  ├─ big_birch_green_stained_glass_flask.json
         │     │  ├─ big_birch_light_blue_stained_glass_flask.json
         │     │  ├─ big_birch_light_gray_stained_glass_flask.json
         │     │  ├─ big_birch_lime_stained_glass_flask.json
         │     │  ├─ big_birch_magenta_stained_glass_flask.json
         │     │  ├─ big_birch_orange_stained_glass_flask.json
         │     │  ├─ big_birch_pink_stained_glass_flask.json
         │     │  ├─ big_birch_purple_stained_glass_flask.json
         │     │  ├─ big_birch_red_stained_glass_flask.json
         │     │  ├─ big_birch_tinted_glass_flask.json
         │     │  ├─ big_birch_white_stained_glass_flask.json
         │     │  ├─ big_birch_yellow_stained_glass_flask.json
         │     │  ├─ big_cherry_black_stained_glass_flask.json
         │     │  ├─ big_cherry_blue_stained_glass_flask.json
         │     │  ├─ big_cherry_brown_stained_glass_flask.json
         │     │  ├─ big_cherry_cyan_stained_glass_flask.json
         │     │  ├─ big_cherry_glass_flask.json
         │     │  ├─ big_cherry_gray_stained_glass_flask.json
         │     │  ├─ big_cherry_green_stained_glass_flask.json
         │     │  ├─ big_cherry_light_blue_stained_glass_flask.json
         │     │  ├─ big_cherry_light_gray_stained_glass_flask.json
         │     │  ├─ big_cherry_lime_stained_glass_flask.json
         │     │  ├─ big_cherry_magenta_stained_glass_flask.json
         │     │  ├─ big_cherry_orange_stained_glass_flask.json
         │     │  ├─ big_cherry_pink_stained_glass_flask.json
         │     │  ├─ big_cherry_purple_stained_glass_flask.json
         │     │  ├─ big_cherry_red_stained_glass_flask.json
         │     │  ├─ big_cherry_tinted_glass_flask.json
         │     │  ├─ big_cherry_white_stained_glass_flask.json
         │     │  ├─ big_cherry_yellow_stained_glass_flask.json
         │     │  ├─ big_crimson_black_stained_glass_flask.json
         │     │  ├─ big_crimson_blue_stained_glass_flask.json
         │     │  ├─ big_crimson_brown_stained_glass_flask.json
         │     │  ├─ big_crimson_cyan_stained_glass_flask.json
         │     │  ├─ big_crimson_glass_flask.json
         │     │  ├─ big_crimson_gray_stained_glass_flask.json
         │     │  ├─ big_crimson_green_stained_glass_flask.json
         │     │  ├─ big_crimson_light_blue_stained_glass_flask.json
         │     │  ├─ big_crimson_light_gray_stained_glass_flask.json
         │     │  ├─ big_crimson_lime_stained_glass_flask.json
         │     │  ├─ big_crimson_magenta_stained_glass_flask.json
         │     │  ├─ big_crimson_orange_stained_glass_flask.json
         │     │  ├─ big_crimson_pink_stained_glass_flask.json
         │     │  ├─ big_crimson_purple_stained_glass_flask.json
         │     │  ├─ big_crimson_red_stained_glass_flask.json
         │     │  ├─ big_crimson_tinted_glass_flask.json
         │     │  ├─ big_crimson_white_stained_glass_flask.json
         │     │  ├─ big_crimson_yellow_stained_glass_flask.json
         │     │  ├─ big_dark_oak_black_stained_glass_flask.json
         │     │  ├─ big_dark_oak_blue_stained_glass_flask.json
         │     │  ├─ big_dark_oak_brown_stained_glass_flask.json
         │     │  ├─ big_dark_oak_cyan_stained_glass_flask.json
         │     │  ├─ big_dark_oak_glass_flask.json
         │     │  ├─ big_dark_oak_gray_stained_glass_flask.json
         │     │  ├─ big_dark_oak_green_stained_glass_flask.json
         │     │  ├─ big_dark_oak_light_blue_stained_glass_flask.json
         │     │  ├─ big_dark_oak_light_gray_stained_glass_flask.json
         │     │  ├─ big_dark_oak_lime_stained_glass_flask.json
         │     │  ├─ big_dark_oak_magenta_stained_glass_flask.json
         │     │  ├─ big_dark_oak_orange_stained_glass_flask.json
         │     │  ├─ big_dark_oak_pink_stained_glass_flask.json
         │     │  ├─ big_dark_oak_purple_stained_glass_flask.json
         │     │  ├─ big_dark_oak_red_stained_glass_flask.json
         │     │  ├─ big_dark_oak_tinted_glass_flask.json
         │     │  ├─ big_dark_oak_white_stained_glass_flask.json
         │     │  ├─ big_dark_oak_yellow_stained_glass_flask.json
         │     │  ├─ big_jungle_black_stained_glass_flask.json
         │     │  ├─ big_jungle_blue_stained_glass_flask.json
         │     │  ├─ big_jungle_brown_stained_glass_flask.json
         │     │  ├─ big_jungle_cyan_stained_glass_flask.json
         │     │  ├─ big_jungle_glass_flask.json
         │     │  ├─ big_jungle_gray_stained_glass_flask.json
         │     │  ├─ big_jungle_green_stained_glass_flask.json
         │     │  ├─ big_jungle_light_blue_stained_glass_flask.json
         │     │  ├─ big_jungle_light_gray_stained_glass_flask.json
         │     │  ├─ big_jungle_lime_stained_glass_flask.json
         │     │  ├─ big_jungle_magenta_stained_glass_flask.json
         │     │  ├─ big_jungle_orange_stained_glass_flask.json
         │     │  ├─ big_jungle_pink_stained_glass_flask.json
         │     │  ├─ big_jungle_purple_stained_glass_flask.json
         │     │  ├─ big_jungle_red_stained_glass_flask.json
         │     │  ├─ big_jungle_tinted_glass_flask.json
         │     │  ├─ big_jungle_white_stained_glass_flask.json
         │     │  ├─ big_jungle_yellow_stained_glass_flask.json
         │     │  ├─ big_mangrove_black_stained_glass_flask.json
         │     │  ├─ big_mangrove_blue_stained_glass_flask.json
         │     │  ├─ big_mangrove_brown_stained_glass_flask.json
         │     │  ├─ big_mangrove_cyan_stained_glass_flask.json
         │     │  ├─ big_mangrove_glass_flask.json
         │     │  ├─ big_mangrove_gray_stained_glass_flask.json
         │     │  ├─ big_mangrove_green_stained_glass_flask.json
         │     │  ├─ big_mangrove_light_blue_stained_glass_flask.json
         │     │  ├─ big_mangrove_light_gray_stained_glass_flask.json
         │     │  ├─ big_mangrove_lime_stained_glass_flask.json
         │     │  ├─ big_mangrove_magenta_stained_glass_flask.json
         │     │  ├─ big_mangrove_orange_stained_glass_flask.json
         │     │  ├─ big_mangrove_pink_stained_glass_flask.json
         │     │  ├─ big_mangrove_purple_stained_glass_flask.json
         │     │  ├─ big_mangrove_red_stained_glass_flask.json
         │     │  ├─ big_mangrove_tinted_glass_flask.json
         │     │  ├─ big_mangrove_white_stained_glass_flask.json
         │     │  ├─ big_mangrove_yellow_stained_glass_flask.json
         │     │  ├─ big_oak_black_stained_glass_flask.json
         │     │  ├─ big_oak_blue_stained_glass_flask.json
         │     │  ├─ big_oak_brown_stained_glass_flask.json
         │     │  ├─ big_oak_cyan_stained_glass_flask.json
         │     │  ├─ big_oak_glass_flask.json
         │     │  ├─ big_oak_gray_stained_glass_flask.json
         │     │  ├─ big_oak_green_stained_glass_flask.json
         │     │  ├─ big_oak_light_blue_stained_glass_flask.json
         │     │  ├─ big_oak_light_gray_stained_glass_flask.json
         │     │  ├─ big_oak_lime_stained_glass_flask.json
         │     │  ├─ big_oak_magenta_stained_glass_flask.json
         │     │  ├─ big_oak_orange_stained_glass_flask.json
         │     │  ├─ big_oak_pink_stained_glass_flask.json
         │     │  ├─ big_oak_purple_stained_glass_flask.json
         │     │  ├─ big_oak_red_stained_glass_flask.json
         │     │  ├─ big_oak_tinted_glass_flask.json
         │     │  ├─ big_oak_white_stained_glass_flask.json
         │     │  ├─ big_oak_yellow_stained_glass_flask.json
         │     │  ├─ big_pale_oak_black_stained_glass_flask.json
         │     │  ├─ big_pale_oak_blue_stained_glass_flask.json
         │     │  ├─ big_pale_oak_brown_stained_glass_flask.json
         │     │  ├─ big_pale_oak_cyan_stained_glass_flask.json
         │     │  ├─ big_pale_oak_glass_flask.json
         │     │  ├─ big_pale_oak_gray_stained_glass_flask.json
         │     │  ├─ big_pale_oak_green_stained_glass_flask.json
         │     │  ├─ big_pale_oak_light_blue_stained_glass_flask.json
         │     │  ├─ big_pale_oak_light_gray_stained_glass_flask.json
         │     │  ├─ big_pale_oak_lime_stained_glass_flask.json
         │     │  ├─ big_pale_oak_magenta_stained_glass_flask.json
         │     │  ├─ big_pale_oak_orange_stained_glass_flask.json
         │     │  ├─ big_pale_oak_pink_stained_glass_flask.json
         │     │  ├─ big_pale_oak_purple_stained_glass_flask.json
         │     │  ├─ big_pale_oak_red_stained_glass_flask.json
         │     │  ├─ big_pale_oak_tinted_glass_flask.json
         │     │  ├─ big_pale_oak_white_stained_glass_flask.json
         │     │  ├─ big_pale_oak_yellow_stained_glass_flask.json
         │     │  ├─ big_spruce_black_stained_glass_flask.json
         │     │  ├─ big_spruce_blue_stained_glass_flask.json
         │     │  ├─ big_spruce_brown_stained_glass_flask.json
         │     │  ├─ big_spruce_cyan_stained_glass_flask.json
         │     │  ├─ big_spruce_glass_flask.json
         │     │  ├─ big_spruce_gray_stained_glass_flask.json
         │     │  ├─ big_spruce_green_stained_glass_flask.json
         │     │  ├─ big_spruce_light_blue_stained_glass_flask.json
         │     │  ├─ big_spruce_light_gray_stained_glass_flask.json
         │     │  ├─ big_spruce_lime_stained_glass_flask.json
         │     │  ├─ big_spruce_magenta_stained_glass_flask.json
         │     │  ├─ big_spruce_orange_stained_glass_flask.json
         │     │  ├─ big_spruce_pink_stained_glass_flask.json
         │     │  ├─ big_spruce_purple_stained_glass_flask.json
         │     │  ├─ big_spruce_red_stained_glass_flask.json
         │     │  ├─ big_spruce_tinted_glass_flask.json
         │     │  ├─ big_spruce_white_stained_glass_flask.json
         │     │  ├─ big_spruce_yellow_stained_glass_flask.json
         │     │  ├─ big_warped_black_stained_glass_flask.json
         │     │  ├─ big_warped_blue_stained_glass_flask.json
         │     │  ├─ big_warped_brown_stained_glass_flask.json
         │     │  ├─ big_warped_cyan_stained_glass_flask.json
         │     │  ├─ big_warped_glass_flask.json
         │     │  ├─ big_warped_gray_stained_glass_flask.json
         │     │  ├─ big_warped_green_stained_glass_flask.json
         │     │  ├─ big_warped_light_blue_stained_glass_flask.json
         │     │  ├─ big_warped_light_gray_stained_glass_flask.json
         │     │  ├─ big_warped_lime_stained_glass_flask.json
         │     │  ├─ big_warped_magenta_stained_glass_flask.json
         │     │  ├─ big_warped_orange_stained_glass_flask.json
         │     │  ├─ big_warped_pink_stained_glass_flask.json
         │     │  ├─ big_warped_purple_stained_glass_flask.json
         │     │  ├─ big_warped_red_stained_glass_flask.json
         │     │  ├─ big_warped_tinted_glass_flask.json
         │     │  ├─ big_warped_white_stained_glass_flask.json
         │     │  ├─ big_warped_yellow_stained_glass_flask.json
         │     │  ├─ birch_copper_barrel.json
         │     │  ├─ birch_copper_barrel_block.json
         │     │  ├─ birch_copper_exposed_barrel.json
         │     │  ├─ birch_copper_exposed_barrel_block.json
         │     │  ├─ birch_copper_oxidized_barrel.json
         │     │  ├─ birch_copper_oxidized_barrel_block.json
         │     │  ├─ birch_copper_weathered_barrel.json
         │     │  ├─ birch_copper_weathered_barrel_block.json
         │     │  ├─ birch_gold_barrel.json
         │     │  ├─ birch_gold_barrel_block.json
         │     │  ├─ birch_iron_barrel.json
         │     │  ├─ birch_iron_barrel_block.json
         │     │  ├─ birch_netherite_barrel.json
         │     │  ├─ birch_netherite_barrel_block.json
         │     │  ├─ cherry_copper_barrel.json
         │     │  ├─ cherry_copper_barrel_block.json
         │     │  ├─ cherry_copper_exposed_barrel.json
         │     │  ├─ cherry_copper_exposed_barrel_block.json
         │     │  ├─ cherry_copper_oxidized_barrel.json
         │     │  ├─ cherry_copper_oxidized_barrel_block.json
         │     │  ├─ cherry_copper_weathered_barrel.json
         │     │  ├─ cherry_copper_weathered_barrel_block.json
         │     │  ├─ cherry_gold_barrel.json
         │     │  ├─ cherry_gold_barrel_block.json
         │     │  ├─ cherry_iron_barrel.json
         │     │  ├─ cherry_iron_barrel_block.json
         │     │  ├─ cherry_netherite_barrel.json
         │     │  ├─ cherry_netherite_barrel_block.json
         │     │  ├─ copper_exposed_keg.json
         │     │  ├─ copper_exposed_keg_block.json
         │     │  ├─ copper_keg.json
         │     │  ├─ copper_keg_block.json
         │     │  ├─ copper_oxidized_keg.json
         │     │  ├─ copper_oxidized_keg_block.json
         │     │  ├─ copper_weathered_keg.json
         │     │  ├─ copper_weathered_keg_block.json
         │     │  ├─ crimson_copper_barrel.json
         │     │  ├─ crimson_copper_barrel_block.json
         │     │  ├─ crimson_copper_exposed_barrel.json
         │     │  ├─ crimson_copper_exposed_barrel_block.json
         │     │  ├─ crimson_copper_oxidized_barrel.json
         │     │  ├─ crimson_copper_oxidized_barrel_block.json
         │     │  ├─ crimson_copper_weathered_barrel.json
         │     │  ├─ crimson_copper_weathered_barrel_block.json
         │     │  ├─ crimson_gold_barrel.json
         │     │  ├─ crimson_gold_barrel_block.json
         │     │  ├─ crimson_iron_barrel.json
         │     │  ├─ crimson_iron_barrel_block.json
         │     │  ├─ crimson_netherite_barrel.json
         │     │  ├─ crimson_netherite_barrel_block.json
         │     │  ├─ dark_oak_copper_barrel.json
         │     │  ├─ dark_oak_copper_barrel_block.json
         │     │  ├─ dark_oak_copper_exposed_barrel.json
         │     │  ├─ dark_oak_copper_exposed_barrel_block.json
         │     │  ├─ dark_oak_copper_oxidized_barrel.json
         │     │  ├─ dark_oak_copper_oxidized_barrel_block.json
         │     │  ├─ dark_oak_copper_weathered_barrel.json
         │     │  ├─ dark_oak_copper_weathered_barrel_block.json
         │     │  ├─ dark_oak_gold_barrel.json
         │     │  ├─ dark_oak_gold_barrel_block.json
         │     │  ├─ dark_oak_iron_barrel.json
         │     │  ├─ dark_oak_iron_barrel_block.json
         │     │  ├─ dark_oak_netherite_barrel.json
         │     │  ├─ dark_oak_netherite_barrel_block.json
         │     │  ├─ gold_keg.json
         │     │  ├─ gold_keg_block.json
         │     │  ├─ iron_keg.json
         │     │  ├─ iron_keg_block.json
         │     │  ├─ jungle_copper_barrel.json
         │     │  ├─ jungle_copper_barrel_block.json
         │     │  ├─ jungle_copper_exposed_barrel.json
         │     │  ├─ jungle_copper_exposed_barrel_block.json
         │     │  ├─ jungle_copper_oxidized_barrel.json
         │     │  ├─ jungle_copper_oxidized_barrel_block.json
         │     │  ├─ jungle_copper_weathered_barrel.json
         │     │  ├─ jungle_copper_weathered_barrel_block.json
         │     │  ├─ jungle_gold_barrel.json
         │     │  ├─ jungle_gold_barrel_block.json
         │     │  ├─ jungle_iron_barrel.json
         │     │  ├─ jungle_iron_barrel_block.json
         │     │  ├─ jungle_netherite_barrel.json
         │     │  ├─ jungle_netherite_barrel_block.json
         │     │  ├─ mangrove_copper_barrel.json
         │     │  ├─ mangrove_copper_barrel_block.json
         │     │  ├─ mangrove_copper_exposed_barrel.json
         │     │  ├─ mangrove_copper_exposed_barrel_block.json
         │     │  ├─ mangrove_copper_oxidized_barrel.json
         │     │  ├─ mangrove_copper_oxidized_barrel_block.json
         │     │  ├─ mangrove_copper_weathered_barrel.json
         │     │  ├─ mangrove_copper_weathered_barrel_block.json
         │     │  ├─ mangrove_gold_barrel.json
         │     │  ├─ mangrove_gold_barrel_block.json
         │     │  ├─ mangrove_iron_barrel.json
         │     │  ├─ mangrove_iron_barrel_block.json
         │     │  ├─ mangrove_netherite_barrel.json
         │     │  ├─ mangrove_netherite_barrel_block.json
         │     │  ├─ medium_acacia_black_stained_glass_flask.json
         │     │  ├─ medium_acacia_blue_stained_glass_flask.json
         │     │  ├─ medium_acacia_brown_stained_glass_flask.json
         │     │  ├─ medium_acacia_cyan_stained_glass_flask.json
         │     │  ├─ medium_acacia_glass_flask.json
         │     │  ├─ medium_acacia_gray_stained_glass_flask.json
         │     │  ├─ medium_acacia_green_stained_glass_flask.json
         │     │  ├─ medium_acacia_light_blue_stained_glass_flask.json
         │     │  ├─ medium_acacia_light_gray_stained_glass_flask.json
         │     │  ├─ medium_acacia_lime_stained_glass_flask.json
         │     │  ├─ medium_acacia_magenta_stained_glass_flask.json
         │     │  ├─ medium_acacia_orange_stained_glass_flask.json
         │     │  ├─ medium_acacia_pink_stained_glass_flask.json
         │     │  ├─ medium_acacia_purple_stained_glass_flask.json
         │     │  ├─ medium_acacia_red_stained_glass_flask.json
         │     │  ├─ medium_acacia_tinted_glass_flask.json
         │     │  ├─ medium_acacia_white_stained_glass_flask.json
         │     │  ├─ medium_acacia_yellow_stained_glass_flask.json
         │     │  ├─ medium_bamboo_black_stained_glass_flask.json
         │     │  ├─ medium_bamboo_blue_stained_glass_flask.json
         │     │  ├─ medium_bamboo_brown_stained_glass_flask.json
         │     │  ├─ medium_bamboo_cyan_stained_glass_flask.json
         │     │  ├─ medium_bamboo_glass_flask.json
         │     │  ├─ medium_bamboo_gray_stained_glass_flask.json
         │     │  ├─ medium_bamboo_green_stained_glass_flask.json
         │     │  ├─ medium_bamboo_light_blue_stained_glass_flask.json
         │     │  ├─ medium_bamboo_light_gray_stained_glass_flask.json
         │     │  ├─ medium_bamboo_lime_stained_glass_flask.json
         │     │  ├─ medium_bamboo_magenta_stained_glass_flask.json
         │     │  ├─ medium_bamboo_orange_stained_glass_flask.json
         │     │  ├─ medium_bamboo_pink_stained_glass_flask.json
         │     │  ├─ medium_bamboo_purple_stained_glass_flask.json
         │     │  ├─ medium_bamboo_red_stained_glass_flask.json
         │     │  ├─ medium_bamboo_tinted_glass_flask.json
         │     │  ├─ medium_bamboo_white_stained_glass_flask.json
         │     │  ├─ medium_bamboo_yellow_stained_glass_flask.json
         │     │  ├─ medium_birch_black_stained_glass_flask.json
         │     │  ├─ medium_birch_blue_stained_glass_flask.json
         │     │  ├─ medium_birch_brown_stained_glass_flask.json
         │     │  ├─ medium_birch_cyan_stained_glass_flask.json
         │     │  ├─ medium_birch_glass_flask.json
         │     │  ├─ medium_birch_gray_stained_glass_flask.json
         │     │  ├─ medium_birch_green_stained_glass_flask.json
         │     │  ├─ medium_birch_light_blue_stained_glass_flask.json
         │     │  ├─ medium_birch_light_gray_stained_glass_flask.json
         │     │  ├─ medium_birch_lime_stained_glass_flask.json
         │     │  ├─ medium_birch_magenta_stained_glass_flask.json
         │     │  ├─ medium_birch_orange_stained_glass_flask.json
         │     │  ├─ medium_birch_pink_stained_glass_flask.json
         │     │  ├─ medium_birch_purple_stained_glass_flask.json
         │     │  ├─ medium_birch_red_stained_glass_flask.json
         │     │  ├─ medium_birch_tinted_glass_flask.json
         │     │  ├─ medium_birch_white_stained_glass_flask.json
         │     │  ├─ medium_birch_yellow_stained_glass_flask.json
         │     │  ├─ medium_cherry_black_stained_glass_flask.json
         │     │  ├─ medium_cherry_blue_stained_glass_flask.json
         │     │  ├─ medium_cherry_brown_stained_glass_flask.json
         │     │  ├─ medium_cherry_cyan_stained_glass_flask.json
         │     │  ├─ medium_cherry_glass_flask.json
         │     │  ├─ medium_cherry_gray_stained_glass_flask.json
         │     │  ├─ medium_cherry_green_stained_glass_flask.json
         │     │  ├─ medium_cherry_light_blue_stained_glass_flask.json
         │     │  ├─ medium_cherry_light_gray_stained_glass_flask.json
         │     │  ├─ medium_cherry_lime_stained_glass_flask.json
         │     │  ├─ medium_cherry_magenta_stained_glass_flask.json
         │     │  ├─ medium_cherry_orange_stained_glass_flask.json
         │     │  ├─ medium_cherry_pink_stained_glass_flask.json
         │     │  ├─ medium_cherry_purple_stained_glass_flask.json
         │     │  ├─ medium_cherry_red_stained_glass_flask.json
         │     │  ├─ medium_cherry_tinted_glass_flask.json
         │     │  ├─ medium_cherry_white_stained_glass_flask.json
         │     │  ├─ medium_cherry_yellow_stained_glass_flask.json
         │     │  ├─ medium_crimson_black_stained_glass_flask.json
         │     │  ├─ medium_crimson_blue_stained_glass_flask.json
         │     │  ├─ medium_crimson_brown_stained_glass_flask.json
         │     │  ├─ medium_crimson_cyan_stained_glass_flask.json
         │     │  ├─ medium_crimson_glass_flask.json
         │     │  ├─ medium_crimson_gray_stained_glass_flask.json
         │     │  ├─ medium_crimson_green_stained_glass_flask.json
         │     │  ├─ medium_crimson_light_blue_stained_glass_flask.json
         │     │  ├─ medium_crimson_light_gray_stained_glass_flask.json
         │     │  ├─ medium_crimson_lime_stained_glass_flask.json
         │     │  ├─ medium_crimson_magenta_stained_glass_flask.json
         │     │  ├─ medium_crimson_orange_stained_glass_flask.json
         │     │  ├─ medium_crimson_pink_stained_glass_flask.json
         │     │  ├─ medium_crimson_purple_stained_glass_flask.json
         │     │  ├─ medium_crimson_red_stained_glass_flask.json
         │     │  ├─ medium_crimson_tinted_glass_flask.json
         │     │  ├─ medium_crimson_white_stained_glass_flask.json
         │     │  ├─ medium_crimson_yellow_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_black_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_blue_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_brown_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_cyan_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_glass_flask.json
         │     │  ├─ medium_dark_oak_gray_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_green_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_light_blue_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_light_gray_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_lime_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_magenta_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_orange_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_pink_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_purple_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_red_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_tinted_glass_flask.json
         │     │  ├─ medium_dark_oak_white_stained_glass_flask.json
         │     │  ├─ medium_dark_oak_yellow_stained_glass_flask.json
         │     │  ├─ medium_jungle_black_stained_glass_flask.json
         │     │  ├─ medium_jungle_blue_stained_glass_flask.json
         │     │  ├─ medium_jungle_brown_stained_glass_flask.json
         │     │  ├─ medium_jungle_cyan_stained_glass_flask.json
         │     │  ├─ medium_jungle_glass_flask.json
         │     │  ├─ medium_jungle_gray_stained_glass_flask.json
         │     │  ├─ medium_jungle_green_stained_glass_flask.json
         │     │  ├─ medium_jungle_light_blue_stained_glass_flask.json
         │     │  ├─ medium_jungle_light_gray_stained_glass_flask.json
         │     │  ├─ medium_jungle_lime_stained_glass_flask.json
         │     │  ├─ medium_jungle_magenta_stained_glass_flask.json
         │     │  ├─ medium_jungle_orange_stained_glass_flask.json
         │     │  ├─ medium_jungle_pink_stained_glass_flask.json
         │     │  ├─ medium_jungle_purple_stained_glass_flask.json
         │     │  ├─ medium_jungle_red_stained_glass_flask.json
         │     │  ├─ medium_jungle_tinted_glass_flask.json
         │     │  ├─ medium_jungle_white_stained_glass_flask.json
         │     │  ├─ medium_jungle_yellow_stained_glass_flask.json
         │     │  ├─ medium_mangrove_black_stained_glass_flask.json
         │     │  ├─ medium_mangrove_blue_stained_glass_flask.json
         │     │  ├─ medium_mangrove_brown_stained_glass_flask.json
         │     │  ├─ medium_mangrove_cyan_stained_glass_flask.json
         │     │  ├─ medium_mangrove_glass_flask.json
         │     │  ├─ medium_mangrove_gray_stained_glass_flask.json
         │     │  ├─ medium_mangrove_green_stained_glass_flask.json
         │     │  ├─ medium_mangrove_light_blue_stained_glass_flask.json
         │     │  ├─ medium_mangrove_light_gray_stained_glass_flask.json
         │     │  ├─ medium_mangrove_lime_stained_glass_flask.json
         │     │  ├─ medium_mangrove_magenta_stained_glass_flask.json
         │     │  ├─ medium_mangrove_orange_stained_glass_flask.json
         │     │  ├─ medium_mangrove_pink_stained_glass_flask.json
         │     │  ├─ medium_mangrove_purple_stained_glass_flask.json
         │     │  ├─ medium_mangrove_red_stained_glass_flask.json
         │     │  ├─ medium_mangrove_tinted_glass_flask.json
         │     │  ├─ medium_mangrove_white_stained_glass_flask.json
         │     │  ├─ medium_mangrove_yellow_stained_glass_flask.json
         │     │  ├─ medium_oak_black_stained_glass_flask.json
         │     │  ├─ medium_oak_blue_stained_glass_flask.json
         │     │  ├─ medium_oak_brown_stained_glass_flask.json
         │     │  ├─ medium_oak_cyan_stained_glass_flask.json
         │     │  ├─ medium_oak_glass_flask.json
         │     │  ├─ medium_oak_gray_stained_glass_flask.json
         │     │  ├─ medium_oak_green_stained_glass_flask.json
         │     │  ├─ medium_oak_light_blue_stained_glass_flask.json
         │     │  ├─ medium_oak_light_gray_stained_glass_flask.json
         │     │  ├─ medium_oak_lime_stained_glass_flask.json
         │     │  ├─ medium_oak_magenta_stained_glass_flask.json
         │     │  ├─ medium_oak_orange_stained_glass_flask.json
         │     │  ├─ medium_oak_pink_stained_glass_flask.json
         │     │  ├─ medium_oak_purple_stained_glass_flask.json
         │     │  ├─ medium_oak_red_stained_glass_flask.json
         │     │  ├─ medium_oak_tinted_glass_flask.json
         │     │  ├─ medium_oak_white_stained_glass_flask.json
         │     │  ├─ medium_oak_yellow_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_black_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_blue_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_brown_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_cyan_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_glass_flask.json
         │     │  ├─ medium_pale_oak_gray_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_green_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_light_blue_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_light_gray_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_lime_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_magenta_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_orange_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_pink_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_purple_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_red_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_tinted_glass_flask.json
         │     │  ├─ medium_pale_oak_white_stained_glass_flask.json
         │     │  ├─ medium_pale_oak_yellow_stained_glass_flask.json
         │     │  ├─ medium_spruce_black_stained_glass_flask.json
         │     │  ├─ medium_spruce_blue_stained_glass_flask.json
         │     │  ├─ medium_spruce_brown_stained_glass_flask.json
         │     │  ├─ medium_spruce_cyan_stained_glass_flask.json
         │     │  ├─ medium_spruce_glass_flask.json
         │     │  ├─ medium_spruce_gray_stained_glass_flask.json
         │     │  ├─ medium_spruce_green_stained_glass_flask.json
         │     │  ├─ medium_spruce_light_blue_stained_glass_flask.json
         │     │  ├─ medium_spruce_light_gray_stained_glass_flask.json
         │     │  ├─ medium_spruce_lime_stained_glass_flask.json
         │     │  ├─ medium_spruce_magenta_stained_glass_flask.json
         │     │  ├─ medium_spruce_orange_stained_glass_flask.json
         │     │  ├─ medium_spruce_pink_stained_glass_flask.json
         │     │  ├─ medium_spruce_purple_stained_glass_flask.json
         │     │  ├─ medium_spruce_red_stained_glass_flask.json
         │     │  ├─ medium_spruce_tinted_glass_flask.json
         │     │  ├─ medium_spruce_white_stained_glass_flask.json
         │     │  ├─ medium_spruce_yellow_stained_glass_flask.json
         │     │  ├─ medium_warped_black_stained_glass_flask.json
         │     │  ├─ medium_warped_blue_stained_glass_flask.json
         │     │  ├─ medium_warped_brown_stained_glass_flask.json
         │     │  ├─ medium_warped_cyan_stained_glass_flask.json
         │     │  ├─ medium_warped_glass_flask.json
         │     │  ├─ medium_warped_gray_stained_glass_flask.json
         │     │  ├─ medium_warped_green_stained_glass_flask.json
         │     │  ├─ medium_warped_light_blue_stained_glass_flask.json
         │     │  ├─ medium_warped_light_gray_stained_glass_flask.json
         │     │  ├─ medium_warped_lime_stained_glass_flask.json
         │     │  ├─ medium_warped_magenta_stained_glass_flask.json
         │     │  ├─ medium_warped_orange_stained_glass_flask.json
         │     │  ├─ medium_warped_pink_stained_glass_flask.json
         │     │  ├─ medium_warped_purple_stained_glass_flask.json
         │     │  ├─ medium_warped_red_stained_glass_flask.json
         │     │  ├─ medium_warped_tinted_glass_flask.json
         │     │  ├─ medium_warped_white_stained_glass_flask.json
         │     │  ├─ medium_warped_yellow_stained_glass_flask.json
         │     │  ├─ netherite_keg.json
         │     │  ├─ netherite_keg_block.json
         │     │  ├─ oak_copper_barrel.json
         │     │  ├─ oak_copper_barrel_block.json
         │     │  ├─ oak_copper_exposed_barrel.json
         │     │  ├─ oak_copper_exposed_barrel_block.json
         │     │  ├─ oak_copper_oxidized_barrel.json
         │     │  ├─ oak_copper_oxidized_barrel_block.json
         │     │  ├─ oak_copper_weathered_barrel.json
         │     │  ├─ oak_copper_weathered_barrel_block.json
         │     │  ├─ oak_gold_barrel.json
         │     │  ├─ oak_gold_barrel_block.json
         │     │  ├─ oak_iron_barrel.json
         │     │  ├─ oak_iron_barrel_block.json
         │     │  ├─ oak_netherite_barrel.json
         │     │  ├─ oak_netherite_barrel_block.json
         │     │  ├─ pale_oak_copper_barrel.json
         │     │  ├─ pale_oak_copper_barrel_block.json
         │     │  ├─ pale_oak_copper_exposed_barrel.json
         │     │  ├─ pale_oak_copper_exposed_barrel_block.json
         │     │  ├─ pale_oak_copper_oxidized_barrel.json
         │     │  ├─ pale_oak_copper_oxidized_barrel_block.json
         │     │  ├─ pale_oak_copper_weathered_barrel.json
         │     │  ├─ pale_oak_copper_weathered_barrel_block.json
         │     │  ├─ pale_oak_gold_barrel.json
         │     │  ├─ pale_oak_gold_barrel_block.json
         │     │  ├─ pale_oak_iron_barrel.json
         │     │  ├─ pale_oak_iron_barrel_block.json
         │     │  ├─ pale_oak_netherite_barrel.json
         │     │  ├─ pale_oak_netherite_barrel_block.json
         │     │  ├─ small_acacia_black_stained_glass_flask.json
         │     │  ├─ small_acacia_blue_stained_glass_flask.json
         │     │  ├─ small_acacia_brown_stained_glass_flask.json
         │     │  ├─ small_acacia_cyan_stained_glass_flask.json
         │     │  ├─ small_acacia_glass_flask.json
         │     │  ├─ small_acacia_gray_stained_glass_flask.json
         │     │  ├─ small_acacia_green_stained_glass_flask.json
         │     │  ├─ small_acacia_light_blue_stained_glass_flask.json
         │     │  ├─ small_acacia_light_gray_stained_glass_flask.json
         │     │  ├─ small_acacia_lime_stained_glass_flask.json
         │     │  ├─ small_acacia_magenta_stained_glass_flask.json
         │     │  ├─ small_acacia_orange_stained_glass_flask.json
         │     │  ├─ small_acacia_pink_stained_glass_flask.json
         │     │  ├─ small_acacia_purple_stained_glass_flask.json
         │     │  ├─ small_acacia_red_stained_glass_flask.json
         │     │  ├─ small_acacia_tinted_glass_flask.json
         │     │  ├─ small_acacia_white_stained_glass_flask.json
         │     │  ├─ small_acacia_yellow_stained_glass_flask.json
         │     │  ├─ small_bamboo_black_stained_glass_flask.json
         │     │  ├─ small_bamboo_blue_stained_glass_flask.json
         │     │  ├─ small_bamboo_brown_stained_glass_flask.json
         │     │  ├─ small_bamboo_cyan_stained_glass_flask.json
         │     │  ├─ small_bamboo_glass_flask.json
         │     │  ├─ small_bamboo_gray_stained_glass_flask.json
         │     │  ├─ small_bamboo_green_stained_glass_flask.json
         │     │  ├─ small_bamboo_light_blue_stained_glass_flask.json
         │     │  ├─ small_bamboo_light_gray_stained_glass_flask.json
         │     │  ├─ small_bamboo_lime_stained_glass_flask.json
         │     │  ├─ small_bamboo_magenta_stained_glass_flask.json
         │     │  ├─ small_bamboo_orange_stained_glass_flask.json
         │     │  ├─ small_bamboo_pink_stained_glass_flask.json
         │     │  ├─ small_bamboo_purple_stained_glass_flask.json
         │     │  ├─ small_bamboo_red_stained_glass_flask.json
         │     │  ├─ small_bamboo_tinted_glass_flask.json
         │     │  ├─ small_bamboo_white_stained_glass_flask.json
         │     │  ├─ small_bamboo_yellow_stained_glass_flask.json
         │     │  ├─ small_birch_black_stained_glass_flask.json
         │     │  ├─ small_birch_blue_stained_glass_flask.json
         │     │  ├─ small_birch_brown_stained_glass_flask.json
         │     │  ├─ small_birch_cyan_stained_glass_flask.json
         │     │  ├─ small_birch_glass_flask.json
         │     │  ├─ small_birch_gray_stained_glass_flask.json
         │     │  ├─ small_birch_green_stained_glass_flask.json
         │     │  ├─ small_birch_light_blue_stained_glass_flask.json
         │     │  ├─ small_birch_light_gray_stained_glass_flask.json
         │     │  ├─ small_birch_lime_stained_glass_flask.json
         │     │  ├─ small_birch_magenta_stained_glass_flask.json
         │     │  ├─ small_birch_orange_stained_glass_flask.json
         │     │  ├─ small_birch_pink_stained_glass_flask.json
         │     │  ├─ small_birch_purple_stained_glass_flask.json
         │     │  ├─ small_birch_red_stained_glass_flask.json
         │     │  ├─ small_birch_tinted_glass_flask.json
         │     │  ├─ small_birch_white_stained_glass_flask.json
         │     │  ├─ small_birch_yellow_stained_glass_flask.json
         │     │  ├─ small_cherry_black_stained_glass_flask.json
         │     │  ├─ small_cherry_blue_stained_glass_flask.json
         │     │  ├─ small_cherry_brown_stained_glass_flask.json
         │     │  ├─ small_cherry_cyan_stained_glass_flask.json
         │     │  ├─ small_cherry_glass_flask.json
         │     │  ├─ small_cherry_gray_stained_glass_flask.json
         │     │  ├─ small_cherry_green_stained_glass_flask.json
         │     │  ├─ small_cherry_light_blue_stained_glass_flask.json
         │     │  ├─ small_cherry_light_gray_stained_glass_flask.json
         │     │  ├─ small_cherry_lime_stained_glass_flask.json
         │     │  ├─ small_cherry_magenta_stained_glass_flask.json
         │     │  ├─ small_cherry_orange_stained_glass_flask.json
         │     │  ├─ small_cherry_pink_stained_glass_flask.json
         │     │  ├─ small_cherry_purple_stained_glass_flask.json
         │     │  ├─ small_cherry_red_stained_glass_flask.json
         │     │  ├─ small_cherry_tinted_glass_flask.json
         │     │  ├─ small_cherry_white_stained_glass_flask.json
         │     │  ├─ small_cherry_yellow_stained_glass_flask.json
         │     │  ├─ small_crimson_black_stained_glass_flask.json
         │     │  ├─ small_crimson_blue_stained_glass_flask.json
         │     │  ├─ small_crimson_brown_stained_glass_flask.json
         │     │  ├─ small_crimson_cyan_stained_glass_flask.json
         │     │  ├─ small_crimson_glass_flask.json
         │     │  ├─ small_crimson_gray_stained_glass_flask.json
         │     │  ├─ small_crimson_green_stained_glass_flask.json
         │     │  ├─ small_crimson_light_blue_stained_glass_flask.json
         │     │  ├─ small_crimson_light_gray_stained_glass_flask.json
         │     │  ├─ small_crimson_lime_stained_glass_flask.json
         │     │  ├─ small_crimson_magenta_stained_glass_flask.json
         │     │  ├─ small_crimson_orange_stained_glass_flask.json
         │     │  ├─ small_crimson_pink_stained_glass_flask.json
         │     │  ├─ small_crimson_purple_stained_glass_flask.json
         │     │  ├─ small_crimson_red_stained_glass_flask.json
         │     │  ├─ small_crimson_tinted_glass_flask.json
         │     │  ├─ small_crimson_white_stained_glass_flask.json
         │     │  ├─ small_crimson_yellow_stained_glass_flask.json
         │     │  ├─ small_dark_oak_black_stained_glass_flask.json
         │     │  ├─ small_dark_oak_blue_stained_glass_flask.json
         │     │  ├─ small_dark_oak_brown_stained_glass_flask.json
         │     │  ├─ small_dark_oak_cyan_stained_glass_flask.json
         │     │  ├─ small_dark_oak_glass_flask.json
         │     │  ├─ small_dark_oak_gray_stained_glass_flask.json
         │     │  ├─ small_dark_oak_green_stained_glass_flask.json
         │     │  ├─ small_dark_oak_light_blue_stained_glass_flask.json
         │     │  ├─ small_dark_oak_light_gray_stained_glass_flask.json
         │     │  ├─ small_dark_oak_lime_stained_glass_flask.json
         │     │  ├─ small_dark_oak_magenta_stained_glass_flask.json
         │     │  ├─ small_dark_oak_orange_stained_glass_flask.json
         │     │  ├─ small_dark_oak_pink_stained_glass_flask.json
         │     │  ├─ small_dark_oak_purple_stained_glass_flask.json
         │     │  ├─ small_dark_oak_red_stained_glass_flask.json
         │     │  ├─ small_dark_oak_tinted_glass_flask.json
         │     │  ├─ small_dark_oak_white_stained_glass_flask.json
         │     │  ├─ small_dark_oak_yellow_stained_glass_flask.json
         │     │  ├─ small_jungle_black_stained_glass_flask.json
         │     │  ├─ small_jungle_blue_stained_glass_flask.json
         │     │  ├─ small_jungle_brown_stained_glass_flask.json
         │     │  ├─ small_jungle_cyan_stained_glass_flask.json
         │     │  ├─ small_jungle_glass_flask.json
         │     │  ├─ small_jungle_gray_stained_glass_flask.json
         │     │  ├─ small_jungle_green_stained_glass_flask.json
         │     │  ├─ small_jungle_light_blue_stained_glass_flask.json
         │     │  ├─ small_jungle_light_gray_stained_glass_flask.json
         │     │  ├─ small_jungle_lime_stained_glass_flask.json
         │     │  ├─ small_jungle_magenta_stained_glass_flask.json
         │     │  ├─ small_jungle_orange_stained_glass_flask.json
         │     │  ├─ small_jungle_pink_stained_glass_flask.json
         │     │  ├─ small_jungle_purple_stained_glass_flask.json
         │     │  ├─ small_jungle_red_stained_glass_flask.json
         │     │  ├─ small_jungle_tinted_glass_flask.json
         │     │  ├─ small_jungle_white_stained_glass_flask.json
         │     │  ├─ small_jungle_yellow_stained_glass_flask.json
         │     │  ├─ small_mangrove_black_stained_glass_flask.json
         │     │  ├─ small_mangrove_blue_stained_glass_flask.json
         │     │  ├─ small_mangrove_brown_stained_glass_flask.json
         │     │  ├─ small_mangrove_cyan_stained_glass_flask.json
         │     │  ├─ small_mangrove_glass_flask.json
         │     │  ├─ small_mangrove_gray_stained_glass_flask.json
         │     │  ├─ small_mangrove_green_stained_glass_flask.json
         │     │  ├─ small_mangrove_light_blue_stained_glass_flask.json
         │     │  ├─ small_mangrove_light_gray_stained_glass_flask.json
         │     │  ├─ small_mangrove_lime_stained_glass_flask.json
         │     │  ├─ small_mangrove_magenta_stained_glass_flask.json
         │     │  ├─ small_mangrove_orange_stained_glass_flask.json
         │     │  ├─ small_mangrove_pink_stained_glass_flask.json
         │     │  ├─ small_mangrove_purple_stained_glass_flask.json
         │     │  ├─ small_mangrove_red_stained_glass_flask.json
         │     │  ├─ small_mangrove_tinted_glass_flask.json
         │     │  ├─ small_mangrove_white_stained_glass_flask.json
         │     │  ├─ small_mangrove_yellow_stained_glass_flask.json
         │     │  ├─ small_oak_black_stained_glass_flask.json
         │     │  ├─ small_oak_blue_stained_glass_flask.json
         │     │  ├─ small_oak_brown_stained_glass_flask.json
         │     │  ├─ small_oak_cyan_stained_glass_flask.json
         │     │  ├─ small_oak_glass_flask.json
         │     │  ├─ small_oak_gray_stained_glass_flask.json
         │     │  ├─ small_oak_green_stained_glass_flask.json
         │     │  ├─ small_oak_light_blue_stained_glass_flask.json
         │     │  ├─ small_oak_light_gray_stained_glass_flask.json
         │     │  ├─ small_oak_lime_stained_glass_flask.json
         │     │  ├─ small_oak_magenta_stained_glass_flask.json
         │     │  ├─ small_oak_orange_stained_glass_flask.json
         │     │  ├─ small_oak_pink_stained_glass_flask.json
         │     │  ├─ small_oak_purple_stained_glass_flask.json
         │     │  ├─ small_oak_red_stained_glass_flask.json
         │     │  ├─ small_oak_tinted_glass_flask.json
         │     │  ├─ small_oak_white_stained_glass_flask.json
         │     │  ├─ small_oak_yellow_stained_glass_flask.json
         │     │  ├─ small_pale_oak_black_stained_glass_flask.json
         │     │  ├─ small_pale_oak_blue_stained_glass_flask.json
         │     │  ├─ small_pale_oak_brown_stained_glass_flask.json
         │     │  ├─ small_pale_oak_cyan_stained_glass_flask.json
         │     │  ├─ small_pale_oak_glass_flask.json
         │     │  ├─ small_pale_oak_gray_stained_glass_flask.json
         │     │  ├─ small_pale_oak_green_stained_glass_flask.json
         │     │  ├─ small_pale_oak_light_blue_stained_glass_flask.json
         │     │  ├─ small_pale_oak_light_gray_stained_glass_flask.json
         │     │  ├─ small_pale_oak_lime_stained_glass_flask.json
         │     │  ├─ small_pale_oak_magenta_stained_glass_flask.json
         │     │  ├─ small_pale_oak_orange_stained_glass_flask.json
         │     │  ├─ small_pale_oak_pink_stained_glass_flask.json
         │     │  ├─ small_pale_oak_purple_stained_glass_flask.json
         │     │  ├─ small_pale_oak_red_stained_glass_flask.json
         │     │  ├─ small_pale_oak_tinted_glass_flask.json
         │     │  ├─ small_pale_oak_white_stained_glass_flask.json
         │     │  ├─ small_pale_oak_yellow_stained_glass_flask.json
         │     │  ├─ small_spruce_black_stained_glass_flask.json
         │     │  ├─ small_spruce_blue_stained_glass_flask.json
         │     │  ├─ small_spruce_brown_stained_glass_flask.json
         │     │  ├─ small_spruce_cyan_stained_glass_flask.json
         │     │  ├─ small_spruce_glass_flask.json
         │     │  ├─ small_spruce_gray_stained_glass_flask.json
         │     │  ├─ small_spruce_green_stained_glass_flask.json
         │     │  ├─ small_spruce_light_blue_stained_glass_flask.json
         │     │  ├─ small_spruce_light_gray_stained_glass_flask.json
         │     │  ├─ small_spruce_lime_stained_glass_flask.json
         │     │  ├─ small_spruce_magenta_stained_glass_flask.json
         │     │  ├─ small_spruce_orange_stained_glass_flask.json
         │     │  ├─ small_spruce_pink_stained_glass_flask.json
         │     │  ├─ small_spruce_purple_stained_glass_flask.json
         │     │  ├─ small_spruce_red_stained_glass_flask.json
         │     │  ├─ small_spruce_tinted_glass_flask.json
         │     │  ├─ small_spruce_white_stained_glass_flask.json
         │     │  ├─ small_spruce_yellow_stained_glass_flask.json
         │     │  ├─ small_warped_black_stained_glass_flask.json
         │     │  ├─ small_warped_blue_stained_glass_flask.json
         │     │  ├─ small_warped_brown_stained_glass_flask.json
         │     │  ├─ small_warped_cyan_stained_glass_flask.json
         │     │  ├─ small_warped_glass_flask.json
         │     │  ├─ small_warped_gray_stained_glass_flask.json
         │     │  ├─ small_warped_green_stained_glass_flask.json
         │     │  ├─ small_warped_light_blue_stained_glass_flask.json
         │     │  ├─ small_warped_light_gray_stained_glass_flask.json
         │     │  ├─ small_warped_lime_stained_glass_flask.json
         │     │  ├─ small_warped_magenta_stained_glass_flask.json
         │     │  ├─ small_warped_orange_stained_glass_flask.json
         │     │  ├─ small_warped_pink_stained_glass_flask.json
         │     │  ├─ small_warped_purple_stained_glass_flask.json
         │     │  ├─ small_warped_red_stained_glass_flask.json
         │     │  ├─ small_warped_tinted_glass_flask.json
         │     │  ├─ small_warped_white_stained_glass_flask.json
         │     │  ├─ small_warped_yellow_stained_glass_flask.json
         │     │  ├─ spruce_copper_barrel.json
         │     │  ├─ spruce_copper_barrel_block.json
         │     │  ├─ spruce_copper_exposed_barrel.json
         │     │  ├─ spruce_copper_exposed_barrel_block.json
         │     │  ├─ spruce_copper_oxidized_barrel.json
         │     │  ├─ spruce_copper_oxidized_barrel_block.json
         │     │  ├─ spruce_copper_weathered_barrel.json
         │     │  ├─ spruce_copper_weathered_barrel_block.json
         │     │  ├─ spruce_gold_barrel.json
         │     │  ├─ spruce_gold_barrel_block.json
         │     │  ├─ spruce_iron_barrel.json
         │     │  ├─ spruce_iron_barrel_block.json
         │     │  ├─ spruce_netherite_barrel.json
         │     │  ├─ spruce_netherite_barrel_block.json
         │     │  ├─ warped_copper_barrel.json
         │     │  ├─ warped_copper_barrel_block.json
         │     │  ├─ warped_copper_exposed_barrel.json
         │     │  ├─ warped_copper_exposed_barrel_block.json
         │     │  ├─ warped_copper_oxidized_barrel.json
         │     │  ├─ warped_copper_oxidized_barrel_block.json
         │     │  ├─ warped_copper_weathered_barrel.json
         │     │  ├─ warped_copper_weathered_barrel_block.json
         │     │  ├─ warped_gold_barrel.json
         │     │  ├─ warped_gold_barrel_block.json
         │     │  ├─ warped_iron_barrel.json
         │     │  ├─ warped_iron_barrel_block.json
         │     │  ├─ warped_netherite_barrel.json
         │     │  └─ warped_netherite_barrel_block.json
         │     ├─ lang
         │     │  └─ en_us.json
         │     ├─ models
         │     │  ├─ block
         │     │  │  ├─ acacia_copper_barrel_block.json
         │     │  │  ├─ acacia_copper_exposed_barrel_block.json
         │     │  │  ├─ acacia_copper_oxidized_barrel_block.json
         │     │  │  ├─ acacia_copper_weathered_barrel_block.json
         │     │  │  ├─ acacia_gold_barrel_block.json
         │     │  │  ├─ acacia_iron_barrel_block.json
         │     │  │  ├─ acacia_netherite_barrel_block.json
         │     │  │  ├─ bamboo_copper_barrel_block.json
         │     │  │  ├─ bamboo_copper_exposed_barrel_block.json
         │     │  │  ├─ bamboo_copper_oxidized_barrel_block.json
         │     │  │  ├─ bamboo_copper_weathered_barrel_block.json
         │     │  │  ├─ bamboo_gold_barrel_block.json
         │     │  │  ├─ bamboo_iron_barrel_block.json
         │     │  │  ├─ bamboo_netherite_barrel_block.json
         │     │  │  ├─ birch_copper_barrel_block.json
         │     │  │  ├─ birch_copper_exposed_barrel_block.json
         │     │  │  ├─ birch_copper_oxidized_barrel_block.json
         │     │  │  ├─ birch_copper_weathered_barrel_block.json
         │     │  │  ├─ birch_gold_barrel_block.json
         │     │  │  ├─ birch_iron_barrel_block.json
         │     │  │  ├─ birch_netherite_barrel_block.json
         │     │  │  ├─ cherry_copper_barrel_block.json
         │     │  │  ├─ cherry_copper_exposed_barrel_block.json
         │     │  │  ├─ cherry_copper_oxidized_barrel_block.json
         │     │  │  ├─ cherry_copper_weathered_barrel_block.json
         │     │  │  ├─ cherry_gold_barrel_block.json
         │     │  │  ├─ cherry_iron_barrel_block.json
         │     │  │  ├─ cherry_netherite_barrel_block.json
         │     │  │  ├─ copper_exposed_keg_block.json
         │     │  │  ├─ copper_keg_block.json
         │     │  │  ├─ copper_oxidized_keg_block.json
         │     │  │  ├─ copper_weathered_keg_block.json
         │     │  │  ├─ crimson_copper_barrel_block.json
         │     │  │  ├─ crimson_copper_exposed_barrel_block.json
         │     │  │  ├─ crimson_copper_oxidized_barrel_block.json
         │     │  │  ├─ crimson_copper_weathered_barrel_block.json
         │     │  │  ├─ crimson_gold_barrel_block.json
         │     │  │  ├─ crimson_iron_barrel_block.json
         │     │  │  ├─ crimson_netherite_barrel_block.json
         │     │  │  ├─ dark_oak_copper_barrel_block.json
         │     │  │  ├─ dark_oak_copper_exposed_barrel_block.json
         │     │  │  ├─ dark_oak_copper_oxidized_barrel_block.json
         │     │  │  ├─ dark_oak_copper_weathered_barrel_block.json
         │     │  │  ├─ dark_oak_gold_barrel_block.json
         │     │  │  ├─ dark_oak_iron_barrel_block.json
         │     │  │  ├─ dark_oak_netherite_barrel_block.json
         │     │  │  ├─ gold_keg_block.json
         │     │  │  ├─ iron_keg.json
         │     │  │  ├─ iron_keg_block.json
         │     │  │  ├─ jungle_copper_barrel_block.json
         │     │  │  ├─ jungle_copper_exposed_barrel_block.json
         │     │  │  ├─ jungle_copper_oxidized_barrel_block.json
         │     │  │  ├─ jungle_copper_weathered_barrel_block.json
         │     │  │  ├─ jungle_gold_barrel_block.json
         │     │  │  ├─ jungle_iron_barrel_block.json
         │     │  │  ├─ jungle_netherite_barrel_block.json
         │     │  │  ├─ mangrove_copper_barrel_block.json
         │     │  │  ├─ mangrove_copper_exposed_barrel_block.json
         │     │  │  ├─ mangrove_copper_oxidized_barrel_block.json
         │     │  │  ├─ mangrove_copper_weathered_barrel_block.json
         │     │  │  ├─ mangrove_gold_barrel_block.json
         │     │  │  ├─ mangrove_iron_barrel_block.json
         │     │  │  ├─ mangrove_netherite_barrel_block.json
         │     │  │  ├─ netherite_keg_block.json
         │     │  │  ├─ oak_copper_barrel_block.json
         │     │  │  ├─ oak_copper_exposed_barrel_block.json
         │     │  │  ├─ oak_copper_oxidized_barrel_block.json
         │     │  │  ├─ oak_copper_weathered_barrel_block.json
         │     │  │  ├─ oak_gold_barrel_block.json
         │     │  │  ├─ oak_iron_barrel.json
         │     │  │  ├─ oak_iron_barrel_block.json
         │     │  │  ├─ oak_netherite_barrel_block.json
         │     │  │  ├─ pale_oak_copper_barrel_block.json
         │     │  │  ├─ pale_oak_copper_exposed_barrel_block.json
         │     │  │  ├─ pale_oak_copper_oxidized_barrel_block.json
         │     │  │  ├─ pale_oak_copper_weathered_barrel_block.json
         │     │  │  ├─ pale_oak_gold_barrel_block.json
         │     │  │  ├─ pale_oak_iron_barrel_block.json
         │     │  │  ├─ pale_oak_netherite_barrel_block.json
         │     │  │  ├─ spruce_copper_barrel_block.json
         │     │  │  ├─ spruce_copper_exposed_barrel_block.json
         │     │  │  ├─ spruce_copper_oxidized_barrel_block.json
         │     │  │  ├─ spruce_copper_weathered_barrel_block.json
         │     │  │  ├─ spruce_gold_barrel_block.json
         │     │  │  ├─ spruce_iron_barrel_block.json
         │     │  │  ├─ spruce_netherite_barrel_block.json
         │     │  │  ├─ warped_copper_barrel_block.json
         │     │  │  ├─ warped_copper_exposed_barrel_block.json
         │     │  │  ├─ warped_copper_oxidized_barrel_block.json
         │     │  │  ├─ warped_copper_weathered_barrel_block.json
         │     │  │  ├─ warped_gold_barrel_block.json
         │     │  │  ├─ warped_iron_barrel_block.json
         │     │  │  └─ warped_netherite_barrel_block.json
         │     │  └─ item
         │     │     ├─ acacia_copper_barrel.json
         │     │     ├─ acacia_copper_barrel_block.json
         │     │     ├─ acacia_copper_exposed_barrel.json
         │     │     ├─ acacia_copper_exposed_barrel_block.json
         │     │     ├─ acacia_copper_oxidized_barrel.json
         │     │     ├─ acacia_copper_oxidized_barrel_block.json
         │     │     ├─ acacia_copper_weathered_barrel.json
         │     │     ├─ acacia_copper_weathered_barrel_block.json
         │     │     ├─ acacia_gold_barrel.json
         │     │     ├─ acacia_gold_barrel_block.json
         │     │     ├─ acacia_iron_barrel.json
         │     │     ├─ acacia_iron_barrel_block.json
         │     │     ├─ acacia_netherite_barrel.json
         │     │     ├─ acacia_netherite_barrel_block.json
         │     │     ├─ bamboo_copper_barrel.json
         │     │     ├─ bamboo_copper_barrel_block.json
         │     │     ├─ bamboo_copper_exposed_barrel.json
         │     │     ├─ bamboo_copper_exposed_barrel_block.json
         │     │     ├─ bamboo_copper_oxidized_barrel.json
         │     │     ├─ bamboo_copper_oxidized_barrel_block.json
         │     │     ├─ bamboo_copper_weathered_barrel.json
         │     │     ├─ bamboo_copper_weathered_barrel_block.json
         │     │     ├─ bamboo_gold_barrel.json
         │     │     ├─ bamboo_gold_barrel_block.json
         │     │     ├─ bamboo_iron_barrel.json
         │     │     ├─ bamboo_iron_barrel_block.json
         │     │     ├─ bamboo_netherite_barrel.json
         │     │     ├─ bamboo_netherite_barrel_block.json
         │     │     ├─ big_acacia_black_stained_glass_flask.json
         │     │     ├─ big_acacia_blue_stained_glass_flask.json
         │     │     ├─ big_acacia_brown_stained_glass_flask.json
         │     │     ├─ big_acacia_cyan_stained_glass_flask.json
         │     │     ├─ big_acacia_glass_flask.json
         │     │     ├─ big_acacia_gray_stained_glass_flask.json
         │     │     ├─ big_acacia_green_stained_glass_flask.json
         │     │     ├─ big_acacia_light_blue_stained_glass_flask.json
         │     │     ├─ big_acacia_light_gray_stained_glass_flask.json
         │     │     ├─ big_acacia_lime_stained_glass_flask.json
         │     │     ├─ big_acacia_magenta_stained_glass_flask.json
         │     │     ├─ big_acacia_orange_stained_glass_flask.json
         │     │     ├─ big_acacia_pink_stained_glass_flask.json
         │     │     ├─ big_acacia_purple_stained_glass_flask.json
         │     │     ├─ big_acacia_red_stained_glass_flask.json
         │     │     ├─ big_acacia_tinted_glass_flask.json
         │     │     ├─ big_acacia_white_stained_glass_flask.json
         │     │     ├─ big_acacia_yellow_stained_glass_flask.json
         │     │     ├─ big_bamboo_black_stained_glass_flask.json
         │     │     ├─ big_bamboo_blue_stained_glass_flask.json
         │     │     ├─ big_bamboo_brown_stained_glass_flask.json
         │     │     ├─ big_bamboo_cyan_stained_glass_flask.json
         │     │     ├─ big_bamboo_glass_flask.json
         │     │     ├─ big_bamboo_gray_stained_glass_flask.json
         │     │     ├─ big_bamboo_green_stained_glass_flask.json
         │     │     ├─ big_bamboo_light_blue_stained_glass_flask.json
         │     │     ├─ big_bamboo_light_gray_stained_glass_flask.json
         │     │     ├─ big_bamboo_lime_stained_glass_flask.json
         │     │     ├─ big_bamboo_magenta_stained_glass_flask.json
         │     │     ├─ big_bamboo_orange_stained_glass_flask.json
         │     │     ├─ big_bamboo_pink_stained_glass_flask.json
         │     │     ├─ big_bamboo_purple_stained_glass_flask.json
         │     │     ├─ big_bamboo_red_stained_glass_flask.json
         │     │     ├─ big_bamboo_tinted_glass_flask.json
         │     │     ├─ big_bamboo_white_stained_glass_flask.json
         │     │     ├─ big_bamboo_yellow_stained_glass_flask.json
         │     │     ├─ big_birch_black_stained_glass_flask.json
         │     │     ├─ big_birch_blue_stained_glass_flask.json
         │     │     ├─ big_birch_brown_stained_glass_flask.json
         │     │     ├─ big_birch_cyan_stained_glass_flask.json
         │     │     ├─ big_birch_glass_flask.json
         │     │     ├─ big_birch_gray_stained_glass_flask.json
         │     │     ├─ big_birch_green_stained_glass_flask.json
         │     │     ├─ big_birch_light_blue_stained_glass_flask.json
         │     │     ├─ big_birch_light_gray_stained_glass_flask.json
         │     │     ├─ big_birch_lime_stained_glass_flask.json
         │     │     ├─ big_birch_magenta_stained_glass_flask.json
         │     │     ├─ big_birch_orange_stained_glass_flask.json
         │     │     ├─ big_birch_pink_stained_glass_flask.json
         │     │     ├─ big_birch_purple_stained_glass_flask.json
         │     │     ├─ big_birch_red_stained_glass_flask.json
         │     │     ├─ big_birch_tinted_glass_flask.json
         │     │     ├─ big_birch_white_stained_glass_flask.json
         │     │     ├─ big_birch_yellow_stained_glass_flask.json
         │     │     ├─ big_cherry_black_stained_glass_flask.json
         │     │     ├─ big_cherry_blue_stained_glass_flask.json
         │     │     ├─ big_cherry_brown_stained_glass_flask.json
         │     │     ├─ big_cherry_cyan_stained_glass_flask.json
         │     │     ├─ big_cherry_glass_flask.json
         │     │     ├─ big_cherry_gray_stained_glass_flask.json
         │     │     ├─ big_cherry_green_stained_glass_flask.json
         │     │     ├─ big_cherry_light_blue_stained_glass_flask.json
         │     │     ├─ big_cherry_light_gray_stained_glass_flask.json
         │     │     ├─ big_cherry_lime_stained_glass_flask.json
         │     │     ├─ big_cherry_magenta_stained_glass_flask.json
         │     │     ├─ big_cherry_orange_stained_glass_flask.json
         │     │     ├─ big_cherry_pink_stained_glass_flask.json
         │     │     ├─ big_cherry_purple_stained_glass_flask.json
         │     │     ├─ big_cherry_red_stained_glass_flask.json
         │     │     ├─ big_cherry_tinted_glass_flask.json
         │     │     ├─ big_cherry_white_stained_glass_flask.json
         │     │     ├─ big_cherry_yellow_stained_glass_flask.json
         │     │     ├─ big_crimson_black_stained_glass_flask.json
         │     │     ├─ big_crimson_blue_stained_glass_flask.json
         │     │     ├─ big_crimson_brown_stained_glass_flask.json
         │     │     ├─ big_crimson_cyan_stained_glass_flask.json
         │     │     ├─ big_crimson_glass_flask.json
         │     │     ├─ big_crimson_gray_stained_glass_flask.json
         │     │     ├─ big_crimson_green_stained_glass_flask.json
         │     │     ├─ big_crimson_light_blue_stained_glass_flask.json
         │     │     ├─ big_crimson_light_gray_stained_glass_flask.json
         │     │     ├─ big_crimson_lime_stained_glass_flask.json
         │     │     ├─ big_crimson_magenta_stained_glass_flask.json
         │     │     ├─ big_crimson_orange_stained_glass_flask.json
         │     │     ├─ big_crimson_pink_stained_glass_flask.json
         │     │     ├─ big_crimson_purple_stained_glass_flask.json
         │     │     ├─ big_crimson_red_stained_glass_flask.json
         │     │     ├─ big_crimson_tinted_glass_flask.json
         │     │     ├─ big_crimson_white_stained_glass_flask.json
         │     │     ├─ big_crimson_yellow_stained_glass_flask.json
         │     │     ├─ big_dark_oak_black_stained_glass_flask.json
         │     │     ├─ big_dark_oak_blue_stained_glass_flask.json
         │     │     ├─ big_dark_oak_brown_stained_glass_flask.json
         │     │     ├─ big_dark_oak_cyan_stained_glass_flask.json
         │     │     ├─ big_dark_oak_glass_flask.json
         │     │     ├─ big_dark_oak_gray_stained_glass_flask.json
         │     │     ├─ big_dark_oak_green_stained_glass_flask.json
         │     │     ├─ big_dark_oak_light_blue_stained_glass_flask.json
         │     │     ├─ big_dark_oak_light_gray_stained_glass_flask.json
         │     │     ├─ big_dark_oak_lime_stained_glass_flask.json
         │     │     ├─ big_dark_oak_magenta_stained_glass_flask.json
         │     │     ├─ big_dark_oak_orange_stained_glass_flask.json
         │     │     ├─ big_dark_oak_pink_stained_glass_flask.json
         │     │     ├─ big_dark_oak_purple_stained_glass_flask.json
         │     │     ├─ big_dark_oak_red_stained_glass_flask.json
         │     │     ├─ big_dark_oak_tinted_glass_flask.json
         │     │     ├─ big_dark_oak_white_stained_glass_flask.json
         │     │     ├─ big_dark_oak_yellow_stained_glass_flask.json
         │     │     ├─ big_jungle_black_stained_glass_flask.json
         │     │     ├─ big_jungle_blue_stained_glass_flask.json
         │     │     ├─ big_jungle_brown_stained_glass_flask.json
         │     │     ├─ big_jungle_cyan_stained_glass_flask.json
         │     │     ├─ big_jungle_glass_flask.json
         │     │     ├─ big_jungle_gray_stained_glass_flask.json
         │     │     ├─ big_jungle_green_stained_glass_flask.json
         │     │     ├─ big_jungle_light_blue_stained_glass_flask.json
         │     │     ├─ big_jungle_light_gray_stained_glass_flask.json
         │     │     ├─ big_jungle_lime_stained_glass_flask.json
         │     │     ├─ big_jungle_magenta_stained_glass_flask.json
         │     │     ├─ big_jungle_orange_stained_glass_flask.json
         │     │     ├─ big_jungle_pink_stained_glass_flask.json
         │     │     ├─ big_jungle_purple_stained_glass_flask.json
         │     │     ├─ big_jungle_red_stained_glass_flask.json
         │     │     ├─ big_jungle_tinted_glass_flask.json
         │     │     ├─ big_jungle_white_stained_glass_flask.json
         │     │     ├─ big_jungle_yellow_stained_glass_flask.json
         │     │     ├─ big_mangrove_black_stained_glass_flask.json
         │     │     ├─ big_mangrove_blue_stained_glass_flask.json
         │     │     ├─ big_mangrove_brown_stained_glass_flask.json
         │     │     ├─ big_mangrove_cyan_stained_glass_flask.json
         │     │     ├─ big_mangrove_glass_flask.json
         │     │     ├─ big_mangrove_gray_stained_glass_flask.json
         │     │     ├─ big_mangrove_green_stained_glass_flask.json
         │     │     ├─ big_mangrove_light_blue_stained_glass_flask.json
         │     │     ├─ big_mangrove_light_gray_stained_glass_flask.json
         │     │     ├─ big_mangrove_lime_stained_glass_flask.json
         │     │     ├─ big_mangrove_magenta_stained_glass_flask.json
         │     │     ├─ big_mangrove_orange_stained_glass_flask.json
         │     │     ├─ big_mangrove_pink_stained_glass_flask.json
         │     │     ├─ big_mangrove_purple_stained_glass_flask.json
         │     │     ├─ big_mangrove_red_stained_glass_flask.json
         │     │     ├─ big_mangrove_tinted_glass_flask.json
         │     │     ├─ big_mangrove_white_stained_glass_flask.json
         │     │     ├─ big_mangrove_yellow_stained_glass_flask.json
         │     │     ├─ big_oak_black_stained_glass_flask.json
         │     │     ├─ big_oak_blue_stained_glass_flask.json
         │     │     ├─ big_oak_brown_stained_glass_flask.json
         │     │     ├─ big_oak_cyan_stained_glass_flask.json
         │     │     ├─ big_oak_glass_flask.json
         │     │     ├─ big_oak_gray_stained_glass_flask.json
         │     │     ├─ big_oak_green_stained_glass_flask.json
         │     │     ├─ big_oak_light_blue_stained_glass_flask.json
         │     │     ├─ big_oak_light_gray_stained_glass_flask.json
         │     │     ├─ big_oak_lime_stained_glass_flask.json
         │     │     ├─ big_oak_magenta_stained_glass_flask.json
         │     │     ├─ big_oak_orange_stained_glass_flask.json
         │     │     ├─ big_oak_pink_stained_glass_flask.json
         │     │     ├─ big_oak_purple_stained_glass_flask.json
         │     │     ├─ big_oak_red_stained_glass_flask.json
         │     │     ├─ big_oak_tinted_glass_flask.json
         │     │     ├─ big_oak_white_stained_glass_flask.json
         │     │     ├─ big_oak_yellow_stained_glass_flask.json
         │     │     ├─ big_pale_oak_black_stained_glass_flask.json
         │     │     ├─ big_pale_oak_blue_stained_glass_flask.json
         │     │     ├─ big_pale_oak_brown_stained_glass_flask.json
         │     │     ├─ big_pale_oak_cyan_stained_glass_flask.json
         │     │     ├─ big_pale_oak_glass_flask.json
         │     │     ├─ big_pale_oak_gray_stained_glass_flask.json
         │     │     ├─ big_pale_oak_green_stained_glass_flask.json
         │     │     ├─ big_pale_oak_light_blue_stained_glass_flask.json
         │     │     ├─ big_pale_oak_light_gray_stained_glass_flask.json
         │     │     ├─ big_pale_oak_lime_stained_glass_flask.json
         │     │     ├─ big_pale_oak_magenta_stained_glass_flask.json
         │     │     ├─ big_pale_oak_orange_stained_glass_flask.json
         │     │     ├─ big_pale_oak_pink_stained_glass_flask.json
         │     │     ├─ big_pale_oak_purple_stained_glass_flask.json
         │     │     ├─ big_pale_oak_red_stained_glass_flask.json
         │     │     ├─ big_pale_oak_tinted_glass_flask.json
         │     │     ├─ big_pale_oak_white_stained_glass_flask.json
         │     │     ├─ big_pale_oak_yellow_stained_glass_flask.json
         │     │     ├─ big_spruce_black_stained_glass_flask.json
         │     │     ├─ big_spruce_blue_stained_glass_flask.json
         │     │     ├─ big_spruce_brown_stained_glass_flask.json
         │     │     ├─ big_spruce_cyan_stained_glass_flask.json
         │     │     ├─ big_spruce_glass_flask.json
         │     │     ├─ big_spruce_gray_stained_glass_flask.json
         │     │     ├─ big_spruce_green_stained_glass_flask.json
         │     │     ├─ big_spruce_light_blue_stained_glass_flask.json
         │     │     ├─ big_spruce_light_gray_stained_glass_flask.json
         │     │     ├─ big_spruce_lime_stained_glass_flask.json
         │     │     ├─ big_spruce_magenta_stained_glass_flask.json
         │     │     ├─ big_spruce_orange_stained_glass_flask.json
         │     │     ├─ big_spruce_pink_stained_glass_flask.json
         │     │     ├─ big_spruce_purple_stained_glass_flask.json
         │     │     ├─ big_spruce_red_stained_glass_flask.json
         │     │     ├─ big_spruce_tinted_glass_flask.json
         │     │     ├─ big_spruce_white_stained_glass_flask.json
         │     │     ├─ big_spruce_yellow_stained_glass_flask.json
         │     │     ├─ big_warped_black_stained_glass_flask.json
         │     │     ├─ big_warped_blue_stained_glass_flask.json
         │     │     ├─ big_warped_brown_stained_glass_flask.json
         │     │     ├─ big_warped_cyan_stained_glass_flask.json
         │     │     ├─ big_warped_glass_flask.json
         │     │     ├─ big_warped_gray_stained_glass_flask.json
         │     │     ├─ big_warped_green_stained_glass_flask.json
         │     │     ├─ big_warped_light_blue_stained_glass_flask.json
         │     │     ├─ big_warped_light_gray_stained_glass_flask.json
         │     │     ├─ big_warped_lime_stained_glass_flask.json
         │     │     ├─ big_warped_magenta_stained_glass_flask.json
         │     │     ├─ big_warped_orange_stained_glass_flask.json
         │     │     ├─ big_warped_pink_stained_glass_flask.json
         │     │     ├─ big_warped_purple_stained_glass_flask.json
         │     │     ├─ big_warped_red_stained_glass_flask.json
         │     │     ├─ big_warped_tinted_glass_flask.json
         │     │     ├─ big_warped_white_stained_glass_flask.json
         │     │     ├─ big_warped_yellow_stained_glass_flask.json
         │     │     ├─ birch_copper_barrel.json
         │     │     ├─ birch_copper_barrel_block.json
         │     │     ├─ birch_copper_exposed_barrel.json
         │     │     ├─ birch_copper_exposed_barrel_block.json
         │     │     ├─ birch_copper_oxidized_barrel.json
         │     │     ├─ birch_copper_oxidized_barrel_block.json
         │     │     ├─ birch_copper_weathered_barrel.json
         │     │     ├─ birch_copper_weathered_barrel_block.json
         │     │     ├─ birch_gold_barrel.json
         │     │     ├─ birch_gold_barrel_block.json
         │     │     ├─ birch_iron_barrel.json
         │     │     ├─ birch_iron_barrel_block.json
         │     │     ├─ birch_netherite_barrel.json
         │     │     ├─ birch_netherite_barrel_block.json
         │     │     ├─ cherry_copper_barrel.json
         │     │     ├─ cherry_copper_barrel_block.json
         │     │     ├─ cherry_copper_exposed_barrel.json
         │     │     ├─ cherry_copper_exposed_barrel_block.json
         │     │     ├─ cherry_copper_oxidized_barrel.json
         │     │     ├─ cherry_copper_oxidized_barrel_block.json
         │     │     ├─ cherry_copper_weathered_barrel.json
         │     │     ├─ cherry_copper_weathered_barrel_block.json
         │     │     ├─ cherry_gold_barrel.json
         │     │     ├─ cherry_gold_barrel_block.json
         │     │     ├─ cherry_iron_barrel.json
         │     │     ├─ cherry_iron_barrel_block.json
         │     │     ├─ cherry_netherite_barrel.json
         │     │     ├─ cherry_netherite_barrel_block.json
         │     │     ├─ copper_exposed_keg.json
         │     │     ├─ copper_exposed_keg_block.json
         │     │     ├─ copper_keg.json
         │     │     ├─ copper_keg_block.json
         │     │     ├─ copper_oxidized_keg.json
         │     │     ├─ copper_oxidized_keg_block.json
         │     │     ├─ copper_weathered_keg.json
         │     │     ├─ copper_weathered_keg_block.json
         │     │     ├─ crimson_copper_barrel.json
         │     │     ├─ crimson_copper_barrel_block.json
         │     │     ├─ crimson_copper_exposed_barrel.json
         │     │     ├─ crimson_copper_exposed_barrel_block.json
         │     │     ├─ crimson_copper_oxidized_barrel.json
         │     │     ├─ crimson_copper_oxidized_barrel_block.json
         │     │     ├─ crimson_copper_weathered_barrel.json
         │     │     ├─ crimson_copper_weathered_barrel_block.json
         │     │     ├─ crimson_gold_barrel.json
         │     │     ├─ crimson_gold_barrel_block.json
         │     │     ├─ crimson_iron_barrel.json
         │     │     ├─ crimson_iron_barrel_block.json
         │     │     ├─ crimson_netherite_barrel.json
         │     │     ├─ crimson_netherite_barrel_block.json
         │     │     ├─ dark_oak_copper_barrel.json
         │     │     ├─ dark_oak_copper_barrel_block.json
         │     │     ├─ dark_oak_copper_exposed_barrel.json
         │     │     ├─ dark_oak_copper_exposed_barrel_block.json
         │     │     ├─ dark_oak_copper_oxidized_barrel.json
         │     │     ├─ dark_oak_copper_oxidized_barrel_block.json
         │     │     ├─ dark_oak_copper_weathered_barrel.json
         │     │     ├─ dark_oak_copper_weathered_barrel_block.json
         │     │     ├─ dark_oak_gold_barrel.json
         │     │     ├─ dark_oak_gold_barrel_block.json
         │     │     ├─ dark_oak_iron_barrel.json
         │     │     ├─ dark_oak_iron_barrel_block.json
         │     │     ├─ dark_oak_netherite_barrel.json
         │     │     ├─ dark_oak_netherite_barrel_block.json
         │     │     ├─ gold_keg.json
         │     │     ├─ gold_keg_block.json
         │     │     ├─ iron_keg.json
         │     │     ├─ iron_keg_block.json
         │     │     ├─ jungle_copper_barrel.json
         │     │     ├─ jungle_copper_barrel_block.json
         │     │     ├─ jungle_copper_exposed_barrel.json
         │     │     ├─ jungle_copper_exposed_barrel_block.json
         │     │     ├─ jungle_copper_oxidized_barrel.json
         │     │     ├─ jungle_copper_oxidized_barrel_block.json
         │     │     ├─ jungle_copper_weathered_barrel.json
         │     │     ├─ jungle_copper_weathered_barrel_block.json
         │     │     ├─ jungle_gold_barrel.json
         │     │     ├─ jungle_gold_barrel_block.json
         │     │     ├─ jungle_iron_barrel.json
         │     │     ├─ jungle_iron_barrel_block.json
         │     │     ├─ jungle_netherite_barrel.json
         │     │     ├─ jungle_netherite_barrel_block.json
         │     │     ├─ mangrove_copper_barrel.json
         │     │     ├─ mangrove_copper_barrel_block.json
         │     │     ├─ mangrove_copper_exposed_barrel.json
         │     │     ├─ mangrove_copper_exposed_barrel_block.json
         │     │     ├─ mangrove_copper_oxidized_barrel.json
         │     │     ├─ mangrove_copper_oxidized_barrel_block.json
         │     │     ├─ mangrove_copper_weathered_barrel.json
         │     │     ├─ mangrove_copper_weathered_barrel_block.json
         │     │     ├─ mangrove_gold_barrel.json
         │     │     ├─ mangrove_gold_barrel_block.json
         │     │     ├─ mangrove_iron_barrel.json
         │     │     ├─ mangrove_iron_barrel_block.json
         │     │     ├─ mangrove_netherite_barrel.json
         │     │     ├─ mangrove_netherite_barrel_block.json
         │     │     ├─ medium_acacia_black_stained_glass_flask.json
         │     │     ├─ medium_acacia_blue_stained_glass_flask.json
         │     │     ├─ medium_acacia_brown_stained_glass_flask.json
         │     │     ├─ medium_acacia_cyan_stained_glass_flask.json
         │     │     ├─ medium_acacia_glass_flask.json
         │     │     ├─ medium_acacia_gray_stained_glass_flask.json
         │     │     ├─ medium_acacia_green_stained_glass_flask.json
         │     │     ├─ medium_acacia_light_blue_stained_glass_flask.json
         │     │     ├─ medium_acacia_light_gray_stained_glass_flask.json
         │     │     ├─ medium_acacia_lime_stained_glass_flask.json
         │     │     ├─ medium_acacia_magenta_stained_glass_flask.json
         │     │     ├─ medium_acacia_orange_stained_glass_flask.json
         │     │     ├─ medium_acacia_pink_stained_glass_flask.json
         │     │     ├─ medium_acacia_purple_stained_glass_flask.json
         │     │     ├─ medium_acacia_red_stained_glass_flask.json
         │     │     ├─ medium_acacia_tinted_glass_flask.json
         │     │     ├─ medium_acacia_white_stained_glass_flask.json
         │     │     ├─ medium_acacia_yellow_stained_glass_flask.json
         │     │     ├─ medium_bamboo_black_stained_glass_flask.json
         │     │     ├─ medium_bamboo_blue_stained_glass_flask.json
         │     │     ├─ medium_bamboo_brown_stained_glass_flask.json
         │     │     ├─ medium_bamboo_cyan_stained_glass_flask.json
         │     │     ├─ medium_bamboo_glass_flask.json
         │     │     ├─ medium_bamboo_gray_stained_glass_flask.json
         │     │     ├─ medium_bamboo_green_stained_glass_flask.json
         │     │     ├─ medium_bamboo_light_blue_stained_glass_flask.json
         │     │     ├─ medium_bamboo_light_gray_stained_glass_flask.json
         │     │     ├─ medium_bamboo_lime_stained_glass_flask.json
         │     │     ├─ medium_bamboo_magenta_stained_glass_flask.json
         │     │     ├─ medium_bamboo_orange_stained_glass_flask.json
         │     │     ├─ medium_bamboo_pink_stained_glass_flask.json
         │     │     ├─ medium_bamboo_purple_stained_glass_flask.json
         │     │     ├─ medium_bamboo_red_stained_glass_flask.json
         │     │     ├─ medium_bamboo_tinted_glass_flask.json
         │     │     ├─ medium_bamboo_white_stained_glass_flask.json
         │     │     ├─ medium_bamboo_yellow_stained_glass_flask.json
         │     │     ├─ medium_birch_black_stained_glass_flask.json
         │     │     ├─ medium_birch_blue_stained_glass_flask.json
         │     │     ├─ medium_birch_brown_stained_glass_flask.json
         │     │     ├─ medium_birch_cyan_stained_glass_flask.json
         │     │     ├─ medium_birch_glass_flask.json
         │     │     ├─ medium_birch_gray_stained_glass_flask.json
         │     │     ├─ medium_birch_green_stained_glass_flask.json
         │     │     ├─ medium_birch_light_blue_stained_glass_flask.json
         │     │     ├─ medium_birch_light_gray_stained_glass_flask.json
         │     │     ├─ medium_birch_lime_stained_glass_flask.json
         │     │     ├─ medium_birch_magenta_stained_glass_flask.json
         │     │     ├─ medium_birch_orange_stained_glass_flask.json
         │     │     ├─ medium_birch_pink_stained_glass_flask.json
         │     │     ├─ medium_birch_purple_stained_glass_flask.json
         │     │     ├─ medium_birch_red_stained_glass_flask.json
         │     │     ├─ medium_birch_tinted_glass_flask.json
         │     │     ├─ medium_birch_white_stained_glass_flask.json
         │     │     ├─ medium_birch_yellow_stained_glass_flask.json
         │     │     ├─ medium_cherry_black_stained_glass_flask.json
         │     │     ├─ medium_cherry_blue_stained_glass_flask.json
         │     │     ├─ medium_cherry_brown_stained_glass_flask.json
         │     │     ├─ medium_cherry_cyan_stained_glass_flask.json
         │     │     ├─ medium_cherry_glass_flask.json
         │     │     ├─ medium_cherry_gray_stained_glass_flask.json
         │     │     ├─ medium_cherry_green_stained_glass_flask.json
         │     │     ├─ medium_cherry_light_blue_stained_glass_flask.json
         │     │     ├─ medium_cherry_light_gray_stained_glass_flask.json
         │     │     ├─ medium_cherry_lime_stained_glass_flask.json
         │     │     ├─ medium_cherry_magenta_stained_glass_flask.json
         │     │     ├─ medium_cherry_orange_stained_glass_flask.json
         │     │     ├─ medium_cherry_pink_stained_glass_flask.json
         │     │     ├─ medium_cherry_purple_stained_glass_flask.json
         │     │     ├─ medium_cherry_red_stained_glass_flask.json
         │     │     ├─ medium_cherry_tinted_glass_flask.json
         │     │     ├─ medium_cherry_white_stained_glass_flask.json
         │     │     ├─ medium_cherry_yellow_stained_glass_flask.json
         │     │     ├─ medium_crimson_black_stained_glass_flask.json
         │     │     ├─ medium_crimson_blue_stained_glass_flask.json
         │     │     ├─ medium_crimson_brown_stained_glass_flask.json
         │     │     ├─ medium_crimson_cyan_stained_glass_flask.json
         │     │     ├─ medium_crimson_glass_flask.json
         │     │     ├─ medium_crimson_gray_stained_glass_flask.json
         │     │     ├─ medium_crimson_green_stained_glass_flask.json
         │     │     ├─ medium_crimson_light_blue_stained_glass_flask.json
         │     │     ├─ medium_crimson_light_gray_stained_glass_flask.json
         │     │     ├─ medium_crimson_lime_stained_glass_flask.json
         │     │     ├─ medium_crimson_magenta_stained_glass_flask.json
         │     │     ├─ medium_crimson_orange_stained_glass_flask.json
         │     │     ├─ medium_crimson_pink_stained_glass_flask.json
         │     │     ├─ medium_crimson_purple_stained_glass_flask.json
         │     │     ├─ medium_crimson_red_stained_glass_flask.json
         │     │     ├─ medium_crimson_tinted_glass_flask.json
         │     │     ├─ medium_crimson_white_stained_glass_flask.json
         │     │     ├─ medium_crimson_yellow_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_black_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_blue_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_brown_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_cyan_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_glass_flask.json
         │     │     ├─ medium_dark_oak_gray_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_green_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_light_blue_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_light_gray_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_lime_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_magenta_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_orange_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_pink_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_purple_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_red_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_tinted_glass_flask.json
         │     │     ├─ medium_dark_oak_white_stained_glass_flask.json
         │     │     ├─ medium_dark_oak_yellow_stained_glass_flask.json
         │     │     ├─ medium_jungle_black_stained_glass_flask.json
         │     │     ├─ medium_jungle_blue_stained_glass_flask.json
         │     │     ├─ medium_jungle_brown_stained_glass_flask.json
         │     │     ├─ medium_jungle_cyan_stained_glass_flask.json
         │     │     ├─ medium_jungle_glass_flask.json
         │     │     ├─ medium_jungle_gray_stained_glass_flask.json
         │     │     ├─ medium_jungle_green_stained_glass_flask.json
         │     │     ├─ medium_jungle_light_blue_stained_glass_flask.json
         │     │     ├─ medium_jungle_light_gray_stained_glass_flask.json
         │     │     ├─ medium_jungle_lime_stained_glass_flask.json
         │     │     ├─ medium_jungle_magenta_stained_glass_flask.json
         │     │     ├─ medium_jungle_orange_stained_glass_flask.json
         │     │     ├─ medium_jungle_pink_stained_glass_flask.json
         │     │     ├─ medium_jungle_purple_stained_glass_flask.json
         │     │     ├─ medium_jungle_red_stained_glass_flask.json
         │     │     ├─ medium_jungle_tinted_glass_flask.json
         │     │     ├─ medium_jungle_white_stained_glass_flask.json
         │     │     ├─ medium_jungle_yellow_stained_glass_flask.json
         │     │     ├─ medium_mangrove_black_stained_glass_flask.json
         │     │     ├─ medium_mangrove_blue_stained_glass_flask.json
         │     │     ├─ medium_mangrove_brown_stained_glass_flask.json
         │     │     ├─ medium_mangrove_cyan_stained_glass_flask.json
         │     │     ├─ medium_mangrove_glass_flask.json
         │     │     ├─ medium_mangrove_gray_stained_glass_flask.json
         │     │     ├─ medium_mangrove_green_stained_glass_flask.json
         │     │     ├─ medium_mangrove_light_blue_stained_glass_flask.json
         │     │     ├─ medium_mangrove_light_gray_stained_glass_flask.json
         │     │     ├─ medium_mangrove_lime_stained_glass_flask.json
         │     │     ├─ medium_mangrove_magenta_stained_glass_flask.json
         │     │     ├─ medium_mangrove_orange_stained_glass_flask.json
         │     │     ├─ medium_mangrove_pink_stained_glass_flask.json
         │     │     ├─ medium_mangrove_purple_stained_glass_flask.json
         │     │     ├─ medium_mangrove_red_stained_glass_flask.json
         │     │     ├─ medium_mangrove_tinted_glass_flask.json
         │     │     ├─ medium_mangrove_white_stained_glass_flask.json
         │     │     ├─ medium_mangrove_yellow_stained_glass_flask.json
         │     │     ├─ medium_oak_black_stained_glass_flask.json
         │     │     ├─ medium_oak_blue_stained_glass_flask.json
         │     │     ├─ medium_oak_brown_stained_glass_flask.json
         │     │     ├─ medium_oak_cyan_stained_glass_flask.json
         │     │     ├─ medium_oak_glass_flask.json
         │     │     ├─ medium_oak_gray_stained_glass_flask.json
         │     │     ├─ medium_oak_green_stained_glass_flask.json
         │     │     ├─ medium_oak_light_blue_stained_glass_flask.json
         │     │     ├─ medium_oak_light_gray_stained_glass_flask.json
         │     │     ├─ medium_oak_lime_stained_glass_flask.json
         │     │     ├─ medium_oak_magenta_stained_glass_flask.json
         │     │     ├─ medium_oak_orange_stained_glass_flask.json
         │     │     ├─ medium_oak_pink_stained_glass_flask.json
         │     │     ├─ medium_oak_purple_stained_glass_flask.json
         │     │     ├─ medium_oak_red_stained_glass_flask.json
         │     │     ├─ medium_oak_tinted_glass_flask.json
         │     │     ├─ medium_oak_white_stained_glass_flask.json
         │     │     ├─ medium_oak_yellow_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_black_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_blue_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_brown_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_cyan_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_glass_flask.json
         │     │     ├─ medium_pale_oak_gray_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_green_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_light_blue_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_light_gray_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_lime_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_magenta_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_orange_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_pink_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_purple_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_red_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_tinted_glass_flask.json
         │     │     ├─ medium_pale_oak_white_stained_glass_flask.json
         │     │     ├─ medium_pale_oak_yellow_stained_glass_flask.json
         │     │     ├─ medium_spruce_black_stained_glass_flask.json
         │     │     ├─ medium_spruce_blue_stained_glass_flask.json
         │     │     ├─ medium_spruce_brown_stained_glass_flask.json
         │     │     ├─ medium_spruce_cyan_stained_glass_flask.json
         │     │     ├─ medium_spruce_glass_flask.json
         │     │     ├─ medium_spruce_gray_stained_glass_flask.json
         │     │     ├─ medium_spruce_green_stained_glass_flask.json
         │     │     ├─ medium_spruce_light_blue_stained_glass_flask.json
         │     │     ├─ medium_spruce_light_gray_stained_glass_flask.json
         │     │     ├─ medium_spruce_lime_stained_glass_flask.json
         │     │     ├─ medium_spruce_magenta_stained_glass_flask.json
         │     │     ├─ medium_spruce_orange_stained_glass_flask.json
         │     │     ├─ medium_spruce_pink_stained_glass_flask.json
         │     │     ├─ medium_spruce_purple_stained_glass_flask.json
         │     │     ├─ medium_spruce_red_stained_glass_flask.json
         │     │     ├─ medium_spruce_tinted_glass_flask.json
         │     │     ├─ medium_spruce_white_stained_glass_flask.json
         │     │     ├─ medium_spruce_yellow_stained_glass_flask.json
         │     │     ├─ medium_warped_black_stained_glass_flask.json
         │     │     ├─ medium_warped_blue_stained_glass_flask.json
         │     │     ├─ medium_warped_brown_stained_glass_flask.json
         │     │     ├─ medium_warped_cyan_stained_glass_flask.json
         │     │     ├─ medium_warped_glass_flask.json
         │     │     ├─ medium_warped_gray_stained_glass_flask.json
         │     │     ├─ medium_warped_green_stained_glass_flask.json
         │     │     ├─ medium_warped_light_blue_stained_glass_flask.json
         │     │     ├─ medium_warped_light_gray_stained_glass_flask.json
         │     │     ├─ medium_warped_lime_stained_glass_flask.json
         │     │     ├─ medium_warped_magenta_stained_glass_flask.json
         │     │     ├─ medium_warped_orange_stained_glass_flask.json
         │     │     ├─ medium_warped_pink_stained_glass_flask.json
         │     │     ├─ medium_warped_purple_stained_glass_flask.json
         │     │     ├─ medium_warped_red_stained_glass_flask.json
         │     │     ├─ medium_warped_tinted_glass_flask.json
         │     │     ├─ medium_warped_white_stained_glass_flask.json
         │     │     ├─ medium_warped_yellow_stained_glass_flask.json
         │     │     ├─ netherite_keg.json
         │     │     ├─ netherite_keg_block.json
         │     │     ├─ oak_copper_barrel.json
         │     │     ├─ oak_copper_barrel_block.json
         │     │     ├─ oak_copper_exposed_barrel.json
         │     │     ├─ oak_copper_exposed_barrel_block.json
         │     │     ├─ oak_copper_oxidized_barrel.json
         │     │     ├─ oak_copper_oxidized_barrel_block.json
         │     │     ├─ oak_copper_weathered_barrel.json
         │     │     ├─ oak_copper_weathered_barrel_block.json
         │     │     ├─ oak_gold_barrel.json
         │     │     ├─ oak_gold_barrel_block.json
         │     │     ├─ oak_iron_barrel.json
         │     │     ├─ oak_iron_barrel_block.json
         │     │     ├─ oak_netherite_barrel.json
         │     │     ├─ oak_netherite_barrel_block.json
         │     │     ├─ pale_oak_copper_barrel.json
         │     │     ├─ pale_oak_copper_barrel_block.json
         │     │     ├─ pale_oak_copper_exposed_barrel.json
         │     │     ├─ pale_oak_copper_exposed_barrel_block.json
         │     │     ├─ pale_oak_copper_oxidized_barrel.json
         │     │     ├─ pale_oak_copper_oxidized_barrel_block.json
         │     │     ├─ pale_oak_copper_weathered_barrel.json
         │     │     ├─ pale_oak_copper_weathered_barrel_block.json
         │     │     ├─ pale_oak_gold_barrel.json
         │     │     ├─ pale_oak_gold_barrel_block.json
         │     │     ├─ pale_oak_iron_barrel.json
         │     │     ├─ pale_oak_iron_barrel_block.json
         │     │     ├─ pale_oak_netherite_barrel.json
         │     │     ├─ pale_oak_netherite_barrel_block.json
         │     │     ├─ small_acacia_black_stained_glass_flask.json
         │     │     ├─ small_acacia_blue_stained_glass_flask.json
         │     │     ├─ small_acacia_brown_stained_glass_flask.json
         │     │     ├─ small_acacia_cyan_stained_glass_flask.json
         │     │     ├─ small_acacia_glass_flask.json
         │     │     ├─ small_acacia_gray_stained_glass_flask.json
         │     │     ├─ small_acacia_green_stained_glass_flask.json
         │     │     ├─ small_acacia_light_blue_stained_glass_flask.json
         │     │     ├─ small_acacia_light_gray_stained_glass_flask.json
         │     │     ├─ small_acacia_lime_stained_glass_flask.json
         │     │     ├─ small_acacia_magenta_stained_glass_flask.json
         │     │     ├─ small_acacia_orange_stained_glass_flask.json
         │     │     ├─ small_acacia_pink_stained_glass_flask.json
         │     │     ├─ small_acacia_purple_stained_glass_flask.json
         │     │     ├─ small_acacia_red_stained_glass_flask.json
         │     │     ├─ small_acacia_tinted_glass_flask.json
         │     │     ├─ small_acacia_white_stained_glass_flask.json
         │     │     ├─ small_acacia_yellow_stained_glass_flask.json
         │     │     ├─ small_bamboo_black_stained_glass_flask.json
         │     │     ├─ small_bamboo_blue_stained_glass_flask.json
         │     │     ├─ small_bamboo_brown_stained_glass_flask.json
         │     │     ├─ small_bamboo_cyan_stained_glass_flask.json
         │     │     ├─ small_bamboo_glass_flask.json
         │     │     ├─ small_bamboo_gray_stained_glass_flask.json
         │     │     ├─ small_bamboo_green_stained_glass_flask.json
         │     │     ├─ small_bamboo_light_blue_stained_glass_flask.json
         │     │     ├─ small_bamboo_light_gray_stained_glass_flask.json
         │     │     ├─ small_bamboo_lime_stained_glass_flask.json
         │     │     ├─ small_bamboo_magenta_stained_glass_flask.json
         │     │     ├─ small_bamboo_orange_stained_glass_flask.json
         │     │     ├─ small_bamboo_pink_stained_glass_flask.json
         │     │     ├─ small_bamboo_purple_stained_glass_flask.json
         │     │     ├─ small_bamboo_red_stained_glass_flask.json
         │     │     ├─ small_bamboo_tinted_glass_flask.json
         │     │     ├─ small_bamboo_white_stained_glass_flask.json
         │     │     ├─ small_bamboo_yellow_stained_glass_flask.json
         │     │     ├─ small_birch_black_stained_glass_flask.json
         │     │     ├─ small_birch_blue_stained_glass_flask.json
         │     │     ├─ small_birch_brown_stained_glass_flask.json
         │     │     ├─ small_birch_cyan_stained_glass_flask.json
         │     │     ├─ small_birch_glass_flask.json
         │     │     ├─ small_birch_gray_stained_glass_flask.json
         │     │     ├─ small_birch_green_stained_glass_flask.json
         │     │     ├─ small_birch_light_blue_stained_glass_flask.json
         │     │     ├─ small_birch_light_gray_stained_glass_flask.json
         │     │     ├─ small_birch_lime_stained_glass_flask.json
         │     │     ├─ small_birch_magenta_stained_glass_flask.json
         │     │     ├─ small_birch_orange_stained_glass_flask.json
         │     │     ├─ small_birch_pink_stained_glass_flask.json
         │     │     ├─ small_birch_purple_stained_glass_flask.json
         │     │     ├─ small_birch_red_stained_glass_flask.json
         │     │     ├─ small_birch_tinted_glass_flask.json
         │     │     ├─ small_birch_white_stained_glass_flask.json
         │     │     ├─ small_birch_yellow_stained_glass_flask.json
         │     │     ├─ small_cherry_black_stained_glass_flask.json
         │     │     ├─ small_cherry_blue_stained_glass_flask.json
         │     │     ├─ small_cherry_brown_stained_glass_flask.json
         │     │     ├─ small_cherry_cyan_stained_glass_flask.json
         │     │     ├─ small_cherry_glass_flask.json
         │     │     ├─ small_cherry_gray_stained_glass_flask.json
         │     │     ├─ small_cherry_green_stained_glass_flask.json
         │     │     ├─ small_cherry_light_blue_stained_glass_flask.json
         │     │     ├─ small_cherry_light_gray_stained_glass_flask.json
         │     │     ├─ small_cherry_lime_stained_glass_flask.json
         │     │     ├─ small_cherry_magenta_stained_glass_flask.json
         │     │     ├─ small_cherry_orange_stained_glass_flask.json
         │     │     ├─ small_cherry_pink_stained_glass_flask.json
         │     │     ├─ small_cherry_purple_stained_glass_flask.json
         │     │     ├─ small_cherry_red_stained_glass_flask.json
         │     │     ├─ small_cherry_tinted_glass_flask.json
         │     │     ├─ small_cherry_white_stained_glass_flask.json
         │     │     ├─ small_cherry_yellow_stained_glass_flask.json
         │     │     ├─ small_crimson_black_stained_glass_flask.json
         │     │     ├─ small_crimson_blue_stained_glass_flask.json
         │     │     ├─ small_crimson_brown_stained_glass_flask.json
         │     │     ├─ small_crimson_cyan_stained_glass_flask.json
         │     │     ├─ small_crimson_glass_flask.json
         │     │     ├─ small_crimson_gray_stained_glass_flask.json
         │     │     ├─ small_crimson_green_stained_glass_flask.json
         │     │     ├─ small_crimson_light_blue_stained_glass_flask.json
         │     │     ├─ small_crimson_light_gray_stained_glass_flask.json
         │     │     ├─ small_crimson_lime_stained_glass_flask.json
         │     │     ├─ small_crimson_magenta_stained_glass_flask.json
         │     │     ├─ small_crimson_orange_stained_glass_flask.json
         │     │     ├─ small_crimson_pink_stained_glass_flask.json
         │     │     ├─ small_crimson_purple_stained_glass_flask.json
         │     │     ├─ small_crimson_red_stained_glass_flask.json
         │     │     ├─ small_crimson_tinted_glass_flask.json
         │     │     ├─ small_crimson_white_stained_glass_flask.json
         │     │     ├─ small_crimson_yellow_stained_glass_flask.json
         │     │     ├─ small_dark_oak_black_stained_glass_flask.json
         │     │     ├─ small_dark_oak_blue_stained_glass_flask.json
         │     │     ├─ small_dark_oak_brown_stained_glass_flask.json
         │     │     ├─ small_dark_oak_cyan_stained_glass_flask.json
         │     │     ├─ small_dark_oak_glass_flask.json
         │     │     ├─ small_dark_oak_gray_stained_glass_flask.json
         │     │     ├─ small_dark_oak_green_stained_glass_flask.json
         │     │     ├─ small_dark_oak_light_blue_stained_glass_flask.json
         │     │     ├─ small_dark_oak_light_gray_stained_glass_flask.json
         │     │     ├─ small_dark_oak_lime_stained_glass_flask.json
         │     │     ├─ small_dark_oak_magenta_stained_glass_flask.json
         │     │     ├─ small_dark_oak_orange_stained_glass_flask.json
         │     │     ├─ small_dark_oak_pink_stained_glass_flask.json
         │     │     ├─ small_dark_oak_purple_stained_glass_flask.json
         │     │     ├─ small_dark_oak_red_stained_glass_flask.json
         │     │     ├─ small_dark_oak_tinted_glass_flask.json
         │     │     ├─ small_dark_oak_white_stained_glass_flask.json
         │     │     ├─ small_dark_oak_yellow_stained_glass_flask.json
         │     │     ├─ small_jungle_black_stained_glass_flask.json
         │     │     ├─ small_jungle_blue_stained_glass_flask.json
         │     │     ├─ small_jungle_brown_stained_glass_flask.json
         │     │     ├─ small_jungle_cyan_stained_glass_flask.json
         │     │     ├─ small_jungle_glass_flask.json
         │     │     ├─ small_jungle_gray_stained_glass_flask.json
         │     │     ├─ small_jungle_green_stained_glass_flask.json
         │     │     ├─ small_jungle_light_blue_stained_glass_flask.json
         │     │     ├─ small_jungle_light_gray_stained_glass_flask.json
         │     │     ├─ small_jungle_lime_stained_glass_flask.json
         │     │     ├─ small_jungle_magenta_stained_glass_flask.json
         │     │     ├─ small_jungle_orange_stained_glass_flask.json
         │     │     ├─ small_jungle_pink_stained_glass_flask.json
         │     │     ├─ small_jungle_purple_stained_glass_flask.json
         │     │     ├─ small_jungle_red_stained_glass_flask.json
         │     │     ├─ small_jungle_tinted_glass_flask.json
         │     │     ├─ small_jungle_white_stained_glass_flask.json
         │     │     ├─ small_jungle_yellow_stained_glass_flask.json
         │     │     ├─ small_mangrove_black_stained_glass_flask.json
         │     │     ├─ small_mangrove_blue_stained_glass_flask.json
         │     │     ├─ small_mangrove_brown_stained_glass_flask.json
         │     │     ├─ small_mangrove_cyan_stained_glass_flask.json
         │     │     ├─ small_mangrove_glass_flask.json
         │     │     ├─ small_mangrove_gray_stained_glass_flask.json
         │     │     ├─ small_mangrove_green_stained_glass_flask.json
         │     │     ├─ small_mangrove_light_blue_stained_glass_flask.json
         │     │     ├─ small_mangrove_light_gray_stained_glass_flask.json
         │     │     ├─ small_mangrove_lime_stained_glass_flask.json
         │     │     ├─ small_mangrove_magenta_stained_glass_flask.json
         │     │     ├─ small_mangrove_orange_stained_glass_flask.json
         │     │     ├─ small_mangrove_pink_stained_glass_flask.json
         │     │     ├─ small_mangrove_purple_stained_glass_flask.json
         │     │     ├─ small_mangrove_red_stained_glass_flask.json
         │     │     ├─ small_mangrove_tinted_glass_flask.json
         │     │     ├─ small_mangrove_white_stained_glass_flask.json
         │     │     ├─ small_mangrove_yellow_stained_glass_flask.json
         │     │     ├─ small_oak_black_stained_glass_flask.json
         │     │     ├─ small_oak_blue_stained_glass_flask.json
         │     │     ├─ small_oak_brown_stained_glass_flask.json
         │     │     ├─ small_oak_cyan_stained_glass_flask.json
         │     │     ├─ small_oak_glass_flask.json
         │     │     ├─ small_oak_gray_stained_glass_flask.json
         │     │     ├─ small_oak_green_stained_glass_flask.json
         │     │     ├─ small_oak_light_blue_stained_glass_flask.json
         │     │     ├─ small_oak_light_gray_stained_glass_flask.json
         │     │     ├─ small_oak_lime_stained_glass_flask.json
         │     │     ├─ small_oak_magenta_stained_glass_flask.json
         │     │     ├─ small_oak_orange_stained_glass_flask.json
         │     │     ├─ small_oak_pink_stained_glass_flask.json
         │     │     ├─ small_oak_purple_stained_glass_flask.json
         │     │     ├─ small_oak_red_stained_glass_flask.json
         │     │     ├─ small_oak_tinted_glass_flask.json
         │     │     ├─ small_oak_white_stained_glass_flask.json
         │     │     ├─ small_oak_yellow_stained_glass_flask.json
         │     │     ├─ small_pale_oak_black_stained_glass_flask.json
         │     │     ├─ small_pale_oak_blue_stained_glass_flask.json
         │     │     ├─ small_pale_oak_brown_stained_glass_flask.json
         │     │     ├─ small_pale_oak_cyan_stained_glass_flask.json
         │     │     ├─ small_pale_oak_glass_flask.json
         │     │     ├─ small_pale_oak_gray_stained_glass_flask.json
         │     │     ├─ small_pale_oak_green_stained_glass_flask.json
         │     │     ├─ small_pale_oak_light_blue_stained_glass_flask.json
         │     │     ├─ small_pale_oak_light_gray_stained_glass_flask.json
         │     │     ├─ small_pale_oak_lime_stained_glass_flask.json
         │     │     ├─ small_pale_oak_magenta_stained_glass_flask.json
         │     │     ├─ small_pale_oak_orange_stained_glass_flask.json
         │     │     ├─ small_pale_oak_pink_stained_glass_flask.json
         │     │     ├─ small_pale_oak_purple_stained_glass_flask.json
         │     │     ├─ small_pale_oak_red_stained_glass_flask.json
         │     │     ├─ small_pale_oak_tinted_glass_flask.json
         │     │     ├─ small_pale_oak_white_stained_glass_flask.json
         │     │     ├─ small_pale_oak_yellow_stained_glass_flask.json
         │     │     ├─ small_spruce_black_stained_glass_flask.json
         │     │     ├─ small_spruce_blue_stained_glass_flask.json
         │     │     ├─ small_spruce_brown_stained_glass_flask.json
         │     │     ├─ small_spruce_cyan_stained_glass_flask.json
         │     │     ├─ small_spruce_glass_flask.json
         │     │     ├─ small_spruce_gray_stained_glass_flask.json
         │     │     ├─ small_spruce_green_stained_glass_flask.json
         │     │     ├─ small_spruce_light_blue_stained_glass_flask.json
         │     │     ├─ small_spruce_light_gray_stained_glass_flask.json
         │     │     ├─ small_spruce_lime_stained_glass_flask.json
         │     │     ├─ small_spruce_magenta_stained_glass_flask.json
         │     │     ├─ small_spruce_orange_stained_glass_flask.json
         │     │     ├─ small_spruce_pink_stained_glass_flask.json
         │     │     ├─ small_spruce_purple_stained_glass_flask.json
         │     │     ├─ small_spruce_red_stained_glass_flask.json
         │     │     ├─ small_spruce_tinted_glass_flask.json
         │     │     ├─ small_spruce_white_stained_glass_flask.json
         │     │     ├─ small_spruce_yellow_stained_glass_flask.json
         │     │     ├─ small_warped_black_stained_glass_flask.json
         │     │     ├─ small_warped_blue_stained_glass_flask.json
         │     │     ├─ small_warped_brown_stained_glass_flask.json
         │     │     ├─ small_warped_cyan_stained_glass_flask.json
         │     │     ├─ small_warped_glass_flask.json
         │     │     ├─ small_warped_gray_stained_glass_flask.json
         │     │     ├─ small_warped_green_stained_glass_flask.json
         │     │     ├─ small_warped_light_blue_stained_glass_flask.json
         │     │     ├─ small_warped_light_gray_stained_glass_flask.json
         │     │     ├─ small_warped_lime_stained_glass_flask.json
         │     │     ├─ small_warped_magenta_stained_glass_flask.json
         │     │     ├─ small_warped_orange_stained_glass_flask.json
         │     │     ├─ small_warped_pink_stained_glass_flask.json
         │     │     ├─ small_warped_purple_stained_glass_flask.json
         │     │     ├─ small_warped_red_stained_glass_flask.json
         │     │     ├─ small_warped_tinted_glass_flask.json
         │     │     ├─ small_warped_white_stained_glass_flask.json
         │     │     ├─ small_warped_yellow_stained_glass_flask.json
         │     │     ├─ spruce_copper_barrel.json
         │     │     ├─ spruce_copper_barrel_block.json
         │     │     ├─ spruce_copper_exposed_barrel.json
         │     │     ├─ spruce_copper_exposed_barrel_block.json
         │     │     ├─ spruce_copper_oxidized_barrel.json
         │     │     ├─ spruce_copper_oxidized_barrel_block.json
         │     │     ├─ spruce_copper_weathered_barrel.json
         │     │     ├─ spruce_copper_weathered_barrel_block.json
         │     │     ├─ spruce_gold_barrel.json
         │     │     ├─ spruce_gold_barrel_block.json
         │     │     ├─ spruce_iron_barrel.json
         │     │     ├─ spruce_iron_barrel_block.json
         │     │     ├─ spruce_netherite_barrel.json
         │     │     ├─ spruce_netherite_barrel_block.json
         │     │     ├─ warped_copper_barrel.json
         │     │     ├─ warped_copper_barrel_block.json
         │     │     ├─ warped_copper_exposed_barrel.json
         │     │     ├─ warped_copper_exposed_barrel_block.json
         │     │     ├─ warped_copper_oxidized_barrel.json
         │     │     ├─ warped_copper_oxidized_barrel_block.json
         │     │     ├─ warped_copper_weathered_barrel.json
         │     │     ├─ warped_copper_weathered_barrel_block.json
         │     │     ├─ warped_gold_barrel.json
         │     │     ├─ warped_gold_barrel_block.json
         │     │     ├─ warped_iron_barrel.json
         │     │     ├─ warped_iron_barrel_block.json
         │     │     ├─ warped_netherite_barrel.json
         │     │     └─ warped_netherite_barrel_block.json
         │     └─ textures
         │        ├─ block
         │        │  ├─ acacia_copper_barrel_block.png
         │        │  ├─ acacia_copper_exposed_barrel_block.png
         │        │  ├─ acacia_copper_oxidized_barrel_block.png
         │        │  ├─ acacia_copper_weathered_barrel_block.png
         │        │  ├─ acacia_gold_barrel_block.png
         │        │  ├─ acacia_iron_barrel_block.png
         │        │  ├─ acacia_netherite_barrel_block.png
         │        │  ├─ bamboo_copper_barrel_block.png
         │        │  ├─ bamboo_copper_exposed_barrel_block.png
         │        │  ├─ bamboo_copper_oxidized_barrel_block.png
         │        │  ├─ bamboo_copper_weathered_barrel_block.png
         │        │  ├─ bamboo_gold_barrel_block.png
         │        │  ├─ bamboo_iron_barrel_block.png
         │        │  ├─ bamboo_netherite_barrel_block.png
         │        │  ├─ birch_copper_barrel_block.png
         │        │  ├─ birch_copper_exposed_barrel_block.png
         │        │  ├─ birch_copper_oxidized_barrel_block.png
         │        │  ├─ birch_copper_weathered_barrel_block.png
         │        │  ├─ birch_gold_barrel_block.png
         │        │  ├─ birch_iron_barrel_block.png
         │        │  ├─ birch_netherite_barrel_block.png
         │        │  ├─ cherry_copper_barrel_block.png
         │        │  ├─ cherry_copper_exposed_barrel_block.png
         │        │  ├─ cherry_copper_oxidized_barrel_block.png
         │        │  ├─ cherry_copper_weathered_barrel_block.png
         │        │  ├─ cherry_gold_barrel_block.png
         │        │  ├─ cherry_iron_barrel_block.png
         │        │  ├─ cherry_netherite_barrel_block.png
         │        │  ├─ copper_exposed_keg_block.png
         │        │  ├─ copper_keg_block.png
         │        │  ├─ copper_oxidized_keg_block.png
         │        │  ├─ copper_weathered_keg_block.png
         │        │  ├─ crimson_copper_barrel_block.png
         │        │  ├─ crimson_copper_exposed_barrel_block.png
         │        │  ├─ crimson_copper_oxidized_barrel_block.png
         │        │  ├─ crimson_copper_weathered_barrel_block.png
         │        │  ├─ crimson_gold_barrel_block.png
         │        │  ├─ crimson_iron_barrel_block.png
         │        │  ├─ crimson_netherite_barrel_block.png
         │        │  ├─ dark_oak_copper_barrel_block.png
         │        │  ├─ dark_oak_copper_exposed_barrel_block.png
         │        │  ├─ dark_oak_copper_oxidized_barrel_block.png
         │        │  ├─ dark_oak_copper_weathered_barrel_block.png
         │        │  ├─ dark_oak_gold_barrel_block.png
         │        │  ├─ dark_oak_iron_barrel_block.png
         │        │  ├─ dark_oak_netherite_barrel_block.png
         │        │  ├─ gold_keg_block.png
         │        │  ├─ iron_keg_block.png
         │        │  ├─ jungle_copper_barrel_block.png
         │        │  ├─ jungle_copper_exposed_barrel_block.png
         │        │  ├─ jungle_copper_oxidized_barrel_block.png
         │        │  ├─ jungle_copper_weathered_barrel_block.png
         │        │  ├─ jungle_gold_barrel_block.png
         │        │  ├─ jungle_iron_barrel_block.png
         │        │  ├─ jungle_netherite_barrel_block.png
         │        │  ├─ mangrove_copper_barrel_block.png
         │        │  ├─ mangrove_copper_exposed_barrel_block.png
         │        │  ├─ mangrove_copper_oxidized_barrel_block.png
         │        │  ├─ mangrove_copper_weathered_barrel_block.png
         │        │  ├─ mangrove_gold_barrel_block.png
         │        │  ├─ mangrove_iron_barrel_block.png
         │        │  ├─ mangrove_netherite_barrel_block.png
         │        │  ├─ netherite_keg_block.png
         │        │  ├─ oak_copper_barrel_block.png
         │        │  ├─ oak_copper_exposed_barrel_block.png
         │        │  ├─ oak_copper_oxidized_barrel_block.png
         │        │  ├─ oak_copper_weathered_barrel_block.png
         │        │  ├─ oak_gold_barrel_block.png
         │        │  ├─ oak_iron_barrel_block.png
         │        │  ├─ oak_netherite_barrel_block.png
         │        │  ├─ pale_oak_copper_barrel_block.png
         │        │  ├─ pale_oak_copper_exposed_barrel_block.png
         │        │  ├─ pale_oak_copper_oxidized_barrel_block.png
         │        │  ├─ pale_oak_copper_weathered_barrel_block.png
         │        │  ├─ pale_oak_gold_barrel_block.png
         │        │  ├─ pale_oak_iron_barrel_block.png
         │        │  ├─ pale_oak_netherite_barrel_block.png
         │        │  ├─ spruce_copper_barrel_block.png
         │        │  ├─ spruce_copper_exposed_barrel_block.png
         │        │  ├─ spruce_copper_oxidized_barrel_block.png
         │        │  ├─ spruce_copper_weathered_barrel_block.png
         │        │  ├─ spruce_gold_barrel_block.png
         │        │  ├─ spruce_iron_barrel_block.png
         │        │  ├─ spruce_netherite_barrel_block.png
         │        │  ├─ warped_copper_barrel_block.png
         │        │  ├─ warped_copper_exposed_barrel_block.png
         │        │  ├─ warped_copper_oxidized_barrel_block.png
         │        │  ├─ warped_copper_weathered_barrel_block.png
         │        │  ├─ warped_gold_barrel_block.png
         │        │  ├─ warped_iron_barrel_block.png
         │        │  └─ warped_netherite_barrel_block.png
         │        └─ item
         │           ├─ acacia_copper_barrel.png
         │           ├─ acacia_copper_exposed_barrel.png
         │           ├─ acacia_copper_oxidized_barrel.png
         │           ├─ acacia_copper_weathered_barrel.png
         │           ├─ acacia_gold_barrel.png
         │           ├─ acacia_iron_barrel.png
         │           ├─ acacia_netherite_barrel.png
         │           ├─ bamboo_copper_barrel.png
         │           ├─ bamboo_copper_exposed_barrel.png
         │           ├─ bamboo_copper_oxidized_barrel.png
         │           ├─ bamboo_copper_weathered_barrel.png
         │           ├─ bamboo_gold_barrel.png
         │           ├─ bamboo_iron_barrel.png
         │           ├─ bamboo_netherite_barrel.png
         │           ├─ big_acacia_black_stained_glass_flask.png
         │           ├─ big_acacia_blue_stained_glass_flask.png
         │           ├─ big_acacia_brown_stained_glass_flask.png
         │           ├─ big_acacia_cyan_stained_glass_flask.png
         │           ├─ big_acacia_glass_flask.png
         │           ├─ big_acacia_gray_stained_glass_flask.png
         │           ├─ big_acacia_green_stained_glass_flask.png
         │           ├─ big_acacia_light_blue_stained_glass_flask.png
         │           ├─ big_acacia_light_gray_stained_glass_flask.png
         │           ├─ big_acacia_lime_stained_glass_flask.png
         │           ├─ big_acacia_magenta_stained_glass_flask.png
         │           ├─ big_acacia_orange_stained_glass_flask.png
         │           ├─ big_acacia_pink_stained_glass_flask.png
         │           ├─ big_acacia_purple_stained_glass_flask.png
         │           ├─ big_acacia_red_stained_glass_flask.png
         │           ├─ big_acacia_tinted_glass_flask.png
         │           ├─ big_acacia_white_stained_glass_flask.png
         │           ├─ big_acacia_yellow_stained_glass_flask.png
         │           ├─ big_bamboo_black_stained_glass_flask.png
         │           ├─ big_bamboo_blue_stained_glass_flask.png
         │           ├─ big_bamboo_brown_stained_glass_flask.png
         │           ├─ big_bamboo_cyan_stained_glass_flask.png
         │           ├─ big_bamboo_glass_flask.png
         │           ├─ big_bamboo_gray_stained_glass_flask.png
         │           ├─ big_bamboo_green_stained_glass_flask.png
         │           ├─ big_bamboo_light_blue_stained_glass_flask.png
         │           ├─ big_bamboo_light_gray_stained_glass_flask.png
         │           ├─ big_bamboo_lime_stained_glass_flask.png
         │           ├─ big_bamboo_magenta_stained_glass_flask.png
         │           ├─ big_bamboo_orange_stained_glass_flask.png
         │           ├─ big_bamboo_pink_stained_glass_flask.png
         │           ├─ big_bamboo_purple_stained_glass_flask.png
         │           ├─ big_bamboo_red_stained_glass_flask.png
         │           ├─ big_bamboo_tinted_glass_flask.png
         │           ├─ big_bamboo_white_stained_glass_flask.png
         │           ├─ big_bamboo_yellow_stained_glass_flask.png
         │           ├─ big_birch_black_stained_glass_flask.png
         │           ├─ big_birch_blue_stained_glass_flask.png
         │           ├─ big_birch_brown_stained_glass_flask.png
         │           ├─ big_birch_cyan_stained_glass_flask.png
         │           ├─ big_birch_glass_flask.png
         │           ├─ big_birch_gray_stained_glass_flask.png
         │           ├─ big_birch_green_stained_glass_flask.png
         │           ├─ big_birch_light_blue_stained_glass_flask.png
         │           ├─ big_birch_light_gray_stained_glass_flask.png
         │           ├─ big_birch_lime_stained_glass_flask.png
         │           ├─ big_birch_magenta_stained_glass_flask.png
         │           ├─ big_birch_orange_stained_glass_flask.png
         │           ├─ big_birch_pink_stained_glass_flask.png
         │           ├─ big_birch_purple_stained_glass_flask.png
         │           ├─ big_birch_red_stained_glass_flask.png
         │           ├─ big_birch_tinted_glass_flask.png
         │           ├─ big_birch_white_stained_glass_flask.png
         │           ├─ big_birch_yellow_stained_glass_flask.png
         │           ├─ big_cherry_black_stained_glass_flask.png
         │           ├─ big_cherry_blue_stained_glass_flask.png
         │           ├─ big_cherry_brown_stained_glass_flask.png
         │           ├─ big_cherry_cyan_stained_glass_flask.png
         │           ├─ big_cherry_glass_flask.png
         │           ├─ big_cherry_gray_stained_glass_flask.png
         │           ├─ big_cherry_green_stained_glass_flask.png
         │           ├─ big_cherry_light_blue_stained_glass_flask.png
         │           ├─ big_cherry_light_gray_stained_glass_flask.png
         │           ├─ big_cherry_lime_stained_glass_flask.png
         │           ├─ big_cherry_magenta_stained_glass_flask.png
         │           ├─ big_cherry_orange_stained_glass_flask.png
         │           ├─ big_cherry_pink_stained_glass_flask.png
         │           ├─ big_cherry_purple_stained_glass_flask.png
         │           ├─ big_cherry_red_stained_glass_flask.png
         │           ├─ big_cherry_tinted_glass_flask.png
         │           ├─ big_cherry_white_stained_glass_flask.png
         │           ├─ big_cherry_yellow_stained_glass_flask.png
         │           ├─ big_crimson_black_stained_glass_flask.png
         │           ├─ big_crimson_blue_stained_glass_flask.png
         │           ├─ big_crimson_brown_stained_glass_flask.png
         │           ├─ big_crimson_cyan_stained_glass_flask.png
         │           ├─ big_crimson_glass_flask.png
         │           ├─ big_crimson_gray_stained_glass_flask.png
         │           ├─ big_crimson_green_stained_glass_flask.png
         │           ├─ big_crimson_light_blue_stained_glass_flask.png
         │           ├─ big_crimson_light_gray_stained_glass_flask.png
         │           ├─ big_crimson_lime_stained_glass_flask.png
         │           ├─ big_crimson_magenta_stained_glass_flask.png
         │           ├─ big_crimson_orange_stained_glass_flask.png
         │           ├─ big_crimson_pink_stained_glass_flask.png
         │           ├─ big_crimson_purple_stained_glass_flask.png
         │           ├─ big_crimson_red_stained_glass_flask.png
         │           ├─ big_crimson_tinted_glass_flask.png
         │           ├─ big_crimson_white_stained_glass_flask.png
         │           ├─ big_crimson_yellow_stained_glass_flask.png
         │           ├─ big_dark_oak_black_stained_glass_flask.png
         │           ├─ big_dark_oak_blue_stained_glass_flask.png
         │           ├─ big_dark_oak_brown_stained_glass_flask.png
         │           ├─ big_dark_oak_cyan_stained_glass_flask.png
         │           ├─ big_dark_oak_glass_flask.png
         │           ├─ big_dark_oak_gray_stained_glass_flask.png
         │           ├─ big_dark_oak_green_stained_glass_flask.png
         │           ├─ big_dark_oak_light_blue_stained_glass_flask.png
         │           ├─ big_dark_oak_light_gray_stained_glass_flask.png
         │           ├─ big_dark_oak_lime_stained_glass_flask.png
         │           ├─ big_dark_oak_magenta_stained_glass_flask.png
         │           ├─ big_dark_oak_orange_stained_glass_flask.png
         │           ├─ big_dark_oak_pink_stained_glass_flask.png
         │           ├─ big_dark_oak_purple_stained_glass_flask.png
         │           ├─ big_dark_oak_red_stained_glass_flask.png
         │           ├─ big_dark_oak_tinted_glass_flask.png
         │           ├─ big_dark_oak_white_stained_glass_flask.png
         │           ├─ big_dark_oak_yellow_stained_glass_flask.png
         │           ├─ big_jungle_black_stained_glass_flask.png
         │           ├─ big_jungle_blue_stained_glass_flask.png
         │           ├─ big_jungle_brown_stained_glass_flask.png
         │           ├─ big_jungle_cyan_stained_glass_flask.png
         │           ├─ big_jungle_glass_flask.png
         │           ├─ big_jungle_gray_stained_glass_flask.png
         │           ├─ big_jungle_green_stained_glass_flask.png
         │           ├─ big_jungle_light_blue_stained_glass_flask.png
         │           ├─ big_jungle_light_gray_stained_glass_flask.png
         │           ├─ big_jungle_lime_stained_glass_flask.png
         │           ├─ big_jungle_magenta_stained_glass_flask.png
         │           ├─ big_jungle_orange_stained_glass_flask.png
         │           ├─ big_jungle_pink_stained_glass_flask.png
         │           ├─ big_jungle_purple_stained_glass_flask.png
         │           ├─ big_jungle_red_stained_glass_flask.png
         │           ├─ big_jungle_tinted_glass_flask.png
         │           ├─ big_jungle_white_stained_glass_flask.png
         │           ├─ big_jungle_yellow_stained_glass_flask.png
         │           ├─ big_mangrove_black_stained_glass_flask.png
         │           ├─ big_mangrove_blue_stained_glass_flask.png
         │           ├─ big_mangrove_brown_stained_glass_flask.png
         │           ├─ big_mangrove_cyan_stained_glass_flask.png
         │           ├─ big_mangrove_glass_flask.png
         │           ├─ big_mangrove_gray_stained_glass_flask.png
         │           ├─ big_mangrove_green_stained_glass_flask.png
         │           ├─ big_mangrove_light_blue_stained_glass_flask.png
         │           ├─ big_mangrove_light_gray_stained_glass_flask.png
         │           ├─ big_mangrove_lime_stained_glass_flask.png
         │           ├─ big_mangrove_magenta_stained_glass_flask.png
         │           ├─ big_mangrove_orange_stained_glass_flask.png
         │           ├─ big_mangrove_pink_stained_glass_flask.png
         │           ├─ big_mangrove_purple_stained_glass_flask.png
         │           ├─ big_mangrove_red_stained_glass_flask.png
         │           ├─ big_mangrove_tinted_glass_flask.png
         │           ├─ big_mangrove_white_stained_glass_flask.png
         │           ├─ big_mangrove_yellow_stained_glass_flask.png
         │           ├─ big_oak_black_stained_glass_flask.png
         │           ├─ big_oak_blue_stained_glass_flask.png
         │           ├─ big_oak_brown_stained_glass_flask.png
         │           ├─ big_oak_cyan_stained_glass_flask.png
         │           ├─ big_oak_glass_flask.png
         │           ├─ big_oak_gray_stained_glass_flask.png
         │           ├─ big_oak_green_stained_glass_flask.png
         │           ├─ big_oak_light_blue_stained_glass_flask.png
         │           ├─ big_oak_light_gray_stained_glass_flask.png
         │           ├─ big_oak_lime_stained_glass_flask.png
         │           ├─ big_oak_magenta_stained_glass_flask.png
         │           ├─ big_oak_orange_stained_glass_flask.png
         │           ├─ big_oak_pink_stained_glass_flask.png
         │           ├─ big_oak_purple_stained_glass_flask.png
         │           ├─ big_oak_red_stained_glass_flask.png
         │           ├─ big_oak_tinted_glass_flask.png
         │           ├─ big_oak_white_stained_glass_flask.png
         │           ├─ big_oak_yellow_stained_glass_flask.png
         │           ├─ big_pale_oak_black_stained_glass_flask.png
         │           ├─ big_pale_oak_blue_stained_glass_flask.png
         │           ├─ big_pale_oak_brown_stained_glass_flask.png
         │           ├─ big_pale_oak_cyan_stained_glass_flask.png
         │           ├─ big_pale_oak_glass_flask.png
         │           ├─ big_pale_oak_gray_stained_glass_flask.png
         │           ├─ big_pale_oak_green_stained_glass_flask.png
         │           ├─ big_pale_oak_light_blue_stained_glass_flask.png
         │           ├─ big_pale_oak_light_gray_stained_glass_flask.png
         │           ├─ big_pale_oak_lime_stained_glass_flask.png
         │           ├─ big_pale_oak_magenta_stained_glass_flask.png
         │           ├─ big_pale_oak_orange_stained_glass_flask.png
         │           ├─ big_pale_oak_pink_stained_glass_flask.png
         │           ├─ big_pale_oak_purple_stained_glass_flask.png
         │           ├─ big_pale_oak_red_stained_glass_flask.png
         │           ├─ big_pale_oak_tinted_glass_flask.png
         │           ├─ big_pale_oak_white_stained_glass_flask.png
         │           ├─ big_pale_oak_yellow_stained_glass_flask.png
         │           ├─ big_spruce_black_stained_glass_flask.png
         │           ├─ big_spruce_blue_stained_glass_flask.png
         │           ├─ big_spruce_brown_stained_glass_flask.png
         │           ├─ big_spruce_cyan_stained_glass_flask.png
         │           ├─ big_spruce_glass_flask.png
         │           ├─ big_spruce_gray_stained_glass_flask.png
         │           ├─ big_spruce_green_stained_glass_flask.png
         │           ├─ big_spruce_light_blue_stained_glass_flask.png
         │           ├─ big_spruce_light_gray_stained_glass_flask.png
         │           ├─ big_spruce_lime_stained_glass_flask.png
         │           ├─ big_spruce_magenta_stained_glass_flask.png
         │           ├─ big_spruce_orange_stained_glass_flask.png
         │           ├─ big_spruce_pink_stained_glass_flask.png
         │           ├─ big_spruce_purple_stained_glass_flask.png
         │           ├─ big_spruce_red_stained_glass_flask.png
         │           ├─ big_spruce_tinted_glass_flask.png
         │           ├─ big_spruce_white_stained_glass_flask.png
         │           ├─ big_spruce_yellow_stained_glass_flask.png
         │           ├─ big_warped_black_stained_glass_flask.png
         │           ├─ big_warped_blue_stained_glass_flask.png
         │           ├─ big_warped_brown_stained_glass_flask.png
         │           ├─ big_warped_cyan_stained_glass_flask.png
         │           ├─ big_warped_glass_flask.png
         │           ├─ big_warped_gray_stained_glass_flask.png
         │           ├─ big_warped_green_stained_glass_flask.png
         │           ├─ big_warped_light_blue_stained_glass_flask.png
         │           ├─ big_warped_light_gray_stained_glass_flask.png
         │           ├─ big_warped_lime_stained_glass_flask.png
         │           ├─ big_warped_magenta_stained_glass_flask.png
         │           ├─ big_warped_orange_stained_glass_flask.png
         │           ├─ big_warped_pink_stained_glass_flask.png
         │           ├─ big_warped_purple_stained_glass_flask.png
         │           ├─ big_warped_red_stained_glass_flask.png
         │           ├─ big_warped_tinted_glass_flask.png
         │           ├─ big_warped_white_stained_glass_flask.png
         │           ├─ big_warped_yellow_stained_glass_flask.png
         │           ├─ birch_copper_barrel.png
         │           ├─ birch_copper_exposed_barrel.png
         │           ├─ birch_copper_oxidized_barrel.png
         │           ├─ birch_copper_weathered_barrel.png
         │           ├─ birch_gold_barrel.png
         │           ├─ birch_iron_barrel.png
         │           ├─ birch_netherite_barrel.png
         │           ├─ cherry_copper_barrel.png
         │           ├─ cherry_copper_exposed_barrel.png
         │           ├─ cherry_copper_oxidized_barrel.png
         │           ├─ cherry_copper_weathered_barrel.png
         │           ├─ cherry_gold_barrel.png
         │           ├─ cherry_iron_barrel.png
         │           ├─ cherry_netherite_barrel.png
         │           ├─ copper_exposed_keg.png
         │           ├─ copper_keg.png
         │           ├─ copper_oxidized_keg.png
         │           ├─ copper_weathered_keg.png
         │           ├─ crimson_copper_barrel.png
         │           ├─ crimson_copper_exposed_barrel.png
         │           ├─ crimson_copper_oxidized_barrel.png
         │           ├─ crimson_copper_weathered_barrel.png
         │           ├─ crimson_gold_barrel.png
         │           ├─ crimson_iron_barrel.png
         │           ├─ crimson_netherite_barrel.png
         │           ├─ dark_oak_copper_barrel.png
         │           ├─ dark_oak_copper_exposed_barrel.png
         │           ├─ dark_oak_copper_oxidized_barrel.png
         │           ├─ dark_oak_copper_weathered_barrel.png
         │           ├─ dark_oak_gold_barrel.png
         │           ├─ dark_oak_iron_barrel.png
         │           ├─ dark_oak_netherite_barrel.png
         │           ├─ gold_keg.png
         │           ├─ iron_keg.png
         │           ├─ jungle_copper_barrel.png
         │           ├─ jungle_copper_exposed_barrel.png
         │           ├─ jungle_copper_oxidized_barrel.png
         │           ├─ jungle_copper_weathered_barrel.png
         │           ├─ jungle_gold_barrel.png
         │           ├─ jungle_iron_barrel.png
         │           ├─ jungle_netherite_barrel.png
         │           ├─ mangrove_copper_barrel.png
         │           ├─ mangrove_copper_exposed_barrel.png
         │           ├─ mangrove_copper_oxidized_barrel.png
         │           ├─ mangrove_copper_weathered_barrel.png
         │           ├─ mangrove_gold_barrel.png
         │           ├─ mangrove_iron_barrel.png
         │           ├─ mangrove_netherite_barrel.png
         │           ├─ medium_acacia_black_stained_glass_flask.png
         │           ├─ medium_acacia_blue_stained_glass_flask.png
         │           ├─ medium_acacia_brown_stained_glass_flask.png
         │           ├─ medium_acacia_cyan_stained_glass_flask.png
         │           ├─ medium_acacia_glass_flask.png
         │           ├─ medium_acacia_gray_stained_glass_flask.png
         │           ├─ medium_acacia_green_stained_glass_flask.png
         │           ├─ medium_acacia_light_blue_stained_glass_flask.png
         │           ├─ medium_acacia_light_gray_stained_glass_flask.png
         │           ├─ medium_acacia_lime_stained_glass_flask.png
         │           ├─ medium_acacia_magenta_stained_glass_flask.png
         │           ├─ medium_acacia_orange_stained_glass_flask.png
         │           ├─ medium_acacia_pink_stained_glass_flask.png
         │           ├─ medium_acacia_purple_stained_glass_flask.png
         │           ├─ medium_acacia_red_stained_glass_flask.png
         │           ├─ medium_acacia_tinted_glass_flask.png
         │           ├─ medium_acacia_white_stained_glass_flask.png
         │           ├─ medium_acacia_yellow_stained_glass_flask.png
         │           ├─ medium_bamboo_black_stained_glass_flask.png
         │           ├─ medium_bamboo_blue_stained_glass_flask.png
         │           ├─ medium_bamboo_brown_stained_glass_flask.png
         │           ├─ medium_bamboo_cyan_stained_glass_flask.png
         │           ├─ medium_bamboo_glass_flask.png
         │           ├─ medium_bamboo_gray_stained_glass_flask.png
         │           ├─ medium_bamboo_green_stained_glass_flask.png
         │           ├─ medium_bamboo_light_blue_stained_glass_flask.png
         │           ├─ medium_bamboo_light_gray_stained_glass_flask.png
         │           ├─ medium_bamboo_lime_stained_glass_flask.png
         │           ├─ medium_bamboo_magenta_stained_glass_flask.png
         │           ├─ medium_bamboo_orange_stained_glass_flask.png
         │           ├─ medium_bamboo_pink_stained_glass_flask.png
         │           ├─ medium_bamboo_purple_stained_glass_flask.png
         │           ├─ medium_bamboo_red_stained_glass_flask.png
         │           ├─ medium_bamboo_tinted_glass_flask.png
         │           ├─ medium_bamboo_white_stained_glass_flask.png
         │           ├─ medium_bamboo_yellow_stained_glass_flask.png
         │           ├─ medium_birch_black_stained_glass_flask.png
         │           ├─ medium_birch_blue_stained_glass_flask.png
         │           ├─ medium_birch_brown_stained_glass_flask.png
         │           ├─ medium_birch_cyan_stained_glass_flask.png
         │           ├─ medium_birch_glass_flask.png
         │           ├─ medium_birch_gray_stained_glass_flask.png
         │           ├─ medium_birch_green_stained_glass_flask.png
         │           ├─ medium_birch_light_blue_stained_glass_flask.png
         │           ├─ medium_birch_light_gray_stained_glass_flask.png
         │           ├─ medium_birch_lime_stained_glass_flask.png
         │           ├─ medium_birch_magenta_stained_glass_flask.png
         │           ├─ medium_birch_orange_stained_glass_flask.png
         │           ├─ medium_birch_pink_stained_glass_flask.png
         │           ├─ medium_birch_purple_stained_glass_flask.png
         │           ├─ medium_birch_red_stained_glass_flask.png
         │           ├─ medium_birch_tinted_glass_flask.png
         │           ├─ medium_birch_white_stained_glass_flask.png
         │           ├─ medium_birch_yellow_stained_glass_flask.png
         │           ├─ medium_cherry_black_stained_glass_flask.png
         │           ├─ medium_cherry_blue_stained_glass_flask.png
         │           ├─ medium_cherry_brown_stained_glass_flask.png
         │           ├─ medium_cherry_cyan_stained_glass_flask.png
         │           ├─ medium_cherry_glass_flask.png
         │           ├─ medium_cherry_gray_stained_glass_flask.png
         │           ├─ medium_cherry_green_stained_glass_flask.png
         │           ├─ medium_cherry_light_blue_stained_glass_flask.png
         │           ├─ medium_cherry_light_gray_stained_glass_flask.png
         │           ├─ medium_cherry_lime_stained_glass_flask.png
         │           ├─ medium_cherry_magenta_stained_glass_flask.png
         │           ├─ medium_cherry_orange_stained_glass_flask.png
         │           ├─ medium_cherry_pink_stained_glass_flask.png
         │           ├─ medium_cherry_purple_stained_glass_flask.png
         │           ├─ medium_cherry_red_stained_glass_flask.png
         │           ├─ medium_cherry_tinted_glass_flask.png
         │           ├─ medium_cherry_white_stained_glass_flask.png
         │           ├─ medium_cherry_yellow_stained_glass_flask.png
         │           ├─ medium_crimson_black_stained_glass_flask.png
         │           ├─ medium_crimson_blue_stained_glass_flask.png
         │           ├─ medium_crimson_brown_stained_glass_flask.png
         │           ├─ medium_crimson_cyan_stained_glass_flask.png
         │           ├─ medium_crimson_glass_flask.png
         │           ├─ medium_crimson_gray_stained_glass_flask.png
         │           ├─ medium_crimson_green_stained_glass_flask.png
         │           ├─ medium_crimson_light_blue_stained_glass_flask.png
         │           ├─ medium_crimson_light_gray_stained_glass_flask.png
         │           ├─ medium_crimson_lime_stained_glass_flask.png
         │           ├─ medium_crimson_magenta_stained_glass_flask.png
         │           ├─ medium_crimson_orange_stained_glass_flask.png
         │           ├─ medium_crimson_pink_stained_glass_flask.png
         │           ├─ medium_crimson_purple_stained_glass_flask.png
         │           ├─ medium_crimson_red_stained_glass_flask.png
         │           ├─ medium_crimson_tinted_glass_flask.png
         │           ├─ medium_crimson_white_stained_glass_flask.png
         │           ├─ medium_crimson_yellow_stained_glass_flask.png
         │           ├─ medium_dark_oak_black_stained_glass_flask.png
         │           ├─ medium_dark_oak_blue_stained_glass_flask.png
         │           ├─ medium_dark_oak_brown_stained_glass_flask.png
         │           ├─ medium_dark_oak_cyan_stained_glass_flask.png
         │           ├─ medium_dark_oak_glass_flask.png
         │           ├─ medium_dark_oak_gray_stained_glass_flask.png
         │           ├─ medium_dark_oak_green_stained_glass_flask.png
         │           ├─ medium_dark_oak_light_blue_stained_glass_flask.png
         │           ├─ medium_dark_oak_light_gray_stained_glass_flask.png
         │           ├─ medium_dark_oak_lime_stained_glass_flask.png
         │           ├─ medium_dark_oak_magenta_stained_glass_flask.png
         │           ├─ medium_dark_oak_orange_stained_glass_flask.png
         │           ├─ medium_dark_oak_pink_stained_glass_flask.png
         │           ├─ medium_dark_oak_purple_stained_glass_flask.png
         │           ├─ medium_dark_oak_red_stained_glass_flask.png
         │           ├─ medium_dark_oak_tinted_glass_flask.png
         │           ├─ medium_dark_oak_white_stained_glass_flask.png
         │           ├─ medium_dark_oak_yellow_stained_glass_flask.png
         │           ├─ medium_jungle_black_stained_glass_flask.png
         │           ├─ medium_jungle_blue_stained_glass_flask.png
         │           ├─ medium_jungle_brown_stained_glass_flask.png
         │           ├─ medium_jungle_cyan_stained_glass_flask.png
         │           ├─ medium_jungle_glass_flask.png
         │           ├─ medium_jungle_gray_stained_glass_flask.png
         │           ├─ medium_jungle_green_stained_glass_flask.png
         │           ├─ medium_jungle_light_blue_stained_glass_flask.png
         │           ├─ medium_jungle_light_gray_stained_glass_flask.png
         │           ├─ medium_jungle_lime_stained_glass_flask.png
         │           ├─ medium_jungle_magenta_stained_glass_flask.png
         │           ├─ medium_jungle_orange_stained_glass_flask.png
         │           ├─ medium_jungle_pink_stained_glass_flask.png
         │           ├─ medium_jungle_purple_stained_glass_flask.png
         │           ├─ medium_jungle_red_stained_glass_flask.png
         │           ├─ medium_jungle_tinted_glass_flask.png
         │           ├─ medium_jungle_white_stained_glass_flask.png
         │           ├─ medium_jungle_yellow_stained_glass_flask.png
         │           ├─ medium_mangrove_black_stained_glass_flask.png
         │           ├─ medium_mangrove_blue_stained_glass_flask.png
         │           ├─ medium_mangrove_brown_stained_glass_flask.png
         │           ├─ medium_mangrove_cyan_stained_glass_flask.png
         │           ├─ medium_mangrove_glass_flask.png
         │           ├─ medium_mangrove_gray_stained_glass_flask.png
         │           ├─ medium_mangrove_green_stained_glass_flask.png
         │           ├─ medium_mangrove_light_blue_stained_glass_flask.png
         │           ├─ medium_mangrove_light_gray_stained_glass_flask.png
         │           ├─ medium_mangrove_lime_stained_glass_flask.png
         │           ├─ medium_mangrove_magenta_stained_glass_flask.png
         │           ├─ medium_mangrove_orange_stained_glass_flask.png
         │           ├─ medium_mangrove_pink_stained_glass_flask.png
         │           ├─ medium_mangrove_purple_stained_glass_flask.png
         │           ├─ medium_mangrove_red_stained_glass_flask.png
         │           ├─ medium_mangrove_tinted_glass_flask.png
         │           ├─ medium_mangrove_white_stained_glass_flask.png
         │           ├─ medium_mangrove_yellow_stained_glass_flask.png
         │           ├─ medium_oak_black_stained_glass_flask.png
         │           ├─ medium_oak_blue_stained_glass_flask.png
         │           ├─ medium_oak_brown_stained_glass_flask.png
         │           ├─ medium_oak_cyan_stained_glass_flask.png
         │           ├─ medium_oak_glass_flask.png
         │           ├─ medium_oak_gray_stained_glass_flask.png
         │           ├─ medium_oak_green_stained_glass_flask.png
         │           ├─ medium_oak_light_blue_stained_glass_flask.png
         │           ├─ medium_oak_light_gray_stained_glass_flask.png
         │           ├─ medium_oak_lime_stained_glass_flask.png
         │           ├─ medium_oak_magenta_stained_glass_flask.png
         │           ├─ medium_oak_orange_stained_glass_flask.png
         │           ├─ medium_oak_pink_stained_glass_flask.png
         │           ├─ medium_oak_purple_stained_glass_flask.png
         │           ├─ medium_oak_red_stained_glass_flask.png
         │           ├─ medium_oak_tinted_glass_flask.png
         │           ├─ medium_oak_white_stained_glass_flask.png
         │           ├─ medium_oak_yellow_stained_glass_flask.png
         │           ├─ medium_pale_oak_black_stained_glass_flask.png
         │           ├─ medium_pale_oak_blue_stained_glass_flask.png
         │           ├─ medium_pale_oak_brown_stained_glass_flask.png
         │           ├─ medium_pale_oak_cyan_stained_glass_flask.png
         │           ├─ medium_pale_oak_glass_flask.png
         │           ├─ medium_pale_oak_gray_stained_glass_flask.png
         │           ├─ medium_pale_oak_green_stained_glass_flask.png
         │           ├─ medium_pale_oak_light_blue_stained_glass_flask.png
         │           ├─ medium_pale_oak_light_gray_stained_glass_flask.png
         │           ├─ medium_pale_oak_lime_stained_glass_flask.png
         │           ├─ medium_pale_oak_magenta_stained_glass_flask.png
         │           ├─ medium_pale_oak_orange_stained_glass_flask.png
         │           ├─ medium_pale_oak_pink_stained_glass_flask.png
         │           ├─ medium_pale_oak_purple_stained_glass_flask.png
         │           ├─ medium_pale_oak_red_stained_glass_flask.png
         │           ├─ medium_pale_oak_tinted_glass_flask.png
         │           ├─ medium_pale_oak_white_stained_glass_flask.png
         │           ├─ medium_pale_oak_yellow_stained_glass_flask.png
         │           ├─ medium_spruce_black_stained_glass_flask.png
         │           ├─ medium_spruce_blue_stained_glass_flask.png
         │           ├─ medium_spruce_brown_stained_glass_flask.png
         │           ├─ medium_spruce_cyan_stained_glass_flask.png
         │           ├─ medium_spruce_glass_flask.png
         │           ├─ medium_spruce_gray_stained_glass_flask.png
         │           ├─ medium_spruce_green_stained_glass_flask.png
         │           ├─ medium_spruce_light_blue_stained_glass_flask.png
         │           ├─ medium_spruce_light_gray_stained_glass_flask.png
         │           ├─ medium_spruce_lime_stained_glass_flask.png
         │           ├─ medium_spruce_magenta_stained_glass_flask.png
         │           ├─ medium_spruce_orange_stained_glass_flask.png
         │           ├─ medium_spruce_pink_stained_glass_flask.png
         │           ├─ medium_spruce_purple_stained_glass_flask.png
         │           ├─ medium_spruce_red_stained_glass_flask.png
         │           ├─ medium_spruce_tinted_glass_flask.png
         │           ├─ medium_spruce_white_stained_glass_flask.png
         │           ├─ medium_spruce_yellow_stained_glass_flask.png
         │           ├─ medium_warped_black_stained_glass_flask.png
         │           ├─ medium_warped_blue_stained_glass_flask.png
         │           ├─ medium_warped_brown_stained_glass_flask.png
         │           ├─ medium_warped_cyan_stained_glass_flask.png
         │           ├─ medium_warped_glass_flask.png
         │           ├─ medium_warped_gray_stained_glass_flask.png
         │           ├─ medium_warped_green_stained_glass_flask.png
         │           ├─ medium_warped_light_blue_stained_glass_flask.png
         │           ├─ medium_warped_light_gray_stained_glass_flask.png
         │           ├─ medium_warped_lime_stained_glass_flask.png
         │           ├─ medium_warped_magenta_stained_glass_flask.png
         │           ├─ medium_warped_orange_stained_glass_flask.png
         │           ├─ medium_warped_pink_stained_glass_flask.png
         │           ├─ medium_warped_purple_stained_glass_flask.png
         │           ├─ medium_warped_red_stained_glass_flask.png
         │           ├─ medium_warped_tinted_glass_flask.png
         │           ├─ medium_warped_white_stained_glass_flask.png
         │           ├─ medium_warped_yellow_stained_glass_flask.png
         │           ├─ netherite_keg.png
         │           ├─ oak_copper_barrel.png
         │           ├─ oak_copper_exposed_barrel.png
         │           ├─ oak_copper_oxidized_barrel.png
         │           ├─ oak_copper_weathered_barrel.png
         │           ├─ oak_gold_barrel.png
         │           ├─ oak_iron_barrel.png
         │           ├─ oak_netherite_barrel.png
         │           ├─ pale_oak_copper_barrel.png
         │           ├─ pale_oak_copper_exposed_barrel.png
         │           ├─ pale_oak_copper_oxidized_barrel.png
         │           ├─ pale_oak_copper_weathered_barrel.png
         │           ├─ pale_oak_gold_barrel.png
         │           ├─ pale_oak_iron_barrel.png
         │           ├─ pale_oak_netherite_barrel.png
         │           ├─ small_acacia_black_stained_glass_flask.png
         │           ├─ small_acacia_blue_stained_glass_flask.png
         │           ├─ small_acacia_brown_stained_glass_flask.png
         │           ├─ small_acacia_cyan_stained_glass_flask.png
         │           ├─ small_acacia_glass_flask.png
         │           ├─ small_acacia_gray_stained_glass_flask.png
         │           ├─ small_acacia_green_stained_glass_flask.png
         │           ├─ small_acacia_light_blue_stained_glass_flask.png
         │           ├─ small_acacia_light_gray_stained_glass_flask.png
         │           ├─ small_acacia_lime_stained_glass_flask.png
         │           ├─ small_acacia_magenta_stained_glass_flask.png
         │           ├─ small_acacia_orange_stained_glass_flask.png
         │           ├─ small_acacia_pink_stained_glass_flask.png
         │           ├─ small_acacia_purple_stained_glass_flask.png
         │           ├─ small_acacia_red_stained_glass_flask.png
         │           ├─ small_acacia_tinted_glass_flask.png
         │           ├─ small_acacia_white_stained_glass_flask.png
         │           ├─ small_acacia_yellow_stained_glass_flask.png
         │           ├─ small_bamboo_black_stained_glass_flask.png
         │           ├─ small_bamboo_blue_stained_glass_flask.png
         │           ├─ small_bamboo_brown_stained_glass_flask.png
         │           ├─ small_bamboo_cyan_stained_glass_flask.png
         │           ├─ small_bamboo_glass_flask.png
         │           ├─ small_bamboo_gray_stained_glass_flask.png
         │           ├─ small_bamboo_green_stained_glass_flask.png
         │           ├─ small_bamboo_light_blue_stained_glass_flask.png
         │           ├─ small_bamboo_light_gray_stained_glass_flask.png
         │           ├─ small_bamboo_lime_stained_glass_flask.png
         │           ├─ small_bamboo_magenta_stained_glass_flask.png
         │           ├─ small_bamboo_orange_stained_glass_flask.png
         │           ├─ small_bamboo_pink_stained_glass_flask.png
         │           ├─ small_bamboo_purple_stained_glass_flask.png
         │           ├─ small_bamboo_red_stained_glass_flask.png
         │           ├─ small_bamboo_tinted_glass_flask.png
         │           ├─ small_bamboo_white_stained_glass_flask.png
         │           ├─ small_bamboo_yellow_stained_glass_flask.png
         │           ├─ small_birch_black_stained_glass_flask.png
         │           ├─ small_birch_blue_stained_glass_flask.png
         │           ├─ small_birch_brown_stained_glass_flask.png
         │           ├─ small_birch_cyan_stained_glass_flask.png
         │           ├─ small_birch_glass_flask.png
         │           ├─ small_birch_gray_stained_glass_flask.png
         │           ├─ small_birch_green_stained_glass_flask.png
         │           ├─ small_birch_light_blue_stained_glass_flask.png
         │           ├─ small_birch_light_gray_stained_glass_flask.png
         │           ├─ small_birch_lime_stained_glass_flask.png
         │           ├─ small_birch_magenta_stained_glass_flask.png
         │           ├─ small_birch_orange_stained_glass_flask.png
         │           ├─ small_birch_pink_stained_glass_flask.png
         │           ├─ small_birch_purple_stained_glass_flask.png
         │           ├─ small_birch_red_stained_glass_flask.png
         │           ├─ small_birch_tinted_glass_flask.png
         │           ├─ small_birch_white_stained_glass_flask.png
         │           ├─ small_birch_yellow_stained_glass_flask.png
         │           ├─ small_cherry_black_stained_glass_flask.png
         │           ├─ small_cherry_blue_stained_glass_flask.png
         │           ├─ small_cherry_brown_stained_glass_flask.png
         │           ├─ small_cherry_cyan_stained_glass_flask.png
         │           ├─ small_cherry_glass_flask.png
         │           ├─ small_cherry_gray_stained_glass_flask.png
         │           ├─ small_cherry_green_stained_glass_flask.png
         │           ├─ small_cherry_light_blue_stained_glass_flask.png
         │           ├─ small_cherry_light_gray_stained_glass_flask.png
         │           ├─ small_cherry_lime_stained_glass_flask.png
         │           ├─ small_cherry_magenta_stained_glass_flask.png
         │           ├─ small_cherry_orange_stained_glass_flask.png
         │           ├─ small_cherry_pink_stained_glass_flask.png
         │           ├─ small_cherry_purple_stained_glass_flask.png
         │           ├─ small_cherry_red_stained_glass_flask.png
         │           ├─ small_cherry_tinted_glass_flask.png
         │           ├─ small_cherry_white_stained_glass_flask.png
         │           ├─ small_cherry_yellow_stained_glass_flask.png
         │           ├─ small_crimson_black_stained_glass_flask.png
         │           ├─ small_crimson_blue_stained_glass_flask.png
         │           ├─ small_crimson_brown_stained_glass_flask.png
         │           ├─ small_crimson_cyan_stained_glass_flask.png
         │           ├─ small_crimson_glass_flask.png
         │           ├─ small_crimson_gray_stained_glass_flask.png
         │           ├─ small_crimson_green_stained_glass_flask.png
         │           ├─ small_crimson_light_blue_stained_glass_flask.png
         │           ├─ small_crimson_light_gray_stained_glass_flask.png
         │           ├─ small_crimson_lime_stained_glass_flask.png
         │           ├─ small_crimson_magenta_stained_glass_flask.png
         │           ├─ small_crimson_orange_stained_glass_flask.png
         │           ├─ small_crimson_pink_stained_glass_flask.png
         │           ├─ small_crimson_purple_stained_glass_flask.png
         │           ├─ small_crimson_red_stained_glass_flask.png
         │           ├─ small_crimson_tinted_glass_flask.png
         │           ├─ small_crimson_white_stained_glass_flask.png
         │           ├─ small_crimson_yellow_stained_glass_flask.png
         │           ├─ small_dark_oak_black_stained_glass_flask.png
         │           ├─ small_dark_oak_blue_stained_glass_flask.png
         │           ├─ small_dark_oak_brown_stained_glass_flask.png
         │           ├─ small_dark_oak_cyan_stained_glass_flask.png
         │           ├─ small_dark_oak_glass_flask.png
         │           ├─ small_dark_oak_gray_stained_glass_flask.png
         │           ├─ small_dark_oak_green_stained_glass_flask.png
         │           ├─ small_dark_oak_light_blue_stained_glass_flask.png
         │           ├─ small_dark_oak_light_gray_stained_glass_flask.png
         │           ├─ small_dark_oak_lime_stained_glass_flask.png
         │           ├─ small_dark_oak_magenta_stained_glass_flask.png
         │           ├─ small_dark_oak_orange_stained_glass_flask.png
         │           ├─ small_dark_oak_pink_stained_glass_flask.png
         │           ├─ small_dark_oak_purple_stained_glass_flask.png
         │           ├─ small_dark_oak_red_stained_glass_flask.png
         │           ├─ small_dark_oak_tinted_glass_flask.png
         │           ├─ small_dark_oak_white_stained_glass_flask.png
         │           ├─ small_dark_oak_yellow_stained_glass_flask.png
         │           ├─ small_jungle_black_stained_glass_flask.png
         │           ├─ small_jungle_blue_stained_glass_flask.png
         │           ├─ small_jungle_brown_stained_glass_flask.png
         │           ├─ small_jungle_cyan_stained_glass_flask.png
         │           ├─ small_jungle_glass_flask.png
         │           ├─ small_jungle_gray_stained_glass_flask.png
         │           ├─ small_jungle_green_stained_glass_flask.png
         │           ├─ small_jungle_light_blue_stained_glass_flask.png
         │           ├─ small_jungle_light_gray_stained_glass_flask.png
         │           ├─ small_jungle_lime_stained_glass_flask.png
         │           ├─ small_jungle_magenta_stained_glass_flask.png
         │           ├─ small_jungle_orange_stained_glass_flask.png
         │           ├─ small_jungle_pink_stained_glass_flask.png
         │           ├─ small_jungle_purple_stained_glass_flask.png
         │           ├─ small_jungle_red_stained_glass_flask.png
         │           ├─ small_jungle_tinted_glass_flask.png
         │           ├─ small_jungle_white_stained_glass_flask.png
         │           ├─ small_jungle_yellow_stained_glass_flask.png
         │           ├─ small_mangrove_black_stained_glass_flask.png
         │           ├─ small_mangrove_blue_stained_glass_flask.png
         │           ├─ small_mangrove_brown_stained_glass_flask.png
         │           ├─ small_mangrove_cyan_stained_glass_flask.png
         │           ├─ small_mangrove_glass_flask.png
         │           ├─ small_mangrove_gray_stained_glass_flask.png
         │           ├─ small_mangrove_green_stained_glass_flask.png
         │           ├─ small_mangrove_light_blue_stained_glass_flask.png
         │           ├─ small_mangrove_light_gray_stained_glass_flask.png
         │           ├─ small_mangrove_lime_stained_glass_flask.png
         │           ├─ small_mangrove_magenta_stained_glass_flask.png
         │           ├─ small_mangrove_orange_stained_glass_flask.png
         │           ├─ small_mangrove_pink_stained_glass_flask.png
         │           ├─ small_mangrove_purple_stained_glass_flask.png
         │           ├─ small_mangrove_red_stained_glass_flask.png
         │           ├─ small_mangrove_tinted_glass_flask.png
         │           ├─ small_mangrove_white_stained_glass_flask.png
         │           ├─ small_mangrove_yellow_stained_glass_flask.png
         │           ├─ small_oak_black_stained_glass_flask.png
         │           ├─ small_oak_blue_stained_glass_flask.png
         │           ├─ small_oak_brown_stained_glass_flask.png
         │           ├─ small_oak_cyan_stained_glass_flask.png
         │           ├─ small_oak_glass_flask.png
         │           ├─ small_oak_gray_stained_glass_flask.png
         │           ├─ small_oak_green_stained_glass_flask.png
         │           ├─ small_oak_light_blue_stained_glass_flask.png
         │           ├─ small_oak_light_gray_stained_glass_flask.png
         │           ├─ small_oak_lime_stained_glass_flask.png
         │           ├─ small_oak_magenta_stained_glass_flask.png
         │           ├─ small_oak_orange_stained_glass_flask.png
         │           ├─ small_oak_pink_stained_glass_flask.png
         │           ├─ small_oak_purple_stained_glass_flask.png
         │           ├─ small_oak_red_stained_glass_flask.png
         │           ├─ small_oak_tinted_glass_flask.png
         │           ├─ small_oak_white_stained_glass_flask.png
         │           ├─ small_oak_yellow_stained_glass_flask.png
         │           ├─ small_pale_oak_black_stained_glass_flask.png
         │           ├─ small_pale_oak_blue_stained_glass_flask.png
         │           ├─ small_pale_oak_brown_stained_glass_flask.png
         │           ├─ small_pale_oak_cyan_stained_glass_flask.png
         │           ├─ small_pale_oak_glass_flask.png
         │           ├─ small_pale_oak_gray_stained_glass_flask.png
         │           ├─ small_pale_oak_green_stained_glass_flask.png
         │           ├─ small_pale_oak_light_blue_stained_glass_flask.png
         │           ├─ small_pale_oak_light_gray_stained_glass_flask.png
         │           ├─ small_pale_oak_lime_stained_glass_flask.png
         │           ├─ small_pale_oak_magenta_stained_glass_flask.png
         │           ├─ small_pale_oak_orange_stained_glass_flask.png
         │           ├─ small_pale_oak_pink_stained_glass_flask.png
         │           ├─ small_pale_oak_purple_stained_glass_flask.png
         │           ├─ small_pale_oak_red_stained_glass_flask.png
         │           ├─ small_pale_oak_tinted_glass_flask.png
         │           ├─ small_pale_oak_white_stained_glass_flask.png
         │           ├─ small_pale_oak_yellow_stained_glass_flask.png
         │           ├─ small_spruce_black_stained_glass_flask.png
         │           ├─ small_spruce_blue_stained_glass_flask.png
         │           ├─ small_spruce_brown_stained_glass_flask.png
         │           ├─ small_spruce_cyan_stained_glass_flask.png
         │           ├─ small_spruce_glass_flask.png
         │           ├─ small_spruce_gray_stained_glass_flask.png
         │           ├─ small_spruce_green_stained_glass_flask.png
         │           ├─ small_spruce_light_blue_stained_glass_flask.png
         │           ├─ small_spruce_light_gray_stained_glass_flask.png
         │           ├─ small_spruce_lime_stained_glass_flask.png
         │           ├─ small_spruce_magenta_stained_glass_flask.png
         │           ├─ small_spruce_orange_stained_glass_flask.png
         │           ├─ small_spruce_pink_stained_glass_flask.png
         │           ├─ small_spruce_purple_stained_glass_flask.png
         │           ├─ small_spruce_red_stained_glass_flask.png
         │           ├─ small_spruce_tinted_glass_flask.png
         │           ├─ small_spruce_white_stained_glass_flask.png
         │           ├─ small_spruce_yellow_stained_glass_flask.png
         │           ├─ small_warped_black_stained_glass_flask.png
         │           ├─ small_warped_blue_stained_glass_flask.png
         │           ├─ small_warped_brown_stained_glass_flask.png
         │           ├─ small_warped_cyan_stained_glass_flask.png
         │           ├─ small_warped_glass_flask.png
         │           ├─ small_warped_gray_stained_glass_flask.png
         │           ├─ small_warped_green_stained_glass_flask.png
         │           ├─ small_warped_light_blue_stained_glass_flask.png
         │           ├─ small_warped_light_gray_stained_glass_flask.png
         │           ├─ small_warped_lime_stained_glass_flask.png
         │           ├─ small_warped_magenta_stained_glass_flask.png
         │           ├─ small_warped_orange_stained_glass_flask.png
         │           ├─ small_warped_pink_stained_glass_flask.png
         │           ├─ small_warped_purple_stained_glass_flask.png
         │           ├─ small_warped_red_stained_glass_flask.png
         │           ├─ small_warped_tinted_glass_flask.png
         │           ├─ small_warped_white_stained_glass_flask.png
         │           ├─ small_warped_yellow_stained_glass_flask.png
         │           ├─ spruce_copper_barrel.png
         │           ├─ spruce_copper_exposed_barrel.png
         │           ├─ spruce_copper_oxidized_barrel.png
         │           ├─ spruce_copper_weathered_barrel.png
         │           ├─ spruce_gold_barrel.png
         │           ├─ spruce_iron_barrel.png
         │           ├─ spruce_netherite_barrel.png
         │           ├─ warped_copper_barrel.png
         │           ├─ warped_copper_exposed_barrel.png
         │           ├─ warped_copper_oxidized_barrel.png
         │           ├─ warped_copper_weathered_barrel.png
         │           ├─ warped_gold_barrel.png
         │           ├─ warped_iron_barrel.png
         │           └─ warped_netherite_barrel.png
         └─ fabric.mod.json

```
