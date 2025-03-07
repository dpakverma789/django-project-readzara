echo "======> INSTALLING REQUIREMENTS <======"
# create a virtual environment named 'venv' if it doesn't already exist
python3.9 -m venv venv

# activate the virtual environment
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "======> REQUIREMENTS INSTALLED <======"

echo "======> COLLECTING STATIC FILES <======"
python3 manage.py collectstatic --noinput
echo "======> STATIC FILES COLLECTED <======"

echo "======> MAKE-MIGRATIONS <======"
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput
echo "======> MAKE-MIGRATIONS-END <======"