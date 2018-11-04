from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'TestChat'
class ChatSession(async_chat):
    """
    处理服务器和一个用户之间连接的类
    """
    def __init__(self,server,sock):
        # 标准设置任务
        async_chat.__init__(self,sock)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        self.push('welcome to %s\r\n' % self.server.name)
    def collect_incoming_data(self,data):
        self.data.append(data)
    def found_terminator(self):
        """
        如果发现了一个终止对象，也就意味着读入了一个完整的行，将其广播给每个人
        :return:
        """
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)

class ChatServer(dispatcher):
    """
    接受连接并且产生单个回话的类。他还会处理到其他回话的广播
    """
    def __init__(self,port,name):
        # Standard setup tasks
        dispatcher.__init__()
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('',port))
        self.listen(5)
        self.name = name
        self.sessions = []
    def disconnect(self,session):
        self.sessions.remove(session)

    def broadcast(self,line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn,addr = self.accept()
        self.sessions.append(ChatSession(self,conn))

if __name__ == '__main__':
    s = ChatSession(PORT,NAME)
    try: asyncore.loop()
    except KeyboardInterrupt: print('\n')