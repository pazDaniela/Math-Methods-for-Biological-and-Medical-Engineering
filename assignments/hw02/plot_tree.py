from numpy import array, mean
from matplotlib.pyplot import scatter, figure, show

def plot_tree(x,y,z):
    fig = figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z)
    def axisEqual3D(ax):
        extents = array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
        sz = extents[:,1] - extents[:,0]
        centers = mean(extents, axis=1)
        maxsize = max(abs(sz))
        r = maxsize/2
        for ctr, dim in zip(centers, 'xyz'):
            getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)
    axisEqual3D(ax)
    show()
