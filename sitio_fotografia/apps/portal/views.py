from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
import pymysql

conn = pymysql.connect(host='localhost', user='glasalvia', passwd='dolina1986', db='sitio_fotografia', charset='utf8mb4')
conn.autocommit(True)
cur = conn.cursor(pymysql.cursors.DictCursor)


def index_portal(request):

    cur.execute("SELECT * from Catalogo where Album = 'Eventos'")
    sql_eventos = cur.fetchall()

    cur.execute("SELECT * from Catalogo where Album = 'Books'")
    sql_books = cur.fetchall()

    cur.execute("SELECT * from Catalogo where Album = 'Miscellaneous'")
    sql_miscel = cur.fetchall()

    cur.execute("SELECT * from Catalogo where Album = 'Infantiles'")
    sql_infantiles = cur.fetchall()

    return render(request, 'portal/index.html',{'Eventos':sql_eventos, 'Books':sql_books, 'Miscel':sql_miscel, 'Infantiles':sql_infantiles})



def index_contacto(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['Asunto']
            from_email = form.cleaned_data['Email']
            message = form.cleaned_data['Mensaje']
            try:
                send_mail(subject, message, from_email, ['glasalviacalio@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "portal/contacto.html", {'form': form})




def index_sobre_mi(request):
	return render(request, 'portal/sobre_mi.html')




def success(request):
    return HttpResponse('Success! Thank you for your message.')
