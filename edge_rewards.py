import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 设置驱动程序路径
driver_path = 'C:/Users/XXXXXXXXX/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.10/msedgedriver.exe'  # 将"path_to_driver"替换为驱动程序的实际路径。替换XXXXXXXXX！

# 设置用户配置文件路径
user_data_dir = 'C:\\Users\\XXXXXXXXX\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default'  # 将"path_to_user_data"替换为用户配置文件的实际路径。这些路径指定 Edge WebDriver 可执行文件的位置和浏览器配置文件的用户数据目录。替换XXXXXXXXX！

# 创建Edge浏览器选项
options = Options()
options.use_chromium = True
options.add_argument("--start-maximized")  # 最大化窗口
options.add_argument(f'--user-data-dir={user_data_dir}')

# 创建驱动程序服务
service = Service(driver_path)

# 创建WebDriver对象
driver = webdriver.Edge(service=service, options=options)

# 打开Bing搜索引擎
driver.get("https://www.bing.com/")

# 依次搜索
for i in range(1,40):
    # 获取搜索框元素
    search_box = driver.find_element(By.NAME, "q")
    
    # 清空搜索框内容
    search_box.clear()
    
    # 输入搜索关键字
    search_box.send_keys(str(i))
    
    # 提交搜索
    search_box.submit()
    
    # 等待搜索结果加载完成
    time.sleep(2)
    
    # 打印当前搜索结果页面的标题
    print("搜索结果页面标题:", driver.title)


time.sleep(1)

pyautogui.press('f12')

# 等待页面加载完成
time.sleep(2)

# 模拟按下Shift+Ctrl+M键
pyautogui.keyDown('shift')
pyautogui.keyDown('ctrl')
pyautogui.press('m')
pyautogui.keyUp('ctrl')
pyautogui.keyUp('shift')

# 等待切换到设备仿真模式
time.sleep(2)

# 依次搜索
for i in range(40,70):
    # 获取搜索框元素
    search_box = driver.find_element(By.NAME, "q")
    
    # 清空搜索框内容
    search_box.clear()
    
    # 输入搜索关键字
    search_box.send_keys(str(i))
    
    # 提交搜索
    search_box.submit()
    
    # 等待搜索结果加载完成
    time.sleep(2)
    
    # 打印当前搜索结果页面的标题
    print("搜索结果页面标题:", driver.title)

# 关闭浏览器
driver.quit()

# 关闭webdriver进程
service.stop()
