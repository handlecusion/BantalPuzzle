from bangtal import *
import random

#수정중
#수정중 확인
setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene("튜토리얼", "Images/main_background.png")
scene_main = Scene("메인화면", "Images/background_white.png")
scene_easy = Scene("쉬움", "Images/Bike/bike_background.png")
scene_normal = Scene("보통", "Images/Landscape/landscape_background.png")
scene_hard = Scene("어려움", "Images/Cat/cat_background.png")

max_time = 1000
timer = Timer(max_time)

button_easy = Object("Images/Button/button_easy_2.png")
button_easy.locate(scene_main, 350, 500)
button_easy.show()

button_normal = Object("Images/Button/button_normal.png")
button_normal.locate(scene_main, 350, 400)
button_normal.show()

button_hard = Object("Images/Button/button_hard.png")
button_hard.locate(scene_main, 350, 300)
button_hard.show()



arr_pos = [[400, 500], [600, 500], [800, 500],
           [400, 300], [600, 300], [800, 300],
           [400, 100], [600, 100], [800, 100]]

arr_pos_easy = [[411, 439], [566, 439], [722, 439],
                [411, 283], [566, 283], [722, 283],
                [411, 128], [566, 128], [722, 128]]
#print(arr_pos_easy)

class Rect:
    def __init__(self, cx, cy, d):
        self.leftX = cx
        self.downY = cy
        self.distance = d

    def checkIn(self, x, y):
        return self.leftX < x < self.leftX + self.distance and self.downY < y < self.downY + self.distance

class PuzzleBlock:

    def __init__(self, pos, right_pos, side, devide, address, empty, mode):
        
        self.pos = pos
        self.right_pos = right_pos
        self.side = side
        self.devide = devide
        self.block = Object("Images/" + address)
        self.mode = mode
        if self.mode == 0:
            self.block_rect = Rect(arr_pos[pos-1][0], arr_pos[pos-1][1], side)
            self.block.locate(scene, arr_pos[pos-1][0], arr_pos[pos-1][1])
        elif self.mode == 1:
            self.block_rect = Rect(arr_pos_easy[pos-1][0], arr_pos_easy[pos-1][1], side)
            self.block.locate(scene_easy, arr_pos_easy[pos-1][0], arr_pos_easy[pos-1][1])
        elif self.mode == 2:
            self.block_rect = Rect(arr_pos[pos-1][0], arr_pos[pos-1][1], side)
            self.block.locate(scene_normal, arr_pos[pos-1][0], arr_pos[pos-1][1])
        elif self.mode == 3:
            self.block_rect = Rect(arr_pos[pos-1][0], arr_pos[pos-1][1], side)
            self.block.locate(scene_hard, arr_pos[pos-1][0], arr_pos[pos-1][1])
        self.block.setScale(1)
        self.block.show()
        self.empty = empty
        

    def checkIn(self, x, y):
        return self.block_rect.checkIn(x, y)

    def getPosition(self):
        pos = self.pos
        return pos

    def changePosition(self, pos):
        self.pos = pos
        if self.mode == 0:
            self.block_rect = Rect(arr_pos[pos-1][0], arr_pos[pos-1][1], self.side)
            self.block.locate(scene, arr_pos[pos-1][0], arr_pos[pos-1][1])
        elif self.mode == 1:
            print("PuzzleBlock안에 들어와서 위치 조정중")
            self.block_rect = Rect(arr_pos_easy[pos-1][0], arr_pos_easy[pos-1][1], self.side)
            self.block.locate(scene_easy, arr_pos_easy[pos-1][0], arr_pos_easy[pos-1][1])
        elif self.mode == 2:
            self.block_rect = Rect(arr_pos[pos-1][0], arr_pos[pos-1][1], self.side)
            self.block.locate(scene_normal, arr_pos[pos-1][0], arr_pos[pos-1][1])
        elif self.mode == 3:
            self.block_rect = Rect(arr_pos[pos-1][0], arr_pos[pos-1][1], self.side)
            self.block.locate(scene_hard, arr_pos[pos-1][0], arr_pos[pos-1][1])
        #self.block.locate(scene, arr_pos[pos-1][0], arr_pos[pos-1][1])
        self.block.show()


