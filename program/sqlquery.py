##########profile table query############

def insert_profiles():
    return("""INSERT INTO profiles (profile_id, profile_layer_id, country_name) VALUES (%s,%s,%s);""")

def select_profiles():
    return(""" select * from profiles limit 10 ;""")

##########layers table query############

def insert_layers():
    return("""INSERT INTO layers (profile_layer_id, profile_id, upper_depth, lower_depth, layer_name) VALUES (%s,%s,%s,%s,%s);""")

def select_lyers():
    return(""" select * from layers limit 10 ;""")

##########data_points table query############

def insert_data_points():
    return("""INSERT INTO data_points (profile_layer_id, X, Y, litter) VALUES (%s,%s,%s,%s);""")

def select_data_points():
    return(""" select * from data_points limit 10 ;""")

##########organic matter table query############
def insert_organic_matter():
    return("""INSERT INTO organic_matter (profile_layer_id, orgc_value, orgc_value_avg, orgc_method, orgc_date, orgc_dataset_id, orgc_profile_code) VALUES (%s,%s,%s,%s,%s,%s,%s);""")

def select_organic_matter():
    return(""" select * from organic_matter limit 10 ;""")
