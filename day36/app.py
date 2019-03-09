
from models import  User
from flask import render_template
import app

# http://www.csdn.net/list/
# http://www.csdn.net/list/1/
# http://www.csdn.net/list/2/

@app.route('/list/')
@app.route('/list/<int:page>/')
def list(page=1):
    # 返回的是 Pagination对象
    userPageObj = User.query.paginate(page=page, per_page=app.config['PER_PAGE'])
    return render_template('list.html',
                           userPageObj=userPageObj
                           )


if __name__ == '__main__':
    app.run(port=5005)
