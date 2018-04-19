from multiprocessing import managers


class MysterySignManager(managers.BaseManager):

    def __init__(self, init=False):
        managers.BaseManager.__init__(self, address=('127.0.0.1', 9999),
                                      authkey='mong')
        if init:
            self.register("MysterySignWebServer",
                          MysterySignWebServer,
                          exposed=['sendMessage',
                                   'start',
                                   'isAlive'])

        else:
            self.register("MysterySignWebServer")
            self.connect()


class MysterySignWebServer(threading.Thread):

    __metaclass__ = g2sUtility.Singleton

    def __init__(self):
