from .models import Question,Choice
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Question
from django.template import loader
from .models import Question
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

# # def index(request):
# #     latest_question_list = Question.objects.order_by("-pub_date")[:5]
# #     output=",".join([q.question_text for q in latest_question_list])
# #     return HttpResponse(output)

# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     # template = loader.get_template("polls/index.html")
#     context = {"latest_question_list": latest_question_list}
#     return render(request,"polls/index.html",context)



# # def detail(request,question_id):
# #     return HttpResponse("You 're looking at question %s" % question_id)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})





# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]


# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

class DetailView(generic.DetailView):
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())
    


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def create_question(question_text, days):
    
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionModelTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])
        
    def test_past_question(self):
        question=create_question(question_text="Past question.",days=-30)
        response=self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],[question],)
        
    def test_future_question(self):
        create_question(question_text="Future question.",days=30)
        response=self.client.get(reverse("polls:index"))
        self.assertContains(response,"No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])   
        
    def test_future_question_and_past_question(self):
        question=create_question(question_text="past question.",day=-30 )
        create_question(question_text="future questions.",day=30)
        response=self.client.get(resverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )         
        
    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )


