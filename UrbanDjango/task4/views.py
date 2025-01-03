from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница',
        'main': 'Главная',
        'vitamin': 'Витамины',
        'medicines': 'Лекарства',
    }
    return render(request, 'fourth_task/index.html', context)


class index2(TemplateView):
    template_name = 'fourth_task/index2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Витамины'
        context['vitamins'] = ['Витамины А', 'Витамины В', 'Витамины C']
        context['buy'] = 'Купить'
        context['back'] = 'Вернуться обратно'
        context['main'] = 'Главная'
        context['vitamin'] = 'Витамины'
        context['medicines'] = 'Лекарства'
        return context

class index3(TemplateView):
    template_name = 'fourth_task/index3.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Лекарства'
        context['message'] = 'Извините в данный момент препарат отсутствует'
        context['back'] = 'Вернуться обратно'
        context['main'] = 'Главная'
        context['vitamin'] = 'Витамины'
        context['medicines'] = 'Лекарства'
        return context

