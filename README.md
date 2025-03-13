# Simple Calculator Docker Image

This repository contains a Dockerized simple calculator application written in Python. The calculator supports basic arithmetic operations: addition, subtraction, multiplication, and division.

---

## **Features**
- Basic arithmetic operations: `+`, `-`, `*`, `/`.
- Interactive input for numbers and operations.
- Dockerized for easy deployment and testing.

---

## **Prerequisites**
- Docker installed on your system. [Install Docker](https://docs.docker.com/get-docker/)


## **How to Use**

### **1. Build the Docker Image**
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/ChristinaScott/Calculator_19.8.24.git
cd Calculator_19.8.24
```

Build the Docker image:
```bash
docker build -t calc-image:v1.0 .
```
### **2. Run the Docker Container**
Run the container in interactive mode:
```bash 
docker run -it calc-image:v1.0 
```

You will be prompted to enter two numbers and select an operation:
```bash 
Enter the first number: 10
Enter the second number: 5
Select operation (+, -, *, /): +
Result: 15.0
```

### **3. Run with Command-Line Arguments (Optional)**
```bash 
docker run calc-image:v1.0 python app/main.py 10 5 +
```


## **Project Structure**
```
calculator_19.08.24/
├── app/
│   ├── main.py            # Main script for the calculator
│   ├── ui.py              # Handles user input and output
│   └── operations/        # Contains arithmetic operation functions
│       ├── addition.py
│       ├── subtraction.py
│       ├── multiplication.py
│       └── division.py
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
└── README.md              # This file
```

## **Dockerfile**

### This simple `Dockerfile`  sets up the environment and runs the calclator application:

```Dockerfile 
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the application code
COPY . .

# Define the command to run the calculator
CMD ["python", "app/main.py"]
```

## **License**
This project is licensed under the MIT License. See the <span style="color:blue">LICENSE</span> file for details.

