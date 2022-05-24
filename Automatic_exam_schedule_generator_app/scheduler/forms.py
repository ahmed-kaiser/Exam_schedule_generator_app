from django import forms
from .models import CSE_eve_batch_info, CSE_eve_course_list, CSE_day_batch_info, CSE_day_course_list
from .models import EEE_eve_batch_info, EEE_eve_course_list, EEE_day_batch_info, EEE_day_course_list
from .models import CEN_eve_batch_info, CEN_eve_course_list, CEN_day_batch_info, CEN_day_course_list
from .models import BTE_eve_batch_info, BTE_eve_course_list, BTE_day_batch_info, BTE_day_course_list
from .models import EVE_routine, DAY_routine

#...CSE...
class cse_eve_batch_info_form(forms.ModelForm):
    class Meta:
        model = CSE_eve_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class cse_eve_course_list_form(forms.ModelForm):
    class Meta:
        model = CSE_eve_course_list
        fields = ['course_code', 'course_name', 'trimister']

class cse_day_batch_info_form(forms.ModelForm):
    class Meta:
        model = CSE_day_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class cse_day_course_list_form(forms.ModelForm):
    class Meta:
        model = CSE_day_course_list
        fields = ['course_code', 'course_name', 'trimister']

#...EEE....
class eee_eve_batch_info_form(forms.ModelForm):
    class Meta:
        model = EEE_eve_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class eee_eve_course_list_form(forms.ModelForm):
    class Meta:
        model = EEE_eve_course_list
        fields = ['course_code', 'course_name', 'trimister']
    
class eee_day_batch_info_form(forms.ModelForm):
    class Meta:
        model = EEE_day_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class eee_day_course_list_form(forms.ModelForm):
    class Meta:
        model = EEE_day_course_list
        fields = ['course_code', 'course_name', 'trimister']

#...CEN...
class cen_eve_batch_info_form(forms.ModelForm):
    class Meta:
        model = CEN_eve_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class cen_eve_course_list_form(forms.ModelForm):
    class Meta:
        model = CEN_eve_course_list
        fields = ['course_code', 'course_name', 'trimister']

class cen_day_batch_info_form(forms.ModelForm):
    class Meta:
        model = CEN_day_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class cen_day_course_list_form(forms.ModelForm):
    class Meta:
        model = CEN_day_course_list
        fields = ['course_code', 'course_name', 'trimister']

#...BTE...
class bte_eve_batch_info_form(forms.ModelForm):
    class Meta:
        model = BTE_eve_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class bte_eve_course_list_form(forms.ModelForm):
    class Meta:
        model = BTE_eve_course_list
        fields = ['course_code', 'course_name', 'trimister']

class bte_day_batch_info_form(forms.ModelForm):
    class Meta:
        model = BTE_day_batch_info
        fields = ['batch_no', 'section', 'st_number', 'trimister']

class bte_day_course_list_form(forms.ModelForm):
    class Meta:
        model = BTE_day_course_list
        fields = ['course_code', 'course_name', 'trimister']


class eve_routine_form(forms.ModelForm):
    class Meta:
        model = EVE_routine
        fields = ['exam_date', 'exam_time', 'weekday', 'course_code', 'course_name', 'dept', 'batch', 'section', 'room', 'st_number']

class day_routine_form(forms.ModelForm):
    class Meta:
        model = DAY_routine
        fields = ['exam_date', 'exam_time', 'weekday', 'course_code', 'course_name', 'dept', 'batch', 'section', 'room', 'st_number']

