import math
from datetime import datetime, date

from flask import Blueprint, render_template, request, redirect, url_for

from pybo.models import Structur_tiltmeter
from pybo.forms import Structur_tiltmeter_Form

bp = Blueprint('structur_tiltmeter', __name__, url_prefix='/structur_tiltmeter')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)    #페이지
    structur_tiltmeter_list = Structur_tiltmeter.query.order_by(Structur_tiltmeter.opdatetime.desc())
    structur_tiltmeter_list = structur_tiltmeter_list.paginate(page=page, per_page=10)
    return render_template('structur_tiltmeter/structur_tiltmeter_list.html', structur_tiltmeter_list=structur_tiltmeter_list)

@bp.route('/detail/<int:structur_tiltmeter_id>/')
def detail(structur_tiltmeter_id):
    structur_tiltmeter = Structur_tiltmeter.query.get_or_404(structur_tiltmeter_id)
    return render_template('structur_tiltmeter/structur_tiltmeter_detail.html', structur_tiltmeter=structur_tiltmeter)

@bp.route('/chart/', methods=['GET'])
def chartGET():
    start1 = "2023-04-30 22:00:00"
    end1 = "2023-04-30 23:59:00"

    structur_tiltmeter_list = Structur_tiltmeter.query.filter(Structur_tiltmeter.opdatetime >= start1,
                                                              Structur_tiltmeter.opdatetime <= end1)
    if structur_tiltmeter_list is None:
        return 'No data'

    label1 = "tilt-01"
    label2 = "tilt-02"
    label3 = "tilt-03"
    label4 = "tilt-04"
    label5 = "tilt-05"
    label6 = "tilt-06"
    label7 = "tilt-07"
    xlabels = []
    dataset1 = []
    dataset2 = []
    dataset3 = []
    dataset4 = []
    dataset5 = []
    dataset6 = []
    dataset7 = []
    for structur_tiltmeter in structur_tiltmeter_list:
        xlabels.append(structur_tiltmeter.opdatetime)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_01_x
        y = structur_tiltmeter.tilt_01_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset1.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_02_x
        y = structur_tiltmeter.tilt_02_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset2.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_03_x
        y = structur_tiltmeter.tilt_03_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset3.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_04_x
        y = structur_tiltmeter.tilt_04_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset4.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_05_x
        y = structur_tiltmeter.tilt_05_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset5.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_06_x
        y = structur_tiltmeter.tilt_06_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset6.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_07_x
        y = structur_tiltmeter.tilt_07_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset7.append(result)

    return render_template('structur_tiltmeter/structur_tiltmeter_chart.html', **locals())

@bp.route('/chart/', methods=['POST'])
def chartPOST():
    form = Structur_tiltmeter_Form()

    start1 = form.start.data.split('T')[0]+" "+form.start.data.split('T')[1]
    end1 = form.end.data.split('T')[0]+" "+form.end.data.split('T')[1]

    structur_tiltmeter_list = Structur_tiltmeter.query.filter(Structur_tiltmeter.opdatetime >= start1, Structur_tiltmeter.opdatetime <= end1)
    if structur_tiltmeter_list is None:
        return 'No data'

    label1 = "tilt-01"
    label2 = "tilt-02"
    label3 = "tilt-03"
    label4 = "tilt-04"
    label5 = "tilt-05"
    label6 = "tilt-06"
    label7 = "tilt-07"
    xlabels = []
    dataset1 = []
    dataset2 = []
    dataset3 = []
    dataset4 = []
    dataset5 = []
    dataset6 = []
    dataset7 = []
    for structur_tiltmeter in structur_tiltmeter_list:
        xlabels.append(structur_tiltmeter.opdatetime)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_01_x
        y = structur_tiltmeter.tilt_01_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset1.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_02_x
        y = structur_tiltmeter.tilt_02_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset2.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_03_x
        y = structur_tiltmeter.tilt_03_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset3.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_04_x
        y = structur_tiltmeter.tilt_04_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset4.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_05_x
        y = structur_tiltmeter.tilt_05_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset5.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_06_x
        y = structur_tiltmeter.tilt_06_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset6.append(result)

    for structur_tiltmeter in structur_tiltmeter_list:
        x = structur_tiltmeter.tilt_07_x
        y = structur_tiltmeter.tilt_07_y
        result = math.atan2(x, y) * 180 / math.pi
        dataset7.append(result)

    return render_template('structur_tiltmeter/structur_tiltmeter_chart.html', **locals())