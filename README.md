Lumos
=====

A UDP interface for bottlerocket x10 control.

Installation
------------

The following instructions are for installing on debian/ubuntu systems.

Install bottlerocket

```
sudo apt-get install bottlerocket
```

Install lumos.py

```
sudo cp lumos.py /usr/local/bin/lumos.py
sudo chmod 755 /usr/local/bin/lumos.py
```

Install Upstart Rule

```
sudo cp lumos.conf /etc/init/lumos.conf
sudo initctl reload-configuration
```
