from dash import Dash, Input, Output, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.queries import (
    get_labels_countries_in_continent_code,
    get_continent_labels,
)

from src.plotting import (
    plot_countries_kpis,
)

from src.components import (
    app_header,
    # card1_blahblah_component,
    # card2_blahblah_component
)

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Div(
            [
                dbc.Row([app_header]),
                dbc.Row(
                    [
                        # dbc.Col(card1_blahblah_component),
                        # dbc.Col(card2_blahblah_component),
                    ]
                ),
            ]
        )
    ],
    style={"padding-right": "0px"},
)

# example of country dropdown options being updated based on selected continent
@app.callback(
    Output("country-selector", "options"),
    Input("continent-selector", "value"),
)
def update_country_dd_options(continent_code):
    return get_labels_countries_in_continent_code(continent_code)


# example of updating plot in card, component_property might not be 'figure'
# in Altair...
@app.callback(
    Output(component_id="component-id-of-plot-in-card", component_property="figure"),
    [
        Input(component_id="continent-dd", component_property="value"),
        Input(component_id="country-msdd", component_property="value"),
        Input(component_id="country_kpi_tab", component_property="value"),
    ],
)
def update_card1_blahblah_component(
    selected_continent, selected_countries, country_kpi_type
):
    return plot_countries_kpis(selected_continent, selected_countries, country_kpi_type)


if __name__ == "__main__":
    app.run_server()
