    def plot(self):
        unwraped = self.itoh_2D(self.VES(self._I0, self._I1, self._I2))
        xlim = unwraped[0, :].size
        ylim = unwraped[:, 0].size
        x = np.linspace(0, xlim, xlim)
        y = np.linspace(0, ylim, ylim)
        X, Y = np.meshgrid(x, y)
        '''        
        l = 100
        p = np.polyfit(y, unwraped[:, l], 1)
        portadora = np.zeros(unwraped.shape)
        for n in range(0, x.size):
            portadora[:, n] = n * p[0] + p[1]
        '''
        phase = unwraped
        fig = plt.figure()
        ax = fig.add_subplot(121, projection='3d')
        ax.plot_surface(X, Y, phase, cmap='gray')
        ax = fig.add_subplot(122)
        plt.imshow(phase, cmap='gray')
        plt.grid()
        plt.show()