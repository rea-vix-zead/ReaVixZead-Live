const campaign = document.getElementById("coupang-campaign");
if (campaign && Date.now() >= Date.parse("2026-11-01T00:00:00+08:00") && Date.now() < Date.parse("2026-11-16T00:00:00+08:00")) campaign.hidden = false;

