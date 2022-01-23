import pyautogui
import keyboard


class Pick_F():
    def run_f(self):
        while 1:
            pyautogui.press('f')
            # 实操过程，f键会按的很快，短按v有时无法断开，长按v(0.5秒以上)可以解决
            if keyboard.is_pressed('v'):
                break


if __name__ == '__main__':
    pick_f = Pick_F()
    keyboard.add_hotkey('alt+f', pick_f.run_f())
    keyboard.wait()
