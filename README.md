# AI-Powered Financial Fraud Detection (Java)

This project is a production-inspired Java Spring Boot fraud detection platform with secure APIs, persistence, Docker deployment, and a polished analytics dashboard.

## Features

- JWT-based login/authentication
- Professional browser dashboard with moving graphics and visual analytics
- Database-backed users and fraud assessment history (H2 + JPA)
- Role-based access control (`ADMIN`, `ANALYST`)
- REST API to assess transaction fraud risk
- AI-style weighted risk scoring (behavior + profile + history signals)
- Risk classification (`LOW`, `MEDIUM`, `HIGH`)
- Action recommendation based on risk level
- Animated UI visuals: live radar, dynamic risk meter, risk distribution donut, signal flow, and particle background
- Styled investigation history table with risk badges and transitions
- Unit tests for fraud scoring logic

## Tech Stack

- Java 17
- Spring Boot 3
- Maven
- JUnit 5
- Docker
- PostgreSQL (profile-based runtime)

## Run Locally

1. Ensure Java 17+ and Maven are installed.
2. From project root:

```bash
mvn spring-boot:run
```

App starts at `http://localhost:8080`.

## Run with Docker + PostgreSQL

From project root:

```bash
docker compose up --build
```

This starts:

- `fraud-app` on `http://localhost:8080`
- `fraud-postgres` on `localhost:5432`

To stop:

```bash
docker compose down
```

## API

### POST `/api/v1/auth/login`

Sample request:

```json
{
  "username": "admin",
  "password": "admin123"
}
```

Analyst login:

```json
{
  "username": "analyst",
  "password": "analyst123"
}
```

### POST `/api/v1/fraud/assess`

Requires `Authorization: Bearer <jwt-token>`.

Accessible to: `ADMIN`, `ANALYST`.

Sample request:

```json
{
  "transactionId": "TXN-10001",
  "customerId": "CUST-209",
  "amount": 7500.00,
  "currency": "INR",
  "country": "NG",
  "deviceId": "DEVICE-99",
  "ipAddress": "10.1.2.5",
  "customerAccountAgeDays": 3,
  "transactionsLast24h": 21,
  "chargebacksLast90d": 2
}
```

### GET `/api/v1/fraud/history`

Requires `Authorization: Bearer <jwt-token>`.

Accessible to: `ADMIN` only.

Sample response:

```json
{
  "transactionId": "TXN-10001",
  "riskScore": 95.0,
  "riskLevel": "HIGH",
  "suspicious": true,
  "triggeredRules": [
    "High transaction amount",
    "Unusual high transaction velocity",
    "Very new customer account",
    "Recent chargeback history",
    "High-risk origin country",
    "Private network IP used in public transaction"
  ],
  "recommendation": "Block transaction and trigger manual review immediately."
}
```

## Test

```bash
mvn test
```

## Dashboard

- Open `http://localhost:8080`
- Login with `admin / admin123` or `analyst / analyst123`
- Submit transaction values and view fraud score response
- Use **Load Recent History (Admin)** to view the latest stored decisions
- Visual modules include:
  - Dynamic Risk Meter
  - Live Threat Radar
  - Risk Distribution Donut
  - Recent Investigations Table
  - Animated background particles and signal flow

## Database

- H2 persistent database file: `./data/frauddb`
- H2 Console: `http://localhost:8080/h2-console`
- PostgreSQL profile config: `src/main/resources/application-postgres.properties`
- Activate PostgreSQL profile locally:

```bash
mvn spring-boot:run "-Dspring-boot.run.profiles=postgres"
```

## Next Enhancements

- Add model training pipeline (XGBoost/LightGBM)
- Store transaction history in PostgreSQL
- Add Kafka for real-time event ingestion
- Add explainability (feature importance) endpoint
