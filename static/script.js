let activeTimers = {};

function startTimer(taskId) {
    fetch(`/start_timer/${taskId}`)
        .then(response => response.json())
        .then(data => {
            activeTimers[taskId] = setInterval(() => {
                updateTimer(taskId);
            }, 1000);
        });
}

function stopTimer(taskId) {
    if (activeTimers[taskId]) {
        clearInterval(activeTimers[taskId]);
        delete activeTimers[taskId];
        fetch(`/stop_timer/${taskId}`);
    }
}

function updateTimer(taskId) {
    fetch(`/get_timer/${taskId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById(`time-${taskId}`).innerText = data.total_time;
        });
}

function exportCSV() {
    window.location.href = '/export_csv';
}

function toggleSettings() {
    const settingsOverlay = document.getElementById('settings-overlay');
    settingsOverlay.style.display = settingsOverlay.style.display === 'none' ? 'flex' : 'none';
}

function changeTheme(theme) {
    document.body.setAttribute('data-theme', theme);
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize any existing timers if needed
});