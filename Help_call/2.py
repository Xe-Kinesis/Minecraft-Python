'''파이썬 마크님께서 질문하신 코드 수정해 드렸어요 ^_^
if문에서 작은 따음표(')로 비교 하시게 되면 문자형 자료를 비교 하는 거에요.
숫자를 비교 하실 때에는 비교 조건식에 상수(type)을 넣어 주시면 됩니다.
화이팅 하세요! ㅎㅎ
'''
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x_sign = int(input("현재 위치에서 설치할블록방향의 x좌표가 +이면1번 -이면2번을 눌러주세요 >>>"))
z_sign = int(input("현재 위치에서 설치할 블록방향의 z좌표가 +이면1번 -이면2번을 눌러주세요 >>>"))
x , y , z = mc.player.getPos()
install_x = int(input("x좌표방향으로 설치할 블록의 갯수를 입력해주세요 >>>"))
install_z = int(input("z좌표방향으로 설치할 블록의 갯수를 입력해주세요 >>>"))
install_y = int(input("설치할 블록의 높이를 입력해주세요 >>>"))
in_block = input("블록안을 비우실려면 yes를눌러주세요 >>>")
print("---------------------------------------------------------------------------")
print("블록의 번호는 https://minecraft-ids.grahamedgecombe.com/에서 확인하실수있습니다")
kind_block = int(input("원하시는 블럭의 번호를 입력해주세요"))
mc.postToChat(x)
mc.postToChat(y)
mc.postToChat(z)
# x,z좌표 둘다+일
#이아래 if문들을 전부 뛰고 print("?")하고 끝남
if x_sign == 1 and z_sign == 1:
    print("?1")
    if in_block == 'yes':
        mc.setBlocks(x,y,z,x+install_x , y+install_y , z+install_z , kind_block)
        mc.setBlocks(x+1,y,z+1,x+install_z-1 , y+install_y-1 , z+install_z-1,0)
    else:
        mc.setBlocks(x,y,z,x+install_x , y+install_y , z+install_z , kind_block)
# x좌표 + z좌표 -일때
elif x_sign == 1 and z_sign == 2:
    print("??")
    if in_block == 'yes':
        mc.setBlocks(x,y,z,x+install_x , y+install_y , z-install_z , kind_block)
        mc.setBlocks(x+1,y,z+1,x+install_z-1 , y+install_y-1 , z-install_z-1,0)
    else:
        mc.setBlocks(x,y,z,x+install_x , y+install_y , z-install_z , kind_block)
# x좌표 - z좌표 +일때
elif x_sign == 2 and z_sign == 1:
    print("???")
    if in_block == 'yes':
        mc.setBlocks(x,y,z,x-install_x , y+install_y-1 , z+install_z , kind_block)
        mc.setBlocks(x+1,y,z+1,x-install_z-1 , y+install_y-1 , z+install_z-1,0)
    else:
        mc.setBlocks(x,y,z,x-install_x , y+install_y , z+install_z , kind_block)
# x,y좌표 둘다-일때
elif x_sign == 2 and z_sign == 2:
    print("????")
    if in_block == 'yes':
        mc.setBlocks(x,y,z,x-install_x , y+install_y , z-install_z , kind_block)
        mc.setBlocks(x+1,y,z+1,x-install_z-1 , y+install_y-1 , z-install_z-1,0)
    else:
        mc.setBlocks(x+1,y,z+1,x-install_x , y+install_y , z-install_z , kind_block)
print("?")