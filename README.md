wildcard_dns_proxy
==================

This is a proxying DNS server that supports wildcards in /etc/hosts.  It's not written by Real Geeks, we are just hosting it here to make it easier to install from scripts and stuff.


## Usage

Edit /etc/hosts, add:
```
    127.0.0.1 *.local
    2404:6800:8005::62 *.blogspot.com
```

start up dnsproxy(here we use Google DNS server as delegating server):

```bash
$ sudo python dnsproxy.py -s 8.8.8.8
```

Then set system dns server as 127.0.0.1, you can verify it by dig:

```bash
$ dig test.local
```

The result should contain 127.0.0.1.
