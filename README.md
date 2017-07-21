# cdis_oauth2client

A Python module providing a Flask blueprint and associated functions for CDIS
microservices such as gdcapi.

## Installation

`cdis_oauth2client` is intended for use as a dependency of packages such as
gdcapi, and it is sufficient to list it in the `requirements.txt` where it is
needed. It can also be installed on its own using:

    pip install .

## Usage

```python
from flask import Flask
import cdis_oauth2client

app = Flask(__name__)
app.register_blueprint(cdis_oauth2client.blueprint)
```
