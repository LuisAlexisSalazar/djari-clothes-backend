import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'luis.salazar.marroquin@ucsp.edu.pe'
password = '72189788'


def send_mail(id_user, text='Email_body', subject='DjariClothe - Solicitud de Recuperación de Contraseña', from_email=username, to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    txt_part = MIMEText(text, 'plain')
    msg.attach(txt_part)
    # id_user = user.id
    to_url_reset_password = "http://localhost:8080/passwd-recover/" + id_user
    html_part = MIMEText(f"<p>Ingrese al enlace para poder cambiar su contraseña: </p> <a href={to_url_reset_password}>link </a>", 'html')
    msg.attach(html_part)
    msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()
