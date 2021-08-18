# UAC Lookup

This is a little script I wrote to lookup the proper User Account Control values listed from an LDAP query. If you are viewing the UAC values, most likely you will be on a windows OS or use some sort of tool that is capable of translating this value, but if you're like me and you tend to view these results from straight-up ldap queries on the command line, it returns an integer value that you have to find some way of translating yourself.

Initially I wrote this in python to use on the command line, but I figured I'd turn it into a web app just because.

## How to use

To use this in python:

```python3
from uacrights import getRights

uac_vals = getRights(512)

```

This will return a list of assigned rights to the given value of `512`. In this case, it will return a single item: `['NORMAL_ACCOUNT']`.

To use this from a web app, you will need Docker:

```bash
sudo docker build -t . uac
sudo docker run -p 8000:8000 uac
```

Then access it by pointing your browser to `http://127.0.0.1:8000`

This docker image has also been uploaded to the docker hub, which can be viewed here: [Hub Link](https://hub.docker.com/r/agr0dan/uac_lookup).
