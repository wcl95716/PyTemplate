from pynput import keyboard

def on_press(key: keyboard.Key) -> None:
    try:
        print(f'Alphanumeric key pressed: {key.char}')
    except AttributeError:
        print(f'Special key pressed: {key}')

def on_release(key: keyboard.Key) -> bool:
    print(f'Key released: {key}')
    if key == keyboard.Key.esc:
        # 停止监听
        return False
    
    return True

# 设置监听器
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
