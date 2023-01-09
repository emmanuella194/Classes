#num1 = 3
#num2 = 4

#num3 = num1 + num2

#print(num3)

#class First:
   # pass

#Fr = First

#print(type(First))
#print(type(Fr))
#an attribute is a characteristics of an object

#import sys
#def function():
 # pass

#print(type(1))
#print(type(""))
#print(type([]))
#print(type({}))

#import csv

#def __init__(filename):
    #mylist = []
    #with open(filename) as numbers:
     # numbers_data = csv.reader(numbers,delimiter=',')

     # next(numbers_data)#skipped the data,i.e to skip the header title
     # for row in numbers_data:
      #   mylist.append(row)
       #  return mylist
#new_list = __init__(filename)
#for row in new_list:
  # print(row)

#using the class .collect and .extract
import csv

class collect:
    def __init__(self, row):
        self.state = row['state']
        self.position = row['position']
        self.age = row['age']

class DataCollection:
    def __init__(self):
        self.data_list = []
    
    def collect(self, file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            self.data_list = [Data(row) for row in reader]
    
    def extract(self):
        for data in self.data_list:
            print(f'state: {data.state}, position: {data.position}, age: {data.age}')

data_collection = DataCollection()
data_collection.collect('data.csv')
data_collection.extract()
#This code defines a Data class that represents a single row of data in the CSV file,
 #with attributes for the name, age, and country fields. 
 #It also defines a DataCollection class that has a collect method to accept a file path
 # and a extract method to iterate over the rows of data and print them.

#To use this code, you can create a `DataCollection


import csv

class collect:
    def __init__(self, row):
        self.state = row['state']
        self.position = row['position']
        self.age = row['age']

class DataCollection:
    def __init__(self):
        self.data_list = []
    
    def collect(self, file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            self.data_list = [row for row in reader]
    
    def extract(self):
        for i in self.data_list:
            for k, v in i.items():
                print(k, v)

data_collection = DataCollection()
data_collection.collect('file.csv')
data_collection.extract()
