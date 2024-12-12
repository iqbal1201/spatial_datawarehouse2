from pipeline.extract import *
from pipeline.load import *
from pipeline.transform import *
from pipeline.utils.db_conn import *

# Execute the functions when the script is run
if __name__ == '__main__':
    
    try:
        print("Start ELT")
        


        extract()  # Ensure this function is handling None values properly

        print("ELT Success")
    except Exception as e:
        print(f"Error {e}")


    