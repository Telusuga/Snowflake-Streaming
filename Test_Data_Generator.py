# %%
!pip install Faker
# %%
import csv
from faker import Faker

# Function to generate fake data
def generate_fake_data(num_records=10):
    """Generates a list of dictionaries containing fake data."""
    fake = Faker() # Initialize Faker within the function or pass it as an argument
    data_holder = []
    try:
        for i in range(num_records):
            d = {}
            d['Id'] = i
            d['name'] = fake.name()
            d['phone_number'] = fake.phone_number()
            d['email'] = fake.email()
            d['address'] = fake.address()
            d['country'] = fake.country()
            d['job'] = fake.job()
            data_holder.append(d)
        print('Data Generation completed')
        return data_holder
    except Exception as e:
        print(f'Data Generation failed due to the following error--> {e}')
        return None # Return None or an empty list to indicate failure

# Function to write data to a CSV file
def write_to_csv(data, filename, fieldnames):
    """Writes a list of dictionaries to a CSV file."""
    if data is None: # Check if data generation was successful
        print("No data to write to CSV.")
        return

    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print('Data writing completed')
    except Exception as e:
        print(f'Data writing failed due to the following error--> {e}')

# --- Main execution ---

# Define field names outside the function if they are constant
field_name = ['Id', 'name', 'phone_number', 'email', 'address', 'country', 'job']
csv_filename = 'fake_data_2.csv'

# Generate data
generated_data = generate_fake_data(num_records=10)

# Write data to CSV
write_to_csv(generated_data, csv_filename, field_name)

# %%
