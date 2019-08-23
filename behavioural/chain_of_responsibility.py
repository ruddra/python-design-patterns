class AbstractHandler(object):
    def __init__(self, successor):
        if successor:
            self._successor = successor

    def handle(self, request):
        handled = self._handle(request)
        if not handled:
            return self._successor.handle(request)

    def _handle(self, request):
        raise NotImplementedError()


class ConcreteHandler(AbstractHandler):
    def _handle(self, request):
        if request < 10:
            print("Handled request {} in concrete handler".format(request))
            return True
        print('Failed handling request {} in Concrete class'.format(request))
        return False


class DefaultHandler(AbstractHandler):
    def _handle(self, request):
        print('No more handler left for request {} in Default class'.format(request))
        return True


class Client:

    def __init__(self, *args, **kwargs):
        self.handler = ConcreteHandler(DefaultHandler(None))

    def delgate(self, requests):
        for request in requests:
            self.handler.handle(request)


requests = [1, 10, 100, -1000]

Client().delgate(requests)
