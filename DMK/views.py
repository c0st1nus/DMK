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

def physics_detail(request, id):
    lesson = Lesson.objects.get(id=id)
    buttons = Step.objects.filter(lesson=lesson)
    return render(request, 'DMK/pl1.html')

@csrf_exempt
def add_item(request):
    if request.method == 'POST':
        data = request.POST.copy()  # Create a mutable copy
        lesson_title = data.pop('lesson_title')[0]  # Get the lesson title and remove it from data
        lesson = Lesson.objects.create(subject="physics", description=lesson_title)  # Create a new Lesson with the title
        for step_description in data.values():  # Now data only contains step descriptions
            Step.objects.create(description=step_description, lesson=lesson, lesson_id=lesson.id)  # Create a new Step for each description, linked to the new Lesson
        return JsonResponse({'status': 'success', 'message': 'Item created successfully'})