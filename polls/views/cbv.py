"""
class based view
"""

from django.views import generic, View

from polls.models import Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class VoteView(View):
    def post(self, request, question_id):
        # if request.method == 'POST'에 해당하는 Block
        pass
