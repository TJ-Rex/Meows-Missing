set -o errexit

#poetry install
# pip install -r requeriments.txt

python manage.py collecstatic --no-input
python manege.py migrate