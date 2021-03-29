"""Plot ISS coordinates on a map"""
import plotly.graph_objects as go


def create_map_image(longitude, latitude):
    """Generates an image showing the ISS location on a map"""
    fig = go.Figure(
        go.Scattergeo(
            lon=[longitude],
            lat=[latitude],
            marker=dict(
                color='crimson',
                size=15,
                symbol='circle'
            )
        )
    )

    fig.update_geos(
        projection_type='natural earth',
    )

    fig.update_layout(
        title=dict(
            text=f"ISS Location",
            yanchor="top",
            x=0.5,
            font=dict(
                size=30
            ),
            pad=dict(
                b=0
            )
        ),
        margin=dict(
            r=20,
            t=70,
            l=20,
            b=0
        ),
        autosize=False,
        width=800,
        height=600,
    )

    fig.write_image('current.png')
