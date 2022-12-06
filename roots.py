from quadratic import Quadratic
import stdio
import sys


# Entry point.
def main():

    # stores the inputs from the terminal into variables
    x = float(sys.argv[1])

    # checks if the input is empty
    while not stdio.isEmpty():
        # stores the inputs from the terminal into variables
        a = stdio.readFloat()
        b = stdio.readFloat()
        c = stdio.readFloat()

        q = Quadratic(a, b, c)

        # displays the output onto the terminal
        stdio.writef("%s; %f; %s; %f; %f\n", q, q[x], q.roots(), q.sum(), q.prod())


if __name__ == '__main__':
    main()
