FROM postgres:15

RUN apt-get update && apt-get install -y \
    postgresql-server-dev-15 \
    git make g++ \
    && git clone --branch v0.7.4 https://github.com/pgvector/pgvector.git \
    && cd pgvector && make && make install \
    && rm -rf /var/lib/apt/lists/* /pgvector
