import random

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy

for x in range(1, 11):
    plt.figure(figsize=(1, 1))
    plt.clf()
    plt.axis('off')
    plt.ion()

    number = random.randint(1, 6)
    def plot_show():
        imgplot = plt.imshow(img)
        plt.show()
        plt.pause(0.5)


    if number == 1:
        img = mpimg.imread(
            '/Users/harishbalaji/documents/mycode/portfolio/projects/inverted-dice-1.png')
        plot_show()

    elif number == 2:
        img = mpimg.imread(
            '/Users/harishbalaji/documents/mycode/portfolio/projects/inverted-dice-2.png')
        plot_show()

    elif number == 3:
        img = mpimg.imread(
            '/Users/harishbalaji/documents/mycode/portfolio/projects/inverted-dice-3.png')
        plot_show()

    elif number == 4:
        img = mpimg.imread(
            '/Users/harishbalaji/documents/mycode/portfolio/projects/inverted-dice-4.png')
        plot_show()

    elif number == 5:
        img = mpimg.imread(
            '/Users/harishbalaji/documents/mycode/portfolio/projects/inverted-dice-5.png')
        plot_show()

    elif number == 6:
        img = mpimg.imread(
            '/Users/harishbalaji/documents/mycode/portfolio/projects/inverted-dice-6.png')
        plot_show()
