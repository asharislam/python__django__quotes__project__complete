from django.contrib import admin

from . models import QuoteCategoty
from . models import Quote


admin.site.register(QuoteCategoty)
admin.site.register(Quote)
