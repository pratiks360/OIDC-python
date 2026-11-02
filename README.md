<p align="center">
  <h1 align="center">🔐 OIDC Python Demo</h1>
  <p align="center">
    <strong>Minimal Flask app that protects an endpoint with an OpenID Connect access token (Keycloak-style realm).</strong>
  </p>
  <p align="center">
    <img src="https://img.shields.io/badge/Python-3-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python">
    <img src="https://img.shields.io/badge/Flask-API-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
    <img src="https://img.shields.io/badge/OpenID_Connect-flask--oidc-f78c40?style=for-the-badge&logo=openid&logoColor=white" alt="OpenID_Connect">
    <img src="https://img.shields.io/github/last-commit/pratiks360/OIDC-python?style=for-the-badge&label=Last+Commit" alt="Last Commit">
  </p>
</p>

---

## ✨ What Is This?

A proof-of-concept showing `flask-oidc` guarding a REST route: one open endpoint, one that only answers when the caller presents a valid access token issued by a local OIDC provider.

## 🔌 Endpoints

| Method | Path | Auth | Description |
|---|---|---|---|
| `GET` | `/withouttoken` | none | Returns `App Started` |
| `POST` | `/token` | Bearer access token | Returns `{"msg": "authenticated"}` |

## 🧩 How It Works

```
┌────────┐  1. login   ┌──────────────┐
│ Client │ ──────────► │ OIDC provider│  (issuer: http://localhost:8888/auth/realms/demo)
│        │ ◄────────── │  (Keycloak)  │
└───┬────┘ 2. token    └──────────────┘
    │ 3. POST /token  (Authorization: Bearer …)
    ▼
┌────────────┐  introspect  ┌──────────────┐
│ Flask app  │ ───────────► │ OIDC provider│
└────────────┘              └──────────────┘
```

## 🚀 Quick Start

**Prerequisites:** Python 3, a running OIDC provider with a `demo` realm.

```bash
git clone https://github.com/pratiks360/OIDC-python.git
cd OIDC-python
pip install flask flask-oidc
# put YOUR provider's client config in client_secrets.json
python main.py          # http://127.0.0.1:8080
```

## 🔒 Security Notes

- `client_secrets.json` is no longer committed; create it locally from your provider's client settings.
- Flask's `SECRET_KEY` comes from the `SECRET_KEY` environment variable (falls back to `change-me` for local demos only).
- `DEBUG` and non-secure cookies are on; this is a local demo, not a deployment template.

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Web** | Flask |
| **Auth** | flask-oidc (token introspection) |

---

<p align="center">
  <sub>Built with ❤️ for auth experiments.</sub>
</p>
