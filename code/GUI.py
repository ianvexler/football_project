import pandas as pd
import matplotlib.pylab as plt
import seaborn
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import *
from PIL import ImageTk, Image

class GUI:
    def openGUI(self):
        root = Tk()
        gui = Window(root)
        gui.root.mainloop()

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Test")
        self.root.geometry("400x400")

        self.plot_hist(root)
        pass

    def plot_hist(self, root, match, type):
        event69 = pd.read_json("/Users/ianvexler/Documents/Archivos Ian/Projects/open-data/data/events/69242.json")
        passes_events = (event69[event69["type"] == {'id': 30, 'name': 'Pass'}])["minute"]

        figure = plt.Figure(figsize=(6,5), dpi=100)
        ax1 = figure.add_subplot(111)
        hist1 = FigureCanvasTkAgg(figure,root)
        hist1.get_tk_widget().pack()

        p = figure.gca()
        p.hist(passes_events, range(91))
