import asyncio

#마인크래프트
from minecraftstuff import MinecraftTurtle
from mcpi.minecraft import Minecraft

#Connect to minecraft
mc = Minecraft.create()
# get the players position
pos = mc.player.getTilePos()

#Using the Minecraft Turtle
steve = MinecraftTurtle(mc, pos)
vine = MinecraftTurtle(mc, pos)
# draw a square
async def sstteevvee():
    steve.forward(5)
    steve.right(90)
    steve.forward(5)
    steve.right(90)
    steve.forward(5)
    steve.right(90)
    steve.forward(5)
#
async def vviinnee():
    vine.forward(3)
    vine.right(90)
    vine.forward(3)
    vine.right(90)
    vine.forward(3)
    vine.right(90)
    vine.forward(3)


asyncio.run(sstteevvee())
asyncio.run(vviinnee())