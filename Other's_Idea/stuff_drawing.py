from minecraftstuff import MinecraftDrawing
from mcpi.minecraft import Minecraft
from mcpi import block

#Connect to minecraft
mc = Minecraft.create()
# get the players position
pos = mc.player.getTilePos()

#Using the Minecraft Drawing API
mcdrawing = MinecraftDrawing(mc)

# draw a circle with a radius of 10 blocks
for a in range(0, 10):
    mcdrawing.drawCircle(pos.x, pos.y + 15 + a, pos.z + a, 10, 5)