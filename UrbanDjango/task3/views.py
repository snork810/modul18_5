from django.shortcuts import render

# Create your views here.
def main_page(request):
    title = "Главная страница"
    text = 'Ассортимент'
    text2 = 'Корзина'
    context = {'title':title, 'text':text, 'text2':text2}
    return render(request,'platform.html', context)

def store(request):
    title = 'Ассортимент'
    game = 'Resident Evil'
    back = 'Вернуться обратно'
    context={'title':title, 'game':game, 'back':back}
    return render(request,'games.html', context)

def korzina(request):
    title = 'Корзина'
    back = 'Вернуться обратно'
    context={'title':title, 'back':back}
    return render(request,'cart.html', context)