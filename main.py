import os
import re

BASE_DIR = "/Users/I742773/LearningGuide/System Design/Databases"

topics = [
    "RDBMS fundamentals",
    "NoSQL fundamentals",
    "ACID properties",
    "Database normalization and denormalization",
    "Indexing and query optimization",
    "Transactions and isolation levels",
    "Joins subqueries and relational modeling",
    "Data modeling principles and schema design",
    "Entity relationship diagrams and key constraints",
    "Sharding and horizontal partitioning",
    "Replication and failover mechanisms",
    "Consistency models strong eventual causal",
    "CAP theorem and PACELC analysis",
    "Distributed transactions and two-phase commit",
    "Data versioning and conflict resolution",
    "Query execution plans and performance tuning",
    "Caching layers and database read replicas",
    "Storage engines InnoDB RocksDB etc",
    "Columnar and row-oriented storage formats",
    "Time-series and graph databases",
    "Search engines and indexing systems Elasticsearch Solr",
    "Data lifecycle management and archival strategies",
    "Backup recovery and snapshot mechanisms",
    "Schema migration and evolution techniques",
    "Multi-region database architecture",
    "Database security and access control",
    "Database observability and monitoring tools",
    "Trade-offs between consistency latency and throughput"
]

def sanitize(text):
    text = text.replace("/", " ")
    text = text.replace(":", " ")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = re.sub(r"[^A-Za-z0-9 _-]", "", text)
    return text.strip()

os.makedirs(BASE_DIR, exist_ok=True)

for i, topic in enumerate(topics, start=1):
    safe_topic = sanitize(topic)
    file_name = f"{i:02d} - {safe_topic}.md"
    file_path = os.path.join(BASE_DIR, file_name)

    with open(file_path, "w") as f:
        f.write(f"# {topic}\n")
