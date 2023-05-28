#import urllib
import socket
import win32serviceutil

def service_manager(action, machine, service):
    if action == 'stop':
        win32serviceutil.StopService(service, machine)
    elif action == 'start':
        win32serviceutil.StartService(service, machine)
    elif action == 'restart':
        win32serviceutil.RestartService(service, machine)
    elif action == 'status':
        if win32serviceutil.QueryServiceStatus(service, machine)[1] == 4:
            print (f"%s is happy {service}")
        else:
            print (f"%s is being a PITA {service}")

#socket.setdefaulttimeout(30)
service_manager('restart', 'localhost', 'WdNisSvc')
# try:
#     f = urllib.urlopen("http://servername:8080/")
#     print (f"Tomcat is smokin'.")
# except:
#     print (f"Tomcat is dead. Restarting the service.")
#     service_manager("restart", "servername", "Apache Tomcat")