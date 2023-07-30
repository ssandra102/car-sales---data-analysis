"""
Car details

"""


import datetime
import calendar
import random
import pandas as pd
import os
import csv

# columns = ['Manufacturer', 'Model', 'Sales_in_thousands', 'Vehicle_type', 'Order Date','dealership','color','Power_perf_factor','Fuel_efficiency','Fuel_capacity','Engine_size','Horsepower','Wheelbase','Width','Length', 'Price_in_lakhs']
columns = ['Order', 'Sales_in_thousands', 'Vehicle_type', 'Order Date','dealership','color','Power_perf_factor','Fuel_efficiency','Fuel_capacity','Engine_size','Horsepower','Wheelbase','Width','Length', 'Price_in_lakhs']

car_manufac = {'Acura':[],
               'Audi':[],
               'BMW':[],
               'Buick':[],
               'Cadillac':[],
               'Chevorlet':[],
               'Chrysler':[],
               'Dodge':[],
               'Ford':[],
               'Honda':[],
               'Hyundai':[],
               'Jeep':[],
               'Lexus':[],
               'Lincoln':[],
               'Mitsubushi':[],
               'Mercury':[],
               'Mercedes-B':[],
               'Nissan':[],
               'Oldsmobile':[],
               'Plymouth':[],
               'Pontiac':[],
               'Porsche':[],
               'Saab':[],
               'Saturn':[],
               'Subaru':[],
               'Toyota':[],
               'Volkswagen':[],
               'Volvo':[]}


def generate_random_sales_in_thousands():
    
    lower_bound = 3 * 10**3  # 3 lakh in Indian numbering system
    upper_bound = 20 * 10**3  # 30 lakh in Indian numbering system
    sales = (random.randint(lower_bound, upper_bound))/10**3
    return f'{sales:.2f}'

def genrate_random_vehicle_type():
    type_ = ["passenger","car"]
    idx = random.randint(0,1)
    return type_[idx]
# print(genrate_random_vehicle_type())


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def generate_random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (rgb_to_hex((red,blue,green)))

def generate_random_order_date():
    ## generates random date after a specified 'start_year'
    start_year = 2021
    end_year = datetime.datetime.now().year

    order_year = random.randint(start_year,end_year)
    order_month = random.randint(datetime.datetime.now().month, 12)
    order_day = random.randint(1, 28)

    order_date = datetime.date(order_year, order_month, order_day)

    return order_year,order_date

def generate_random_price_in_lakhs():
    
    lower_bound = 3 * 10**5  # 3 lakh in Indian numbering system
    upper_bound = 30 * 10**5  # 30 lakh in Indian numbering system
    price = (random.randint(lower_bound, upper_bound))/10**5
    return f'{price:.2f}L'

    # Example usage:
    # random_number_in_lakhs = generate_random_price_in_lakhs()
    # print("Random Number in lakhs:", random_number_in_lakhs)

def generate_random_address():
    # street_names = ['Main', '2nd', '1st', '4th', '5th', 'Park', '6th', '7th', 'Maple', 'Pine', 'Washington', '8th', 'Cedar', 'Elm', 'Walnut', '9th', '10th', 'Lake', 'Sunset', 'Lincoln', 'Jackson', 'Church', 'River', '11th', 'Willow', 'Jefferson', 'Center', '12th', 'North', 'Lakeview', 'Ridge', 'Hickory', 'Adams', 'Cherry', 'Highland', 'Johnson', 'South', 'Dogwood', 'West', 'Chestnut', '13th', 'Spruce', '14th', 'Wilson', 'Meadow', 'Forest', 'Hill', 'Madison']
    cities = ['San Francisco', 'Boston', 'New York City', 'Austin', 'Dallas', 'Atlanta', 'Portland', 'Portland', 'Los Angeles', 'Seattle']
    weights = [9,4,5,2,3,3,2,0.5,6,3]
    zips = ['94016', '02215', '10001', '73301', '75001', '30301', '97035', '04101', '90001', '98101']
    state = ['CA', 'MA', 'NY', 'TX', 'TX', 'GA', 'OR', 'ME', 'CA', 'WA']

    # street = random.choice(street_names)
    index = random.choices(range(len(cities)), weights=weights)[0]

    return f"{random.randint(1,999)}, {cities[index]}, {state[index]}, {zips[index]}"

def write_row(order_number,Sales_in_thousands, Vehicle_type, order_date,dealership,color,Power_perf_factor,Fuel_capacity,Fuel_efficiency,Engine_size, Horsepower,Wheelbase,Width,Length, Price_in_lakhs):

    output = [order_number,Sales_in_thousands, Vehicle_type, order_date,dealership,color,Power_perf_factor,Fuel_capacity,Fuel_efficiency,Engine_size, Horsepower,Wheelbase,Width,Length, Price_in_lakhs]
    return output

if __name__ == '__main__':

    years = [2021, 2022, 2023]
    order_number = 4100134

    folder_name = "carSalesAnalysis/car_sales_data" # to store year wise data
    folder_path = "carSalesAnalysis/Output" # to store combined data
    output_file = "all_Data.csv"

    i=0

    while i<500:


        color = generate_random_color()
        product_price = generate_random_price_in_lakhs()
        dealership = generate_random_address()
        Sales_in_thousands = generate_random_sales_in_thousands()
        Vehicle_type = genrate_random_vehicle_type()
        order_year, order_date = generate_random_order_date()

        Engine_size = round(random.uniform(1, 6), 2)
        Horsepower = random.randint(150,280)
        Wheelbase = round(random.uniform(80, 110), 2)
        Width = round(random.uniform(60, 90), 2)
        Length = round(random.uniform(160,300), 2)
        Fuel_capacity = round(random.uniform(15,30), 1)
        Fuel_efficiency = random.randint(15,28)
        Power_perf_factor = round(random.uniform(30, 190), 5)

        # product_choice = random.choices(car_manufac)[0]
        
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        file_name = f"Sales_{order_year}.csv"
        file_path = os.path.join(folder_name, file_name)
        file_exists = os.path.isfile(file_path)

        with open(file_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)

            if not file_exists:
                # If the file doesn't exist, write the header (if needed).
                # header = ['Column1', 'Column2', 'Column3']  # Replace with your column headers.
                writer.writerow(columns)

            data = [[order_number,Sales_in_thousands, Vehicle_type, order_date,dealership,color,Power_perf_factor,Fuel_capacity, Fuel_efficiency,Engine_size, Horsepower,Wheelbase,Width,Length, product_price]]
            # print(type(data))
            writer.writerows(data)

        i+=1
        order_number += 1
        


    ### combine the data
    file_list = os.listdir(folder_name)
    # print(file_list)
    combined_data = []

    # Loop through each file in the folder
    for file_name in file_list:
        file_path = os.path.join(folder_name, file_name)
        if file_name.endswith('.csv') and os.path.isfile(file_path):
            with open(file_path, 'r', newline='') as csv_file:
                reader = csv.reader(csv_file)
                if combined_data:
                    next(reader)
                for row in reader:
                    combined_data.append(row)

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    output_file = os.path.join(folder_path, output_file)
    # Write the combined data to the output CSV file
    with open(output_file, 'w', newline='') as csv_output:
        writer = csv.writer(csv_output)
        writer.writerows(combined_data)


        

