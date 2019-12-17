import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 이 Question의 pub_date가 (현재시간 -1일) 보다 크거나 같은지 여부
        # 23일 12시에 published, 지금 날짜가 24일 09시면
        # 24일 09시 - 1일 = 23시 09시
        # 즉, 이 Question이 발행된지 24시간 이내인지 여부 True/False
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
