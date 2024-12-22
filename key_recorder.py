import keyboard
import time


def main():
    recorded_keys = []
    try:
        while True:
            event = keyboard.read_event()  # 读取键盘事件
            if event.event_type == keyboard.KEY_DOWN:  # 只记录按键按下事件
                recorded_keys.append((event.name, time.time()))  # 存储按键名称和按下时间
                print(f"Key {event.name} pressed at {time.time()}")
    except KeyboardInterrupt:
        print("Recording stopped.")
    finally:
        print("Recorded keys:")
        for key, timestamp in recorded_keys:
            print(f"Key: {key}, Timestamp: {timestamp}")


if __name__ == "__main__":
    main()