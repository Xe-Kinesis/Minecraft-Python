from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftShape

mc = Minecraft.create()

pos = mc.player.getTilePos()

myShape = MinecraftShape(mc, pos)

# create a big cube
myShape.setBlocks(-5, -5, -5, 5, 5, 5, block.WOOL.id, 5)

#move it 10 blocks up
myShape.moveBy(0, 30, 0)

#rotate it 45 degrees
myShape.rotate(45, 0, 0)