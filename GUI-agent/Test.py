import pyautogui

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()
print(f"屏幕宽度: {screen_width}, 屏幕高度: {screen_height}")

# 获取当前鼠标位置
current_x, current_y = pyautogui.position()
print(f"当前鼠标位置: x={current_x}, y={current_y}")

pyautogui.moveTo(357, 571)