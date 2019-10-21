dsn_hostname = "dashdb-txn-sbox-yp-lon02-02.services.eu-gb.bluemix.net" # e.g.: "dashdb-txn-sbox-yp-dal09-04.services.dal.bluemix.net"
dsn_uid = "ssb05683"        # e.g. "abc12345"
dsn_pwd = "18blj3q40zl5b@hh"      # e.g. "7dBZ3wWt9XN6$o0J"

dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "50000"                # e.g. "50000" 
dsn_protocol = "TCPIP"            # i.e. "TCPIP"

dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd)

#print the connection string to check correct values are specified
print(dsn)
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )

#Load data
import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')

#insert data
insertQuery="INSERT INTO chicago_socioeconomic_data (ca,community_area_name,percent_of_housing_crowded,percent_households_below_poverty,percent_aged_16_unemployed,percent_aged_25_without_high_school_diploma ,percent_aged_under_18_or_over_64 ,per_capita_income_,hardship_index) "
for index,row in chicago_socioeconomic_data.iterrows():
             insertQuery1=insertQuery+"VALUES({0},'{1}',{2},{3},{4},{5},{6},{7},{8})".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
             createStmt=ibm_db.exec_immediate(conn,insertQuery1)

#Query examples
pconn=ibm_db_dbi.Connection(conn)
selectQuery="SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000"
pdf=pandas.read_sql(selectQuery,pconn)
            