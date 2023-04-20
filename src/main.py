import numpy as np
import matplotlib.pyplot as plt
import sympy
import threading


def calculate_derivative(y_function):
    x = sympy.symbols('x')
    y = eval(y_function)
    return sympy.diff(y, x)


keep_animating = True


def keypress_listener():
    global keep_animating
    while True:
        key = input()
        if key == 'q':
            keep_animating = False
            print('Animation stopped')
            exit()


def animate(y_function, y_derivative):
    x = np.arange(-100, 100, 0.1)
    y = eval(y_function)

    current_pos = (80, eval(y_function.replace('x', '80')))

    learning_rate = 0.01

    keypress_thread = threading.Thread(target=keypress_listener)
    keypress_thread.start()

    while keep_animating:
        new_x = current_pos[0] - learning_rate * \
            eval(y_derivative.replace('x', str(current_pos[0])))
        new_y = eval(y_function.replace('x', str(new_x)))
        current_pos = (new_x, new_y)

        plt.plot(x, y)
        plt.scatter(current_pos[0], current_pos[1], color='red')
        plt.pause(0.001)
        plt.clf()


def main():
    # Take user input of which function to use as f(x)
    y_function_str = input('Enter a function: ')

    try:
        y_function = eval('lambda x: ' + y_function_str)

        y_derivative = str(calculate_derivative(y_function_str))

    except Exception:
        print('Invalid function')
        return

    animate(y_function_str, y_derivative)


if __name__ == '__main__':
    main()
