from flask_restful import Resource
from flask_restful.reqparse import RequestParser

from models.device_model import DeviceModel
from errors.exceptions.resource_does_not_exist import ResourceDoesNotExist

class Devices(Resource):

    """Implementation of /devices endpoint"""

    def __init__(self):
        """
        Setup the request parser

        """
        self.__parser = RequestParser()

        self.__parser.add_argument('user', type=str, required=True)
        self.__parser.add_argument('pass', type=str, required=True)

    def get(self):
        """
        GET /devices implementation

        :returns: On success, the data of all registered devices; otherwise the
                  suitable error message

        """
        args = self.__parser.parse_args()

        # request parameters
        user = args['user']
        passwd = args['pass']

        data = DeviceModel(user, passwd).get_all()
        if not data:
            raise ResourceDoesNotExist

        return data, 200
