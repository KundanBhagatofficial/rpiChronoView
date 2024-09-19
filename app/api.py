from flask import Flask, jsonify, request
from app.scheduler import Scheduler
from app.weather import Weather
from app.github_tracker import GitHubTracker
from app.youtube_tracker import YouTubeTracker
from config import Config

app = Flask(__name__)

# Initialize components
scheduler = Scheduler()
weather = Weather(api_key=Config.WEATHER_API_KEY)
github_tracker = GitHubTracker(user=Config.GITHUB_USER, repo=Config.GITHUB_REPO)
youtube_tracker = YouTubeTracker(api_key=Config.YOUTUBE_API_KEY)

@app.route('/api/stats', methods=['GET'])
def get_stats():
    stats = {
        'date_time': scheduler.get_current_time(),
        'weather': weather.get_weather(city='YourCity'),
        'tasks': scheduler.get_today_tasks(),
        'youtube_time': youtube_tracker.get_watch_time(),
        'github_tasks': github_tracker.get_issues(),
    }
    return jsonify(stats)

@app.route('/api/schedule', methods=['POST'])
def add_schedule():
    data = request.json
    date = data.get('date')
    task = data.get('task')
    details = data.get('details')

    scheduler.add_schedule(date, task, details)
    return jsonify({'message': 'Schedule added successfully'}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
