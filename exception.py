class Error(Exception):
    """ Base exception """

    pass


class RouteNotFound(Error):
    """ Raised when not found the route """

    pass
