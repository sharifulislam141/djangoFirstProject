from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template import loader
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .utils import generate_token, TokenGenerator
from django.conf import settings
from django.views.generic import View
from django.contrib import messages

from django.core.mail import EmailMessage
# Create your views here.
def handlelogin(request):
    return render(request, 'login.html')


from django.shortcuts import render
from django.contrib.auth.models import User

# def signin(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")
        
#         # Check if passwords match
#         if password != confirm_password:
#             return render(request, 'sign.html', {'error_message': 'Passwords do not match'})
        
#         # Check if email is unique
#         if User.objects.filter(email=email).exists():
#             return render(request, 'sign.html', {'error_message': 'Email already exists'})
        
#         # Create the user
#         user = User.objects.create_user(username=email, email=email, password=password)
#         user.is_active = False
#         user.save()
        



#         email_subject = 'Active your account'
#         # template = loader.get_template('email_template.html')  # Path to your HTML template file

# # Render the template with context data
#         # context = {'message': 'This is a test email sent from Django using Mailtrap.'}
#         # message = template.render(context)
#         message = render_to_string('auth/activate.html',{
#                                    'user':user,
#                                    'domain':'127.0.0.1:8000',
#                                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                                    'token': generate_token.make_token(user)

#                                   } )
#         email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER, [email],)
#         email_message.send()
#         return redirect('/auth/login')
       

         

 
    
#     return render(request, 'sign.html')


from django.contrib import messages

def signin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        # Check if passwords match
        if password != confirm_password:
            return render(request, 'sign.html', {'error_message': 'Passwords do not match'})
        
        # Check if email is unique
        if User.objects.filter(email=email).exists():
            return render(request, 'sign.html', {'error_message': 'Email already exists'})
        
        # Create the user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.is_active = False
        user.save()
        
        # Send activation email
        email_subject = 'Activate your account'
        message = render_to_string('activate.html', {
            'user': user,
            'domain': '127.0.0.1:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        email_message = EmailMessage(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.send()
        
        # Add success message
        messages.success(request, 'Account created successfully. Please check your email to activate your account.')
        
        return redirect('/auth/login')
    
    return render(request, 'sign.html')




class ActivateAccountView(View):

    def get(self,request,uid64,token):
        try:
            uid = force_str(urlsafe_base64_decode(uid64))

            user= User.objects.get(pk = uid)
        except Exception as identifier:
            user=None

        if user is not None and generate_token.check_token(user,token):
            user.is_active = True
            user.save()
            return redirect('/auth/login')
        return redirect(request,'auth/activatefail.html')




def handlelogout(request):
    return redirect( 'handleLogin')
