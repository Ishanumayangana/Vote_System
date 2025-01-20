from dash import html, dcc

# Layout of the voting system page
layout = html.Div([
    html.H1("Online Voting System", style={'textAlign': 'center', 'color': '#4A90E2'}),  # Light blue header color
    html.Div([
        html.Label("Choose a Candidate:", style={'color': 'black', 'fontSize': '18px'}),  # Black for label color
        dcc.Dropdown(
            id='candidate-dropdown',
            options=[
                {'label': 'Candidate A', 'value': 'A'},
                {'label': 'Candidate B', 'value': 'B'},
                {'label': 'Candidate C', 'value': 'C'}
            ],
            value='A',
            style={'width': '50%', 'padding': '10px', 'backgroundColor': '#f4f4f4'}  # Light background for dropdown
        ),
        html.Button('Vote', id='vote-button', style={
            'padding': '10px 20px', 'backgroundColor': '#388E3C', 'color': 'white', 'border': 'none'}),  # Green button
        html.Div(id='vote-result', style={'padding': '10px', 'textAlign': 'center', 'color': '#333333'}),  # Dark gray for vote result text
    ], style={'width': '60%', 'margin': 'auto', 'padding': '20px'}),
    
    html.Div([
        dcc.Graph(id='results-graph', style={'height': '80vh'})
    ], style={'padding': '20px'}),
    
    # Total votes box in the top-right corner
    html.Div([
        html.H3(id='total-votes', style={
            'position': 'absolute', 
            'top': '20px', 
            'right': '20px', 
            'color': '#1f77b4',  # Blue color for total votes
            'backgroundColor': '#f4f4f4',  # Light background color
            'padding': '10px',
            'borderRadius': '5px',
            'boxShadow': '2px 2px 10px rgba(0,0,0,0.1)',
            'fontSize': '18px'
        })
    ]),
    
], style={'backgroundColor': '#FFF9E6', 'minHeight': '100vh'})  # Light yellow background for the whole page
