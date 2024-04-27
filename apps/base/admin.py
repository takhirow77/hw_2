from django.contrib import admin
from apps.base.models import Settings,Rewards,Works,Experience,ExpModel,Journal,Research,Latest

# Register your models here.
admin.site.register(Settings)
admin.site.register(Rewards)
admin.site.register(Works)
admin.site.register(Experience)
admin.site.register(ExpModel)
admin.site.register(Journal)
admin.site.register(Research)
admin.site.register(Latest)