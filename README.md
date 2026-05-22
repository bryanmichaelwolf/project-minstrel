# Minstrel

API-first editorial workflow infrastructure for literary journals, magazines, and publishers.

## Overview

Minstrel is a modular editorial workflow platform designed for literary journals, magazines, and independent publishers.

The platform provides infrastructure for:

- submission management
- editorial workflows
- publication administration
- review pipelines
- contributor management
- payment processing
- asynchronous workflow automation

Minstrel is being developed as a frontend-agnostic, API-first system capable of supporting both independent literary journals and larger multi-publication publishing organizations.

## Design Principles

Minstrel is built around several core architectural principles:

### API-First
The platform is deisnged as a backend system with fully documented REST APIs.

### Frontend Agnostic
Minstrel is intended to support multiple frontend implementations, including custom publication websites, editorial dashboards, and third-party integrations.

### Wrokflow-Oriented
The platform models editorial and publishing operations as explicit workflow systems rather than simple CRUD applications.

### Modular Monolith Architecture
Minstrel currently follows a modular monolith architecture emphasizing domain separation, maintainability, and future scalability.

### Async-Capable Infrastructure
Background processing is powered by Celery and Redis to support notifications, file processing, payment handling, and future workflow automation.

## Technology Stack

### Backend
- Django
- Django REST Framework
- PostgreSQL
- Celery
- Redis

### Infrastructure
- Docker
- Docker Compose

### API Documentation
- OpenAPI
- DRF Spectacular
- Swagger UI
- ReDoc

## Current Features
- Dockerized development environment
- Modular Django application structure
- Publication management
- Submission workflows
- Workflow transition endpoints
- File upload support
- OpenAPI documentation
- Celery task infrastructure
- Redis-backed async processing

## Roadmap

Minstrel is being developed iteratively in architectural phases focused on long-term platform scalability and workflow extensibility.

### Completed Phases

#### Phase 1 - Foundational Infrastructure

Completed foundational backend and infrastructure setup, including:

- Dockerized development environment
- Django + DRF project architecture
- PostgreSQL integration
- Redis integration
- Celery workflow infrastructure
- Environment variable configuration
- Media upload handling
- Dependency pinning
- OpenAPI documentation setup

#### Phase 2 - Editorial Workflow Foundations

Implemented core editorial workflow systems, including:

- Publications domain models
- Submission domain models
- File upload support
- Workflow status transitions
- API endpoints for workflow actions
- Modular application structure refactor
- Initial async task execution support

#### Phase 3 - Identity & Authorization

Implemented core access & authentication systems, including:

- Accounts domain models
- JWT authentication
- Submission ownership
- Publication membership systems
- Role-based permissions
- Access control architecture

### Current Phase

#### Phase 4 - Editorial Collaboration

Planned features include:

- Reviewer assignments
- Internal editorial notes
- Blind review workflows
- Editorial discussion systems
- Workflow event logging

### Future Phases

#### Phase 5 - Payments & Platform Operations

Planned features include:

- Stripe integration
- Submission fee support
- Payment webhooks
- Refund handling
- Financial reporting

#### Phase 6 - Multi-Tenant Publishing Infrastructure

Planned features include:

- Publication isolation
- Organization support
- Tenant-aware permissions
- Publication-level branding
- Platform administration tools

## Local Development Setup

### Clone Repository

```bash
git clone <repo-url>
cd minstrel
```

---

### Configure Enviroment Variables

Create a local environment configuration file:

```bash
cp .env.example .env
```

---

### Build Containers

```bash
docker compose build
```

---

### Start Services

```bash
docker compose up
```

---

### Run Database Migrations

```bash
docker compose exec backend python manage.py migrate
```

---

### Create Superuser

```bash
docker compose exec backend python manage.py createsuperuser
```

---

### Stop Services

```bash
docker compose down
```

---

## API Documentation

Swagger UI:
https://localhost:8000/api/schema/swagger-ui/

ReDoc:
http://localhost:8000/api/schema/redoc/

## Prerequisites

- Docker
- Docker Compose
- Git

## Service Architecture

The local development environment currently includes:

- Django backend
- PostgreSQL database
- Redis broker
- Celery worker

## Development Status

Minstrel is currently under active development and is not production-ready.

## License

This project is licensed under the MIT license.







