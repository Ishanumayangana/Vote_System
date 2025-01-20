from dash import Input, Output, dcc, html  # Updated import
import db_handler
import plotly.graph_objects as go
import pandas as pd

def register_callbacks(app):
    # Voting Callback
    @app.callback(
        Output('vote-result', 'children'),
        [Input('vote-button', 'n_clicks')],
        [Input('candidate-dropdown', 'value')]
    )
    def cast_vote(n_clicks, selected_candidate):
        if n_clicks is None:
            return ""
        # Insert vote into the database
        db_handler.record_vote(selected_candidate)
        return f"Vote casted for {selected_candidate}"

    # Update Graph with vote results
    @app.callback(
        Output('results-graph', 'figure'),
        Output('total-votes', 'children'),  # Output for total votes display
        [Input('vote-button', 'n_clicks')]
    )
    def update_graph(n_clicks):
        # Retrieve vote counts from DB
        results = db_handler.get_results()

        # Ensure the results is a list of dictionaries
        if not results:
            return go.Figure(), "Total Votes: 0"  # Empty chart and zero votes if no data

        # Convert the results to a DataFrame
        df = pd.DataFrame(results)

        # Ensure we only have the top 3 candidates in the funnel chart
        df = df[df['Candidate'].isin(['A', 'B', 'C'])]

        # Sort the DataFrame by the 'Votes' column in descending order
        df = df.sort_values('Votes', ascending=False)

        # Create the Funnel chart
        fig_funnel = go.Figure(go.Funnel(
            y=df['Candidate'],  # Categories (Candidates)
            x=df['Votes'],  # Values (Votes)
            textinfo="label+value+percent total",  # Show label (candidate name), value (vote count), and percentage of total votes
            textposition="inside",  # Position the text inside the funnel sections
            marker=dict(
                color=['#FF5733', '#33FF57', '#3357FF'],  # Colors for each candidate
                line=dict(color="black", width=1)  # Black border around sections
            )
        ))

        # Customize funnel chart layout
        fig_funnel.update_layout(
            title="Vote Distribution (Funnel Chart)",
            title_x=0.5,  # Center the title
            title_font=dict(color="black", size=24),  # Black color for the title text
            showlegend=False,
            plot_bgcolor='#FFF9E6',  # Light yellow background for the plot area
            paper_bgcolor='#FFF4CC',  # Slightly darker yellow background for the overall page
            xaxis_title="Votes",
            yaxis_title="Candidates",
            template="plotly_dark",  # Use dark theme for better contrast
        )

        # Total votes count
        total_votes = df['Votes'].sum()

        return fig_funnel, f"Total Votes: {total_votes}"  # Return both the figure and total votes as text
