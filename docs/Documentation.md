# THINK-BASE APP

## Architecture

### DB Setup
#### DB Schema

``` -- Table for original documents
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    source VARCHAR(255),               -- where it came from (s3, api, user-upload, etc.)
    title TEXT,
    content BYTEA,                     -- raw content stored as blob
    created_at TIMESTAMP DEFAULT NOW()
);

-- Table for document chunks
CREATE TABLE chunks (
    id SERIAL PRIMARY KEY,
    document_id INT REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INT,                   -- order of chunk in the doc
    text TEXT,                         -- actual text of chunk
    embedding VECTOR(768),             -- FAISS-compatible embedding (later)
    created_at TIMESTAMP DEFAULT NOW()
);

-- Simple run log for reproducibility
CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    run_id UUID DEFAULT gen_random_uuid(),
    query TEXT,
    result JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
-- Table for original documents
CREATE TABLE documents (
    id SERIAL PRIMARY KEY,
    source VARCHAR(255),               -- where it came from (s3, api, user-upload, etc.)
    title TEXT,
    content BYTEA,                     -- raw content stored as blob
    created_at TIMESTAMP DEFAULT NOW()
);

-- Table for document chunks
CREATE TABLE chunks (
    id SERIAL PRIMARY KEY,
    document_id INT REFERENCES documents(id) ON DELETE CASCADE,
    chunk_index INT,                   -- order of chunk in the doc
    text TEXT,                         -- actual text of chunk
    embedding VECTOR(768),             -- FAISS-compatible embedding (later)
    created_at TIMESTAMP DEFAULT NOW()
);

-- Simple run log for reproducibility
CREATE TABLE runs (
    id SERIAL PRIMARY KEY,
    run_id UUID DEFAULT gen_random_uuid(),
    query TEXT,
    result JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);
```