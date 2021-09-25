from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getPos()

# mc.setBlocks(x, y, z, x, y + 255, z, 5)
 


while True:
    x, y, z = mc.player.getPos()
    # mc.postToChat(y)
    if y < -170:
        mc.setBlock(x, y - 5, z, 8)
        time.sleep(0.5)
        mc.setBlock(x, y - 5, z, 0)
        mc.postToChat("SYSTEM : Emergency system on")
        break