'''
杀皮5.0

4.0 更新人物血量检查机制，人物血量不足就拍个血瓶子；
5.0 小yi被封号了，督促我们要继续改进；
    增加了物品名称的MOD，现在捡拾的物品有四种：符文、底材、非蓝、其他；
    现在改用电法刷，刷矫正者、去库拉斯特三个场景小站开尸体，刷皮叔
    增加随机时间间隔和随机点击范围；

现在程序的流程是：
0 进入到游戏任务画面
1 进行游戏 选择难度
2 检查米山状态
3 检查人物状态
4.1 找小站，杀矫正者
4.2 从冰冻高原去库拉斯特下层
4.3 库拉斯特翻箱子X3
    去哈洛加斯
4.5 杀皮
6 把货放在箱子里
重复 1-4，平均3分一盘
每40盘要休息15分钟
报异常后，按ESC+退出, 然后从1开始执行
'''

'''
挂机杀皮叔的软条件，防止人物挂机中死亡
1 米山等级高就能站住，人物等级必须大于76 米山等级大于75（可以用死神丧钟）；人物大于85级可以有效减少意外
2 米山装备：塔拉夏头、利维坦、死神丧钟（打孔镶钻）；
3 米山的光环选择祈祷
4 人物装备：箭止、暴风之盾（打孔镶22号/钻）
5 人物冰抗电抗75，火抗尽量高
6 人物生命回复+7
'''

'''
运行前设置参数，数字的单位默认是秒，位置的单位是屏幕像素
1 设置难度； 普通y=454，噩梦y=522，地狱y=586
2 设置传送皮叔屋子坐标；每台机器传送进皮叔屋子的坐标不一致
'''


import pyautogui
import time
import random
import logging
import logging.config

# 用配置文件的方式来处理日志
# 配置文件logging.conf有中文时出现解码问题，已删除注释；需要时参考
# https://blog.csdn.net/weixin_39918285/article/details/79551104
logging.config.fileConfig('logging.conf')


# 定义全局变量
# 需要修改的参数  ****************************************************************************************
# 选择游戏难度, (普通y=454，噩梦y=522，地狱y=586)
diff = 586

# 记录器
rootLogger = logging.getLogger()
logger = logging.getLogger('applog')

# 图片识别信心指数
confidence = 0.7

# 每走一步的时间
time_pace = 1.8


