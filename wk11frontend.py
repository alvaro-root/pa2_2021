import requests
import json


def main():
    host = "http://localhost:5006"
    urlpattern = "/user/"

    response = requests.post(f"{host}{urlpattern}", json={'key1': 'random value'})
    if 199 < response.status_code < 300:
        for k, v in response.headers.items():
            print(f"{k} -> {v}")

        print(f"{'=' * 50}")

        body = json.loads(response.text)

        for k, v in body.items():
            print(f"{k} -> {v}")
    else:
        print(f"Something bad happened: {response.status_code}")


if __name__ == "__main__":
    main()
