from mcpi.minecraft import Minecraft
from mcpi import block
from minecraftstuff import MinecraftShape

mc = Minecraft.create()

pos = mc.player.getTilePos()

myShape = MinecraftShape(mc, pos)

# create a big cube
myShape.setBlocks(-5, -5, -5, 5, 5, 5, block.WOOL.id, 5)

#move it 10 blocks up
myshape.moveBy(0, 10, 0)

#rotate it 45 degrees
myshape.rotate(45, 0, 0)