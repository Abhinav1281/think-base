-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS vector;

-- =========================
-- Documents table
-- =========================
CREATE TABLE IF NOT EXISTS documents (
    document_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    title TEXT NOT NULL,
    source TEXT,
    author TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- Chunks table
-- =========================
CREATE TABLE IF NOT EXISTS chunks (
    chunk_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID REFERENCES documents(document_id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    embedding VECTOR(768),     -- adjust dim depending on model
    token_count INT,
    position INT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- =========================
-- Runs table (observability)
-- =========================
CREATE TABLE IF NOT EXISTS runs (
    run_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    query TEXT NOT NULL,
    response JSONB,
    citations JSONB,
    latency_ms INT,
    created_at TIMESTAMP DEFAULT NOW()
);
