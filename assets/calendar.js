const calendarFrame = document.querySelector('#stream-calendar');
if (calendarFrame) {
  const narrowScreen = window.matchMedia('(max-width: 600px)');
  function updateCalendarView() {
    const url = new URL(calendarFrame.dataset.calendarSrc);
    url.searchParams.set('mode', narrowScreen.matches ? 'AGENDA' : 'MONTH');
    if (calendarFrame.src !== url.href) calendarFrame.src = url.href;
  }
  updateCalendarView();
  narrowScreen.addEventListener('change', updateCalendarView);
}
