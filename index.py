import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import appinverse, appkinematics, appmeasurements, appminimalmeasurements

# --------------
# Navigation bar partial
# --------------
div_nav = html.Div([
  dcc.Link('Kinematics', href='/kinematics'),
  html.Br(),
  dcc.Link('Inverse Kinematics', href='/inverse-kinematics'),
  html.Br(),
  dcc.Link('Measurements', href='/measurements'),
  html.Br(),

  dcc.Link('Root', href='/')
])

# --------------
# Layout
# --------------
app.layout = html.Div([
  dcc.Location(id='url', refresh=False),
  html.Div(id='page-content'),
  div_nav,
])

# --------------
# URL redirection
# --------------
PAGES = {
  '/inverse-kinematics': appinverse.layout,
  '/kinematics': appkinematics.layout,
  '/measurements': appmeasurements.layout,
  '/': appminimalmeasurements.layout

}

# --------------
# Display page given URL
# --------------
@app.callback(
  Output('page-content', 'children'),
  [Input('url', 'pathname')]
)
def display_page(pathname):
  try:
    return PAGES[pathname]
  except KeyError:
    return '404'

# --------------
# Run server
# --------------
if __name__ == '__main__':
  app.run_server(debug=True)