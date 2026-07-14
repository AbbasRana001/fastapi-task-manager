# ---------------------------------------------------------
# TODO 1: Choose a base image
# Use an official lightweight Python image, e.g. python:3.11-slim
# ---------------------------------------------------------
FROM python:3.11-slim

# ---------------------------------------------------------
# TODO 2: Set the working directory inside the container
# Hint: use WORKDIR /app
# ---------------------------------------------------------

WORKDIR /app

# ---------------------------------------------------------
# TODO 3: Copy requirements.txt into the container
# and install dependencies with pip
# Hint: COPY requirements.txt .
#       RUN pip install --no-cache-dir -r requirements.txt
# ---------------------------------------------------------

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------------------
# TODO 4: Copy the rest of the app code into the container
# ---------------------------------------------------------

COPY . .

# ---------------------------------------------------------
# TODO 5: Expose the port FastAPI/uvicorn will run on
# Hint: EXPOSE 8000
# ---------------------------------------------------------

EXPOSE 8000

# ---------------------------------------------------------
# TODO 6: Set the command to run the app with uvicorn
# Hint: CMD ["uvicorn", "task_manager_starter:app", "--host", "0.0.0.0", "--port", "8000"]
# ---------------------------------------------------------

CMD ["uvicorn", "task_manager_starter:app", "--host", "0.0.0.0", "--port", "8000"]


