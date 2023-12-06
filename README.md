# BuiltWithCli

# Description

**BuiltWithCli** - interface cli to find domains linked to a domain by tags via builtwith.com

Tool for all my buddies who want to quickly **find an organization's domains** by starting with the main domain and using [builtwith.com](https://builtwith.com)'s **analytics code/tag relationship** function.

It quickly **parse out domains that no longer exist**, **removing duplicates** and sorting by the date when the analytic tag was last linked to the main domain.

Basically for all my neighborhood guys who are too lazy to read the doc / use the api / pay the api ([TLDR](https://twitter.com/gf_256/status/1716645916285768121))

# Requirements

- [Python 3](https://www.python.org/download/releases/3.0/)

- beautifulsoup4 `pip install beautifulsoup4`

- Requires an account on [https://builtwith.com](https://builtwith.com) to get the **BWSSON** cookie 

# Usage

bultwithcli can be run from the CLI and rapidly embedded within existing python applications.

Put the main domain name after the `-d` argument and the **BWSSON cookie value** after the `-c` argument.

```bash
usage: bultwithcli.py [-h] -d DOMAIN -c COOKIE

options:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Domain to search
  -c COOKIE, --cookie COOKIE
                        Cookie or path to cookie file

Examples:
  ./bultwithcli.py -d google.com -c cookies.txt
```

# Demo

![](https://cdn.discordapp.com/attachments/890363963483758644/1182040569216782448/Capture.PNG)
