from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x, y, z = mc.player.getPos()

mc.setBlocks(x, y, z, x + 5, y + 5, z + 5, 4)
mc.setBlocks(x + 1, y + 1, z + 1, x + 4, y + 4, z + 4, 0)