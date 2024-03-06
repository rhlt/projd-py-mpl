# Bron: https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
# Met aanpassing op regel 40 (bestandsnaam) 

from matplotvideo import attach_video_player_to_figure
import matplotlib.pyplot as plt

# (timestamp, value) pairs

# sample: big bunny scene cuts
fancy_data = [
    (0, 1),
    (11.875, 1),
    (11.917, 2),
    (15.75, 2),
    (15.792, 3),
    (23.042, 3),
    (23.083, 4),
    (47.708, 4),
    (47.75, 5),
    (56.083, 5),
    (56.125, 6),
    (60, 6)
]


def on_frame(video_timestamp, line):
    timestamps, y = zip(*fancy_data)
    x = [timestamp - video_timestamp for timestamp in timestamps]

    line.set_data(x, y)
    line.axes.relim()
    line.axes.autoscale_view()
    line.axes.figure.canvas.draw()


def main():
    fig, ax = plt.subplots()
    plt.xlim(-15, 15)
    plt.axvline(x=0, color='k', linestyle='--')

    line, = ax.plot([], [], color='blue')

    attach_video_player_to_figure(fig, "filename.avi", on_frame, line=line) # Bestand gegenereerd door 3_2webcamvideo.py (NB: Deze functie van Matplotvideo werkt niet)

    plt.show()


main()