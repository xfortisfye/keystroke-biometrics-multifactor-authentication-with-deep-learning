# chmod +x <file> 

# if pip install -r requirements.txt; then
#      echo “Success”
# else
#      echo “Failure, exit status: $?”
# fi

virtualenv env
source env/bin/activate
pip install pynput
pip install captcha
pip install pyinstaller
pip install jupyterlab
pip install pandas
pip install numpy
pip install matplotlib
pip install seaborn
pip install sklearn
pip install tensorflow
pip install keras
pip freeze > requirements.txt


