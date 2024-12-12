# test_environments.py
import sys
import os



def test_environment():
    print("\n=== Environment Test ===")
    print(f"Python version: {sys.version}")
    print(f"Python executable: {sys.executable}")
    print(f"Current working directory: {os.getcwd()}")
    
    # Test database connection
    from pipeline.utils.db_conn import db_connection
    src_engine, dwh_engine = db_connection()
    if src_engine is not None:
        print("Database connection successful")
    else:
        print("Database connection failed")
    print("=====================\n")

if __name__ == "__main__":
    test_environment()
