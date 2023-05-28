FROM library/python
WORKDIR /hub-finder-demo
ADD . /hub-finder-demo
RUN pip install --trusted-host pypi.python.org -r requirements.txt
WORKDIR /hub-finder-demo