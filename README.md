# 🥗 JSON Data Cleaning and Renaming Script (Vegan Restaurants)

## Redacted by Victor

This Python script is designed to streamline and normalize raw JSON data pertaining to vegan restaurants. It renames cryptic field keys to more descriptive and human-readable names, and removes redundant or less essential information, making the data more accessible and useful for further analysis or integration.

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [⚙️ How It Works](#%EF%B8%8F-how-it-works)
- [🚀 Getting Started](#-getting-started)
  - [✔️ Prerequisites](#%EF%B8%8F-prerequisites)
  - [⬇️ Installation](#%EF%B8%8F-installation)
  - [▶️ Usage](#%EF%B8%8F-usage)
- [📥 Input JSON Format](#-input-json-format)
- [📤 Output JSON Format](#-output-json-format)
- [🤝 Contribution](#-contribution)
- [©️ License](#%EF%B8%8F-license)

---

## ✨ Features

* **Intelligent Field Renaming**: Converts obscure field names (e.g., `mr1`, `flex`, `lineclamp1`, `textgray800`) into intuitive ones (e.g., `rating`, `review_count`, `cuisine_type`, `full_description`).
* **Data Cleaning**: Strips unnecessary characters (e.g., `tel:` prefix from phone numbers, parentheses from review counts).
* **Essential Information Extraction**: Focuses on retaining only the most relevant details for each restaurant, discarding noisy or less useful fields.
* **Feature Consolidation**: Combines disparate fields (like `Field7`, `Field8`, `Field9`) into a single `features` list where applicable.
* **Automatic File Handling**: Reads from a predefined input JSON file and writes to a new, cleaned JSON file, all within the current working directory.
* **Robust Error Handling**: Includes checks for file existence, valid JSON format, and expected data structure.

---

## ⚙️ How It Works

The script operates in a few simple steps:

1.  **Locate Input File** 🔍: It looks for a JSON file named `vegan_resto.json` in the same directory where the script is executed.
2.  **Load Data** 💾: Reads the content of `vegan_resto.json` and parses it into a Python list of dictionaries.
3.  **Process Each Record** 🔄: Iterates through each restaurant's data (dictionary) in the loaded list.
    * For each restaurant, it creates a new dictionary with standardized, clear field names.
    * It extracts and cleans data from the original fields as necessary.
    * Less essential original fields are omitted from the new, cleaned record.
4.  **Save Output** ✅: Writes the entire list of processed restaurant data to a new JSON file named `cleaned_vegan_resto.json` in the current working directory, formatted for readability.

---

## 🚀 Getting Started

### ✔️ Prerequisites

* Python 3.6 or higher installed on your system.

### ⬇️ Installation

No special installation is required beyond having Python. Simply download the script file (`.py`) and place it in the directory where your JSON data resides.

### ▶️ Usage

1.  **Save the script**: Save the provided Python code as `clean_restaurants.py` (or any other `.py` name you prefer) in a folder on your computer.
2.  **Prepare your data**: Place your raw JSON data file containing vegan restaurant information in the **same folder** as the script. **Crucially, this file must be named `vegan_resto.json`**. The JSON should be an array (list) of objects, where each object represents a restaurant.
    ```json
    [
      {
        "Title": "apeti - Ségur",
        "Title_URL": "...",
        // ... more raw fields ...
      },
      {
        "Title": "Another Restaurant",
        "Title_URL": "...",
        // ... more raw fields ...
      }
    ]
    ```
    (If your JSON is a single object, the script will attempt to handle it, but a list is preferred.)
3.  **Run the script**: Open your terminal or command prompt, navigate to the folder where you saved the script and the `vegan_resto.json` file, and run the following command:

    ```bash
    python clean_restaurants.py
    ```
4.  **Check the output**: After execution, a new file named `cleaned_vegan_resto.json` will be created in the same directory, containing your beautifully organized and renamed restaurant data.

---

## 📥 Input JSON Format

The script expects an input JSON file named `vegan_resto.json` in the following general structure:

```json
[
  {
    "Title": "Restaurant Name",
    "Title_URL": "URL to restaurant page",
    "Image": "URL to main image",
    "mr1": "Rating value (e.g., '4.5')",
    "flex": "Review count (e.g., '(135)')",
    "lineclamp1": "Cuisine type (e.g., 'VeganRestaurant')",
    "flex1": "Status (e.g., 'Open Now')",
    "mlauto": "Partner status (less essential)",
    "Abstract": "Short abstract of restaurant offerings",
    "textgray800": "Detailed description of the restaurant",
    "Number": "Phone number (e.g., 'tel:+33-123456789')",
    "fontnormal_URL": "Map URL (less essential)",
    "fontnormal": "Full address",
    "wauto": "Read Reviews link text (less essential)",
    "Field1": "",
    "Field2": "Website URL (e.g., 'example.com')",
    "Field3": "Duplicate phone number (less essential)",
    "Field4": "Combined description and hours (mostly redundant)",
    "Field5": "Combined categories and description (mostly redundant)",
    "Field6_text": "Delivery text (e.g., 'Delivery')",
    "Field6_links": "Delivery service URL",
    "Field7": "Feature 1 (e.g., 'Outdoor seating')",
    "Field8": "Feature 2 (e.g., 'Accepts credit cards')",
    "Field9": "Other features (e.g., 'FriendVegan')",
    "Field10": "Duplicate review count (less essential)",
    "Field11": "Thumbnail image 1 URL",
    "Field12": "Thumbnail image 2 URL",
    "Field13": "Thumbnail image 3 URL"
  },
  // ... more restaurant objects
]

📤 Output JSON Format

The cleaned_vegan_resto.json file will contain data structured as follows:
JSON

[
  {
    "name": "Restaurant Name",
    "url": "URL to restaurant page",
    "image_url": "URL to main image",
    "rating": "Rating value (e.g., '4.5')",
    "review_count": "Cleaned review count (e.g., '135')",
    "cuisine_type": "Cuisine type (e.g., 'VeganRestaurant')",
    "status": "Open/Closed status (e.g., 'Open Now')",
    "abstract": "Short abstract of restaurant offerings",
    "full_description": "Detailed description of the restaurant",
    "phone_number": "Cleaned phone number (e.g., '+33-123456789')",
    "address": "Full address",
    "website": "Website URL",
    "delivery_link": "Delivery service URL (if available, otherwise null)",
    "features": [
      "Outdoor seating",
      "Accepts credit cards",
      "Vegan-friendly"
    ],
    "thumbnail_images": [
      "Thumbnail image 1 URL",
      "Thumbnail image 2 URL",
      "Thumbnail image 3 URL"
    ]
  },
  // ... more cleaned restaurant objects
]

🤝 Contribution

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the repository where this code is hosted. Your contributions are welcome!

©️ License

This project is open-source and available under the MIT License.
