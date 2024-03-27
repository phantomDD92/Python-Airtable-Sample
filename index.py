from airtable import Airtable

# Replace these with your Airtable API key, base ID, and table name
AIRTABLE_API_KEY = 'your_airtable_api_key'
AIRTABLE_BASE_ID = 'your_airtable_base_id'
AIRTABLE_TABLE_NAME = 'your_airtable_table_name'

# Initialize Airtable instance
airtable = Airtable(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME, api_key=AIRTABLE_API_KEY)

print('airtable: ', airtable)

# Function to read all records from the table
def read_records():
    try:
        records = airtable.get_all()
        print('records: ', records)
        for record in records:
            print(record['id'], record['fields'])
    except Exception as e:
        print("Error occurred while reading records:", e)

# Function to create a new record
def create_record(name, age):
    try:
        record_data = {'Name': name, 'Age': age}
        airtable.insert(record_data)
        print("Record created successfully.")
    except Exception as e:
        print("Error occurred while creating record:", e)

# Function to update a record
def update_record(record_id, name, age):
    try:
        update_data = {'Name': name, 'Age': age}
        airtable.update(record_id, update_data)
        print("Record updated successfully.")
    except Exception as e:
        print("Error occurred while updating record:", e)

# Function to delete a record
def delete_record(record_id):
    try:
        airtable.delete(record_id)
        print("Record deleted successfully.")
    except Exception as e:
        print("Error occurred while deleting record:", e)

# Example usage
if __name__ == '__main__':
    try:
        # Read all records
        print("Existing records:")
        read_records()

        # Create a new record
        create_record('John', 30)

        # Read all records after creation
        print("\nRecords after creation:")
        read_records()

        # Update a record (assuming record ID exists)
        update_record('record_id_to_update', 'Updated Name', 35)

        # Read all records after update
        print("\nRecords after update:")
        read_records()

        # Delete a record (assuming record ID exists)
        delete_record('record_id_to_delete')

        # Read all records after deletion
        print("\nRecords after deletion:")
        read_records()
    except Exception as e:
        print("An unexpected error occurred:", e)
