import http

import connexion_buzz


class InvalidPhone(connexion_buzz.ConnexionBuzz):
    status_code = http.HTTPStatus.BAD_REQUEST
