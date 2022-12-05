import plotly.express as px
import plotly.graph_objects as go
import numpy

data_x = []
data_y = []
data_z = []

databorder_x = []
databorder_y = []
databorder_z = []
for z in numpy.arange(0, 10, 0.05):
    for x in numpy.arange(0, 4, 0.05):
        for y in numpy.arange(0, 4, 0.05):
            if 0<=x<=2 and 0<=y<=x:

                max_z = 9-(x**2)
                delta_border = 0.4
                if 0 <= z < max_z-delta_border:
                    # data inside
                    data_x.append(x)
                    data_y.append(y)
                    data_z.append(z)
                elif max_z-delta_border <= z <= max_z:
                    # data next to border
                    databorder_x.append(x)
                    databorder_y.append(y)
                    databorder_z.append(z)

fig = go.Figure(data=[
    go.Scatter3d(
        x=data_x,
        y=data_y,
        z=data_z,
        mode='markers',
        marker=dict(
            size=12,
            color=data_z,        # set color to an array/list of desired values
            colorscale='blues',  # choose a colorscale
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

# colorspace
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

fig.write_html("file.html", auto_open=True)
