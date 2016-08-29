"""
Populates a table with data from a Python tuple.
"""


import MySQLdb as mdb
from database import login_info

if __name__ =="__main__":

    db = mdb.Connect('localhost', 'root', '$epultur@99', 'animals'); 
    #db = MySQLdb.connector.Connect(**login_info)

    # This is used so the DB can track our session in the DB
    cursor = db.cursor()
    
    
    # cursor.execute("DELETE FROM animal")
    
    cursor.execute("""SELECT DISTINCT family, feed FROM animal JOIN food ON animal.id=food.anid""")
    foo = cursor.fetchall()

    db.commit()
    print (foo)

    print (foo.__class__)

   

    print("Finished")