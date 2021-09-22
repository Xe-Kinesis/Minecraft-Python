'''
다이아 감지 봇
Developer : Glen
'''
#환경 설정
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

#bag는 다이아 감지 저장 통
bag = []
x, y, z = mc.player.getPos()

mc.postToChat("Fiding now.. " + str(y))

#y축 최대 감지 범위 : 69칸(변경 가능)
for i in range(0, 70):
    block_finder = mc.getBlock(x, y - i, z)
    bag.append(block_finder)


#인덱스 중복값 출력
fin_bag = [i for i, value in enumerate(bag) if value == 56]
mc.postToChat("Done!")
time.sleep(1)

if 56 in bag:
    mc.postToChat("==========")       
    mc.postToChat("Found the location of the diamond!")
    mc.postToChat("Total Count : " + str(bag.count(56)))
    mc.postToChat("The diamond is located below the " + str(fin_bag) + "column on the y-axis.")
    mc.postToChat("==========")    
else:
    mc.postToChat("No Diamond here T.T")

#리스트 초기화
bag.clear()
fin_bag.clear()