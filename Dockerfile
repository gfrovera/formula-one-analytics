FROM ubuntu:22.04

ENV LANG=C.UTF-8

# updating and installing packages
# Updating and installing necessary packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        --no-install-recommends \
        gnupg gnupg2 gnupg1 \
        software-properties-common \
        openssh-client

# Add deadsnakes PPA
RUN add-apt-repository ppa:deadsnakes

# Install Python 3.11
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
        --no-install-recommends \
        python3.11 \
        python3.11-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# configure python venv and install packages
COPY requirements.txt /tmp/

ENV PATH=/venv/bin:$PATH
RUN python3.11 -m venv /venv && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt
# config working directory, project files, volume
WORKDIR /fomula_one_project

COPY . .
