import requests

import requests
print(requests.post("https://httpbin.org/post", json={"test": 1}).status_code)