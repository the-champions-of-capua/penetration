import pymysql

from website.settings import MPP_CONFIG


def from_sql_get_data(sql, MPP_CONFIG=MPP_CONFIG):
    # Connect to the database
    connection = pymysql.connect(**MPP_CONFIG)
    corsor = connection.cursor()
    corsor.execute(sql)
    try:
        res = corsor.fetchall()
        try:
            data = {"data": res, "heads": [x[0] for x in corsor.description]}
        except:
            data = None
    finally:
        ## connection.commit()
        corsor.close()
        connection.close()
    return data


## 单纯执行的
def sql_action(sql):
    connection = pymysql.connect(**MPP_CONFIG)
    corsor = connection.cursor()
    corsor.execute(sql)
    # print(sql)
    connection.commit()
    corsor.close()
    connection.close()
    return


from django.http import HttpResponse
# Create your views here.
def send_email(request):

    if request.method == 'POST':
        from django.core.mail import EmailMultiAlternatives
        getters = request.POST["mail_geters"].split(";")
        mail_content = str(request.POST["mail_content"])
        subject = '审计邮件|请求协助'
        msg = EmailMultiAlternatives(subject, mail_content, 'm13429888211@163.com', getters)
        msg.send()
        return HttpResponse("发送成功")

    if request.method == 'GET':
        s_id = request.session["eid"]
        e_id = int(str(s_id).split('opt')[1])

        from django.core.mail import EmailMultiAlternatives
        # print(request.GET["mail_geters"])
        getters = str(request.GET["mail_geters"]).split(";")
        getters.append("actanble@163.com")
        # print(getters)
        mail_content = request.GET["mail_content"]
        title = '代建局审计邮件|请求协助'
        # html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
        msg = EmailMultiAlternatives(title, mail_content, 'actanble@163.com', getters)
        msg.content_subtype = "html"

        # 添加附件（可选）
        ### msg.attach_file('./twz.pdf')
        msg.send()

        s_id = request.session["eid"]
        e_id = int(str(s_id).split('opt')[1])
        extra_add = "向技术支持求助"
        from datetime import datetime
        params = {
            "event_stat": "求助",
            "event_time": str(datetime.today()),
            "extra_add": extra_add,
            "event_id": int(e_id),
            "opreater_name": request.user.username
            # "opreater_name": '网站管理员',
        }
        sql = """insert into proj_eventdetail(event_stat, event_time, extra_add, event_id, opreater_name) 
                            values('{event_stat}', '{event_time}', '{extra_add}', {event_id}, '{opreater_name}')""".format(
            **params)
        sql_action(sql)


        return HttpResponse("发送成功")
