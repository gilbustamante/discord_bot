"""Plot ISS coordinates on a map"""
import plotly.graph_objects as go

fig = go.Figure(data=go.Scattergeo(
        lon  = [-60.5748],
        lat  = [48.6304],
        ))

fig.update_layout(title="ISS Location")

fig.write_image('current.png')
