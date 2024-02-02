from ssl import ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
               
# Create your views here.

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto", #Asunto
                "De {} <{}>\n\nEscribio:\n\n{}".format(name, email, content),#cuerpo
                "no-reply@inbox.mailtrap.io",#email_origen
                ["stevenwng_2@hotmail.com"],#email_destino
                reply_to=[email]   
            )
            try:
                email.send() 
                #Envio exitoso, redireccionando a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo salio mal, redireccionando a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
