from hdbcli import dbapi

# Establish a connection
conn = dbapi.connect(
    address="",    # Hostname or IP address of the SAP HANA server
    port=,                  # Port number (default is 30015)
    user="",        # Username for the SAP HANA database
    password=""     # Password for the SAP HANA database
)

# Create a cursor object
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM ZRETAILER")

# Fetch all results from the query
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
