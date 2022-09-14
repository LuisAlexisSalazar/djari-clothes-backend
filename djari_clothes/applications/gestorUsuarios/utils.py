import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'djari1clothes@gmail.com'
password = 'rdegtdaiusvrgjay'


# rdegtdaiusvrgjay

def send_mail(id_user=None, mesage="", subject='DjariClothe - Solicitud de Recuperación de Contraseña',
              from_email=username, ResetPassword=False, to_emails=[]):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg['Subject'] = subject
    # txt_part = MIMEText(text, 'plain')
    # msg.attach(txt_part)
    # id_user = user.id
    html_part = ""
    if ResetPassword:
        to_url_reset_password = "http://localhost:8080/passwd-recover/" + id_user
        html_part = MIMEText(
            f"<p>Ingrese al enlace para poder cambiar su contraseña: </p> <a href={to_url_reset_password}>link </a>",
            'html')
        print("Mensaje Resetear Contraseña")

    else:
        print("Mensaje Normal")
        html_part = MIMEText(mesage)
    msg.attach(html_part)
    # msg_str = msg.as_string()

    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_email, to_emails, msg.as_string())
    server.quit()
