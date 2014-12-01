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

Example Usage
-------------

Setup your phone to turn on lights when your alarm goes off using the following setup

 * SleepAsAndroid (Alarm Clock)
 * Tasker (for Automation)
 * UDP Sender (for sending UDP messages)

Create a new system event in taskter for ``Intent Received``. 
From [their API](https://sites.google.com/site/sleepasandroid/doc/developer-api), use
the intent ``com.urbandroid.sleep.alarmclock.ALARM_ALERT_START``. 
Then add a new Task to send a message using UDP Sender!
