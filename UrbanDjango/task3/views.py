from django.views.generic import TemplateView

# Create your views here.
class index(TemplateView):
    template_name = 'third_task/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['main'] = 'Главная'
        context['vitamin'] = 'Витамины'
        context['medicines'] = 'Лекарства'
        return context

class index2(TemplateView):
    template_name = 'third_task/index2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Витамины'
        context['vit1'] = 'Витамины А'
        context['vit2'] = 'Витамины В'
        context['vit3'] = 'Витамины С'
        context['buy'] = 'Купить'
        context['back'] = 'Вернуться обратно'
        return context

class index3(TemplateView):
    template_name = 'third_task/index3.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Лекарства'
        context['message'] = 'Извините в данный момент препарат отсутствует'
        context['back'] = 'Вернуться обратно'
        return context