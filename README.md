# cdis_oauth2client

A Python module providing a Flask blueprint and associated functions for CDIS
microservices such as gdcapi.

## Installation

Requirements must be installed with:

    pip install -r requirements.txt

Then, this module can be installed with:

    python setup.py build
    python setup.py install

## Usage

```python
from flask import Flask
import cdis_oauth2client

app = Flask(__name__)
app.register_blueprint(cdis_oauth2client.blueprint)
```
