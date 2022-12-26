DROP TABLE IF EXISTS profiles;

CREATE TABLE profiles (
    profile_id integer,
    profile_layer_id integer ,
    country_name varchar(255)
);

DROP TABLE IF EXISTS layers;
CREATE TABLE layers (
    profile_layer_id integer REFERENCES profiles(profile_layer_id),
    profile_id integer ,
    upper_depth double(10,2),
    lower_depth double(10,2),
    layer_name varchar(255) default 'unknown'
);

DROP TABLE IF EXISTS data_points ;
CREATE TABLE data_points (
    data_point_id integer auto_increment PRIMARY KEY,
    profile_layer_id integer REFERENCES layers(profile_layer_id),
    X double(10,2),
    Y double(10,2),
    litter double(10,2) default 0.0
);


DROP TABLE IF EXISTS organic_matter;
CREATE TABLE organic_matter (
    orgc_value_id integer auto_increment PRIMARY KEY,
    profile_layer_id integer REFERENCES layers(profile_layer_id),
    orgc_value varchar(50),
    orgc_value_avg double(10,2),
    orgc_method varchar(500),
    orgc_date varchar(50),
    orgc_dataset_id varchar(50),
    orgc_profile_code varchar(50)
);



