from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.conf import settings
from django.contrib import messages

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            mensaje = form.cleaned_data['mensaje']

            try:
                send_mail(
                    subject=f'Mensaje de {nombre}',
                    message=mensaje,
                    from_email=correo,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Mensaje enviado correctamente.')
                return redirect('contacto')
            except:
                messages.error(request, 'Error al enviar el mensaje. Inténtalo más tarde.')
    else:
        form = ContactoForm()

    return render(request, 'contacto/contacto.html', {'form': form})
