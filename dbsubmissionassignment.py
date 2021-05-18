    

import sqlite3 #access methods from the module sqlite3


def createDB():
    conn = sqlite3.connect('dbassignment.db')#establish connection to sqlite3
    with conn: #using connection to database
        cur = conn.cursor() #allows us to type into sqlite3
        #execute a sql statement on database
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_txtfiles(\
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_filename TEXT \
            )")
        conn.commit() #commits changes to database
    conn.close() #closes connection with database to prevent memory leaks

def addtoDB():
    conn = sqlite3.connect('dbassignment.db')

    fileList = ('information.docx','Hello.txt','myImage.png', \
                'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
    for file in fileList: #iterate through fileList
        if file.endswith('.txt'): #if file ends with .txt,
            with conn: #using connection to database
                cur = conn.cursor()
                #add file to col_filename in tbl_txtfiles
                cur.execute("INSERT INTO tbl_txtfiles(col_filename) VALUES (?)", \
                            (file,))
                #print added files to console
                print(file)
        conn.commit()
    conn.close()

if __name__ == "__main__":
    createDB()
    addtoDB()


    

