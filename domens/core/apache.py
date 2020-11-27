import os

def main_apache(domen):
    with open('/var/domensApache/temlates.conf', 'r') as f:
        new_file = f.read().replace('###domen###', '%s' % domen)
    os.popen('sudo /usr/bin/mkdir /var/domensApache/%s' % domen).read()
    os.popen('sudo /usr/bin/echo "%s" > /var/domensApache/%s/index.html' % (domen,domen)).read()
    with open('/etc/apache2/sites-available/%s%s' % (domen, '.conf'), 'w') as f:
        f.write(new_file)
    os.popen('sudo /usr/bin/ln -s /etc/apache2/sites-available/%s%s /etc/apache2/sites-enabled/' % (domen, '.conf')).read
    os.popen('/etc/init.d/apache2 restart').read()