import speedtest  # This imports the speedtest-cli module
import sqlite3
import time

def measure_speed():
    s = speedtest.Speedtest()
    download = s.download()
    upload = s.upload()
    ping = s.results.ping
    return int(download), int(upload), int(ping)

def store_results(download, upload, ping):
    with sqlite3.connect('speedtest.db') as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS results (
                timestamp INTEGER PRIMARY KEY,
                download INTEGER,
                upload INTEGER,
                ping INTEGER
            )
        """)
        conn.execute("INSERT INTO results (timestamp, download, upload, ping) VALUES (?, ?, ?, ?)",
                     (int(time.time()), download, upload, ping))
        conn.commit()

if __name__ == "__main__":
    download, upload, ping = measure_speed()
    store_results(download, upload, ping)
    print(f"Download: {download} bps, Upload: {upload} bps, Ping: {ping} ms")
