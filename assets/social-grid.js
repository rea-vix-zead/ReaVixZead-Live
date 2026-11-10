document.querySelectorAll('.social-preview[data-script]').forEach(card => {
  const script = document.createElement('script');
  script.src = card.dataset.script;
  script.async = true;
  script.addEventListener('error', () => {
    card.querySelector('.social-hint').textContent =
      '目前無法載入站內預覽，請用上方連結查看。';
  });
  document.head.append(script);
});
