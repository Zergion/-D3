from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime
import string


class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

    def censor(text, bad_words):
        text_list = text.split()
        censored_text_list = []

        for word in text_list:
            clean_word = ''.join(c for c in word if c not in string.punctuation)
            if clean_word.lower() in bad_words:
                censored_word = clean_word[0] + (len(clean_word) - 1) * '*'
                censored_text_list.append(word.replace(clean_word, censored_word))
            else:
                censored_text_list.append(word)

        return ' '.join(censored_text_list)


