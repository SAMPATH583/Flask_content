from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base
	
engine = create_engine('sqlite:///BVC.db',connect_args={'check_same_thread': False},echo=True)
Base.metadata.bind=engine

DBSession=sessionmaker(bind=engine)
session=DBSession()




app = Flask('__name__')

@app.route("/Home")
def hello():
	return "<p><h1>Hello , this is sampath</h1></p><p><h2> Welcome to home page</h2></p>"

@app.route("/data/<name>")
def data(name):
	name = "Sampath"
	return "<font color = 'blue'>hello {} </font>".format(name)
@app.route("/details/<name>/<int:age>/<int:number>/<float:marks>")
def details(name,age,number,marks):
	return render_template("sample3.html",sname=name,sage=age,snumber=number,smarks=marks)

@app.route("/s")
def sample():
	return render_template("sample.html")
@app.route("/person/<uname>")
def person(uname):
	return render_template("sample2.html",name=uname)

@app.route("/user/<call>")
def call(call):
	if call == 'details':
		return redirect(url_for('details'))
	
@app.route("/table/<int:num>")
def table(num):
	return render_template("table.html",n=num)

dummy_data=[{'name':'sampath','org':'bvcec','dob':'6 sep 2000'},{'name':'jeevana','org':'rjukt','dob':'4 oct 2003'}]
@app.route("/show")
def data_show():
	return render_template("data_show.html",dict=dummy_data)


@app.route("/registor")
def registor():
	return render_template("registor.html")


@app.route("/File")
def file():
	return render_template("upload.html")

@app.route("/success", methods=["POST"])
def success():
	if request.method=='POST':
		f=request.files["file"]
		f.save(f.filename)
		return render_template("display.html", name = f.filename)

@app.route("/show_data")
def showData():
	register=session.query(Register).all()
	return render_template("show.html",register=register)


@app.route('/add',methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Register(Name=request.form['Name'],Surname=request.form['Surname'],Reg_no=request.form['Reg_no'],Mobile_no=request.form['Mobile_no'],Branch=request.form['Branch'])
		session.add(newData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('new.html')

@app.route('/<registor_id>/edit',methods=["POST","GET"])
def editData(registor_id):
	editedData = session.query(Register).filter_by(Id = registor_id).one()
	if request.method=="POST":
		editedData.Name=request.form['Name']
		editedData.Surname=request.form['Surname']
		editedData.Reg_no=request.form['Reg_no']
		editedData.Mobile_no=request.form['Mobile_no']
		editedData.Branch=request.form['Branch']

		session.add(editedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template("edit.html", register=editedData)


@app.route("/<int:registor_id>/delete",methods=['POST','GET'])
def deleteData(registor_id):
	deletedData=session.query(Register).filter_by(Id=registor_id).one()
	if request.method == 'POST':
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('showData',registor_id=registor_id))
	else:
		return render_template("delete.html",register=deletedData)







if __name__=='__main__':
	app.run(debug=True)




