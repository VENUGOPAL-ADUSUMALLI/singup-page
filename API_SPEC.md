# API Specification - Signup Endpoint

## Overview
This document describes the Signup API endpoint for the Builder Backend application.

## Base URL
- **Development**: `http://localhost:8000`
- **Production**: `https://api.example.com`

---

## Signup Endpoint

### Create User Account

**Endpoint:** `POST /signup/`

**Description:** Register a new user account with email, password, name, and preferred language.

### Request

**Method:** `POST`

**Content-Type:** `application/json`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!",
  "confirm_password": "SecurePassword123!",
  "name": "John Doe",
  "Preferred_language": "English"
}
```

**Request Parameters:**

| Parameter | Type | Required | Description | Constraints |
|-----------|------|----------|-------------|-------------|
| `email` | string (email) | Yes | User's email address | Must be unique, valid email format |
| `password` | string | Yes | User's password | Minimum 1 character |
| `confirm_password` | string | Yes | Password confirmation | Must match `password` |
| `name` | string | Yes | User's full name | Maximum 255 characters |
| `Preferred_language` | string | Yes | User's preferred language | Maximum 255 characters |

### Response

#### Success Response (201 Created)

**Status Code:** `201 Created`

**Response Body:**
```json
{
  "message": "Account created successfully"
}
```

**Example:**
```bash
curl -X POST http://localhost:8000/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "password": "SecurePassword123!",
    "confirm_password": "SecurePassword123!",
    "name": "John Doe",
    "Preferred_language": "English"
  }'
```

#### Error Responses

##### 400 Bad Request - Password Mismatch

**Status Code:** `400 Bad Request`

**Response Body:**
```json
{
  "error": "Passwords do not match"
}
```

**Example:**
```json
{
  "email": "user@example.com",
  "password": "Password123",
  "confirm_password": "DifferentPassword",
  "name": "John Doe",
  "Preferred_language": "English"
}
```

##### 500 Internal Server Error

**Status Code:** `500 Internal Server Error`

**Response Body:**
```json
{
  "error": "An error occurred while creating the account"
}
```

### User Model

The created user object has the following structure:

```json
{
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "Preferred_language": "English",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**User Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `user_id` | UUID | Unique identifier (auto-generated) |
| `name` | string | User's full name |
| `email` | string | User's email address (unique) |
| `password` | string | Hashed password (not returned in responses) |
| `Preferred_language` | string | User's preferred language |
| `created_at` | datetime | Account creation timestamp |

---

## Testing

### Using cURL

```bash
# Successful signup
curl -X POST http://localhost:8000/signup/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "TestPassword123",
    "confirm_password": "TestPassword123",
    "name": "Test User",
    "Preferred_language": "English"
  }'
```

### Using Python requests

```python
import requests

url = "http://localhost:8000/signup/"
data = {
    "email": "test@example.com",
    "password": "TestPassword123",
    "confirm_password": "TestPassword123",
    "name": "Test User",
    "Preferred_language": "English"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
```

### Using JavaScript (fetch)

```javascript
fetch('http://localhost:8000/signup/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    email: 'test@example.com',
    password: 'TestPassword123',
    confirm_password: 'TestPassword123',
    name: 'Test User',
    Preferred_language: 'English'
  })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
```

---

## Notes

- The endpoint does not require authentication
- Email addresses must be unique across all users
- Passwords are stored in the database (consider hashing in production)
- The `user_id` is automatically generated as a UUID
- The `created_at` timestamp is automatically set when the account is created

