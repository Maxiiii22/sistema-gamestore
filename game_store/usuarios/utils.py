from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


from django.contrib.sessions.models import Session
from django.utils.timezone import now

REGEX = {
    "username": r'[^a-zA-ZñÑ0-9._-]', 
    "username_contiene_al_menos_una_letra": r'[a-zA-ZñÑ]',
    "email": r"^(?!\.)"  
        r"[\w!#$%&'*+/=?^_`{|}~-]+"  
        r"(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*" 
        r"@"  
        r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+" 
        r"[A-Za-z]{2,}$" , 
    "password": r'^(?=.*[A-Za-zñÑ])(?=.*[A-ZñÑ])(?=.*\d)[A-Za-zñÑ\d._@#$%&*!?-]{6,}$',  
    "nombreYapellido": r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,}$',
    "telefono": r'^\d{6,8}$' 
}



def enviar_email_bienvenida(user):
    asunto = "Bienvenido a Game Store"  
    from_email = settings.DEFAULT_FROM_EMAIL 
    to = user.email  

    datos = {
        'username': user.username,
        'pagina_url': 'http://127.0.0.1:8000/', 
    }

    html_content = render_to_string('plantillas_emails/bienvenida.html', datos)  
    text_content = f"Hola {user.username}!\nGracias por registrarte en nuestro sitio. Visita nuestros productos en: {datos['pagina_url']}" # Versión en texto plano del email (alternativa para clientes de correo que no soportan HTML)

    msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])  
    msg.attach_alternative(html_content, "text/html")  
    
    msg.send() 

def cerrar_otras_sesiones(request):
    current_session_key = request.session.session_key  
    user_id = request.user.id

    for session in Session.objects.filter(expire_date__gt=now()):  
        data = session.get_decoded()  
        if (data.get('_auth_user_id') == str(user_id) 
            and session.session_key != current_session_key):  
            session.delete()  


def renderizarMiCuentaConError(request,form,error_msg,campo,nuevoValor):
    return render(request, "miCuenta.html", {
        "form": form,
        "error": error_msg,
        "abrir_modal": True,
        "campo_modal": campo,
        "campo_valor": nuevoValor
    })    