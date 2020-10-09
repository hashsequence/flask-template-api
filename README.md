## INSTALLATION 

### Ubuntu 16.04

run this command to download the package
```
curl https://www.python.org/ftp/python/3.9.0/Python-3.9.0.tar.xz --output ./Python-3.9.0.tar.xz

```

extract it to the local directory
```

tar -xvf Python-3.9.0.tar.xz
```

go into extracted directory
```
cd Python-3.9.0/
```

configure prefix to /usr/local/ or whatever path you choose to install pthon3.9 binary:
```
sudo ./configure --prefix=/usr/local/
```

run make install to install
```
sudo make install
```

install pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.9 get-pip.py
```

checking version of pip
```
$ pip --version
pip 20.2.3 from /home/avwong13/.local/lib/python3.9/site-packages/pip (python 3.9)

```

install flask
``` 
pip install flask
```

go to working directory of flask application and run:
```
flask run
```

## Python Refresher

* [python basics](notes/README.md)

## Resourses
* pytests
  * [https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/](https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)