#arr_pos_tuto = list(range(1, 10))
#random.shuffle(arr_pos_tuto)
'''
for i in range(100):
    num1 = random.randrange(9)
    num2 = random.randint(0, 8)

    temp = arr_pos_tuto[num1]
    arr_pos_tuto[num1] = arr_pos_tuto[num2]
    arr_pos_tuto[num2] = temp
'''

#print(arr_pos_tuto)
tuto_empty = 9
tuto_devide = 3

easy_empty = 1
easy_devide = 3

block_tutorial = [
    PuzzleBlock(1, 1, 200, 3, "Number/tutorial_1.png", False, 0),
    PuzzleBlock(2, 2, 200, 3, "Number/tutorial_2.png", False, 0),
    PuzzleBlock(3, 3, 200, 3, "Number/tutorial_3.png", False, 0),
    PuzzleBlock(4, 4, 200, 3, "Number/tutorial_4.png", False, 0),
    PuzzleBlock(5, 5, 200, 3, "Number/tutorial_5.png", False, 0),
    PuzzleBlock(6, 6, 200, 3, "Number/tutorial_6.png", False, 0),
    PuzzleBlock(7, 7, 200, 3, "Number/tutorial_7.png", False, 0),
    PuzzleBlock(8, 8, 200, 3, "Number/tutorial_8.png", False, 0),
    PuzzleBlock(9, 9, 200, 3, "Number/tutorial_blank.png", True, 0)
]

block_easy = [
    PuzzleBlock(1, 1, 155, 3, "Bike/tranparent_155.png", True, 1),
    PuzzleBlock(2, 2, 155, 3, "Bike/bike_02.png", False, 1),
    PuzzleBlock(3, 3, 155, 3, "Bike/bike_03.png", False, 1),
    PuzzleBlock(4, 4, 155, 3, "Bike/bike_04.png", False, 1),
    PuzzleBlock(5, 5, 155, 3, "Bike/bike_05.png", False, 1),
    PuzzleBlock(6, 6, 155, 3, "Bike/bike_06.png", False, 1),
    PuzzleBlock(7, 7, 155, 3, "Bike/bike_07.png", False, 1),
    PuzzleBlock(8, 8, 155, 3, "Bike/bike_08.png", False, 1),
    PuzzleBlock(9, 9, 155, 3, "Bike/bike_09.png", False, 1)
]

background = Object("Images/background_transparent.png")
background.locate(scene, 0, 0)
background.show()

background_easy = Object("Images/background_transparent.png")
background_easy.locate(scene_easy, 0, 0)
background_easy.show()

background_normal = Object("Images/background_transparent.png")
background_normal.locate(scene_normal, 0, 0)
background_normal.show()

background_hard = Object("Images/background_transparent.png")
background_hard.locate(scene_hard, 0, 0)
background_hard.show()

def movable(pos, mode):
    devide = 0
    if mode == 0:
        devide = tuto_devide
    elif mode == 1:
        devide = easy_devide

    check_pos = [pos - devide, pos - 1, pos + 1, pos + devide]
    if check_pos[0] <= 0:
        check_pos[0] = 0
    if pos % devide == 1:
        check_pos[1] = 0
    if pos % devide == 0:
        check_pos[2] = 0
    if check_pos[3] > devide * devide:
        check_pos[3] = 0
    #print(check_pos)
    return check_pos

def change_list(block, num1, num2):
    temp = block[num1]
    block[num1] = block[num2]
    block[num2] = temp

