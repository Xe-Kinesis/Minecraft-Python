#환경 설정
import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

def delay():
    time.sleep(0.3)

pos = mc.player.getTilePos()
x, y, z = pos.x, pos.y, pos.z

#밑 바닥 0F
mc.setBlocks(x, y + 1, z, x + 14, y + 1, z + 10, 43, 5)
delay()
mc.setBlocks(x + 1, y + 1, z + 1 , x + 13, y + 1, z + 9, 3, 2)
delay()

#1F
mc.setBlocks(x + 2, y + 2, z + 1, x + 12, y + 2, z + 9, 5)
delay()
#기둥 세우기
for i in range(0, 3):
    mc.setBlock(x + 3, y + 3 + i, z + 2, 17)
    mc.setBlock(x + 11, y + 3 + i, z + 2, 17)
    mc.setBlock(x + 3, y + 3 + i, z + 8, 17)
    mc.setBlock(x + 11, y + 3 + i, z + 8, 17)
    delay()

#벽 매우기
for a in range(0, 3):
    #x축
    mc.setBlocks(x + 4, y + 3, z + 2, x + 10, y + 3 + a, z + 2, 80)
    mc.setBlocks(x + 4, y + 3, z + 8, x + 10, y + 3 + a, z + 8, 80)
    #z축
    mc.setBlocks(x + 3, y + 3, z + 3, x + 3, y + 3 + a, z + 7, 80)
    mc.setBlocks(x + 11, y + 3, z + 3, x + 11, y + 3 + a, z + 7, 80)
    delay() 
#벽 세부 디자인
for b in range(0, 3):
    #x축
    mc.setBlock(x + 9, y + 3 + b, z + 2, 5)
    #z축
    mc.setBlock(x + 3, y + 3 + b, z + 4, 5)
    mc.setBlock(x + 11, y + 3 + b, z + 6, 5)
    delay()

#입구 나무 윗 기둥
for c in range(0, 7):
    mc.setBlock(x + 4 + c, y + 5, z + 8, 5)
    delay()
#유리 설치 
mc.setBlock(x + 11, y + 4, z + 3, 102)
mc.setBlocks(x + 4, y + 4, z + 2, x + 5, y + 4, z + 2, 102)
#문 설치 칸 확보
mc.setBlocks(x + 6, y + 3, z + 8, x + 7, y + 4, z + 8, 0)
mc.setBlock(x + 1, y + 2, z + 5, 193)

#기와 세우기

#x축
for d in range(0, 9):
    mc.setBlock(x + 3 + d, y + 6, z + 1, 44)
    mc.setBlock(x + 3 + d, y + 6, z + 9, 44)
    delay() 
#z축
for e in range(0, 7):
    mc.setBlock(x + 2, y + 6, z + 2 + e, 44)
    mc.setBlock(x + 12, y + 6, z + 2 + e, 44)
    delay()

#기와 세우기 2
mc.setBlocks(x + 3 , y + 6, z + 2, x + 11, y + 6, z + 8, 43)
delay()
mc.setBlocks(x + 4 , y + 7, z + 3, x + 10, y + 7, z + 7, 44)
delay()
#air
mc.setBlocks(x + 5 , y + 7, z + 4, x + 9, y + 7, z + 6, 0)
delay()
mc.setBlocks(x + 5 , y + 7, z + 4, x + 9, y + 7, z + 6, 43)
delay()
mc.setBlocks(x + 5 , y + 8, z + 4, x + 9, y + 8, z + 6, 0)
delay()
mc.setBlocks(x + 6 , y + 8, z + 5, x + 8, y + 8, z + 5, 43)
delay()

#인테리어 
mc.setBlocks(x + 4, y + 3, z + 7, x + 4, y + 3, z + 6, 54)
mc.setBlock(x + 4, y + 3, z + 5, 120)

#책상
mc.setBlock(x + 9, y + 3, z + 5, 116)
#카펫
mc.setBlock(x + 9, y + 3, z + 6, 171, 15)
mc.setBlock(x + 9, y + 3, z + 4, 171, 15)
#횃불
mc.setBlock(x + 10, y + 5, z + 6, 50)

mc.postToChat("LEEVI : Hanok is all made!")