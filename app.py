import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load the data
df = pd.read_csv("output.csv")
df['date'] = pd.to_datetime(df['date'])

# App
app = dash.Dash(__name__)
app.title = "Pink Morsel Sales Visualiser"

# Layout
app.layout = html.Div(style={'fontFamily': 'Arial', 'padding': '30px'}, children=[
    html.H1("Soul Foods: Pink Morsel Sales Over Time", style={'textAlign': 'center'}),

    html.Div([
        html.Label("Select Region:", style={'fontWeight': 'bold'}),
        dcc.RadioItems(
            id='region-filter',
            options=[
                {'label': 'All', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all',
            labelStyle={'display': 'inline-block', 'marginRight': '15px'}
        )
    ], style={'textAlign': 'center', 'marginBottom': '30px'}),

    dcc.Graph(id='sales-graph')
])

# Callback to update graph
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(region):
    if region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['region'] == region.lower()]

    grouped = filtered_df.groupby('date').sum().reset_index()
    fig = px.line(grouped, x='date', y='sales', title=f"Sales Over Time ({region.title()})")
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales ($)',
        shapes=[
            dict(
                type="line",
                x0="2021-01-15",
                y0=0,
                x1="2021-01-15",
                y1=grouped['sales'].max() if not grouped.empty else 0,
                line=dict(color="red", dash="dash")
            )
        ],
        annotations=[
            dict(
                x="2021-01-15",
                y=grouped['sales'].max() if not grouped.empty else 0,
                text="Price Increase (15 Jan 2021)",
                showarrow=True,
                arrowhead=1
            )
        ]
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)