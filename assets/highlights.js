// Both pages follow this playlist; add future videos to it on YouTube.
const highlightPlaylistId = 'PLDTGe-7_gr4g';

document.querySelectorAll('[data-youtube-highlight]').forEach(section => {
  if (!highlightPlaylistId) return;
  const embedPath = 'videoseries?list=' + encodeURIComponent(highlightPlaylistId);

  const player = document.createElement('iframe');
  player.src = 'https://www.youtube-nocookie.com/embed/' + embedPath;
  player.title = '杰德精華播放清單';
  player.loading = 'lazy';
  player.allowFullscreen = true;
  player.referrerPolicy = 'strict-origin-when-cross-origin';

  const frame = section.querySelector('[data-highlight-player]');
  frame.append(player);
  frame.hidden = false;
  section.querySelector('[data-highlight-placeholder]').hidden = true;
});