def suffle_block(mode):
    print("suffle_block execute")
    global tuto_empty
    global easy_empty
    pos_empty = 0
    block = block_tutorial
    for i in range(1000):
        if mode == 0:
            pos_empty = tuto_empty
            block = block_tutorial
        elif mode == 1:
            pos_empty = easy_empty
            block = block_easy
        movable_pos = [0, 0, 0, 0]
        movable_pos = movable(pos_empty, mode)
        index = random.randrange(4)
        if movable_pos[index] != 0:
            block[movable_pos[index]-1].changePosition(pos_empty)
            block[pos_empty-1].changePosition(movable_pos[index])
            change_list(block, movable_pos[index]-1, pos_empty-1)
            #global tuto_empty
            if mode == 0:
                tuto_empty = movable_pos[index]
            elif mode == 1:
                easy_empty = movable_pos[index]
        print("pos_empty: ", pos_empty)

suffle_block(0)
timer.start()

def background_onMouseAction(x, y, action):
    #suffle_block()
    pos_empty = 0
    pos_click = 0
    count = 0
    index_click = 0
    index_empty = 0
    check_pos = [0, 0, 0, 0]
    print("x: ",x ,", y: ",y)
    for b in block_tutorial:
        if b.checkIn(x, y):
            check_pos = movable(b.pos, 0)
            print("check_pos in click action: ", check_pos)
            pos_click = b.pos
            index_click = count

        if b.empty:
            #pos_empty
            pos_empty = b.getPosition()
            index_empty = count
            print("empty: ", pos_empty)
        count = count + 1

    for i in range(4):
        if check_pos[i] == pos_empty:
            block_tutorial[index_click].changePosition(pos_empty)
            block_tutorial[index_empty].changePosition(pos_click)

            print("index_click: ", index_click)
            print("index_empty: ", index_empty)
            change_list(block_tutorial, index_click, index_empty)

            check_right_pos = 1
            for k in block_tutorial:
                #print("pos: ", k.pos)
                #print("right_pos: ", k.right_pos)
                if k.pos != k.right_pos:
                    check_right_pos = 0
                    break
            print("check_right_pos: ", check_right_pos)


            if check_right_pos == 1:
                scene_main.enter()
                timer.stop()
                showMessage("튜토리얼 클리어 타임: " + str(max_time-int(timer.get())) + "초")

            
background.onMouseAction = background_onMouseAction

def background_easy_onMouseAction(x, y, action):
    #suffle_block()
    pos_empty = 0
    pos_click = 0
    count = 0
    index_click = 0
    index_empty = 0
    check_pos = [0, 0, 0, 0]
    print("x: ",x ,", y: ",y)
    for b in block_easy:
        if b.checkIn(x, y):
            check_pos = movable(b.pos, 1)
            print("check_pos in click action: ", check_pos)
            pos_click = b.pos
            index_click = count

        if b.empty:
            #pos_empty
            pos_empty = b.getPosition()
            index_empty = count
            print("empty: ", pos_empty)
        count = count + 1

    for i in range(4):
        if check_pos[i] == pos_empty:
            block_easy[index_click].changePosition(pos_empty)
            block_easy[index_empty].changePosition(pos_click)

            print("index_click: ", index_click)
            print("index_empty: ", index_empty)
            change_list(block_easy, index_click, index_empty)

            check_right_pos = 1
            for k in block_easy:
                #print("pos: ", k.pos)
                #print("right_pos: ", k.right_pos)
                if k.pos != k.right_pos:
                    check_right_pos = 0
                    break
            print("check_right_pos: ", check_right_pos)


            if check_right_pos == 1:
                scene_main.enter()
                timer.stop()
                showMessage("이지 단계 클리어 타임: " + str(max_time-int(timer.get())) + "초")

background_easy.onMouseAction = background_easy_onMouseAction


def button_easy_onMouseAction(x, y, action):
    scene_easy.enter()
    for i in range(9):
        block_easy[i].block.show()
    showMessage("가장 왼쪽-위가 빈칸이 되어야 합니다.(1번 자리)")
    timer.set(max_time)
    timer.start()
    suffle_block(1)

button_easy.onMouseAction = button_easy_onMouseAction

def button_normal_onMouseAction(x, y, action):
    scene_normal.enter()

button_normal.onMouseAction = button_normal_onMouseAction

def button_hard_onMouseAction(x, y, action):
    scene_hard.enter()

button_hard.onMouseAction = button_hard_onMouseAction


startGame(scene)
