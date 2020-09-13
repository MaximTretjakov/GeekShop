rm -rf venv
mkvirtualenv venv --python=/usr/bin/python3.7
pip install -r requirements.txt
python manage.py collectstatic