# - 1 进行游戏 选择难度
def start():

    # 找到“进行游戏”图标点击
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.moveTo(802+rx, 966+ry, duration=0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    

    # 选择难度
    logger.debug('鼠标移动到难度选项，耗时0.2秒')
    pyautogui.moveTo(x=(960+rx), y=(diff+ry), duration=0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标\n')
    pyautogui.click()
    
    logger.debug('游戏等待开始游戏的过场画面15秒\n')
    time.sleep(15+rt)


# - 2 检查米山状态
def check_ms():

    logger.debug('等待5秒，准备检查米山状态\n')
    time.sleep(5)

    pix = pyautogui.pixel(79, 25)
    print('米山血条颜色：', pix)
    print()

    # 米山血条颜色为绿色，1号机(0, 138, 0)，如果不匹配，判断米山挂了
    if not pyautogui.pixelMatchesColor(79, 25, (0, 138, 0), tolerance=12):
        logger.debug('米山挂了? 等待90秒后再次检测\n')
        time.sleep(90)

        # 可能是报错“和游戏服务器连接发生问题，检查网络再试一次”
        logger.debug('尝试点击弹窗-和游戏服务器连接发生问题，鼠标移动到弹窗，耗时0.2秒')
        pyautogui.moveTo(x=960, y=582, duration=0.2)

        time.sleep(0.1)
        logger.debug('点击鼠标\n')
        pyautogui.click()

        # 空白地方点一下，还原为初始画面
        logger.debug('空白地方点一下，还原为初始画面，鼠标移动到空白地方，耗时0.2秒')
        pyautogui.moveTo(x=960, y=128, duration=0.2)

        time.sleep(0.1)
        logger.debug('点击鼠标\n')
        pyautogui.click()

        # 找到“进行游戏”图标点击
        logger.debug('鼠标移动，耗时0.2秒')
        pyautogui.moveTo(802, 966, duration=0.2)
        
        time.sleep(0.1)
        logger.debug('点击鼠标')
        pyautogui.click()

        # 选择难度
        logger.debug('鼠标移动到难度选项，耗时0.2秒')
        pyautogui.moveTo(x=1056, y=diff, duration=0.2)
        
        time.sleep(0.1)
        logger.debug('点击鼠标\n')
        pyautogui.click()

        logger.debug('等待20秒')
        time.sleep(20)
        
        # 再次检查米山状态
        if not pyautogui.pixelMatchesColor(79, 25, (0, 138, 0), tolerance=12):
            logger.debug('米山确实挂了，不打了')
            time.sleep(360000)

        # 如果米山血条颜色匹配，则进行下面的跑进红门步骤


# - 3 检查法师状态
def check_sor():
    
    logger.debug('等待0.2秒，准备检查法师血量\n')
    time.sleep(0.2)

    pix = pyautogui.pixel(479, 972)
    print('法师血球颜色：', pix)
    print()

    # 利用TXT文件设置自增数，每次拍完瓶子后数字+1
    # 打开number-is-potion.txt，自增计数文件z
    f = open('number-si-potion.txt', 'r+')
    number = int(f.read())

    # 计算拍几号瓶子，用自增数求余，如果余数为零则排4
    key = number % 4
    if key == 0:
        key = 4

    # 法师血球颜色为红色，在图不停变化，1号机白点左下方颜色大致为(208, 29, 32)，如果不匹配，则加血
    if not pyautogui.pixelMatchesColor(479, 972, (208, 29, 32), tolerance=20):
        
        # 补血
        logger.debug('血不满,补血')
        time.sleep(0.1)
        pyautogui.press(f'{key}')
        print(f'按了{key}号位置的血瓶')

        # number-is-potion文件指针移到开头
        f.seek(0)
        # 清除文件的内容
        f.truncate()
        # 写入自增新数
        f.write(str(int(number) + 1))

    f.close

    # 按alt
    time.sleep(0.5)
    logger.debug('按一下alt，显示物品名称\n\n\n')
    pyautogui.press('alt')


# 4.1 找小站，杀矫正者
def kj():
    
    logger.debug('米山状态正常，人物状态正常，游戏继续\n')
    logger.debug('4.1 去杀矫正者\n')
    time.sleep(0.2+rt)

    # 顶个球
    logger.debug('按一下F5键,准备顶球')
    pyautogui.press('f5')
    time.sleep(0.2)
    logger.debug('点击鼠标右键\n')
    pyautogui.click(button='right')

    # 第一步，泥坑中间
    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(960, 520, 0.3)
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.move(-350+rx, 400+ry, 0.3)

    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)

    # 第二步，台阶下面的中间
    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(960, 400, 0.3)
    
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.move(-300+rx, 390+ry, 0.3)

    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)


    # 进小站
    logger.debug('定位屏幕中的小站图片')
    location_waypoint51 = pyautogui.locateCenterOnScreen("pics\\waypoint51.png", confidence=0.5)
    
    logger.debug('确定小站的X坐标和Y坐标')
    point_waypoint51_x, point_waypoint51_y = location_waypoint51

    # 切换心灵传动，进小站
    logger.debug('按一下F3键,准备心灵传动')
    pyautogui.press('f3')
    
    logger.debug('鼠标移动到小站上，耗时0.3秒')
    pyautogui.moveTo(point_waypoint51_x, point_waypoint51_y, 0.3)

    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')

    logger.debug('鼠标移动冰冻高地，在冻和高之间，耗时1秒')
    pyautogui.moveTo(335, 328, 1)

    logger.debug('点击鼠标')
    pyautogui.click()

    logger.debug('屏幕切换，等待4秒\n')
    time.sleep(4)

    # 传送
    logger.debug('按一下F4键,准备传送')
    pyautogui.press('f4')
    
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.moveTo(1057, 0, 0.3)
    
    time.sleep(0.1)
    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')
    
    time.sleep(0.5)
    logger.debug('再次点击鼠标右键')
    pyautogui.click(button='right')

   # 开打
    time.sleep(0.1)
    logger.debug('按一下F1键,准备开打')
    pyautogui.press('f1')
    
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.moveTo(860, 380, 0.3)
    
    time.sleep(0.1)
    logger.debug('10秒内点击鼠标右键50下')
    pyautogui.click(button='right', clicks=50, interval=0.2)


