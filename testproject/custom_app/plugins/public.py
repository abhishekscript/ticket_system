
import http.client
import json

from rest_framework_simplejwt.tokens import RefreshToken


def get_refresh_token_for_instance(data):
    """Returns jwt refresh token given data"""

    conn = http.client.HTTPConnection("localhost", 5000)
    payload = json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    conn.request("POST", "/api/token/", payload, headers)
    return json.loads(conn.getresponse().read().decode("utf-8"))


def get_tokens_for_user(user):
    """Returns jwt refresh token given user instance"""

    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

