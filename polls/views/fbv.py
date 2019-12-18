from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from ..models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
    }

    return render(request, 'polls/index.html', context)
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist!')

    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/detail.html', context)


def results(request, question_id):
    # Template: /polls/templates/polls/results.html

    # question_id에 해당하는 Question을 보여주고
    # 해당 Question에 연결된 Choice목록을 보여주며
    #   보여줄때, votes값도 같이 보여주도록 함
    question = get_object_or_404(Question, pk=question_id)
    context = {
        'question': question,
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    # 특정 Question에 해당하는
    # 특정 Choice의 votes를 1늘리기
    # 이후 특정 Question에 해당하는 results페이지로 이동
    if request.method == 'POST':
        try:
            question = get_object_or_404(Question, pk=question_id)
            choice_pk = request.POST['choice']
            choice = get_object_or_404(Choice, pk=choice_pk)
            choice.votes += 1
            choice.save()
            return redirect('polls:results', question_id=question_id)
        except KeyError:
            return redirect('polls:detail', question_id=question_id)
