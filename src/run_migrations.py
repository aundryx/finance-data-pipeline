from db_connection import get_rds_connection
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sql_dir = os.path.join(BASE_DIR, "..", "sql")
migrations_dir = os.path.join(sql_dir, "migrations")

def run_migrations():
    conn = get_rds_connection()
    cursor = conn.cursor()

    migration_files = sorted(os.listdir(migrations_dir))

    for migration_file in migration_files:
        file_path = os.path.join(migrations_dir, migration_file)
        with open(file_path, "r") as f:
            cursor.execute(f.read())
            print(f"Executed migration: {migration_file}")
    
    conn.commit()
    cursor.close()
    conn.close()


if __name__ == "__main__":
    run_migrations()
            
