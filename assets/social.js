document.querySelectorAll('.social-preview').forEach(panel => {
  panel.addEventListener('toggle', () => {
    if (!panel.open) return;

    const template = panel.querySelector('template');
    if (!template) return;

    panel.querySelector('.social-embed').append(template.content.cloneNode(true));
    template.remove();

    if (panel.dataset.script) {
      const script = document.createElement('script');
      script.src = panel.dataset.script;
      script.async = true;
      script.addEventListener('error', () => {
        panel.querySelector('.social-hint').textContent =
          '目前無法載入站內預覽，請用上方連結查看。';
      });
      document.head.append(script);
    }
  });
});
