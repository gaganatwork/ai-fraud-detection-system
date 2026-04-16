# Project Overview - AI Fraud Detection

## What this project demonstrates

- Secure Java backend using Spring Boot + Spring Security + JWT
- AI-style fraud scoring workflow with risk-level classification
- Role-based access control with `ADMIN` and `ANALYST`
- Persistent storage of users and fraud assessments (JPA)
- Professional browser dashboard with moving graphics and visual analytics
- Dockerized deployment with PostgreSQL for production-style setup

## Demo Credentials

- `admin / admin123` (ADMIN)
- `analyst / analyst123` (ANALYST)

## Quick Demo Flow (2 minutes)

1. Open `http://localhost:8080`
2. Login using `admin / admin123`
3. Click **Assess Risk** to generate a fraud decision
4. Click **Load Recent History (Admin)** to show persisted records
5. Showcase dynamic visuals (radar, risk meter, donut chart, animated history table)
6. Explain that analyst role can score transactions but cannot access history

## Key API Endpoints

- `POST /api/v1/auth/login`
- `POST /api/v1/fraud/assess` (ADMIN/ANALYST)
- `GET /api/v1/fraud/history` (ADMIN only)

## How to run

- Local (H2): `mvn spring-boot:run`
- Docker + PostgreSQL: `docker compose up --build`

## Share this project

Share these files/folders together:

- `src/`
- `pom.xml`
- `README.md`
- `PROJECT_OVERVIEW.md`
- `AI_Fraud_Detection_Project_Brief.pdf`
- `Dockerfile`
- `docker-compose.yml`
- `.dockerignore`
