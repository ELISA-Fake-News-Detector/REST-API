# `ELISA - The AI for News Reliability`

This repo contains the backend code of ELISA developed using Django REST Framework.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Demo
<a href="http://elisatheai.me">ELISA</a>

## Installation of packages

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```
## Database and static files setup
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

## Running server

```bash
python manage.py runserver
```

## URLs at localhost:8000
 * /admin
 * /api/article
 * /api/post
 * /api/feedback
 * /api/docs


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Credits
  * Clickbait detection approach used from <a href="https://github.com/saurabhmathur96/clickbait-detector">this repo</a>.
  * Fake news predictor method has been inspired from <a href="https://github.com/Cisco-Talos/fnc-1">Fake News Challenge - Team SOLAT IN THE SWEN</a>.
