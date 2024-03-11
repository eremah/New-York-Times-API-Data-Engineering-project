
FROM python:3.9.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install pydantic[dotenv]
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]




















#WORKS BUT CAN NOT GET DB

# FROM python:3.7

# WORKDIR /usr/src/app

# COPY ./requirements.txt .

# RUN pip install pydantic[dotenv]

# RUN pip3 install -r requirements.txt

# COPY . .


# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]










