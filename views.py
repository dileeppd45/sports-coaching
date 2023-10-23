from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.db import connection
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from . import views

def login(request):
    if request.method == "POST":
        userid = request.POST['userid']
        password = request.POST['password']
        cursor = connection.cursor()
        cursor.execute("select * from login where user_id= '" + userid + "' AND password = '" + password + "'")
        admin = cursor.fetchone()
        if admin == None:
            cursor.execute("select * from coach_details where coach_id = '" + userid + "' AND password = '" + password + "' ")
            coach = cursor.fetchone()
            if coach == None:
                cursor.execute("select * from physios  where physios_id ='"+ userid +"' and password ='"+ password +"' ")
                physios = cursor.fetchone()
                if physios == None:
                    return HttpResponse("<script>alert('Invalid User or not approved yet..');window.location='../login';</script>")
                else:
                    request.session['phyid'] = userid
                    return redirect('physios_home')

            else:
                request.session['coachid'] = userid
                return redirect('coach_home')
        else:
            request.session['adminid'] = userid
            return redirect('admin_home')
    return render(request, "login.html")

def admin_home(request):
    return render(request, 'admin_header.html')

def physios_home(request):
    return render(request, 'physios_home.html')

def coach_home(request):
    return render(request, 'coach_home.html')

def register_physios(request):
    return render(request, 'register_physios.html')

def physios_register(request):
    if request.method=="POST":
        id = request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        age = request.POST['age']
        password = request.POST['password']
        cursor = connection.cursor()
        cursor.execute("select * from physios where idcollege ='"+str(id)+"' ")
        data = cursor.fetchone()
        if data == None:
            cursor.execute("select * from coach_details where coach_id = '"+str(id)+"' ")
            data = cursor.fetchone()
            if data == None:
                cursor.execute("select * from login where admin_id = '" + str(id) + "' ")
                data = cursor.fetchone()
                if data == None:
                    cursor.execute("select * from player_details where player_id = '" + str(id) + "' ")
                    data = cursor.fetchone()
                    if data == None:
                        cursor.execute("insert into physios values ('" + str(id) + "','" + str(name) + "', '" + str(address) + "', '" + str(phone) + "','" + str(email) + "','" + str(age) + "','" + str(password) + "')")
                        return render(request, "login.html")
        else:
            return HttpResponse("<script>alert('id already exists..  please enter a unique id');window.location='../admin_home';</script>")

def view_physios(request):
    cursor=connection.cursor()
    cursor.execute("select * from physios")
    data = cursor.fetchall()
    return render(request, 'view_physios.html', {'data':data})



def register_coach(request):
    return render(request, 'register_coach.html')


def coach_register(request):
    if request.method=="POST":
        id = request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        age = request.POST['age']
        password = request.POST['password']
        cursor = connection.cursor()
        cursor.execute("select * from physios where idcollege ='"+str(id)+"' ")
        data = cursor.fetchone()
        if data == None:
            cursor.execute("select * from coach_details where coach_id = '"+str(id)+"' ")
            data = cursor.fetchone()
            if data == None:
                cursor.execute("select * from login where admin_id = '" + str(id) + "' ")
                data = cursor.fetchone()
                if data == None:
                    cursor.execute("select * from player_details where player_id = '" + str(id) + "' ")
                    data = cursor.fetchone()
                    if data == None:
                        cursor.execute("insert into coach_details values ('" + str(id) + "','" + str(name) + "', '" + str(address) + "', '" + str(phone) + "','" + str(email) + "','" + str(age) + "','" + str(password) + "','pending')")
                        return render(request, "login.html")
        else:
            return HttpResponse("<script>alert('id already exists..  please enter a unique id');window.location='../admin_home';</script>")

def admin_view_coach(request):
    cursor=connection.cursor()
    cursor.execute("select * from coach_details")
    data = cursor.fetchall()
    return render(request, 'admin_view_coach.html', {'data':data})

def admin_view_venue(request):
    cursor = connection.cursor()
    cursor.execute("select * from venues_details")
    data = cursor.fetchall()
    return render(request, 'admin_view_venue.html', {'data':data})

