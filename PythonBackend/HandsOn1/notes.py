"""
=========================================================
Hands-on 1
Web Framework Foundations & Django Project Setup
=========================================================
"""

# =========================================================
# Task 1
# Understand the Request-Response Cycle
# =========================================================

# 1. Journey of a GET /api/courses/ request
#
# Browser
#     |
#     | HTTP GET Request
#     V
# Django Server
#     |
# URL Router (urls.py)
#     |
# Middleware (before view)
#     |
# View (views.py)
#     |
# Model (models.py)
#     |
# Database Query
#     |
# Model returns data
#     |
# View prepares response
#     |
# Middleware (after view)
#     |
# HTTP Response
#     |
# Browser displays result


# =========================================================
# 2. Middleware
# =========================================================

# Middleware is software that processes every request
# before it reaches the view and every response before
# it is sent back to the browser.

# Built-in Middleware Examples

# SecurityMiddleware
# ------------------
# Adds security-related HTTP headers and protects
# the application against common security attacks.

# SessionMiddleware
# -----------------
# Enables session support so users can stay logged in
# across multiple requests.


# =========================================================
# 3. WSGI vs ASGI
# =========================================================

# WSGI (Web Server Gateway Interface)
#
# - Supports synchronous applications.
# - Handles one request at a time.
# - Default interface used by Django.
# - Best for normal websites.

# ASGI (Asynchronous Server Gateway Interface)
#
# - Supports asynchronous programming.
# - Can handle multiple requests concurrently.
# - Supports WebSockets and real-time applications.
# - Used for chat apps, live notifications,
#   streaming and async APIs.

# Django uses WSGI by default.
# Switch to ASGI when building asynchronous or
# real-time applications.


# =========================================================
# 4. MVC vs Django MVT
# =========================================================

# MVC
#
# Model      -> Handles database
# View       -> User Interface
# Controller -> Business Logic

# Django MVT
#
# Model      -> Database
# View       -> Business Logic
# Template   -> User Interface

# Mapping

# MVC Model       ---> Django Model
# MVC View        ---> Django Template
# MVC Controller  ---> Django View