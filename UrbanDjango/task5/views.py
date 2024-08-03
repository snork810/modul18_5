from django.shortcuts import render
from task5.forms import UserRegister
from django.http import HttpResponse

users = ['Andrei', 'Elena556', 'User007', 'abUseR']
# Create your views here.
# def sign_up_by_html(request):
    # i = 0
#     info = {'error':[]}
#     if request.method=='POST':
#         #Получаем данные
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         repeate_password = request.POST.get('repeate_password')
#         age = request.POST.get('age')

#         print(f'Username: {username}')
#         print(f'Password: {password}')
#         print(f'Repeate password: {repeate_password}')
#         print(f'Age: {age}')
#         if username not in users and password == repeate_password and int(age)>=18:
#             users.append(username)
#             print(users)
#             return HttpResponse(f'Приветствуем {username}')
#         elif username in users:
#             i +=1
            # info[f'error {i}'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login') 
#             return HttpResponse('Этот логин уже занят', status=400, reason='repeated login')
#         elif password != repeate_password:
#             i +=1
            # info[f'error {i}'] = HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')   
#             return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
#         elif int(age) < 18:
#             i +=1
            # info[f'error {i}'] = HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')  
#             return HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
    
#     context = {'info':info}
#     return render(request, 'registration_page.html', context)


def sign_up_by_django(request):
    info = {'error':[]}
    i = 0
    if request.method =="POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeate_password = form.cleaned_data['repeate_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeate_password and int(age)>=18:
                users.append(username)
                print(users)
                return HttpResponse(f'Приветствуем {username}')
            elif username in users:
                i +=1
                info[f'error {i}'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login') 
                print(info[f'error {i}'])   
                return HttpResponse('Этот логин уже занят', status=400, reason='repeated login')    
            elif password != repeate_password:
                i +=1
                info[f'error {i}'] = HttpResponse('Этот логин уже занят', status=400, reason='repeated login') 
                print(info[f'error {i}'])   
                return HttpResponse('Пароли не совпадают', status=400, reason='non-identical passwords')
            elif int(age) < 18:
                i +=1
                info[f'error {i}'] = HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
                  
                return HttpResponse(f'Регистрация разрешена с 18ти лет. Будем рады видеть вас через {18-int(age)} лет', status=400, reason='insufficient age')
    else:
        
        form = UserRegister()
        context = {'info':info, 'form':form}
        return render(request, 'registration_page.html', context)