def edit_venue(request, id):
    cursor = connection.cursor()
    cursor.execute("select * from venues_details where venue_id = '"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request, 'edit_venue.html', {'data': data})

def venue_edit(request):
    if request.method == "POST":
        id=request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        cursor = connection.cursor()
        cursor.execute("update venues_details set name = '"+str(name)+"' where venue_id = '"+str(id)+"' ")
        cursor.execute("update venues_details set address ='"+str(address)+"' where venue_id = '"+str(id)+"' ")
        cursor.execute("update venues_details set phone = '" + str(phone) + "' where venue_id = '" + str(id) + "' ")
        cursor.execute("update venues_details set email ='" + str(email) + "' where venue_id = '" + str(id) + "' ")
        return redirect("admin_view_venue")


def register_venue(request):
    return render(request, 'register_venue.html')

def venue_register(request):
    if request.method == "POST":
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        cursor = connection.cursor()
        cursor.execute("insert into venues_details values (null,'" + str(name) + "','" + str(address) + "', '" + str(email) + "', '" + str(phone)+"') ")
        return redirect("admin_view_venue")


def register_player(request):
    return render(request, 'register_player.html')

def player_register(request):
    if request.method=="POST":
        id = request.POST['id']
        name = request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        salary = request.POST['salary']
        cursor = connection.cursor()
        cursor.execute("select * from physios where idcollege ='"+str(id)+"' ")
        data = cursor.fetchone()
        cursor.execute("insert into player_details values ('" + str(id) + "','" + str(name) + "', '" + str(address) + "', '" + str(phone) + "','" + str(email) + "','" + str(password) + "','" + str(salary) + "','pending')")
        return redirect('coach_view_player')
def coach_view_player(request):
    cursor = connection.cursor()
    cursor.execute("select * from player_details")
    data = cursor.fetchall()
    return render(request, 'coach_view_player.html', {'data': data})

def physio_view_players(request):
    cursor = connection.cursor()
    cursor.execute("select * from player_details")
    data = cursor.fetchall()
    return render(request, 'physio_view_player.html', {'data': data})

def physio_view_fitness_details(request, id):
    cursor = connection.cursor()
    cursor.execute("select * from player_fitness_details where player_id ='"+str(id)+"' ")
    data =cursor.fetchall()
    return render(request, 'physio_view_fitness_details.html',{'data': data})

def upload_game_plan(request):
    return render(request, 'upload_game_plan.html')

def coach_view_game_plan(request):
    cursor = connection.cursor()
    cursor.execute("select * from game_planning ")
    data = cursor.fetchall()
    return render(request, 'coach_view_game_plan.html',{'data':data})


def add_schedule(request):
    return render(request, 'add_schedule.html')

def schedule_add(request):
    if request.method == "POST":
        wakeup = request.POST['match_date']
        morning = request.POST['oponent']
        match_place = request.POST['match_place']
        timing = request.POST['timing']
        cursor = connection.cursor()
        cursor.execute("insert into schedule values (null,'" + str(wakeup) + "','" + str(morning) + "', '" + str(match_place) + "', '" + str(timing)+"') ")
        return redirect("coach_view_schedule")

def coach_view_schedule(request):
    cursor = connection.cursor()
    cursor.execute("select * from game_schedule ")
    data = cursor.fetchall()
    return render(request, 'coach_view_schedule.html',{'data':data})

def add_time_schedule(request):
    return render(request, 'add_time_schedule.html')

def time_schedule_add(request):
    if request.method == "POST":
        wakeup = request.POST['wakeup']
        morning = request.POST['morning']
        intervel = request.POST['intervel']
        cursor = connection.cursor()
        cursor.execute("insert into time_schedule values (null,'" + str(wakeup) + "','" + str(morning) + "', '" + str(intervel) + "')")
        return redirect("coach_view_time_schedule")

def coach_view_time_schedule(request):
    cursor = connection.cursor()
    cursor.execute("select * from time_schedule ")
    data = cursor.fetchall()
    return render(request, 'coach_view_time_schedule.html',{'data':data})

def upload_video(request):
    return render(request, 'upload_video.html')

