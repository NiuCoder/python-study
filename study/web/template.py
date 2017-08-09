# -*- encoding:utf-8 -*-
# 使用模板，我们需要预先准备一个HTML文档，这个HTML文档不是普通的HTML，而是嵌入了一些变量和质量，然后，根据
# 我们传入的数据,替换后,得到最终的HTML,发送给用户

# 浏览器请求(传参)--->app.py(处理参数并跳转到相应的View)--->在View中加载参数显示给用户
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html')

@app.route('/signin',methods=['GET'])
def signin_form():
	return render_template('form.html')

@app.route('/signin',methods=['POST'])
def signin():
	username = request.form['username']
	password = request.form['password']
	if username=='admin' and password=='password':
		return render_template('signin-ok.html',username=username)
	return render_template('form.html',message='Bad username or password',username=username)

if __name__ == '__main__':
	app.run()

# 跟app.py相比，template.py将python代码和html分离，python控制逻辑，html只负责显示，
# 依靠{{ name }}这样的变量进行联系

# 由于Flask默认支持的模板是Jinja2，在Jinja2中，用{% ... %}表示循环判断等指令，
# {{ name }}表示我一个需要替换的变量

# 除了Jinja2，常见的模板还有Mako,Cheetah,Django
