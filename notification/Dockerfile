# ---- Base image ----
FROM python:3.12-slim AS base

# Prevent Python from writing .pyc and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# Create a non-root user
RUN useradd -m -u 10001 appuser

# ---- App deps layer ----
FROM base AS deps
WORKDIR /app
COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

# ---- Runtime image ----
FROM base AS runtime
WORKDIR /app
COPY --from=deps /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=deps /usr/local/bin /usr/local/bin
COPY app .

# Switch to non-root
USER appuser

# Expose the API port
EXPOSE 8000

# Start the server
CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "8000"]
