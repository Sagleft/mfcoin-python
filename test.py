from jsonrpc import ServiceProxy

access = ServiceProxy("http://admin:passqt@127.0.0.1:22823")
access.getinfo()
# что-то не работает. не может найти ServiceProxy в jsonrpc
# разобраться позже