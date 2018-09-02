cd server
sudo dnf install -y pylint
python -m venv ~/venv
source ~/venv/bin/activate
pip install --upgrade pip
pip install django-cors-headers
pip install Pillow
python manage.py makemigrations backend
python manage.py migrate