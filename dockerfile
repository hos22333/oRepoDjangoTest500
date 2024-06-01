# Base Image: Use a stable Python image with slim variant to reduce size
FROM python:3.9-slim

# Set Working Directory (where your app will live)
WORKDIR /app

# Install Python Dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy App Code
COPY . /app/

# Collect Static Files (if needed)
RUN python manage.py collectstatic --noinput

# Expose Port (default for Django)
EXPOSE 8000

# Set Up Production Web Server (Gunicorn)
CMD ["gunicorn", "DjangoTest500.wsgi:application", "--bind", "0.0.0.0:8000"]
