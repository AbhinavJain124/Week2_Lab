# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API using the FastAPI framework to understand web development concepts including routing, request handling, data validation, and API documentation. You will create a functional web service that can handle HTTP requests and return structured responses.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application with Multiple Endpoints

#### Description
Set up a FastAPI application with multiple HTTP endpoints that handle different operations. Your API should follow REST conventions and provide meaningful responses for various request types.

#### Requirements
Completed program should:

- Install and import FastAPI and Uvicorn dependencies
- Create a basic FastAPI application instance
- Implement at least 3 different endpoints (GET, POST, and DELETE)
- Define request and response models using Pydantic
- Validate incoming request data using type hints
- Include appropriate HTTP status codes for responses
- Include comprehensive docstrings and comments for clarity


### 🛠️ Add Data Persistence and Error Handling

#### Description
Enhance your API to store and manage data effectively. Implement proper error handling to provide meaningful feedback when requests fail or contain invalid data.

#### Requirements
Completed program should:

- Store and retrieve data using a simple in-memory data structure (dictionary or list)
- Implement proper validation with informative error messages
- Return appropriate HTTP status codes (200, 201, 400, 404, etc.)
- Include exception handling for missing resources and invalid operations
- Test endpoints using the interactive Swagger documentation (available at `/docs`)
