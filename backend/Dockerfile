FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt ./
RUN python -m venv /venv \
	&& . /venv/bin/activate \
	&& pip install --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt
ENV VIRTUAL_ENV=/venv
ENV PATH="/venv/bin:$PATH"
COPY . .
ENV PYTHONUNBUFFERED=1
CMD ["python", "run.py"]
