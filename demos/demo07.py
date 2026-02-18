import fixpath
import colorultra

# Demonstrate cursor relative movement: UP, DOWN, FORWARD, and BACK in colorultra.CURSOR

up = colorultra.Cursor.UP
down = colorultra.Cursor.DOWN
forward = colorultra.Cursor.FORWARD
back = colorultra.Cursor.BACK

def main():
    """
    expected output:
    1a2
    aba
    3a4
    """
    colorultra.just_fix_windows_console()
    print("aaa")
    print("aaa")
    print("aaa")
    print(forward() + up(2) + "b" + up() + back(2) + "1" + forward() + "2" + back(3) + down(2) + "3" + forward() + "4")


if __name__ == '__main__':
    main()
