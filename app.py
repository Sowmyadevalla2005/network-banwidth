import json
import plotly
from flask import Flask, render_template
from plotly.utils import PlotlyJSONEncoder
from datetime import datetime
import sqlite3  # Assuming you're using SQLite to store your data

app = Flask(__name__)

# Fetch real data from your SQLite database (or another source)
def fetch_data():
    # Connect to the SQLite database
    with sqlite3.connect('speedtest.db') as conn:
        cursor = conn.execute("SELECT timestamp, download, upload, ping FROM results ORDER BY timestamp")
        rows = cursor.fetchall()  # Fetch all rows
    return rows

# Format data into a structure Plotly can use for graphing
def create_graph(rows):
    # Create empty lists to store the x (timestamps) and y (data) values
    times = []
    download_speeds = []
    upload_speeds = []
    pings = []

    # Process each row and convert the Unix timestamp to a human-readable date
    for row in rows:
        timestamp = datetime.utcfromtimestamp(row[0]).strftime('%Y-%m-%dT%H:%M:%S')  # Convert Unix timestamp
        times.append(timestamp)
        download_speeds.append(row[1] / 1e6)  # Convert download speed to Mbps
        upload_speeds.append(row[2] / 1e6)  # Convert upload speed to Mbps
        pings.append(row[3])  # Ping in ms

    # Prepare the graph data in Plotly's format
    graph_data = {
        "data": [
            {
                "mode": "lines+markers",
                "name": "Download Speed (Mbps)",
                "x": times,
                "y": download_speeds,
                "type": "scatter"
            },
            {
                "mode": "lines+markers",
                "name": "Upload Speed (Mbps)",
                "x": times,
                "y": upload_speeds,
                "type": "scatter"
            },
            {
                "mode": "lines+markers",
                "name": "Ping (ms)",
                "x": times,
                "y": pings,
                "type": "scatter"
            }
        ],
        "layout": {
            "title": {"text": "Internet Speed Over Time"},
            "xaxis": {"title": {"text": "Time"}},
            "yaxis": {"title": {"text": "Speed/Ping"}}
        }
    }
    return graph_data

@app.route('/')
def index():
    rows = fetch_data()  # Fetch real data from the database
    graph_data = create_graph(rows)  # Generate the graph data
    graph_json = json.dumps(graph_data, cls=PlotlyJSONEncoder)  # Convert graph data to JSON for rendering

    # Debugging: print the graph JSON to check its content
    print("Graph JSON:", graph_json)

    return render_template('index.html', graphJSON=graph_json)

if __name__ == '__main__':
    app.run(debug=True)