# 4.2 从冰冻高原到库拉斯特下层
def bing2kuxia():
    
    # 传送
    time.sleep(0.2)
    logger.debug('按一下F4键,准备传送')
    pyautogui.press('f4')
    
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.moveTo(850, 930, 0.3)
    
    time.sleep(0.1)
    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')
    
    time.sleep(0.5)
    logger.debug('再次点击鼠标右键')
    pyautogui.click(button='right')

    time.sleep(0.5)
    logger.debug('再次点击鼠标右键')
    pyautogui.click(button='right')

    # 站定打空气
    time.sleep(0.5)
    logger.debug('按一下F2键,准备静电力场')
    pyautogui.press('f2')

    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(960, 400, 0.3)

    logger.debug('3秒内点击鼠标右键15下')
    pyautogui.click(button='right', clicks=15, interval=0.2)

     # 进小站
    time.sleep(0.5)
    logger.debug('定位屏幕中的小站图片')
    location_waypoint52 = pyautogui.locateCenterOnScreen("pics\\waypoint52.png", confidence=0.5)
    
    logger.debug('确定小站的X坐标和Y坐标')
    point_waypoint52_x, point_waypoint52_y = location_waypoint52

    # 切换心灵传动，进门
    time.sleep(0.3)
    logger.debug('按一下F3键,准备心灵传动')
    pyautogui.press('f3')
    
    logger.debug('鼠标移动到小站上，耗时0.3秒')
    pyautogui.moveTo(point_waypoint52_x, point_waypoint52_y, 0.3)

    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')

    logger.debug('鼠标移动III，在正中间，耗时1秒')
    pyautogui.moveTo(410, 220, 1)

    logger.debug('点击鼠标\n')
    pyautogui.click()

    time.sleep(0.3)
    logger.debug('鼠标移动库拉斯特下层，在斯和特之间，耗时1秒')
    pyautogui.moveTo(350+rx, 510+ry, 1)

    logger.debug('点击鼠标\n')
    pyautogui.click()

    logger.debug('大场景切换，等待12秒')
    time.sleep(12+rt)


# 4.3 库拉斯特翻箱子
def kufan():

    # 切换心灵传动
    time.sleep(1+rt)
    logger.debug('等待1秒，按一下F3键,准备心灵传动，准备翻箱子')
    pyautogui.press('f3')

    logger.debug('鼠标移动至右下角尸体，耗时0.3秒')
    pyautogui.moveTo(1670, 770, 0.3)

    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')


# 4.4 找红门
def find_portal():

    # 第一步，走到马路牙子
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.moveTo(580+rx, 920+ry, 0.3)

    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)
    
    # 下一步，火炬下方
    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(580+rx, 940+ry, 0.3)
    
    logger.debug('点击鼠标')
    pyautogui.click()

    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)
    
    # 找到尼拉塞克的传送门
    logger.debug('定位屏幕中的红门图片')
    location_nila_portal = pyautogui.locateCenterOnScreen("pics\\red-portal.png", confidence=0.5)
    
    logger.debug('确定红门的X坐标和Y坐标')
    point_nila_portal_x, point_nila_portal_y = location_nila_portal

    # 切换心灵传动，进门
    time.sleep(0.1)
    logger.debug('按一下F3键,准备心灵传动')
    pyautogui.press('f3')
    
    logger.debug('鼠标移动到红门，耗时0.3秒')
    pyautogui.moveTo(point_nila_portal_x, point_nila_portal_y, 0.3)

    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')
    
    logger.debug('等待4秒，等待画面切换\n')
    time.sleep(4)
    

