#!/usr/bin/env python

import json
import mysql.connector
import pandas as pd
import yaml
from sqlquery import *

class TEST():
    def __init__(self):
        self.params = self.get_yaml_param()
        self.mysql_connect = self.get_mysql_connection()

    def get_yaml_param(self):
        yaml_path = './config.yml'
        with open(yaml_path) as file:
            params = yaml.load(file, Loader=yaml.FullLoader)
        return params

    def get_mysql_connection(self):
        mysql_connector = mysql.connector.connect(
            host = self.params["mysql_connection"]["mysql_hostname"],
            user = self.params["mysql_connection"]["mysql_username"],
            db = self.params['mysql_connection']['mysql_database'],
            password = self.params["mysql_connection"]["mysql_password"],
            port = self.params["mysql_connection"]["mysql_port"],
            autocommit = True
        )
        return mysql_connector

    def insert_tb(self):
        #read file:
        with open('../data/seqanadb_data.csv', encoding="utf-8") as csv_file:
            df = pd.read_csv(csv_file)

        print("df data ", df.head())
        #data insertion
        profile_df = df[['profile_id', 'profile_layer_id','country_name']].copy()
        print("profile df data \n ", profile_df.head())
        layers_df = df [['profile_layer_id', 'profile_id', 'upper_depth', 'lower_depth', 'layer_name']].copy()
        layers_df['layer_name']=layers_df['layer_name'].fillna('unknown')
        print("layers df data \n ", layers_df.head())
        data_points_df = df[['profile_layer_id', 'X', 'Y', 'litter']].copy()
        data_points_df['litter']= data_points_df['litter'].fillna(0.0)
        print("data_points df data \n ", data_points_df.head())
        organic_matter_df = df[['profile_layer_id', 'orgc_value', 'orgc_value_avg', 'orgc_method', 'orgc_date', 'orgc_dataset_id', 'orgc_profile_code']].copy()
        print("organic_matter df data \n ", organic_matter_df.head())
        with self.mysql_connect.cursor() as cursor:
            #loop through the data frame
            print("Record insertion started in profile table")
            for i,row in profile_df.iterrows():
                sql = insert_profiles()
                cursor.execute(sql, tuple(row))
                self.mysql_connect.commit()
            print("Record inserted in profiles table")

            print("Record insertion started in layers table")
            for i,row in layers_df.iterrows():
                sql = insert_layers()
                cursor.execute(sql, tuple(row))
                self.mysql_connect.commit()
            print("Record inserted in layers table")

            print("Record insertion started in data_points table")
            for i,row in data_points_df .iterrows():
                sql = insert_data_points()
                cursor.execute(sql, tuple(row))
                self.mysql_connect.commit()
            print("Record inserted in data points table")

            print("Record insertion started in organic_matter table")
            for i,row in organic_matter_df .iterrows():
                sql = insert_organic_matter()
                cursor.execute(sql, tuple(row))
                self.mysql_connect.commit()
            print("Record inserted in organic table")



    def read_file(self):
        
        #open connection to fetch data
        with self.mysql_connect.cursor() as cursor:
            cursor.execute(select_profiles())
            data = cursor.fetchall() #fetching profiles data
            print("the data from profiles")
            for row in data:
                print(row)



if __name__=='__main__':
    etltest = TEST()
    #etltest.create_table_people()
    etltest.insert_tb()
    etltest.read_file()

    
