async function fetchStats() {
    try {
        const response = await fetch('/api/stats');
        const data = await response.json();

        document.getElementById('date-time').innerHTML = `<h2>Date & Time</h2><p>${data.date_time}</p>`;
        document.getElementById('weather').innerHTML = `<h2>Weather</h2><p>${data.weather.main.temp}°C, ${data.weather.weather[0].description}</p>`;
        document.getElementById('current-task').innerHTML = `<h2>Current Task</h2><p>${data.tasks.length > 0 ? data.tasks[0].task : 'No tasks'}</p>`;
        document.getElementById('upcoming-tasks').innerHTML = `<h2>Upcoming Tasks</h2><p>${data.tasks.slice(1).map(task => task.task).join('<br>')}</p>`;
        document.getElementById('youtube-time').innerHTML = `<h2>YouTube Time</h2><p>${data.youtube_time || 'Not available'}</p>`;
    } catch (error) {
        console.error('Error fetching stats:', error);
    }
}

// Fetch data every minute
fetchStats();
setInterval(fetchStats, 60000);
