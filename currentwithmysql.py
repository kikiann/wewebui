#!/usr/bin/env python3
import os
import time, datetime
import difflib
import time
import hashlib
#import sqlite3
#import psutil
import mysql.connector
from mysql.connector import Error, connect
from mysql.connector import errorcode

# function to get time since epoch
now = lambda: int(round(time.time() * 1000))

# function to watch file
def watch(file_to_watch, diff_store_path, check_interval=10):
    last_text = None
    
    while True:
        # read file
        with open(file_to_watch, 'r') as fl:
            current_text = list(fl.readlines())
        if last_text is not None:
            # Create differences
            diff = difflib.Differ().compare(last_text, current_text)#actual difference comparision.
            diff = list(diff)
            # check for any differences
            no_difference = all([line[0].strip() == '' for line in diff])
            if no_difference:
                print('No diff')
            else:
                print('Diff found')
                # Generate writable text
                print("[*] Generate writable text")
                text_to_write = ''.join([str(index)+ line for index, line in enumerate(diff) if line[0].strip() != ''])
                time_formatted = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                # Get time in time since epoch format
                print("[*] Get time in time since epoch format")
                _now = now()
                timestamp = str(_now)
                b = bytearray()
                b.extend(timestamp.encode())
                timestamp = b
                del b # deleted temporary object
                # Generate filename
                print("[*] Generate filename")
                file_name = 'diff_file_'+  hashlib.sha256(timestamp).hexdigest()
                path_to_write = diff_store_path+ file_name
                # Write to file
                print("[*] Write to file")
                with open(path_to_write, 'a+') as fl:
                    fl.write('\ndiff_file_{}'.format(time_formatted))
                    fl.write('\n')
                    fl.write(text_to_write)
                    
                # Check if db file is in use then wait else write to db
                print("[*] Connect to DB, Make a table, Insert data.")
                
                try:
                    conn = mysql.connector.connect(host='127.0.0.1', database='project_db', 
                                                    user='root', password='anushreya')
                    if conn.is_connected():
                        print('    [*] Connection to MySQL database succeeded')
                        TABLES = {}
                        TABLES[file_to_watch] = (
                            "CREATE TABLE `"+ file_to_watch +"` ("
                            "  `timestamp` bigint NOT NULL,"
                            "  `filepath` varchar(256) NOT NULL,"
                            "  PRIMARY KEY (`timestamp`)"
                            ") ENGINE=InnoDB")
                        cursor = conn.cursor()
                        for name, ddl in TABLES.items():
                            try:
                                print("        [*] Creating table {}: ".format(name),end = '')
                                cursor.execute(ddl)
                                conn.commit()
                            except mysql.connector.Error as err:
                                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                                    print("        [*] Table already exists.")
                                else:
                                    print("        [*] [ERROR] : ", str(err))
                                    print("        [*] I will handle this exception later.")
                            else:
                                print("        [*] Table created.")
                                
                        insert_diff_data = ("INSERT INTO `"+ file_to_watch +"` "
                           "(timestamp, filepath) "
                           "VALUES (%s, %s)")
                        diff_data = (_now, path_to_write)
                        print("        [*] Inserting data")
                        try:
                            cursor.execute(insert_diff_data, diff_data)
                            conn.commit()
                        except Error as e:
                            print("        [*] [ERROR] : ", str(err))
                            print("        [*] I will handle this exception later.")
                        else:
                            print("        [*] Data inserted.")
                            
                        cursor.close()
                        conn.close()

                    else:
                        print('    [*] Connection to MySQL database failed')
 
                except Error as e:
                    print("    [*] [ERROR] : ", e)
                    print("    [*] I will handle this exception later. Bye...")
                    exit()
 
                finally:
                    conn.close()
                
        last_text = current_text
        time.sleep(check_interval)
        
store = '/home/anushreya/watch/diffs/' #path where difference is saved
to_watch = '/etc/apache2/sites-enabled/code4you.com.conf' # file name 
watch(to_watch, store)
