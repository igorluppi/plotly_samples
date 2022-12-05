import plotly.express as px
import plotly.graph_objects as go
import numpy

data_x = []
data_y = []
data_z = []

databorder_x = []
databorder_y = []
databorder_z = []

# Create a 3D grid of (x, y, z) coordinates
x, y, z = numpy.meshgrid(numpy.arange(0, 4, 0.03),
                         numpy.arange(0, 4, 0.03),
                         numpy.arange(0, 10, 0.03))

# Select the elements of the grid that satisfy the given conditions
indices = numpy.where((0 <= x) & (x <= 2) & (0 <= y) & (y <= x))
x = x[indices]
y = y[indices]
z = z[indices]

# Compute the maximum value of z for each (x, y) pair
max_z = 9 - (x**2)
delta_border = 0.4

# Select the data inside the region
inside = numpy.where((0 <= z) & (z < max_z - delta_border))
data_x.extend(x[inside])
data_y.extend(y[inside])
data_z.extend(z[inside])

# Select the data next to the border of the region
border = numpy.where((max_z - delta_border <= z) & (z <= max_z))
databorder_x.extend(x[border])
databorder_y.extend(y[border])
databorder_z.extend(z[border])

fig = go.Figure(data=[
    go.Scatter3d(
        x=data_x,
        y=data_y,
        z=data_z,
        mode='markers',
        marker=dict(
            size=12,
            color=data_z,           # set color to an array/list of desired values
            colorscale='blues',     # choose a colorscale
            opacity=0.03
        )
    ),
    go.Scatter3d(
        x=databorder_x,
        y=databorder_y,
        z=databorder_z,
        mode='markers',
        marker=dict(
            size=12,
            color=databorder_z,     # set color to an array/list of desired values
            colorscale='Viridis',   # choose a colorscale
            opacity=0.8
        )
    )
])

# colorscale
# One of the following named colorscales:
# [‘aggrnyl’, ‘agsunset’, ‘algae’, ‘amp’, ‘armyrose’, ‘balance’,
# ‘blackbody’, ‘bluered’, ‘blues’, ‘blugrn’, ‘bluyl’, ‘brbg’, ‘brwnyl’,
# ‘bugn’, ‘bupu’, ‘burg’, ‘burgyl’, ‘cividis’, ‘curl’, ‘darkmint’, ‘deep’,
# ‘delta’, ‘dense’, ‘earth’, ‘edge’, ‘electric’, ‘emrld’, ‘fall’, ‘geyser’,
# ‘gnbu’, ‘gray’, ‘greens’, ‘greys’, ‘haline’, ‘hot’, ‘hsv’, ‘ice’, ‘icefire’,
# ‘inferno’, ‘jet’, ‘magenta’, ‘magma’, ‘matter’, ‘mint’, ‘mrybm’, ‘mygbm’, ‘oranges’,
# ‘orrd’, ‘oryel’, ‘oxy’, ‘peach’, ‘phase’, ‘picnic’, ‘pinkyl’, ‘piyg’, ‘plasma’,
# ‘plotly3’, ‘portland’, ‘prgn’, ‘pubu’, ‘pubugn’, ‘puor’, ‘purd’, ‘purp’, ‘purples’,
# ‘purpor’, ‘rainbow’, ‘rdbu’, ‘rdgy’, ‘rdpu’, ‘rdylbu’, ‘rdylgn’, ‘redor’, ‘reds’, ‘solar’,
# ‘spectral’, ‘speed’, ‘sunset’, ‘sunsetdark’, ‘teal’, ‘tealgrn’, ‘tealrose’, ‘tempo’, ‘temps’,
# ‘thermal’, ‘tropic’, ‘turbid’, ‘turbo’, ‘twilight’, ‘viridis’, ‘ylgn’, ‘ylgnbu’, ‘ylorbr’, ‘ylorrd’].


fig.update_layout(
    # set axis
    scene = dict(
        xaxis = dict(range=[0,4],),
        yaxis = dict(range=[0,4],),
        zaxis = dict(range=[0,12],),
        xaxis_title='X AXIS TITLE',
        yaxis_title='Y AXIS TITLE',
        zaxis_title='Z AXIS TITLE',
    ),
    # width (optional)
    # width=700,

    # margin (optional)
    # margin=dict(r=20, l=10, b=10, t=10)
)

fig.write_html("file.html", auto_open=True)
