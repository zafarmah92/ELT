FROM python:3.10-slim

# Change working directory
WORKDIR /usr/src/app
ENV DAGSTER_HOME=/usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy source code
COPY docker/dagster.yaml workspace.yaml .
COPY ownerjobs ./ownerjobs
COPY dbt_project ./dbt_project

CMD ["dagit", "-w", "workspace.yaml", "-h", "0.0.0.0", "-p", "3333"]
 