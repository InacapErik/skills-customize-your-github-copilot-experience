# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework. Practice defining routes, request validation, CRUD operations, and API documentation with Pydantic models.

## 📝 Tasks

### 🛠️ Initialize a FastAPI App

#### Description
Create a simple FastAPI application with a root route and a route for retrieving an item by ID.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a root route at `/` that returns a welcome JSON message.
- Add a route at `/items/{item_id}` that returns the requested item details.
- Use path parameter validation for `item_id`.


### 🛠️ Build CRUD Endpoints

#### Description
Implement create, read, update, and delete endpoints for a small in-memory data store.

#### Requirements
Completed program should:

- Define a Pydantic model named `Item` with `id`, `name`, `description`, and `price` fields.
- Implement the following routes:
  - `GET /items/` to return all items.
  - `POST /items/` to add a new item.
  - `PUT /items/{item_id}` to update an existing item.
  - `DELETE /items/{item_id}` to remove an item.
- Return proper HTTP status codes and errors using `HTTPException` when an item is not found.


### 🛠️ Add Query Parameters and Validation

#### Description
Enhance the API with query parameters, optional fields, and automatic documentation.

#### Requirements
Completed program should:

- Add a route at `/search/` that accepts optional query parameters like `q` and `max_price`.
- Use Pydantic validation for request data and response models.
- Include example data so the API documentation is easy to test in the browser.
- Verify the API docs are available at `/docs` and the OpenAPI schema at `/openapi.json`.
