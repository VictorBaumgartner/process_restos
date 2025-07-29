import json
import os

def clean_and_rename_store_data(data):
    """
    Cleans and renames fields in a list of health food store data dictionaries.

    Args:
        data (list): A list of dictionaries, where each dictionary represents
                     a store's information.

    Returns:
        list: A new list of dictionaries with cleaned and renamed fields.
    """
    cleaned_data = []
    for item in data:
        new_item = {
            "name": item.get("Title"),
            "url": item.get("Title_URL"),
            "image_url": item.get("Image"),
            "rating": item.get("mr1"), # Main rating
            "review_count": item.get("flex4").replace("(", "").replace(")", "") if item.get("flex4") else None, # Reviews count
            "store_type": item.get("lineclamp1"), # e.g., "Health Food Store"
            "status": item.get("flex1"), # Open/Closed status
            "description": item.get("textgray800"), # Full description
            "phone_number": item.get("Number").replace("tel:", "") if item.get("Number") else item.get("Number3"), # Try Number first, then Number3
            "address": item.get("fontnormal"),
            "website": item.get("Field2"),
            "main_image_url_field5": item.get("Field5") # Keeping this as it seems to be an image URL
        }
        cleaned_data.append(new_item)
    return cleaned_data

def main():
    input_file_name = "vegan_resto2.json"
    output_file_name = "cleaned_health_food_stores.json"

    if not os.path.exists(input_file_name):
        print(f"Error: Input file '{input_file_name}' not found in the current directory.")
        print(f"Please make sure '{input_file_name}' is in the same folder as this script.")
        return

    try:
        with open(input_file_name, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{input_file_name}'. Please ensure it's a valid JSON file.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading '{input_file_name}': {e}")
        return

    if not isinstance(raw_data, list):
        print(f"Warning: The root of '{input_file_name}' is not a list. The script expects a JSON array of store objects.")
        if isinstance(raw_data, dict):
            print("Attempting to process it as a single store object within a list.")
            raw_data = [raw_data]
        else:
            print("Error: The script cannot process the input JSON format. It must be a list of objects or a single dictionary object.")
            return

    processed_data = clean_and_rename_store_data(raw_data)

    try:
        with open(output_file_name, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, indent=4, ensure_ascii=False)
        print(f"Successfully processed data from '{input_file_name}' and saved to '{output_file_name}' in the current directory.")
    except Exception as e:
        print(f"An error occurred while writing the output file '{output_file_name}': {e}")

if __name__ == "__main__":
    main()