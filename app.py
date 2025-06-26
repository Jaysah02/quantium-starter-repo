import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Read cleaned data
df = pd.read_csv("output.csv")
df['date'] = pd.to_datetime(df['date'])

# Group by date and sum sales
df_grouped = df.groupby('date').sum().reset_index()
df_grouped = df_grouped.sort_values('date')

# Create Dash app
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Dashboard"

# Create line chart
fig = px.line(df_grouped, x='date', y='sales', title='Daily Sales of Pink Morsels')
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales ($)",
    shapes=[
        # Add vertical line at Jan 15, 2021
        dict(
            type="line",
            x0="2021-01-15",
            y0=0,
            x1="2021-01-15",
            y1=df_grouped['sales'].max(),
            line=dict(color="red", dash="dash"),
            name="Price Increase"
        )
    ],
    annotations=[
        dict(
            x="2021-01-15",
            y=df_grouped['sales'].max(),
            text="Price Increase (15 Jan 2021)",
            showarrow=True,
            arrowhead=1
        )
    ]
)

# Layout
app.layout = html.Div(children=[
    html.H1(children="Soul Foods Pink Morsel Sales Visualiser"),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# Run app
if __name__ == '__main__':
    app.run
app.run(debug=True)

