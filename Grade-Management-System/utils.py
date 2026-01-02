import logging
import os
import json
logger = logging.getLogger(__name__)
logger_path =os.path.join(os.path.dirname(__file__), "app.log")
logging.basicConfig(filename=logger_path,encoding="utf-8",level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ids_path = os.path.join(os.path.dirname(__file__), "ids.json")

def print_and_log(type,message,also_print=None):
    if also_print:
        print(message)
    if type.lower() == "info":
        logger.info(message)
    elif type.lower() == "error":
        logger.error(message)
    elif type.lower() == "warning":
        logger.warning(message)

def generate_id(category):
    """
    Reads the current ID for the category, increments it, saves it back, and returns the new ID.
    """
    # Initialize if not exists
    if not os.path.exists(ids_path):
        initial_ids = {
            "students_id": 0,
            "courses_id": 0,
            "grades_id": 0
        }
        try:
            with open(ids_path, "w") as f:
                json.dump(initial_ids, f, indent=4)
            print_and_log("INFO", "ids.json file created and initialized", 1)
        except Exception as e:
            print_and_log("ERROR", f"Failed to initialize ids.json: {e}", 1)
            return None

    try:
        with open(ids_path, "r") as f:
            try:
                ids = json.load(f)
            except json.JSONDecodeError:
                ids = {}
        
        # Handle case where file exists but is empty or corrupted list
        if not isinstance(ids, dict):
             ids = {
                "students_id": 0,
                "courses_id": 0,
                "grades_id": 0
            }

        if category not in ids:
            ids[category] = 0
            
        ids[category] += 1
        new_id = ids[category]
        
        with open(ids_path, "w") as f:
            json.dump(ids, f, indent=4)
            
        return new_id
    except Exception as e:
        print_and_log("ERROR", f"Error generating ID for {category}: {e}", 1)
        return None