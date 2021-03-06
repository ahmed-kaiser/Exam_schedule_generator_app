from django.urls import path, include
from . import views

urlpatterns = [
    path('login.html', views.login_page, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('', views.admin, name='admin'),
    path('admin.html', views.admin, name='admin'),
    path('changepass.html', views.changepass, name='changepass'),
    path('superuser.html', views.superuser, name='superuser'),
    path('subuser.html', views.subuser, name='subuser'),
    path('create_superuser', views.create_superuser, name='create_superuser'),
    path('createuser', views.createuser, name='createuser'),
    path('remove_user/<int:value>', views.remove_user, name='remove_user'),
    path('error.html', views.error, name='error'),

    path('index.html', views.index, name='index'),
    path('view_routine_eve.html', views.view_routine_eve, name='view_routine_eve'),
    path('view_routine_day.html', views.view_routine_day, name='view_routine_day'),
    path('view_search_schedule_day.html', views.view_search_schedule_day, name='view_search_schedule_day'),
    path('view_search_schedule_eve.html', views.view_search_schedule_eve, name='view_search_schedule_eve'),
    
    #...........Room.........................
    path('room.html', views.room, name='room'),
    path('room_search.html', views.room_search, name='room_search'),
    path('room_delete/<int:value>', views.room_delete, name='room_delete'),

    # CSE.................................
    path('cse_admin.html', views.cse_admin, name='cse_admin'),
    path('cse_eve_offered_courses.html', views.cse_eve_offered_courses, name='cse_eve_offered_courses'),
    path('cse_eve_course_search.html', views.cse_eve_course_search, name='cse_eve_course_search'),
    path('cse_eve_course_delete/<int:value>', views.cse_eve_course_delete, name='cse_eve_course_delete'),
    path('cse_eve_get_offered_courses/<int:value>', views.cse_eve_get_offered_courses, name='cse_eve_get_offered_courses'),
    path('cse_eve_edit_offered_courses.html', views.cse_eve_edit_offered_courses, name='cse_eve_edit_offered_courses'),
    path('cse_eve_update_offered_courses/<int:value>', views.cse_eve_update_offered_courses, name='cse_eve_update_offered_courses'),
    path('cse_eve_batch_info.html', views.cse_eve_batch_info, name='cse_eve_batch_info'),
    path('cse_eve_get_batch_info/<int:value1>/<str:value2>', views.cse_eve_get_batch_info, name='cse_eve_get_batch_info'),
    path('cse_eve_edit_batch_info.html', views.cse_eve_edit_batch_info, name='cse_eve_edit_batch_info'),
    path('cse_eve_update_batch_info/<int:value>', views.cse_eve_update_batch_info, name='cse_eve_update_batch_info'),
    path('cse_eve_delete_batch_info/<int:value>', views.cse_eve_delete_batch_info, name='cse_eve_delete_batch_info'),
    path('cse_eve_trimister.html', views.cse_eve_trimister, name='cse_eve_trimister'),
    path('cse_eve_delete_trimister/<str:value>', views.cse_eve_delete_trimister, name='cse_eve_delete_trimister'),

    path('cse_day_offered_courses.html', views.cse_day_offered_courses, name='cse_day_offered_courses'),
    path('cse_day_course_search.html', views.cse_day_course_search, name='cse_day_course_search'),
    path('cse_day_course_delete/<int:value>', views.cse_day_course_delete, name='cse_day_course_delete'),
    path('cse_day_get_offered_courses/<int:value>', views.cse_day_get_offered_courses, name='cse_day_get_offered_courses'),
    path('cse_day_edit_offered_courses.html', views.cse_day_edit_offered_courses, name='cse_day_edit_offered_courses'),
    path('cse_day_update_offered_courses/<int:value>', views.cse_day_update_offered_courses, name='cse_day_update_offered_courses'),
    path('cse_day_batch_info.html', views.cse_day_batch_info, name='cse_day_batch_info'),
    path('cse_day_get_batch_info/<int:value1>/<str:value2>', views.cse_day_get_batch_info, name='cse_day_get_batch_info'),
    path('cse_day_edit_batch_info.html', views.cse_day_edit_batch_info, name='cse_day_edit_batch_info'),
    path('cse_day_update_batch_info/<int:value>', views.cse_day_update_batch_info, name='cse_day_update_batch_info'),
    path('cse_day_delete_batch_info/<int:value>', views.cse_day_delete_batch_info, name='cse_day_delete_batch_info'),
    path('cse_day_trimister.html', views.cse_day_trimister, name='cse_day_trimister'),
    path('cse_day_delete_trimister/<str:value>', views.cse_day_delete_trimister, name='cse_day_delete_trimister'),

     # EEE.................................
    path('eee_admin.html', views.eee_admin, name='eee_admin'),
    path('eee_eve_offered_courses.html', views.eee_eve_offered_courses, name='eee_eve_offered_courses'),
    path('eee_eve_course_search.html', views.eee_eve_course_search, name='eee_eve_course_search'),
    path('eee_eve_course_delete/<int:value>', views.eee_eve_course_delete, name='eee_eve_course_delete'),
    path('eee_eve_get_offered_courses/<int:value>', views.eee_eve_get_offered_courses, name='eee_eve_get_offered_courses'),
    path('eee_eve_edit_offered_courses.html', views.eee_eve_edit_offered_courses, name='eee_eve_edit_offered_courses'),
    path('eee_eve_update_offered_courses/<int:value>', views.eee_eve_update_offered_courses, name='eee_eve_update_offered_courses'),
    path('eee_eve_batch_info.html', views.eee_eve_batch_info, name='eee_eve_batch_info'),
    path('eee_eve_get_batch_info/<int:value1>/<str:value2>', views.eee_eve_get_batch_info, name='eee_eve_get_batch_info'),
    path('eee_eve_edit_batch_info.html', views.eee_eve_edit_batch_info, name='eee_eve_edit_batch_info'),
    path('eee_eve_update_batch_info/<int:value>', views.eee_eve_update_batch_info, name='eee_eve_update_batch_info'),
    path('eee_eve_delete_batch_info/<int:value>', views.eee_eve_delete_batch_info, name='eee_eve_delete_batch_info'),
    path('eee_eve_trimister.html', views.eee_eve_trimister, name='eee_eve_trimister'),
    path('eee_eve_delete_trimister/<str:value>', views.eee_eve_delete_trimister, name='eee_eve_delete_trimister'),

    path('eee_day_offered_courses.html', views.eee_day_offered_courses, name='eee_day_offered_courses'),
    path('eee_day_course_search.html', views.eee_day_course_search, name='eee_day_course_search'),
    path('eee_day_course_delete/<int:value>', views.eee_day_course_delete, name='eee_day_course_delete'),
    path('eee_day_get_offered_courses/<int:value>', views.eee_day_get_offered_courses, name='eee_day_get_offered_courses'),
    path('eee_day_edit_offered_courses.html', views.eee_day_edit_offered_courses, name='eee_day_edit_offered_courses'),
    path('eee_day_update_offered_courses/<int:value>', views.eee_day_update_offered_courses, name='eee_day_update_offered_courses'),
    path('eee_day_batch_info.html', views.eee_day_batch_info, name='eee_day_batch_info'),
    path('eee_day_get_batch_info/<int:value1>/<str:value2>', views.eee_day_get_batch_info, name='eee_day_get_batch_info'),
    path('eee_day_edit_batch_info.html', views.eee_day_edit_batch_info, name='eee_day_edit_batch_info'),
    path('eee_day_update_batch_info/<int:value>', views.eee_day_update_batch_info, name='eee_day_update_batch_info'),
    path('eee_day_delete_batch_info/<int:value>', views.eee_day_delete_batch_info, name='eee_day_delete_batch_info'),
    path('eee_day_trimister.html', views.eee_day_trimister, name='eee_day_trimister'),
    path('eee_day_delete_trimister/<str:value>', views.eee_day_delete_trimister, name='eee_day_delete_trimister'),

    # CEN.................................
    path('cen_admin.html', views.cen_admin, name='cen_admin'),
    path('cen_eve_offered_courses.html', views.cen_eve_offered_courses, name='cen_eve_offered_courses'),
    path('cen_eve_course_search.html', views.cen_eve_course_search, name='cen_eve_course_search'),
    path('cen_eve_course_delete/<int:value>', views.cen_eve_course_delete, name='cen_eve_course_delete'),
    path('cen_eve_get_offered_courses/<int:value>', views.cen_eve_get_offered_courses, name='cen_eve_get_offered_courses'),
    path('cen_eve_edit_offered_courses.html', views.cen_eve_edit_offered_courses, name='cen_eve_edit_offered_courses'),
    path('cen_eve_update_offered_courses/<int:value>', views.cen_eve_update_offered_courses, name='cen_eve_update_offered_courses'),
    path('cen_eve_batch_info.html', views.cen_eve_batch_info, name='cen_eve_batch_info'),
    path('cen_eve_get_batch_info/<int:value1>/<str:value2>', views.cen_eve_get_batch_info, name='cen_eve_get_batch_info'),
    path('cen_eve_edit_batch_info.html', views.cen_eve_edit_batch_info, name='cen_eve_edit_batch_info'),
    path('cen_eve_update_batch_info/<int:value>', views.cen_eve_update_batch_info, name='cen_eve_update_batch_info'),
    path('cen_eve_delete_batch_info/<int:value>', views.cen_eve_delete_batch_info, name='cen_eve_delete_batch_info'),
    path('cen_eve_trimister.html', views.cen_eve_trimister, name='cen_eve_trimister'),
    path('cen_eve_delete_trimister/<str:value>', views.cen_eve_delete_trimister, name='cen_eve_delete_trimister'),

    path('cen_day_offered_courses.html', views.cen_day_offered_courses, name='cen_day_offered_courses'),
    path('cen_day_course_search.html', views.cen_day_course_search, name='cen_day_course_search'),
    path('cen_day_course_delete/<int:value>', views.cen_day_course_delete, name='cen_day_course_delete'),
    path('cen_day_get_offered_courses/<int:value>', views.cen_day_get_offered_courses, name='cen_day_get_offered_courses'),
    path('cen_day_edit_offered_courses.html', views.cen_day_edit_offered_courses, name='cen_day_edit_offered_courses'),
    path('cen_day_update_offered_courses/<int:value>', views.cen_day_update_offered_courses, name='cen_day_update_offered_courses'),
    path('cen_day_batch_info.html', views.cen_day_batch_info, name='cen_day_batch_info'),
    path('cen_day_get_batch_info/<int:value1>/<str:value2>', views.cen_day_get_batch_info, name='cen_day_get_batch_info'),
    path('cen_day_edit_batch_info.html', views.cen_day_edit_batch_info, name='cen_day_edit_batch_info'),
    path('cen_day_update_batch_info/<int:value>', views.cen_day_update_batch_info, name='cen_day_update_batch_info'),
    path('cen_day_delete_batch_info/<int:value>', views.cen_day_delete_batch_info, name='cen_day_delete_batch_info'),
    path('cen_day_trimister.html', views.cen_day_trimister, name='cen_day_trimister'),
    path('cen_day_delete_trimister/<str:value>', views.cen_day_delete_trimister, name='cen_day_delete_trimister'),

    # BTE.................................
    path('bte_admin.html', views.bte_admin, name='bte_admin'),
    path('bte_eve_offered_courses.html', views.bte_eve_offered_courses, name='bte_eve_offered_courses'),
    path('bte_eve_course_search.html', views.bte_eve_course_search, name='bte_eve_course_search'),
    path('bte_eve_course_delete/<int:value>', views.bte_eve_course_delete, name='bte_eve_course_delete'),
    path('bte_eve_get_offered_courses/<int:value>', views.bte_eve_get_offered_courses, name='bte_eve_get_offered_courses'),
    path('bte_eve_edit_offered_courses.html', views.bte_eve_edit_offered_courses, name='bte_eve_edit_offered_courses'),
    path('bte_eve_update_offered_courses/<int:value>', views.bte_eve_update_offered_courses, name='bte_eve_update_offered_courses'),
    path('bte_eve_batch_info.html', views.bte_eve_batch_info, name='bte_eve_batch_info'),
    path('bte_eve_get_batch_info/<int:value1>/<str:value2>', views.bte_eve_get_batch_info, name='bte_eve_get_batch_info'),
    path('bte_eve_edit_batch_info.html', views.bte_eve_edit_batch_info, name='bte_eve_edit_batch_info'),
    path('bte_eve_update_batch_info/<int:value>', views.bte_eve_update_batch_info, name='bte_eve_update_batch_info'),
    path('bte_eve_delete_batch_info/<int:value>', views.bte_eve_delete_batch_info, name='bte_eve_delete_batch_info'),
    path('bte_eve_trimister.html', views.bte_eve_trimister, name='bte_eve_trimister'),
    path('bte_eve_delete_trimister/<str:value>', views.bte_eve_delete_trimister, name='bte_eve_delete_trimister'),

    path('bte_day_offered_courses.html', views.bte_day_offered_courses, name='bte_day_offered_courses'),
    path('bte_day_course_search.html', views.bte_day_course_search, name='bte_day_course_search'),
    path('bte_day_course_delete/<int:value>', views.bte_day_course_delete, name='bte_day_course_delete'),
    path('bte_day_get_offered_courses/<int:value>', views.bte_day_get_offered_courses, name='bte_day_get_offered_courses'),
    path('bte_day_edit_offered_courses.html', views.bte_day_edit_offered_courses, name='bte_day_edit_offered_courses'),
    path('bte_day_update_offered_courses/<int:value>', views.bte_day_update_offered_courses, name='bte_day_update_offered_courses'),
    path('bte_day_batch_info.html', views.bte_day_batch_info, name='bte_day_batch_info'),
    path('bte_day_get_batch_info/<int:value1>/<str:value2>', views.bte_day_get_batch_info, name='bte_day_get_batch_info'),
    path('bte_day_edit_batch_info.html', views.bte_day_edit_batch_info, name='bte_day_edit_batch_info'),
    path('bte_day_update_batch_info/<int:value>', views.bte_day_update_batch_info, name='bte_day_update_batch_info'),
    path('bte_day_delete_batch_info/<int:value>', views.bte_day_delete_batch_info, name='bte_day_delete_batch_info'),
    path('bte_day_trimister.html', views.bte_day_trimister, name='bte_day_trimister'),
    path('bte_day_delete_trimister/<str:value>', views.bte_day_delete_trimister, name='bte_day_delete_trimister'),

    #....Routine Evening...............
    path('eve_routine.html', views.eve_routine, name='eve_routine'),
    path('eve_generate_routine', views.eve_generate_routine, name='eve_generate_routine'),
    path('eve_delete_routine', views.eve_delete_routine, name='eve_delete_routine'),
    path('eve_search_schedule.html/<int:value>', views.eve_search_schedule, name='eve_search_schedule'),
    path('eve_edit_schedule.html', views.eve_edit_schedule, name='eve_edit_schedule'),
    path('eve_get_schedule_info/<int:value>', views.eve_get_schedule_info, name='eve_get_schedule_info'),
    path('eve_update_schedule_info/<int:value>', views.eve_update_schedule_info, name='eve_update_schedule_info'),
    path('eve_delete_schedule_info/<int:value>', views.eve_delete_schedule_info, name='eve_delete_schedule_info'),
    path('eve_publish_schedule.html', views.eve_publish_schedule, name='eve_publish_schedule'),
    path('eve_cancel_publish_schedule', views.eve_cancel_publish_schedule, name='eve_cancel_publish_schedule'),


    #....Routine Day...............
    path('day_routine.html', views.day_routine, name='day_routine'),
    path('day_generate_routine', views.day_generate_routine, name='day_generate_routine'),
    path('day_delete_routine', views.day_delete_routine, name='day_delete_routine'),
    path('day_search_schedule.html/<int:value>', views.day_search_schedule, name='day_search_schedule'),
    path('day_edit_schedule.html', views.day_edit_schedule, name='day_edit_schedule'),
    path('day_get_schedule_info/<int:value>', views.day_get_schedule_info, name='day_get_schedule_info'),
    path('day_update_schedule_info/<int:value>', views.day_update_schedule_info, name='day_update_schedule_info'),
    path('day_delete_schedule_info/<int:value>', views.day_delete_schedule_info, name='day_delete_schedule_info'),
    path('day_publish_schedule.html', views.day_publish_schedule, name='day_publish_schedule'),
    path('day_cancel_publish_schedule', views.day_cancel_publish_schedule, name='day_cancel_publish_schedule'),

]
