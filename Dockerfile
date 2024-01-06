FROM python:3.11.6

# Set the working directory inside the container to /usr/src/application
WORKDIR /usr/src/application

# Copy the requirements.txt file to the working directory
COPY requirements.txt ./ 

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire local directory into the container at /usr/src/application
COPY . .

# Command runs when the container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]