# 4.5 KP
def kp():

    # 第一次飞
    logger.debug('飞往皮叔的屋子')
    logger.debug('按一下F4键,准备传送')
    pyautogui.press('f4')
    
    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(960, 520, 0.3)
    
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.move(640, -510, 0.3)
    
    time.sleep(0.1)
    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')
    
    logger.debug('等待0.2秒\n')
    time.sleep(0.2)
    
    # 下一次，到正门口
    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(960, 520, 0.3)
    
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.move(640, -510, 0.3)
    
    time.sleep(0.1)
    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')
    
    logger.debug('等待0.2秒\n')
    time.sleep(0.2)
    

    # 下一次，进屋子
    logger.debug('鼠标回归屏幕中央，耗时0.3秒')
    pyautogui.moveTo(960, 520, 0.3)
    
    # 需要修改的参数  ****************************************************************************************
    # 1号机传送进屋子的坐标是：pyautogui.move(520, -130, 0.3)
    # 2号机传送进屋子的坐标是：pyautogui.move(625, -185, 0.3)
    logger.debug('鼠标移动，耗时0.3秒')
    pyautogui.move(520, -130, 0.3)
    
    time.sleep(0.1)
    logger.debug('点击鼠标右键')
    pyautogui.click(button='right')
    
    logger.debug('等待0.2秒\n')
    time.sleep(0.2)
    
    # 切换连锁闪电
    logger.debug('按一下F1键')
    pyautogui.press('f1')
    
    # 开打
    logger.debug('移动鼠标，耗时0.3秒')
    pyautogui.moveTo(1150, 380, 0.3)
    
    time.sleep(0.1)
    logger.debug('10秒内点击鼠标右键50下')
    pyautogui.click(button='right', clicks=50, interval=0.2)

    time.sleep(0.2)
    
