from ivy.std_api import *

class MyIvy:
    def __init__(self, appname, bus):
        self.appname = appname
        self.bus = bus

        sisreadymsg = '[%s is ready]' % self.appname
        print('Ivy will broadcast on %s ', self.bus)

        # initialising the bus
        IvyInit(self.appname,  # application name for Ivy
                sisreadymsg,  # ready message
                0,  # main loop is local (ie. using IvyMainloop)
                self.oncxproc,  # handler called on connection/disconnection
                self.ondieproc)  # handler called when a <die> message is received

        self._createbind()

        IvyStart(self.bus)

    def oncxproc(self, agent, connected):
        if connected == IvyApplicationDisconnected:
            print('Ivy application %r was disconnected', agent)
        else:
            print('Ivy application %r was connected', agent)
        print('currents Ivy application are [%s]', IvyGetApplicationList())

    def ondieproc(self, agent, _id):
        print('received the order to die from %r with id = %d', agent, _id)

    def onmsgproc(self, agent, *larg):
        print('Received from %r: [%s] ', agent, larg[0])

    def ontick(self):
        print('%s send a tick', self.appname)
        IvySendMsg('%s_tick' % self.appname)

    def _createbind(self):
        pass
        # redefine for create some bind : IvyBindMsg(self.oncreate, '^PALETTE form=(.*) x=(.*) y=(.*) couleur=(.*)')
