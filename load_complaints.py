from snowflake_connect import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("CREATE OR REPLACE STAGE COMPLAINTS_STAGE")

file_path = "/Users/sri/Downloads/Customer churn NLP project/complaints-2026-06-19_17_22.csv"
cur.execute(f"PUT 'file://{file_path}' @COMPLAINTS_STAGE")

print("Upload complete")
