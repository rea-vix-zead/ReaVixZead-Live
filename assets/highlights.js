// Published highlights shown on the homepage and watch page.
const highlightIds = {
  video: 'IJ8tQnSIS8o',
  playlist: 'PLDTGe-7_gr4g',
};

document.querySelectorAll('[data-youtube-highlight]').forEach(section => {
  const kind = section.dataset.youtubeHighlight;
  const id = highlightIds[kind];
  if (!id) return;

  const playlist = kind === 'playlist';
  const embedPath = playlist
    ? 'videoseries?list=' + encodeURIComponent(id)
    : encodeURIComponent(id);

  const player = document.createElement('iframe');
  player.src = 'https://www.youtube-nocookie.com/embed/' + embedPath;
  player.title = playlist ? '杰德精華播放清單' : '杰德精華影片';
  player.loading = 'lazy';
  player.allowFullscreen = true;
  player.referrerPolicy = 'strict-origin-when-cross-origin';

  const frame = section.querySelector('[data-highlight-player]');
  frame.append(player);
  frame.hidden = false;
  section.querySelector('[data-highlight-placeholder]').hidden = true;
});
