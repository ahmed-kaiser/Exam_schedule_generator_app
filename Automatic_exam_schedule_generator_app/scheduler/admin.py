from django.contrib import admin
from .models import Rooms, EVE_routine, DAY_routine, publish
from .models import CSE_eve_batch_info, CSE_eve_trimister, CSE_eve_course_list
from .models import CSE_day_batch_info, CSE_day_trimister, CSE_day_course_list
from .models import EEE_eve_batch_info, EEE_eve_trimister, EEE_eve_course_list
from .models import EEE_day_batch_info, EEE_day_trimister, EEE_day_course_list
from .models import CEN_eve_batch_info, CEN_eve_trimister, CEN_eve_course_list
from .models import CEN_day_batch_info, CEN_day_trimister, CEN_day_course_list
from .models import BTE_eve_batch_info, BTE_eve_trimister, BTE_eve_course_list
from .models import BTE_day_batch_info, BTE_day_trimister, BTE_day_course_list


admin.site.register(Rooms)

admin.site.register(CSE_eve_batch_info)
admin.site.register(CSE_eve_trimister)
admin.site.register(CSE_eve_course_list)
admin.site.register(CSE_day_batch_info)
admin.site.register(CSE_day_trimister)
admin.site.register(CSE_day_course_list)

admin.site.register(EEE_eve_batch_info)
admin.site.register(EEE_eve_trimister)
admin.site.register(EEE_eve_course_list)
admin.site.register(EEE_day_batch_info)
admin.site.register(EEE_day_trimister)
admin.site.register(EEE_day_course_list)

admin.site.register(CEN_eve_batch_info)
admin.site.register(CEN_eve_trimister)
admin.site.register(CEN_eve_course_list)
admin.site.register(CEN_day_batch_info)
admin.site.register(CEN_day_trimister)
admin.site.register(CEN_day_course_list)

admin.site.register(BTE_eve_batch_info)
admin.site.register(BTE_eve_trimister)
admin.site.register(BTE_eve_course_list)
admin.site.register(BTE_day_batch_info)
admin.site.register(BTE_day_trimister)
admin.site.register(BTE_day_course_list)

admin.site.register(EVE_routine)
admin.site.register(DAY_routine)
admin.site.register(publish)
