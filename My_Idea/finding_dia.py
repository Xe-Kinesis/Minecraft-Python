'''
다이아 감지 봇
'''
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x, y, z = mc.player.getPos()

while True:
    for i in range(0, 50):
        block_finder = mc.getBlock(x, y-i, z)
        if block_finder == 56:
            mc.postToChat("Found the Dia!" + str(i))
        else:
            mc.postToChat("No dia here" + str(i))
            time.sleep(1)