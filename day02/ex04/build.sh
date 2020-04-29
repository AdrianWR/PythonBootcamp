PACKAGE_DIR=. 

mkdir -p $PACKAGE_DIR/ai42
mkdir -p $PACKAGE_DIR/ai42/logging

mv progressbar.py $PACKAGE_DIR/ai42
mv log.py $PACKAGE_DIR/ai42/logging
touch $PACKAGE_DIR/ai42/__init__.py

python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
