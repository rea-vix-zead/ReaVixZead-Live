const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
function closeMenu() {
  nav.removeAttribute('data-open');
  menuButton.setAttribute('aria-expanded', 'false');
  menuButton.setAttribute('aria-label', '開啟導覽選單');
}
menuButton?.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  nav.toggleAttribute('data-open', open);
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? '關閉導覽選單' : '開啟導覽選單');
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menuButton?.getAttribute('aria-expanded') === 'true') {
    closeMenu();
    menuButton.focus();
  }
});
nav?.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
let toastTimer;
document.querySelector('[data-copy-email]')?.addEventListener('click', async event => {
  const toast = document.querySelector('.toast');
  try {
    await navigator.clipboard.writeText(event.currentTarget.dataset.copyEmail);
    toast.textContent = '信箱已複製，可以貼到你的郵件程式。';
  } catch {
    toast.textContent = '無法自動複製，請選取上方信箱，或按「寄信給我」。';
  }
  toast.hidden = false;
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => { toast.hidden = true; }, 4500);
});