def video_upload(request):
    if request.method == "POST" and request.FILES['video']:
        title = request.POST['title']
        description = request.POST['description']
        video = request.POST['video']
        cursor = connection.cursor()
        cursor.execute("insert into video_library values (null,'" + str(title) + "','" + str(description) + "', '" + str(video) + "')")
        return redirect("coach_view_video")

def coach_view_video(request):
    cursor = connection.cursor()
    cursor.execute("select * from video_library ")
    data = cursor.fetchall()
    return render(request, 'coach_view_video.html',{'data':data})

def physio_interactions(request):
    cursor = connection.cursor()
    cursor.execute("select * from player_physio_interaction ")
    data = cursor.fetchall()
    return render(request, 'physio_reply_interactions.html', {'data': data})

def reply_players(request, id):
    cursor = connection.cursor()
    cursor.execute("select * from player_physio_interaction where interaction_id ='"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request, 'reply_players.html',{'data':data})

def players_reply(request):
    if request.method == "POST":
        reply = request.POST['reply']
        id = request.POST['id']
        cursor = connection.cursor()
        cursor.execute("update player_physio_interaction set  message_reply = '"+str(reply)+"' where interaction_id ='"+ str(id) + "'")
        cursor.execute("update player_physio_interaction set  reply_date = curdate() where interaction_id ='"+ str(id) + "'")
        return redirect("physio_interactions")

def edit_fitness_details(request,id):
    cursor = connection.cursor()
    cursor.execute("select * from player_fitness_details where fitness_id ='" + str(id) + "' ")
    data = cursor.fetchone()
    return render(request, 'edit_fitness_details.html', {'data': data})

def add_fitness_details(request,id):

    return render(request, 'add_fitness_details.html', {'id': id})

def fitness_details_add(request):
    if request.method == "POST":
        age = request.POST['age']
        id = request.POST['id']
        weight = request.POST['weight']
        height = request.POST['height']
        running = request.POST['running']
        pushup = request.POST['pushup']
        pullup = request.POST['pullup']
        muscle = request.POST['muscle']
        stamina = request.POST['stamina']
        cursor = connection.cursor()
        cursor.execute("insert into player_fitness_details values (null,'" + str(id) + "', curdate(),'" + str(age) + "', '" + str(weight) + "', '" + str(height) + "', '" + str(running) + "', '" + str(pushup) + "', '" + str(pullup) + "', '" + str(muscle) + "', '" + str(stamina) + "')")
        return redirect('physio_view_fitness_details', id=str(id))




def fitness_details_edit(request):
    if request.method == "POST":
        age = request.POST['age']
        id = request.POST['id']
        name= request.POST['name']
        weight = request.POST['weight']
        height = request.POST['height']
        running = request.POST['running']
        pushup = request.POST['pushup']
        pullup = request.POST['pullup']
        muscle = request.POST['muscle']
        stamina = request.POST['stamina']
        cursor = connection.cursor()
        cursor.execute("update player_fitness_details set  age = '" + str(age) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  waight = '" + str(weight) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  height = '" + str(height) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  running_speed = '" + str(running) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  push_up = '" + str(pushup) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  pull_up = '" + str(pullup) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  muscle_pain = '" + str(muscle) + "' where fitness_id ='" + str(id) + "'")
        cursor.execute("update player_fitness_details set  stamina = '" + str(stamina) + "' where fitness_id ='" + str(id) + "'")
        return redirect("physio_view_fitness_details", id=str(name))

def delete_fitness_details(request, id):
    cursor = connection.cursor()
    cursor.execute("select player_id from player_fitness_details where fitness_id ='"+str(id)+"' ")
    data =cursor.fetchone()
    name=list(data)
    name=name[0]
    cursor.execute("delete from player_fitness_details where fitness_id = '" + str(id) + "' ")
    return redirect("physio_view_fitness_details", id=str(name))

def edit_physio(request, id):
    cursor = connection.cursor()
    cursor.execute("select  * from physios  where physios_id ='"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request, 'edit_physio.html',{'data':data})

