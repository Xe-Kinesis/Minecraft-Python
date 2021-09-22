import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

mc.setBlocks(x, y, z, x, y + 12, z + 12, 0)
mc.setBlocks(x, y, z, x, y + 12, z + 12, 35)

