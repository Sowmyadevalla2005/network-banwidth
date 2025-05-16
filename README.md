# Network Bandwidth Monitor

## About the Project

The Network Bandwidth Monitor is a simple application that allows users to track internet speed (both download and upload) in real-time.

## Key Features

- **Real-Time Speed Monitoring**: Tracks both download and upload speeds.
- **User-Friendly Interface**: Displays internet usage and speeds in an easy-to-read format.
- **Cross-Platform Compatibility**: Works seamlessly on Windows and Linux.

## How It Works

1. **Data Collection**: `speed_test.py` utilizes the speedtest module to measure internet speeds and ping.
2. **Data Retrieval**: `fetch_data()` in `app.py` pulls speed data from an SQLite database.
3. **Graph Preparation**: `create_graph()` converts data to JSON format for use with Plotly.
4. **Data Rendering**: `index()` in `app.py` passes JSON data to `index.html`, enabling frontend plotting.

## Tech Stack

- **Backend**: Python (Flask), SQLite
- **Frontend**: HTML, CSS, JavaScript (Plotly for graphing)

## Benefits

- **Real-Time Monitoring**: Provides instant access to internet speed data.
- **User-Friendly Design**: Offers a simple and intuitive interface.
- **Persistent Stats**: Saves data across sessions.
- **Customizable**: Editable configuration file for user preferences.
- **Portable**: Can be packaged as a standalone app.

## File Structure
<pre>
network-bandwidth-monitor/
│
├── __pycache__/          # Python bytecode cache (auto-generated)
│
├── templates/            # Flask HTML templates
│   └── index.html        # Main dashboard page
│
├── app.py                # Main Flask application
├── favicon.ico           # Website icon
├── speed_test.py         # Speed test functionality
├── speedtest.db          # SQLite database
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── .gitignore            # Version control ignore rules
</pre>

## How to Run

### Prerequisites
- Python 3.7+
- pip package manager
## Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/network-bandwidth-monitor.git
cd network-bandwidth-monitor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
First terminal (Flask server):
```bash
python app.py
```

Second terminal (Speed test monitor):
```bash
python speed_test.py
```

### 4. Access the dashboard
Open in your browser:
```
http://localhost:5000
```
