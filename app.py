from flask import Flask, render_template

app = Flask(__name__)

MATCHES = [
    {
        'name': 'Group A Match 1',
        'dateTime': '2024-06-01T21:00:00',
        'timeToGame': -1,
        'fullTimeFlag' : True,
        'homeTeam': 'Germany',
        'awayTeam': 'Scotland',
        'homeTeamGoals': 5,
        'awayTeamGoals': 1,
        'homeTeamPoints': 3,
        'awayTeamPoints': 0,
        'homeTeamUser': 'Lewis',
        'awayTeamUser': 'Jake',
        'venue': 'Munich Football Arena, Munich'
    }
]

USERS = [
    {   
        'position':1,
        'name': 'Elliot',
        'matches_played': 2,
        'tier1': 'Spain',
        'tier2': 'Czechia',
        'tier3': 'Croatia',
        'tier4': 'Slovakia',
        'wins': 1,
        'draws': 0,
        'losses': 1,
        'goals_for': 3,
        'goals_against': 3,
        'goal_difference': 0,
        'points': 3
    },
    {   
        'position':2,
        'name': 'Jake',
        'matches_played': 2,
        'tier1': 'Portugal',
        'tier2': 'Denmark',
        'tier3': 'Turkey',
        'tier4': 'Scotland',
        'wins': 0,
        'draws': 1,
        'losses': 1,
        'goals_for': 2,
        'goals_against': 6,
        'goal_difference': -4,
        'points': 1.25
    },
    {   
        'position':3,
        'name': 'Lewis',
        'matches_played': 3,
        'tier1': 'Germany',
        'tier2': 'Netherlands',
        'tier3': 'Serbia',
        'tier4': 'Georgia',
        'wins': 2,
        'draws': 0,
        'losses': 1,
        'goals_for': 7,
        'goals_against': 2,
        'goal_difference': 5,
        'points': 6.75
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',users=USERS ,matches=MATCHES)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

