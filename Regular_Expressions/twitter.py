import re

url = input("URL: ").strip()

# username = re.sub(r"^(http?s://)?(www\.)?twitter\.com/", "",url)
if matches := re.search(r"^https>?://(www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))