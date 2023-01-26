from re import I
import socket
from xml.dom.minidom import Document
from xmlrpc.client import _HostType
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )
#                    ^
#                    |              ^
#                    Host           |
#                                    Port

#http://    www.dr-chuck.com    /page1.htm
#protocol            host            Document