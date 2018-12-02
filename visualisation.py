import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import interrogation


repo_name, commit_count = zip(*interrogation.repo_commits)

x = repo_name
y = commit_count

data = [go.Bar(
            x=x,
            y=y,
            text=y,
            textposition = 'auto',
            marker=dict(
                color='rgb(158,202,225)',
                line=dict(
                    color='rgb(8,48,107)',
                    width=1.5),
            ),
            opacity=0.6
        )]

py.plot(data, filename='first_bar_chart')