def physio_edit(request):
    if request.method == "POST":
        id = request.POST['id']
        age = request.POST['age']
        name= request.POST['name']
        address = request.POST['address']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        cursor = connection.cursor()
        cursor.execute("update physios set  age = '" + str(age) + "' where physios_id ='" + str(id) + "'")
        cursor.execute("update physios set  name = '" + str(name) + "' where physios_id ='" + str(id) + "'")
        cursor.execute("update physios set  address = '" + str(address) + "' where physios_id ='" + str(id) + "'")
        cursor.execute("update physios set  phone = '" + str(phone) + "' where physios_id ='" + str(id) + "'")
        cursor.execute("update physios set  email = '" + str(email) + "' where physios_id ='" + str(id) + "'")
        cursor.execute("update physios set  password = '" + str(password) + "' where physios_id ='" + str(id) + "'")

        return redirect('view_physios')

def delete_physio(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from physios where physios_id = '" + str(id) + "' ")
    return redirect('view_physios')

def delete_venue(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from venues_details where venue_id = '" + str(id) + "' ")
    return redirect('admin_view_venue')


def edit_schedule(request, id):
    cursor = connection.cursor()
    cursor.execute("select  * from game_schedule  where game_schedule_id ='"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request, 'edit_schedule.html',{'data':data})

def schedule_edit(request):
    if request.method == "POST":
        id = request.POST['id']
        match_date= request.POST['match_date']
        opponent= request.POST['opponent']
        match_place = request.POST['match_place']
        timing = request.POST['timing']
        cursor = connection.cursor()
        cursor.execute("update game_schedule set  match_date = '" + str(match_date) + "' where game_schedule_id ='" + str(id) + "'")
        cursor.execute("update game_schedule set  opponent_name = '" + str(opponent) + "' where game_schedule_id ='" + str(id) + "'")
        cursor.execute("update game_schedule set  match_place = '" + str(match_place) + "' where game_schedule_id ='" + str(id) + "'")
        cursor.execute("update game_schedule set  timing = '" + str(timing) + "' where game_schedule_id ='" + str(id) + "'")

        return redirect('coach_view_schedule')

def delete_schedule(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from game_schedule where game_schedule_id = '" + str(id) + "' ")
    return redirect('coach_view_schedule')


def edit_game_plan(request, id):
    cursor = connection.cursor()
    cursor.execute("select  * from game_planning  where game_planning_id ='"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request, 'edit_game_planning.html',{'data':data})

def game_plan_edit(request):
    if request.method == "POST":
        id = request.POST['id']
        title= request.POST['title']
        description= request.POST['description']
        cursor = connection.cursor()
        cursor.execute("update game_planning set  title = '" + str(title) + "' where game_planning_id ='" + str(id) + "'")
        cursor.execute("update game_planning set  description = '" + str(description) + "' where game_planning_id ='" + str(id) + "'")

        return redirect('coach_view_game_plan')

def delete_game_plan(request,id):
    cursor = connection.cursor()
    cursor.execute("delete from game_planning where game_schedule_id = '" + str(id) + "' ")
    return redirect('coach_view_schedule')
def delete_video(request, id):
    cursor = connection.cursor()
    cursor.execute("delete from video_library where video_id = '" + str(id) + "' ")
    return redirect('coach_view_video')

def edit_time_schedule(request, id):
    cursor = connection.cursor()
    cursor.execute("select  * from time_schedule  where time_schedule_id ='"+str(id)+"' ")
    data = cursor.fetchone()
    return render(request, 'edit_time_schedule.html',{'data':data})

def time_schedule_edit(request):
    if request.method == "POST":
        id = request.POST['id']
        wakeup= request.POST['wakeup']
        morning= request.POST['morning']
        interval = request.POST['interval']
        cursor = connection.cursor()
        cursor.execute("update time_schedule set  wakeup_time = '" + str(wakeup) + "' where time_schedule_id ='" + str(id) + "'")
        cursor.execute("update time_schedule set  morning_ground_time = '" + str(morning) + "' where time_schedule_id ='" + str(id) + "'")
        cursor.execute("update time_schedule set  interval_details = '" + str(interval) + "' where time_schedule_id ='" + str(id) + "'")
        return redirect('coach_view_time_schedule')

def delete_time_schedule(request, id):
    cursor = connection.cursor()
    cursor.execute("delete from time_schedule where time_schedule_id = '" + str(id) + "' ")
    return redirect('coach_view_time_schedule')