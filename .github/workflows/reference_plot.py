#!/etc/bin/python
import matplotlib.pyplot as plt
import sys

# if len(sys.argv) < 2:
#     print("Usage: %s <data_file>" % (sys.argv[0]))
#     sys.exit()

coord_x = []
coord_y = []
heading = []
kappa = []
dkappa = []

min_x = 1000000000
min_y = 1000000000
max_x = 0
max_y = 0

# file_obj = open(sys.argv[1], 'r')
file_obj = open('./tmp.txt', 'r')
try:
    for line in file_obj:
        items = line.strip().split(",")
        try:
            coord_x.append(float(items[0]))
            coord_y.append(float(items[1]))
            heading.append(float(items[2]))
            if len(items) > 3:
                kappa.append(float(items[3]))
            if len(items) > 4:
                dkappa.append(float(items[4]))
            min_x = min(min_x, float(items[0]))
            min_y = min(min_y, float(items[1]))
            max_x = max(max_x, float(items[0]))
            max_y = max(max_y, float(items[1]))
        except ValueError:
            continue
    file_obj.close()
except IOError:
    print("file open fail")
    file_obj.close()
    sys.exit()

len_x = len(coord_x)
len_y = len(coord_y)
len_heading = len(heading)
len_kappa = len(kappa)
len_dkappa = len(dkappa)
if len_x != len_y or len_y != len_heading or len_heading != len_kappa or len_kappa != len_dkappa:
    print("invalid data")

max_range = max(max_x - min_x, max_y - min_y)

fig = plt.figure(figsize=(14, 7))
ax1 = plt.subplot(221)
ax1.set_xlim(min_x - 10, min_x + max_range + 10)
ax1.set_ylim(min_y - 10, min_y + max_range + 10)
plt.scatter(coord_x, coord_y, s=2, marker=".", c='red')
plt.title("pose")
plt.legend()

ax2 = plt.subplot(222)
plt.scatter(range(482), heading, s=2, marker=".")
plt.title("heading")

ax3 = plt.subplot(223)
plt.scatter(range(482), kappa, s=2, marker=".")
plt.title("kappa")

ax4 = plt.subplot(224)
plt.scatter(range(482), dkappa, s=2, marker=".")
plt.title("dkappa")


def call_back(event):
    if event.inaxes in (ax2, ax3, ax4) and event.button:
        x_data = event.xdata
        ter = list()
        for index, valve in enumerate(coord_x):
            if index >= x_data:
                ter.append(index)
        x = ter[0]
        x_axis = coord_x[x]
        if event.button:
            ax1.set(xlim=(x_axis - 0.1, x_axis + 0.1))
            ax2.set(xlim=(x_data - 10, x_data + 10))
            ax3.set(xlim=(x_data - 10, x_data + 10))
            ax4.set(xlim=(x_data - 10, x_data + 10))
    if event.inaxes not in (ax1, ax2, ax3, ax4):
        ax1.set_xlim(min_x - 10, min_x + max_range + 10)
        ax1.set_ylim(min_y - 10, min_y + max_range + 10)
        ax2.set_xlim(-20, len(heading) + 20)
        ax3.set_xlim(-20, len(heading) + 20)
        ax4.set_xlim(-20, len(heading) + 20)
    fig.canvas.draw_idle()


def move(event):
    if event.inaxes in (ax2, ax3, ax4) and event.button:
        ax = event.inaxes
        x_min, x_max = ax.get_xlim()
        if event.button == 'up' and (x_max > (x_min + 25)):
            ter_min_1 = list()
            ter_max_1 = list()
            for index, value in enumerate(coord_x):
                if index >= x_min:
                    ter_min_1.append(index)
                if index <= x_max:
                    ter_max_1.append(index)
            x_min_t = ter_min_1[0]
            x_max_t = ter_max_1[-1]
            # x_axis_min = coord_x[x_min_t:x_max_t]
            y_min_t = list()
            # y_max_t = list()
            for i, value in enumerate(coord_x):
                if i >= x_min_t and i <= x_max_t:
                    y_min_t.append(coord_x[i])
            # for i in ter_max_1:
            #     y_max_t.append(coord_x[i])
            # x_axis_max = coord_x[x_max_t]
            ax1.set(xlim=(sorted(y_min_t)[0], sorted(y_min_t)[-1]))
            ax2.set(xlim=(x_min + 10, x_max - 10))
            ax3.set(xlim=(x_min + 10, x_max - 10))
            ax4.set(xlim=(x_min + 10, x_max - 10))
            if x_max >= len(coord_x) and x_min <= 0:
                ax1.set_xlim(min_x - 10, min_x + max_range + 10)
                ax1.set_ylim(min_y - 10, min_y + max_range + 10)

        if event.button == 'down':
            ter_min_2 = list()
            ter_max_2 = list()
            for index, value in enumerate(coord_x):
                if index >= x_min:
                    ter_min_2.append(index)
                if index <= x_max:
                    ter_max_2.append(index)
            x_min_t = ter_min_2[0]
            # x_axis_min = coord_x[x_min_t]
            x_max_t = ter_max_2[-1]
            # x_axis_max = coord_x[x_max_t]
            y_min_t = list()
            # y_max_t = list()
            for i, value in enumerate(coord_x):
                if i >= x_min_t and i <= x_max_t:
                    y_min_t.append(coord_x[i])
            # for i in ter_min_2:
            #     y_min_t.append(coord_x[i])
            # for i in ter_max_2:
            #     y_max_t.append(coord_x[i])
            ax1.set(xlim=(sorted(y_min_t)[0], sorted(y_min_t)[-1]))
            ax2.set(xlim=(x_min - 10, x_max + 10))
            ax3.set(xlim=(x_min - 10, x_max + 10))
            ax4.set(xlim=(x_min - 10, x_max + 10))
            if x_max >= len(coord_x) and x_min <= 0:
                ax1.set_xlim(min_x - 10, min_x + max_range + 10)
                ax1.set_ylim(min_y - 10, min_y + max_range + 10)
    fig.canvas.draw_idle()


fig.canvas.mpl_connect('button_press_event', call_back)
fig.canvas.mpl_connect('scroll_event', move)
fig.canvas.mpl_connect('axes_enter_event', move)
fig.canvas.mpl_connect('axes_leave_event', move)

plt.show()
