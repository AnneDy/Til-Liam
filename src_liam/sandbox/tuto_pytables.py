from tables import *
import pdb

class Particle(IsDescription):
    identity = StringCol(itemsize=22, dflt=" ", pos=0)  # character String
    idnumber = Int16Col(dflt=1, pos = 1)  # short integer
    speed    = Float32Col(dflt=1, pos = 1)  # single-precision

# Open a file in "w"rite mode
fileh = openFile("objecttree.h5", mode = "w")
# Get the HDF5 root group
root = fileh.root

# Create the groups:
group1 = fileh.createGroup(root, "group1")
group2 = fileh.createGroup(root, "group2")

# Now, create an array in root group
array1 = fileh.createArray(root, "array1", ["string", "array"], "String array")
# Create 2 new tables in group1
table1 = fileh.createTable(group1, "table1", Particle)
table2 = fileh.createTable("/group2", "table2", Particle)
# Create the last table in group2
array2 = fileh.createArray("/group1", "array2", [1,2,3,4])

# Now, fill the tables:
for table in (table1, table2):
    # Get the record object associated with the table:
    row = table.row
    # Fill the table with 10 records
    for i in xrange(10):
        # First, assign the values to the Particle record
        row['identity']  = 'This is particle: %2d' % (i)
        row['idnumber'] = i
        row['speed']  = i * 2.
        # This injects the Record values
        row.append()

    # Flush the table buffers
    table.flush()

# Finally, close the file (this also will flush all the remaining buffers!)
fileh.close()


##### add columns 
from tables import *
 
# Describe a water class
class Water(IsDescription):
    waterbody_name = StringCol(16, pos=1) # 16-character String
    lati = Int32Col(pos=2) # integer
    longi = Int32Col(pos=3) # integer
    airpressure = Float32Col(pos=4) # float (single-precision)
    temperature = Float64Col(pos=5) # double (double-precision)
 
# Open a file in "w"rite mode
fileh = openFile("myadd-column.h5", mode = "w")
# Create a new group
group = fileh.createGroup(fileh.root, "newgroup")
 
# Create a new table in newgroup group
table = fileh.createTable(group, 'table', Water, "A table", Filters(1))
 
# Append several rows
table.append([("Atlantic", 10, 0, 10*10, 10**2),
("Pacific", 11, -1, 11*11, 11**2),
("Atlantic", 12, -2, 12*12, 12**2)])
 
print "Contents of the original table:", fileh.root.newgroup.table[:]
 
# Create another table but this time in the root directory
tableroot = fileh.createTable(fileh.root, 'root_table', Water, "A table at root", Filters(1))
 
# Append data...
tableroot.append([("Mediterranean", 10, 0, 10*10, 10**2),
("Mediterranean", 11, -1, 11*11, 11**2),
("Adriatic", 12, -2, 12*12, 12**2)])
 
# close the file
 
# close the file
fileh.close()
 
# Open it again in append mode
fileh = openFile("myadd-column.h5", "a")
group = fileh.root.newgroup
table = group.table
 
# Get a description of table in dictionary format
descr = table.description._v_colObjects
descr2 = descr.copy()
 
# Add a column to description
descr2['hot'] = None
 
# Create a new table with the new description
table2 = fileh.createTable(group, 'table2', descr2, "A table", Filters(1))
 
# Copy the user attributes
table.attrs._f_copy(table2)
 
# Fill the rows of new table with default values
for i in xrange(table.nrows):
    table2.row.append() 
# Flush the rows to disk
table2.flush()
 
# Copy the columns of source table to destination
for col in descr:
    getattr(table2.cols, col)[:] = getattr(table.cols, col)[:]
 
# Fill the new column
table2.cols.hot[:] = [ row["temperature"] > 11**2 for row in table ]
 
# Remove the original table
table.remove()
 
# Move table2 to table
fileh.root.root_table.remove()
table2.move('/','root_table')
 
# Print the new table
#print "Contents of the table with column added:", fileh.root.newgroup.table[:]


fileh.close()