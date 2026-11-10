const music = document.querySelector('[data-site-music]');
const audio = music.querySelector('audio');
const musicButton = music.querySelector('button');
const action = music.querySelector('[data-music-action]');
const storageKey = 'rea-site-music';

let saved = {};
try {
  saved = JSON.parse(sessionStorage.getItem(storageKey)) || {};
} catch {
  // Playback still works when session storage is unavailable.
}

let optedOut = saved.paused === true;
audio.volume = 0.25;

function saveMusic() {
  try {
    sessionStorage.setItem(storageKey, JSON.stringify({
      paused: optedOut,
      position: audio.currentTime || saved.position || 0,
    }));
  } catch {
    // Playback does not depend on session storage.
  }
}

function playMusic() {
  // When autoplay is blocked, the play button remains available.
  audio.play().catch(() => {});
}

audio.addEventListener('loadedmetadata', () => {
  if (Number.isFinite(saved.position) && saved.position > 0 && saved.position < audio.duration) {
    audio.currentTime = saved.position;
  }
}, { once: true });

audio.addEventListener('play', () => { action.textContent = '暫停音樂'; });
audio.addEventListener('pause', () => { action.textContent = '播放音樂'; });
audio.addEventListener('error', () => {
  action.textContent = '音樂暫無法載入';
  musicButton.disabled = true;
});

musicButton.addEventListener('click', () => {
  optedOut = !audio.paused;
  if (optedOut) {
    audio.pause();
  } else {
    playMusic();
  }
  saveMusic();
});

window.addEventListener('pagehide', saveMusic);
music.hidden = false;
if (!optedOut) playMusic();
