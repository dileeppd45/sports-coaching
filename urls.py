from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.login, name="login"),
    path('login', views.login, name="login"),
    path('admin_home', views.admin_home, name='admin_home'),
    path('register_physios', views.register_physios, name='register_physios'),
    path('physios_register', views.physios_register, name='physios_register'),
    path('register_coach', views.register_coach, name='register_coach'),
    path('coach_register', views.coach_register, name='coach_register'),
    path('admin_view_coach', views.admin_view_coach, name='admin_view_coach'),
    path('edit_venue/<int:id>', views.edit_venue, name='edit_venue'),
    path('venue_edit', views.venue_edit, name='venue_edit'),
    path('admin_view_venue', views.admin_view_venue, name='admin_view_venue'),
    path('venue_register', views.venue_register, name='venue_register'),
    path('register_venue', views.register_venue, name='register_venue'),
    path('view_physios', views.view_physios, name='view_physios'),
    path('physios_home', views.physios_home, name='physios_home'),
    path('coach_home', views.coach_home, name='coach_home'),
    path('player_register', views.player_register, name='player_register'),
    path('register_player', views.register_player, name='register_player'),
    path('coach_view_player', views.coach_view_player, name='coach_view_player'),
    path('upload_game_plan', views.upload_game_plan, name='upload_game_plan'),
    path('coach_view_game_plan', views.coach_view_game_plan, name='coach_view_game_plan'),
    path('add_schedule', views.add_schedule, name='add_schedule'),
    path('coach_view_schedule', views.coach_view_schedule, name='coach_view_schedule'),
    path('add_time_schedule', views.add_time_schedule, name='add_time_schedule'),
    path('time_schedule_add', views.time_schedule_add, name='time_schedule_add'),
    path('coach_view_time_schedule', views.coach_view_time_schedule, name='coach_view_time_schedule'),
    path('upload_video', views.upload_video, name='upload_video'),
    path('video_upload', views.video_upload, name='video_upload'),
    path('coach_view_video', views.coach_view_video, name='coach_view_video'),
    path('physio_view_players', views.physio_view_players, name='physio_view_players'),
    path('physio_view_fitness_details/<str:id>', views.physio_view_fitness_details, name='physio_view_fitness_details'),
    path('physio_interactions', views.physio_interactions, name='physio_interactions'),
    path('reply_players/<int:id>', views.reply_players, name='reply_players'),
    path('players_reply', views.players_reply, name='players_reply'),
    path('edit_fitness_details/<int:id>', views.edit_fitness_details, name='edit_fitness_details'),
    path('fitness_details_edit', views.fitness_details_edit, name='fitness_details_edit'),
    path('add_fitness_details/<str:id>', views.add_fitness_details, name='add_fitness_details'),
    path('fitness_details_add', views.fitness_details_add, name='fitness_details_add'),
    path('fitness_details_edit', views.fitness_details_edit, name='fitness_details_edit'),
    path('delete_fitness_details/<int:id>', views.delete_fitness_details, name='delete_fitness_details'),
    path('edit_physio/<str:id>', views.edit_physio, name='edit_physio'),
    path('physio_edit', views.physio_edit, name='physio_edit'),
    path('delete_physio/<str:id>', views.delete_physio, name='delete_physio'),
    path('delete_venue/<int:id>', views.delete_venue, name='delete_venue'),
    path('edit_schedule/<int:id>', views.edit_schedule, name='edit_schedule'),
    path('schedule_edit', views.schedule_edit, name='schedule_edit'),
    path('delete_schedule/<int:id>', views.delete_schedule, name='delete_schedule'),
    path('edit_game_plan/<int:id>', views.edit_game_plan, name='edit_game_plan'),
    path('game_plan_edit', views.game_plan_edit, name='game_plan_edit'),
    path('delete_game_plan/<int:id>', views.delete_game_plan, name='delete_game_plan'),
    path('delete_video/<int:id>', views.delete_video, name='delete_video'),
    path('edit_time_schedule/<int:id>', views.edit_time_schedule, name='edit_time_schedule'),
    path('time_schedule_edit', views.game_plan_edit, name='time_schedule_edit'),
    path('delete_time_schedule/<int:id>', views.delete_time_schedule, name='delete_time_schedule'),







    ]