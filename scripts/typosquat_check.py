import re
import sys

POPULAR = [
    "requests", "flask", "django", "numpy", "pandas", "urllib3", "setuptools",
    "pyyaml", "jinja2", "werkzeug", "gunicorn", "click", "markupsafe",
    "itsdangerous", "blinker", "certifi", "idna", "charset-normalizer", "boto3",
    "botocore", "cryptography", "pytest", "pillow", "sqlalchemy", "scipy",
    "matplotlib", "beautifulsoup4", "lxml", "colorama", "six", "pip", "wheel",
    "packaging", "attrs", "typing-extensions", "python-dateutil", "pytz",
]


def norm(name):
    return re.sub(r"[-_.]+", "-", name.lower())


def lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


suspects = 0
for line in open(sys.argv[1], encoding="utf-8"):
    line = line.strip()
    if not line or line.startswith(("#", "-")):
        continue
    name = norm(re.split(r"[=<>!~\[; ]", line, maxsplit=1)[0])
    if name in POPULAR:
        print(f"OK       {name}")
        continue
    limit = 1 if len(name) <= 5 else 2
    best = min(POPULAR, key=lambda p: lev(name, p))
    dist = lev(name, best)
    if dist <= limit:
        print(f"SUSPECT  {name}  (very similar to '{best}', distance {dist})")
        suspects += 1
    else:
        print(f"unknown  {name}  (not in the list, check manually)")

sys.exit(1 if suspects else 0)
