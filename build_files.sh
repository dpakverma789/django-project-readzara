echo "======> INSTALLING REQUIREMENTS <======"
pip install -r requirements.txt
echo "======> REQUIREMENTS INSTALLED <======"

echo "======> COLLECTING STATIC FILES <======"
python3.9 manage.py collectstatic --noinput --clear
echo "======> STATIC FILES COLLECTED <======"