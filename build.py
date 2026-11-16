"""Build all public pages from their reviewed HTML templates."""
from pathlib import Path

ROOT = Path(__file__).parent
BASE = "https://rea-vix-zead.github.io/ReaVixZead-Live/"
PAGES = ("index.html", "about.html", "community.html", "social.html", "schedule.html", "watch.html", "support.html")

def build():
    # Read and validate every source before writing any output.
    sources = {name: (ROOT / "templates" / name).read_text(encoding="utf-8") for name in PAGES}
    for name, content in sources.items():
        if "<main" not in content or "</html>" not in content:
            raise ValueError("Incomplete page template: " + name)
    for name, content in sources.items():
        (ROOT / name).write_text(content, encoding="utf-8", newline="\n")
    urls = "".join(f"<url><loc>{BASE}{name}</loc></url>" for name in PAGES)
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + urls + '</urlset>', encoding="utf-8", newline="\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8", newline="\n")
    (ROOT / ".nojekyll").touch()
    print(f"Built {len(sources)} pages.")

if __name__ == "__main__":
    build()
