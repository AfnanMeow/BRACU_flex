let videos = document.querySelectorAll("video");  // ✅ Get all video elements
let watchTime = parseInt(document.getElementById("userWatchTime").value) || 0;
let watchTracker;
let activeVideo = null;  // Track currently playing video

videos.forEach((video) => {
    video.addEventListener("play", function () {
        if (activeVideo && activeVideo !== video) {
            activeVideo.pause();  // Pause other videos when a new one plays
        }
        activeVideo = video;
        startTracking();
    });

    video.addEventListener("pause", function () {
        stopTracking();
    });
});

function playPause() {
    if (activeVideo) {
        if (activeVideo.paused) {
            activeVideo.play();
        } else {
            activeVideo.pause();
        }
    }
}

function skip(seconds) {
    if (activeVideo) {
        activeVideo.currentTime += seconds;
    }
}

function startTracking() {
    stopTracking();  // Prevent duplicate intervals
    watchTracker = setInterval(() => {
        watchTime += 1; // Track every second
        document.getElementById("watchTime").innerText = Math.floor(watchTime / 60);
        sendWatchTimeToServer();
    }, 1000);
}

function stopTracking() {
    clearInterval(watchTracker);
}

function sendWatchTimeToServer() {
    console.log("Attempting to send watch time:", watchTime);
    
    fetch('/update-watch-time/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
        body: JSON.stringify({ watch_time: watchTime })
    })
    .then(response => response.json())
    .then(data => {
        console.log("✅ Watch time updated successfully:", data);
    })
    .catch(error => {
        console.error("❌ Error sending watch time:", error);
    });
}

function getCSRFToken() {
    return document.cookie.split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}

// Stop tracking when user leaves the page
window.addEventListener("beforeunload", stopTracking);
