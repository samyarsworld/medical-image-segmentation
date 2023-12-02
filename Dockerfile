FROM python:3.8-slim-buster

RUN apt update -y && \
    apt install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /root/.cache

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install torch==2.0.0+cpu -f https://download.pytorch.org/whl/cpu/torch_stable.html \
    --upgrade accelerate \
    && pip uninstall -y transformers accelerate \
    && pip install transformers accelerate

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /root/.cache

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]