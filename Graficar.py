import matplotlib.pyplot as plt
import numpy as np
import os, sys

class graficar:

    def resource_path(self, relative_path):
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def scatter_graph(self,ax,ay):
        #plt.style.use('_mpl-gallery')

        x = np.array(ax)
        y = np.array(ay)

        # plot
        # size and color:
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(title="Gráfica de Disperción")

        ax.scatter(x, y, vmin=0, vmax=100, alpha=0.4)


        #plt.show()
        fig.savefig(self.resource_path("scatter.png"))