# -5 捡东西
def loot():

    # 先切换到传送
    time.sleep(0.2)
    logger.debug('按一下F4键,准备传送')
    pyautogui.press('f4')

    # 捡东西，按先后顺序依次判别
    logger.debug('判定是否有符文，没有则返回空值')
    location_runes = pyautogui.locateCenterOnScreen('pics\\runes.png', confidence=confidence)
    print(location_runes)

    if location_runes is not None:

        logger.debug('有一个符文，确定符文坐标的x, y值')
        point_x, point_y = location_runes

        logger.debug('移动并点击鼠标右键，传过去')
        pyautogui.moveTo(point_x, point_y, duration=0.3)
        pyautogui.click(button='right')

        time.sleep(0.5)
        logger.debug('再次判定符文坐标')
        location_runes = pyautogui.locateCenterOnScreen('pics\\runes.png', confidence=confidence)
        point_x, point_y = location_runes

        logger.debug('移动并点击鼠标左键，过去捡')
        pyautogui.moveTo(point_x, point_y, duration=0.3)
        pyautogui.click()
        
        pyautogui.click()
        logger.debug('捡了一个符文')
        time.sleep(0.2)

    logger.debug('判定是否有底材，没有则返回空值')
    location_hui = pyautogui.locateCenterOnScreen('pics\\hui.png', confidence=confidence)
    print(location_hui)

    if location_hui is not None:
        logger.debug('有一个底材，确定底材坐标的x, y值')
        point_x, point_y = location_hui
        x = int(point_x)
        y = int(point_y)

        logger.debug('检测底材颜色，只捡灰色的')
        if pyautogui.pixelMatchesColor(x, y, (99, 99, 99), tolerance=25):

            logger.debug('移动并点击鼠标右键，传过去')
            pyautogui.moveTo(point_x, point_y, duration=0.3)
            pyautogui.click(button='right')

            time.sleep(0.5)
            logger.debug('再次判定底材坐标')
            location_hui = pyautogui.locateCenterOnScreen('pics\\hui.png', confidence=confidence)
            point_x, point_y = location_hui

            logger.debug('移动并点击鼠标左键，过去捡')
            pyautogui.moveTo(point_x, point_y, duration=0.3)
            pyautogui.click()
            
            pyautogui.click()
            logger.debug('捡了一个底材')
            time.sleep(0.2)

    logger.debug('判定是否有戒指、项链等非蓝色想要的物品，没有则返回空值')
    location_feilan = pyautogui.locateCenterOnScreen('pics\\feilan.png', confidence=confidence)
    print(location_feilan)

    if location_feilan is not None:
        logger.debug('有一个非蓝想要的物品，如戒指、项链；确定戒指坐标的x, y值')
        point_x, point_y = location_feilan
        x = int(point_x)
        y = int(point_y)

        logger.debug('检测非蓝物品颜色，蓝色的不捡')
        if not pyautogui.pixelMatchesColor(x, y, (116, 116, 255), tolerance=25):

            logger.debug('移动并点击鼠标右键，传过去')
            pyautogui.moveTo(point_x, point_y, duration=0.3)
            pyautogui.click(button='right')

            time.sleep(0.5)
            logger.debug('再次判定非蓝物品坐标')
            location_feilan = pyautogui.locateCenterOnScreen('pics\\feilan.png', confidence=confidence)
            point_x, point_y = location_feilan

            logger.debug('移动并点击鼠标左键，过去捡')
            pyautogui.moveTo(point_x, point_y, duration=0.3)
            pyautogui.click()
            

            pyautogui.click()
            logger.debug('捡了一个非蓝物品')
            time.sleep(0.2)

    logger.debug('判定是否有咒符、珠宝、无瑕宝石等其他物品，没有则返回空值')
    location_qita = pyautogui.locateCenterOnScreen('pics\\qita.png', confidence=confidence)
    print(location_qita)

    if location_qita is not None:

        point_x, point_y = location_qita

        logger.debug('移动并点击鼠标右键，传过去')
        pyautogui.moveTo(point_x, point_y, duration=0.3)
        pyautogui.click(button='right')

        time.sleep(0.5)
        logger.debug('再次其他物品坐标')
        location_qita = pyautogui.locateCenterOnScreen('pics\\qita.png', confidence=confidence)
        point_x, point_y = location_qita

        logger.debug('移动并点击鼠标左键，过去捡')
        pyautogui.moveTo(point_x, point_y, duration=0.3)
        pyautogui.click()
        
        pyautogui.click()
        logger.debug('捡了一个其他物品')
        time.sleep(0.2)
        
    logger.debug('等待1秒,撤\n')
    time.sleep(1)


