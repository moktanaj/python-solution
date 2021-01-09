
# set base image (host OS)
FROM python:3.9


## output folder were json file and other dumps are written
VOLUME /app/output


# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY . /app

# install dependencies
RUN pip install -r requirements.txt && \
    ls -ltra && \
    echo "Running unit tests" && \
    /usr/local/bin/pytest -v -s



# command to run on container start
ENTRYPOINT [ "/usr/local/bin/python3", "main.py" ]
