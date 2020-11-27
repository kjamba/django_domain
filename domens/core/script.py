#!/usr/bin/python
import os, sys

#serve = sys.argv[1]
#domen = sys.argv[2]

class CreateDomen():
    domen = None
    web_server = None
    
    def save_base(self, domen, web_server):
        if web_server == 'nginx':
            self.web_server = web_server
            result = __create_domen_for_nginx()
        if web_server == 'apache':
            self.web_server = web_server
            result = __create_domen_for_apache()

            return True
        else:
            return False
       
    def __create_domen_for_nginx(self, delete_web_server = False):
        if delete_web_server:
            pass
        else:
            web_server = self.web_server
            with open('/var/domens/temlates.conf', 'r') as f:
                new_file = f.read().replace('###domen###', '%s' % domen)
            os.popen('sudo /usr/bin/mkdir /var/domens/%s' % domen).read()
            os.popen('sudo /usr/bin/echo "%s" > /var/domens/%s/index.html' % (domen,domen)).read()
            with open('/etc/nginx/sites-available/%s' % domen, 'w') as f:
                f.write(new_file)
            os.popen('sudo /usr/bin/ln -s /etc/nginx/sites-available/%s /etc/nginx/sites-enabled/' % domen).read
            os.popen('/etc/init.d/nginx restart').read()
        pass
    
    def __create_domen_for_apache(self, delete_web_server = False):
        with open('/var/domensApache/temlates.conf', 'r') as f:
            new_file = f.read().replace('###domen###', '%s' % domen)
        os.popen('sudo /usr/bin/mkdir /var/domensApache/%s' % domen).read()
        os.popen('sudo /usr/bin/echo "%s" > /var/domensApache/%s/index.html' % (domen,domen)).read()
        with open('/etc/apache2/sites-available/%s%s' % (domen, '.conf'), 'w') as f:
            f.write(new_file)
        os.popen('sudo /usr/bin/ln -s /etc/apache2/sites-available/%s%s /etc/apache2/sites-enabled/' % (domen, '.conf')).read
        os.popen('sudo /etc/init.d/apache2 restart').read()

# def inputWeb():
    # #serve = input('Please choose apache or nginx: ')
    # #print(serve)
    
    # if serve == u'apache':
        # print (1)
        # print(serve)
        # apache();
    # else:
        # print(2)
        # print(serve)
        # nginx();
    # return serve[0]
    
def __apache():
    #domen = sys.argv[2]
    #domen=input("Enter site's name:  ")
    with open('/var/domensApache/temlates.conf', 'r') as f:
        new_file = f.read().replace('###domen###', '%s' % domen)
    os.popen('sudo /usr/bin/mkdir /var/domensApache/%s' % domen).read()
    os.popen('sudo /usr/bin/echo "%s" > /var/domensApache/%s/index.html' % (domen,domen)).read()
    with open('/etc/apache2/sites-available/%s%s' % (domen, '.conf'), 'w') as f:
        f.write(new_file)
    os.popen('sudo /usr/bin/ln -s /etc/apache2/sites-available/%s%s /etc/apache2/sites-enabled/' % (domen, '.conf')).read
    os.popen('sudo /etc/init.d/apache2 restart').read()
#if __name__ == "__main__":
#    main()
    
def nginx():
    #domen=sys.argv[2]
    with open('/var/domens/temlates.conf', 'r') as f:
        new_file = f.read().replace('###domen###', '%s' % domen)
    os.popen('sudo /usr/bin/mkdir /var/domens/%s' % domen).read()
    os.popen('sudo /usr/bin/echo "%s" > /var/domens/%s/index.html' % (domen,domen)).read()
    with open('/etc/nginx/sites-available/%s' % domen, 'w') as f:
        f.write(new_file)
    os.popen('sudo /usr/bin/ln -s /etc/nginx/sites-available/%s /etc/nginx/sites-enabled/' % domen).read
    os.popen('/etc/init.d/nginx restart').read()
#if __name__ == "__main__":
#    main()

# inputWeb()