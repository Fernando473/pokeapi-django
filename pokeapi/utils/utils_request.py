import requests

import requests
from requests.exceptions import RequestException


def do_get(url: str, offset=0, limit=20):
    try:
        if not (isinstance(offset, int) and isinstance(limit, int) and offset >= 0 and limit >= 1):
            raise ValueError("Los valores de offset y limit deben ser enteros no negativos.")

        params = {'offset': offset, 'limit': limit}
        response = requests.get(url, params=params)
        response.raise_for_status()

        if response.status_code == 200:
            return response.json()
        else:
            raise requests.exceptions.HTTPError(f"Código de estado HTTP no exitoso: {response.status_code}")

    except ValueError as ve:
        raise ve
    except RequestException as re:
        raise re
    except Exception as e:
        raise Exception(f"Error desconocido: {str(e)}")
