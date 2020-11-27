#!/usr/bin/python
import os

def delete_host(host, webserver):

    if webserver == "apache2":
        os.popen('/bin/rm -rf /var/domensApache/%s' % (host)).read()
        os.popen('/bin/rm /etc/%s/sites-available/%s.conf' % (webserver, host)).read()
        os.popen('/bin/rm /etc/%s/sites-enabled/%s.conf' % (webserver, host)).read()
    else:
        os.popen('/bin/rm -rf /var/domens/%s' % (host)).read()
        os.popen('/bin/rm /etc/%s/sites-available/%s' % (webserver, host)).read()
        os.popen('/bin/rm /etc/%s/sites-enabled/%s' % (webserver, host)).read()
    os.popen('/etc/init.d/%s restart' % webserver).read()
