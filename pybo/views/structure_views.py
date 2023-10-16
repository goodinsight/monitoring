from flask import Blueprint, render_template, request

from pybo.models import Structure
from pybo.forms import Structure_Form

bp = Blueprint('structure', __name__, url_prefix='/structure')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)    #페이지
    structure_list = Structure.query.order_by(Structure.date.desc())
    structure_list = structure_list.paginate(page=page, per_page=10)
    return render_template('structure/structure_list.html', structure_list=structure_list)

@bp.route('/detail/<int:structure_id>/')
def detail(structure_id):
    structure = Structure.query.get_or_404(structure_id)
    return render_template('structure/structure_detail.html', structure=structure)

@bp.route('/chart/', methods=['GET'])
def chartGET():
    start1 = "2023-04-30 22:00:00"
    end1 = "2023-04-30 23:59:00"

    structure_list = Structure.query.filter(Structure.date >= start1,
                                                              Structure.date <= end1)
    if structure_list is None:
        return 'No data'

    label1 = "batt"
    label2 = "temp"
    label3 = "ch1_a"
    label4 = "ch1_b"
    label5 = "ch1_c"
    label6 = "ch1_d"

    xlabels = []
    dataset1 = []
    dataset2 = []
    dataset3 = []
    dataset4 = []
    dataset5 = []
    dataset6 = []

    for structure in structure_list:
        xlabels.append(structure.date)

    for structure in structure_list:
        dataset1.append(structure.batt)

    for structure in structure_list:
        dataset2.append(structure.temp)

    for structure in structure_list:
        dataset3.append(structure.ch1_a)

    for structure in structure_list:
        dataset4.append(structure.ch1_b)

    for structure in structure_list:
        dataset5.append(structure.ch1_c)

    for structure in structure_list:
        dataset6.append(structure.ch1_d)


    return render_template('structure/structure_chart.html', **locals())

@bp.route('/chart/', methods=['POST'])
def chartPOST():
    form = Structure_Form()

    start1 = form.start.data.split('T')[0]+" "+form.start.data.split('T')[1]
    end1 = form.end.data.split('T')[0]+" "+form.end.data.split('T')[1]

    structure_list = Structure.query.filter(Structure.date >= start1, Structure.date <= end1)
    if structure_list is None:
        return 'No data'

    label1 = "batt"
    label2 = "temp"
    label3 = "ch1_a"
    label4 = "ch1_b"
    label5 = "ch1_c"
    label6 = "ch1_d"

    xlabels = []
    dataset1 = []
    dataset2 = []
    dataset3 = []
    dataset4 = []
    dataset5 = []
    dataset6 = []

    for structure in structure_list:
        xlabels.append(structure.date)

    for structure in structure_list:
        dataset1.append(structure.batt)

    for structure in structure_list:
        dataset2.append(structure.temp)

    for structure in structure_list:
        dataset3.append(structure.ch1_a)

    for structure in structure_list:
        dataset4.append(structure.ch1_b)

    for structure in structure_list:
        dataset5.append(structure.ch1_c)

    for structure in structure_list:
        dataset6.append(structure.ch1_d)

    return render_template('structure/structure_chart.html', **locals())