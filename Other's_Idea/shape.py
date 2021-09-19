from minecraftstuff import MinecraftShape
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

#Connect to minecraft
mc = Minecraft.create()
# get the players position
pos = mc.player.getTilePos()

#Using the Minecraft Shape API
mcshape = MinecraftShape(mc, pos)

# create a stone cube
mcshape.setBlocks(-5, -5, -5, 5, 5, 5, block.STONE.id)

# move it around
for i in range(0,10):
    mcshape.moveBy(1,0,1)
    sleep(0.5)