from flask import Flask, render_template
app = Flask(__name__)

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         f_name = request.form['f_name']
         l_name = request.form['l_name']
         Email = request.form['email']
         phone = request.form['phone']

         with sql.connect("database1.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO Contact (f_name TEXT, l_name TEXT, email TEXT, phone integer) VALUES (?,?,?,?)",(f_name,l_name,email,phone) )

            con.commit()
            msg = "Record successfully added"
      except:
         con.rollback()
         msg = "error in insert operation"

      finally:
         return render_template("submit1.html",msg = msg)
         con.close()
if __name__ == '__main__':
       app.run(debug = True)