# - 6 把货存在箱子里
def stash():

    logger.debug('这局只存箱子，8秒后出发\n')
    time.sleep(8)

    # 去存箱子
    # 第一步，泥坑中间
    logger.debug('鼠标回归屏幕中央，耗时0.2秒')
    pyautogui.moveTo(960, 520, 0.2)
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.move(-360, 360, 0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)
    
    # 下一步，第一个台阶中间
    logger.debug('鼠标回归屏幕中央，耗时0.2秒')
    pyautogui.moveTo(960, 520, 0.2)
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.move(550, 180, 0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)
    
    # 下一步，走道尽头中间
    logger.debug('鼠标回归屏幕中央，耗时0.2秒')
    pyautogui.moveTo(960, 520, 0.2)
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.move(250, 270, 0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)
    
    # 下一步，箱子下面路正中间
    logger.debug('鼠标回归屏幕中央，耗时0.2秒')
    pyautogui.moveTo(960, 520, 0.2)
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.move(-600, 250, 0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('停滞一段时间，等待角色跑路\n')
    time.sleep(time_pace)
    
    # 找到箱子
    logger.debug('定位屏幕中的箱子，确定箱子的坐标')
    location_stash = pyautogui.locateCenterOnScreen("pics\\stash.png", confidence=0.6)
    
    logger.debug('等待0.2秒')
    time.sleep(0.2)
    
    logger.debug('确定箱子的X坐标和Y坐标')
    point_stash_x, point_stash_y = location_stash
    
    logger.debug('鼠标移动到箱子坐标')
    pyautogui.moveTo(point_stash_x, point_stash_y, duration=0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()
    
    logger.debug('等待2秒，走过去开箱子\n')
    time.sleep(2)

    # 按下ctrlleft，放东西
    logger.debug('按下ctrlleft键')
    pyautogui.keyDown('ctrlleft')

    logger.debug('鼠标移动到左上角第一个格子上，耗时0.2秒')
    pyautogui.moveTo(1293, 577, 0.2)

    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()

    # 下面动作重复7次
    for i in range(7):
        logger.debug('等待0.2秒\n')
        time.sleep(0.2)

        logger.debug('鼠标向右移动49，耗时0.2秒')
        pyautogui.move(49, 0, 0.2)

        time.sleep(0.1)
        logger.debug('点击鼠标')
        pyautogui.click()

    logger.debug('等待0.2秒\n')
    time.sleep(0.2)

    logger.debug('鼠标向下移动一格，耗时0.2秒')
    pyautogui.move(0, 49, 0.2)

    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()

    # 下面动作重复7次
    for i in range(7):
        logger.debug('等待0.2秒\n')
        time.sleep(0.2)

        logger.debug('鼠标向左移动49，耗时0.2秒')
        pyautogui.move(-49, 0, 0.2)

        time.sleep(0.1)
        logger.debug('点击鼠标')
        pyautogui.click()

    logger.debug('等待0.2秒\n')
    time.sleep(0.2)

    logger.debug('鼠标向下移动一格，耗时0.2秒')
    pyautogui.move(0, 49, 0.2)

    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()    

    # 下面动作重复7次
    for i in range(7):
        logger.debug('等待0.2秒\n')
        time.sleep(0.2)

        logger.debug('鼠标向右移动49，耗时0.2秒')
        pyautogui.move(49, 0, 0.2)

        time.sleep(0.1)
        logger.debug('点击鼠标')
        pyautogui.click()

    logger.debug('等待0.2秒\n')
    time.sleep(0.2)

    logger.debug('鼠标向下移动一格，耗时0.2秒')
    pyautogui.move(0, 49, 0.2)

    time.sleep(0.1)
    logger.debug('点击鼠标')
    pyautogui.click()

    # 下面动作重复7次
    for i in range(7):
        logger.debug('等待0.2秒\n')
        time.sleep(0.2)

        logger.debug('鼠标向左移动49，耗时0.2秒')
        pyautogui.move(-49, 0, 0.2)

        time.sleep(0.1)
        logger.debug('点击鼠标')
        pyautogui.click()

    logger.debug('蛇形点击完了\n')

    # 松开ctrlleft
    logger.debug('松开ctrlleft键')
    pyautogui.keyUp('ctrlleft')

    logger.debug('鼠标移动到空白处点一下，')
    pyautogui.moveTo(960, 560, duration=0.2)
    time.sleep(0.1)
    pyautogui.click()

    # 退出游戏
    # 按ESC，点击“储存并离开”图标
    logger.debug('按一下ESC键')
    pyautogui.press('esc')
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.moveTo(961, 474, duration=0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标\n')
    pyautogui.click()
    
    logger.debug('存箱子结束，等待退出游戏的过场画面35秒\n')
    time.sleep(35)


# - 10 程序出错，退出游戏
def quit():

    logger.error('程序出错了，60秒后退出游戏重新进')
    time.sleep(60)
    
    # 退出游戏
    # 按ESC，点击“储存并离开”图标
    logger.debug('按一下ESC键')
    pyautogui.press('esc')
    
    logger.debug('鼠标移动，耗时0.2秒')
    pyautogui.moveTo(961, 474, duration=0.2)
    
    time.sleep(0.1)
    logger.debug('点击鼠标\n')
    pyautogui.click()
    
    logger.debug('等待退出游戏的过场画面10秒\n')
    time.sleep(10)


def main():

    while True:
    
        logger.debug('程序5秒后开始，请切换到游戏画面，祝你好运\n')
        time.sleep(5)

        ran = random.randint(30, 36)
        logger.debug(f'这一轮打{ran}把，然后去存箱子\n')

        for i in range(ran):

            # 随机延时变量
            global rt
            rt = random.randint(1, 5)
            logger.debug(f'随机延时变量是{rt}\n')

            # 随机范围变量
            global rx
            rx = random.randint(-10, 10)
            logger.debug(f'随机范围变量rx是{rx}\n')

            # 随机范围变量
            global ry
            ry = random.randint(-10, 10)
            logger.debug(f'随机范围变量ry是{ry}\n')

            # 1 进行游戏 选择难度
            logger.debug(f'# 1 开始游戏；开始第{i}局\n')
            start()

            logger.debug('# 2 检查米山状态\n')
            check_ms()

            logger.debug('# 3 检查法师状态\n')
            check_sor()

            try:

                logger.debug('# 4.1 杀矫正者\n')
                kj()

            except TypeError as e:

                quit()

                # 程序报错退出本次循环，继续下一个循环
                continue
            
            logger.debug('# 5 捡东西\n')
            loot()

            logger.debug('# 4.2 从冰冻高原去库拉斯特\n')
            bing2kuxia()

            kufan()

            loot()

            
            time.sleep(0.2)
            logger.debug('# 库拉斯市集，按一下F4键,准备传送')
            pyautogui.press('f4')
            
            logger.debug('鼠标回归屏幕中央，耗时0.3秒')
            pyautogui.moveTo(960, 520, 0.3)
            
            logger.debug('鼠标移动，耗时0.3秒')
            pyautogui.move(-480, 0+ry, 0.3)
            
            time.sleep(0.1)
            logger.debug('点击鼠标右键')
            pyautogui.click(button='right')
            
            logger.debug('等待0.2秒\n')
            time.sleep(0.2)

            # 进小站
            time.sleep(0.5)
            logger.debug('定位屏幕中的小站图片')
            location_waypoint3 = pyautogui.locateCenterOnScreen("pics\\waypoint3.png", confidence=0.5)
            
            logger.debug('确定小站的X坐标和Y坐标')
            point_waypoint3_x, point_waypoint3_y = location_waypoint3

            # 切换心灵传动，进门
            time.sleep(0.1)
            logger.debug('按一下F3键,准备心灵传动')
            pyautogui.press('f3')
            
            logger.debug('鼠标移动到小站上，耗时0.3秒')
            pyautogui.moveTo(point_waypoint3_x, point_waypoint3_y, 0.3)

            logger.debug('点击鼠标右键')
            pyautogui.click(button='right')

            time.sleep(0.3)
            logger.debug('鼠标移动库拉斯特市集，在斯和特之间，耗时1秒')
            pyautogui.moveTo(350+rx, 580+ry, 1)

            logger.debug('点击鼠标\n')
            pyautogui.click()

            logger.debug('屏幕切换，等待3秒')
            time.sleep(3)

            kufan()

            loot()

            # 去库拉斯上层
            time.sleep(0.2)
            logger.debug('按一下F4键,准备传送')
            pyautogui.press('f4')
            
            logger.debug('鼠标回归屏幕中央，耗时0.3秒')
            pyautogui.moveTo(960, 520, 0.3)
            
            logger.debug('鼠标移动，耗时0.3秒')
            pyautogui.move(-480, 0, 0.3)
            
            time.sleep(0.1)
            logger.debug('点击鼠标右键')
            pyautogui.click(button='right')
            
            logger.debug('等待0.2秒\n')
            time.sleep(0.2)

            # 进小站
            time.sleep(0.5)
            logger.debug('定位屏幕中的小站图片')
            location_waypoint3 = pyautogui.locateCenterOnScreen("pics\\waypoint3.png", confidence=0.5)
            
            logger.debug('确定小站的X坐标和Y坐标')
            point_waypoint3_x, point_waypoint3_y = location_waypoint3

            # 切换心灵传动，进门
            time.sleep(0.1)
            logger.debug('按一下F3键,准备心灵传动')
            pyautogui.press('f3')
            
            logger.debug('鼠标移动到小站上，耗时0.3秒')
            pyautogui.moveTo(point_waypoint3_x, point_waypoint3_y, 0.3)

            logger.debug('点击鼠标右键')
            pyautogui.click(button='right')

            time.sleep(0.3)
            logger.debug('鼠标移动库拉斯特市集，在斯和特之间，耗时1秒')
            pyautogui.moveTo(350, 650, 1)

            logger.debug('点击鼠标\n')
            pyautogui.click()

            logger.debug('屏幕切换，等待3秒')
            time.sleep(3)

            kufan()

            loot()

            # 去哈洛加斯
            time.sleep(0.2)
            logger.debug('按一下F4键,准备传送')
            pyautogui.press('f4')
            
            logger.debug('鼠标回归屏幕中央，耗时0.3秒')
            pyautogui.moveTo(960, 520, 0.3)
            
            logger.debug('鼠标移动，耗时0.3秒')
            pyautogui.move(-480, 0, 0.3)
            
            time.sleep(0.1)
            logger.debug('点击鼠标右键')
            pyautogui.click(button='right')
            
            logger.debug('等待0.2秒\n')
            time.sleep(0.2)

            # 进小站
            time.sleep(0.5)
            logger.debug('定位屏幕中的小站图片')
            location_waypoint3 = pyautogui.locateCenterOnScreen("pics\\waypoint3.png", confidence=0.5)
            
            logger.debug('确定小站的X坐标和Y坐标')
            point_waypoint3_x, point_waypoint3_y = location_waypoint3

            # 切换心灵传动，进门
            time.sleep(0.1)
            logger.debug('按一下F3键,准备心灵传动')
            pyautogui.press('f3')
            
            logger.debug('鼠标移动到小站上，耗时0.3秒')
            pyautogui.moveTo(point_waypoint3_x, point_waypoint3_y, 0.3)

            logger.debug('点击鼠标右键')
            pyautogui.click(button='right')

            logger.debug('鼠标移动V，在正中间，耗时1秒')
            pyautogui.moveTo(580, 220, 1)

            logger.debug('点击鼠标\n')
            pyautogui.click()

            time.sleep(0.3)
            logger.debug('鼠标移动哈洛加斯，在洛和加之间，耗时1秒')
            pyautogui.moveTo(335, 270, 1)

            logger.debug('点击鼠标\n')
            pyautogui.click()

            logger.debug('大场景切换，等待12秒')
            time.sleep(12)

            try:
                # 4 找红门
                logger.debug('# 4 找红门\n')
                find_portal()
                logger.debug('找红门结束\n')

            except TypeError as e:

                quit()

                # 如果找红门失败，程序报错，继续循环
                continue
            
            # 4.5 KP
            logger.debug('# 5 开始杀皮叔\n')
            kp()
            logger.debug('杀皮叔结束\n')

            loot()

            # 退出游戏
            # 按ESC，点击“储存并离开”图标（线程1）
            time.sleep(0.1)
            logger.debug('按一下ESC键')
            pyautogui.press('esc')
            
            logger.debug('鼠标移动，耗时0.2秒')
            pyautogui.moveTo(961, 474, duration=0.2)
            
            time.sleep(0.1)
            logger.debug('点击鼠标\n')
            pyautogui.click()
            
            logger.debug('等待退出游戏的过场画面15秒\n')
            time.sleep(15)


        # 6 存箱子去喽
        logger.debug('# 1 开始游戏，这局去存箱子\n')
        start()

        logger.debug('# 5 去存箱子啦\n')
        stash()

        logger.debug(f'这一轮结束了，这一轮打了{ran}把，下一轮900秒后开始\n\n\n')
        time.sleep(900)
        

if __name__ == '__main__':
    main()