CREATE EXTENSION IF NOT EXISTS vector;
CREATE TABLE IF NOT EXISTS patterns (
    id SERIAL PRIMARY KEY,
    fingerprint VARCHAR(32) UNIQUE,
    type VARCHAR(50),
    domain VARCHAR(50),
    pattern_summary TEXT,
    context TEXT,
    outcome TEXT,
    tags TEXT[],
    license VARCHAR(50),
    namespace VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
