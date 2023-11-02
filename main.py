from flask import Flask, request

from utils import generate_password, commit_sql

app = Flask(__name__)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/password")
def password():
    length = request.args.get('length', '10')

    if length.isdigit():
        length = int(length)
        max_length = 200

        if length > max_length:
            return f'Length should be less then {max_length}'

        return generate_password(length)

    return f'Invalid length value: {length}'


@app.route('/email/create')
def emails_create():
    email_value = request.args.get('email', 'a')

    sql = f"""
    INSERT INTO Emails (Email)
    VALUES ({email_value});
    """
    commit_sql(sql)

    return 'emails_create'


@app.route('/email/read')
def emails_read():
    import sqlite3
    con = sqlite3.connect('example.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Emails;
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()

    return result


@app.route('/email/update')
def emails_update():
    email_value = request.args['email']
    email_id = request.args['id']

    sql = f"""
    UPDATE Emails
    SET Email = '{email_value}'
    WHERE EmailID = {email_id};
    """
    commit_sql(sql)

    return 'emails_update'


@app.route('/email/delete')
def emails_delete():
    email_id = request.args['id']

    sql = f"""
    DELETE FROM Emails
    WHERE EmailID = {email_id};
    """
    commit_sql(sql)

    return 'emails_delete'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)


'''
http://127.0.0.1:5001/hello?name=John&age=20

http:// 127.0.0.1 :5001 /hello

1. Protocol
http/s

ftp

smtp 

2. IP address

IPv4
127.0.0.1

x.x.x.x

[0-255].[0-255].[0-255].[0-255]
0.0.0.0
255.255.255.255
23.34.21
35.35.37.38.21
32.256.12.10

127.0.0.1

IPv6

3. PORT

5001

0-65535

http - 80
https - 443
ssh - 22

4. PATH

/hello

5. Query parameters 

?name=John&age=20

'''

'''
CRUD operations
C - create
R - read
U - update
D - delete
'''
