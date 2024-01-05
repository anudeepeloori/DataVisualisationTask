from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import plotly.io as pio

app = Flask(__name__)

coaches_season = pd.read_csv("C:/Users/DELL/OneDrive/Desktop/USFproject2/coaches_season.csv")

@app.route('/')
def index():
    # Question 1: Which coach had the highest number of season wins in the year 1985?
    coaches_1985 = coaches_season[coaches_season['year'] == 1985]
    fig1 = px.bar(coaches_1985, x='first_name', y='season_win', title='Season Wins in 1985')

    # Question 2: Visualize the average number of wins for each TID
    avg_wins_by_tid = coaches_season.groupby('tid').agg({'season_win': 'mean', 'playoff_win': 'mean'}).reset_index()
    fig2 = px.bar(avg_wins_by_tid, x='tid', y=['season_win', 'playoff_win'], title='Average Wins by TID')

    # Question 3: Visualize which coach has coached the most teams
    teams_coached_count = coaches_season.groupby(['first_name', 'last_name']).agg({'tid': 'nunique'}).reset_index()
    fig3 = px.bar(teams_coached_count, x='first_name', y='tid', color='last_name', title='Number of Teams Coached by Coach')
    fig3.update_layout(xaxis_title='Coach', yaxis_title='Number of Teams Coached')

    graphJSON1 = pio.to_json(fig1)
    graphJSON2 = pio.to_json(fig2)
    graphJSON3 = pio.to_json(fig3)

    return render_template('index.html', graphJSON1=graphJSON1, graphJSON2=graphJSON2, graphJSON3=graphJSON3)

if __name__ == '__main__':
    app.run(debug=True)