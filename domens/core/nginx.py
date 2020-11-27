import os

def main_nginx(domen):
    with open('/var/domens/temlates.conf', 'r') as f:
        new_file = f.read().replace('###domen###', '%s' % domen)
    os.popen('sudo /usr/bin/mkdir /var/domens/%s' % domen).read()
    os.popen('sudo /usr/bin/echo "%s" > /var/domens/%s/index.html' % (domen,domen)).read()
    with open('/etc/nginx/sites-available/%s' % domen, 'w') as f:
        f.write(new_file)
    os.popen('sudo /usr/bin/ln -s /etc/nginx/sites-available/%s /etc/nginx/sites-enabled/' % domen).read
    os.popen('/etc/init.d/nginx restart').read()