# operator/execute.py -
import platform

import pyautogui
import pyperclip
import mss
import time

# 允许鼠标移动到屏幕角落（默认会触发fail-safe）
pyautogui.FAILSAFE = False

class Operation:
    def __init__(self):
        # 自动识别系统修饰键
        self.modifier = 'command' if platform.system() == 'Darwin' else 'ctrl'

    def input(self, text: str):
        """修复版：支持粘贴后自动回车"""
        print(f"⌨️  输入内容: {text.strip()}")

        # 检查是否包含换行符（回车）
        has_enter = '\n' in text
        clean_text = text.replace('\n', '')

        pyperclip.copy(clean_text)
        time.sleep(0.1)
        pyautogui.hotkey(self.modifier, 'v')

        if has_enter:
            time.sleep(0.2)
            print("⌨️  执行回车确认...")
            pyautogui.press('enter')

    """GUI操作工具类"""
    def click(self, x: int, y: int):
        """点击指定坐标"""
        print(f"🖱️  点击坐标 ({x}, {y})")
        pyautogui.click(x=x, y=y)

    def double_click(self, x: int, y: int):
        """双击指定坐标"""
        print(f"🖱️🖱️ 双击坐标 ({x}, {y})")
        pyautogui.doubleClick(x=x, y=y) # 调用 pyautogui 的双击功能

    def input(self, text: str):
        """输入文本（使用粘贴方式，支持中文）"""
        print(f"⌨️  输入: {text}")
        pyperclip.copy(text)  # 复制到剪贴板
        pyautogui.hotkey('ctrl', 'v')  # Mac用command，Windows用ctrl

    def screenshot(self, save_path: str):
        """截图并保存"""
        with mss.mss() as sct:
            sct.shot(output=save_path)
        print(f"📸 截图已保存: {save_path}")

    def hotkey(self, *keys):
        """按下组合键（如ctrl+c）"""
        print(f"⌨️  按下组合键: {' + '.join(keys)}")
        pyautogui.hotkey(*keys)

    def wait(self, seconds: float = 1.0):
        """等待指定时间"""
        print(f"⏱️  等待 {seconds} 秒...")
        time.sleep(seconds)