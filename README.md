# FastAPI Minimal Template

This project is a **minimal FastAPI template** with support for:

- **SQLAlchemy** (async / ORM)
- **Alembic** (database migrations)
- **Pydantic** (data validation and serialization)
- **User registration, authentication, and authorization** (roles & rights)

It is designed to serve as a starting point for your FastAPI applications with a ready-to-use structure for auth and database setup.

---

## Environment Variables

Create a `.env` file in the root directory with the following parameters:

```env
# PostgreSQL database credentials
POSTGRES_USER=your_user        # your database username
POSTGRES_PASSWORD=your_password # your database password
POSTGRES_DB=postgres           # database name
POSTGRES_HOST=db               # database host (usually Docker service name)
POSTGRES_PORT=5432             # database port

# API / JWT settings
API_SECRET_KEY=your_api_key    # secret key for JWT signing
ALGORITHM=HS256                # JWT algorithm (or your preferred)
ACCESS_TOKEN_EXPIRE_MINUTES=30 # token expiration in minutes
```

To generate a secure key, you can use OpenSSL:
```bash
openssl rand -hex 32
```

[OpenSSL Documentation](https://www.openssl.org/docs/man1.1.1/man1/openssl.html)

## Quick Start with Docker

Build and start the application:

```bash
docker-compose up -d --build
```

## Initial Setup

> **Note:** Registration and authorization are implemented according to your project requirements.

After starting the application, you should:

1. Run scripts or migrations to **initialize roles, rights, and other initial data**.  
2. Ensure at least one admin or default user is created if needed.  
3. Adjust the registration/auth flow to fit your project logic.
