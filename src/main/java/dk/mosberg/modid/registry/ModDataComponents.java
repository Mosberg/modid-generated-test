package dk.mosberg.modid.registry;

import com.mojang.serialization.Codec;
import com.mojang.serialization.codecs.RecordCodecBuilder;
import dk.mosberg.modid.ModId;
import net.minecraft.component.ComponentType;
import net.minecraft.network.RegistryByteBuf;
import net.minecraft.network.codec.PacketCodec;
import net.minecraft.registry.Registries;
import net.minecraft.registry.Registry;
import net.minecraft.util.Identifier;

/**
 * Stores a simple fluid payload on ItemStacks (fluid id + amount). Note: this intentionally does
 * NOT store FluidVariant NBT; it supports "any fluid" by id.
 */
public final class ModDataComponents {
    private ModDataComponents() {}

    public record FluidContent(Identifier fluidId, long amount) {
        public static final FluidContent EMPTY =
                new FluidContent(Identifier.of("minecraft", "empty"), 0);

        public static final Codec<FluidContent> CODEC =
                RecordCodecBuilder.create(instance -> instance
                        .group(Identifier.CODEC.fieldOf("fluid").forGetter(FluidContent::fluidId),
                                Codec.LONG.fieldOf("amount").forGetter(FluidContent::amount))
                        .apply(instance, FluidContent::new));

        public static final PacketCodec<RegistryByteBuf, FluidContent> PACKET_CODEC =
                PacketCodec.tuple(Identifier.PACKET_CODEC, FluidContent::fluidId, PacketCodec.LONG,
                        FluidContent::amount, FluidContent::new);

        public boolean isEmpty() {
            return amount <= 0 || fluidId.equals(EMPTY.fluidId);
        }
    }

    public static final ComponentType<FluidContent> FLUID_CONTENT = Registry.register(
            Registries.DATA_COMPONENT_TYPE, Identifier.of(ModId.MOD_ID, "fluid_content"),
            ComponentType.<FluidContent>builder().codec(FluidContent.CODEC)
                    .packetCodec(FluidContent.PACKET_CODEC).build());

    public static void init() {
        ModId.LOGGER.info("Registered data components for {}", ModId.MOD_ID);
    }
}
