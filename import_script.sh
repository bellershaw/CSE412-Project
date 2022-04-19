#!/bin/bash
import_dir='/coin_data/import_data/*'
username=$USER
database_name=cryptoproject

for file in $import_dir
do
	file_name="$( basename "$file" .csv)"
	coin_name="${file_name:5}"
	echo $coin_name
	create_script_1="CREATE TABLE ${coin_name}"
	create_script_2='(sno INT,name VARCHAR(30), sym VARCHAR(4), date VARCHAR(25), high FLOAT(24), low FLOAT(24), open FLOAT(24), close FLOAT(24), volume float(24), mcap FLOAT(24), PRIMARY KEY(sno))'
	create_script_full="${create_script_1} ${create_script_2}"
	echo $create_script_full
	import_script_1="COPY ${coin_name}"
	import_script_2='(sno, name, sym, date, high, low, open, close, volume, mcap) FROM '
	import_script_3="'${file}' DELIMITER ',' CSV HEADER"
	import_script_full="${import_script_1} ${import_script_2} ${import_script_3}"
	echo $import_script_full
	psql -h localhost -U $USER -d $database_name -c "DROP TABLE ${coin_name}"
	psql -h localhost -U $USER -d $database_name -c "$create_script_full"
	psql -h localhost -U $USER -d $database_name -c "$import_script_full"
done
