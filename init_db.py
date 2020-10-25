import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute('INSERT INTO items (title, selling_price, imageurl, buy_price, link) VALUES (?, ?, ?, ?, ?)', ('Galaxy Tab S7+', '929.99', 'https://static.bhphoto.com/images/images500x500/samsung_sm_t970nzkexar_12_4_galaxy_tab_s7_1599004292_1579622.jpg', '800', 'https://www.bhphotovideo.com/c/product/1579622-REG/samsung_sm_t970nzkexar_12_4_galaxy_tab_s7.html'))

cur.execute('INSERT INTO items (title, selling_price, imageurl, buy_price, link) VALUES (?, ?, ?, ?, ?)', ('MacBook Pro', '1300.00', 'https://static.bhphoto.com/images/images500x500/apple_mxk32ll_a_13_3_macbook_pro_with_1588701104_1560523.jpg', '1500', 'https://www.bhphotovideo.com/c/product/1560523-REG/apple_mxk32ll_a_13_3_macbook_pro_with.html'))

connection.commit()
connection.close()