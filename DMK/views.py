from multiprocessing import Pool

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI

from DMK.models import Lesson, Step

client = OpenAI(api_key='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')

def home(request):
    return render(request, 'DMK/index.html')

def comingSoon(request):
    return render(request, 'DMK/comingSoon.html')

def physics(request):
    lessons = Lesson.objects.all()
    return render(request, 'DMK/physics.html', {'lessons': lessons})


def generate_text(_):  # добавляем аргумент
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Write a question on russian based on the text I provide below. Just formulate the question without adding any additional symbols or markers like '###', '**', 'Question:', etc. Физическая величина – количественная характеристика тела или явления. Каждая физическая величина имеет название, обозначение и несколько единиц для её измерения: основную и другие. Измерить значение физической величины – значит сравнить изучаемое свойство с мерой, то есть образцом для сравнения. Меры могут существовать как самостоятельно, так и являться неотъемлемой частью измерительных приборов. Результат измерения любой физической величины всегда имеет некоторую погрешность. Она обусловлена прежде всего неточностью использованной меры или прибора. Погрешность также может быть связана с неточностью снятия показаний прибора, непостоянством самой измеряемой величины и другими причинами."},
        ],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()  # use dot notation here
def test(request):
    with Pool(2) as p:
        results = p.map(generate_text, range(2))
    return render(request, 'DMK/test.html', {'Text': results[0], 'Text2': results[1]})


def constructor(request):
    return render(request, 'DMK/Constructor.html')


@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        data = request.POST
        lesson = Lesson.objects.get(id=1)
        print("success")
        for st in data:
            newStep = Step(description=st)
            newStep.lesson = lesson
            newStep.save()

        return JsonResponse({'status': 'success', 'message': 'Item created successfully'})