from requests_html import HTMLSession

session = HTMLSession()
res = session.get("https://www.google.pl/search?q=samochody")

links = res.html.links
for a in links:
    if a.startswith("https"):
        print(a)