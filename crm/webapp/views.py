from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, UpadteRecordForm, AddRecordForm
from django.contrib.auth.models import auth #უიზერი რომ დალოგაუთდეს
from django.contrib.auth import authenticate #აუთენთიპიკაციისთვის იუზერის სახილის და პაროლის მიხედვით

from django.contrib.auth.decorators import login_required #დარეგისტრირება აუცილებელია

from . models import Record #მოდელების დაიმპორტება რომ გამოვაჩინო ჩანაწერები დაშბორძე

#ჰოუმ გვერდი

def home(request):
    return render(request, "webapp/index.html")


#რეგისტრაცია იუზერის
def register(request):
    form = CreateUserForm()
    #ამოწმებს იუზერის მიერ შემოყვანილი ინფორმაცია პოსტის მეთოდით არის თუ არა forms.py-დან შეყვანილი
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            #გადაჰყავს იუზერი რეგისტრაციის მერე
            return redirect('my-login')

    #გადააქვს ინფორმაცია register თემფლეითში
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)



#ლოგინი იუზერის
def my_login(request):
    form = LoginForm()
    #თუ რექუესტი პოსტია იგზავნება ყველა ინფორმაცია იუზერის მიერ შეყვანილი ლოგინის ფორმაში(forms.py)
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            #თუ იუზერის მიერ შეყვანილი ინფორმაცია ემთხვევა დატაბეისში შენახულ ინფორმაციას
            user = authenticate(request, username=username, password=password) 
            
            #ამოწმებს აუტენტიფიკაციას და გადაჰყავს დაშბორძე თუ ესეთი იუზერი არსებობს
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    #გადააქვს ინფორმაცია my-login თემფლეითში     
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)


#დაშბორდი, თუ დარეგისტრირებული არ ხარ ვერ შეხვალ

@login_required(login_url='my-login')
def dashboard(request):
    #წამოგვაქვს ინფორმაცია მოდელიდან
    my_records = Record.objects.all()

    #key-ს გამოყენებით მივმართავთ for ლუპში ინფორმაციას dashboard.html-ში
    context = {"records": my_records}

    return render(request, 'webapp/dashboard.html', context=context)




#ჩანაწერის დამატება
@login_required(login_url='my-login')
def create_record(request):
    form = AddRecordForm()

    if request.method == "POST":
        form = AddRecordForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


#ჩანაწერის დააპდეითება
@login_required(login_url='my-login')
def update_record(request, pk): #pk-ს გაწერით ფუნქცია იჭერს აიდის
    record = Record.objects.get(id=pk) #pk-ზე დაყრდნობით იღებს ცვლადს და ინახება record-ში

    form = UpadteRecordForm(instance=record) #იღებს შესავსებ ფორმას რომელიც დაყრდნობილია pk-ზე

    if request.method == "POST":
        form = UpadteRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/update-record.html', context=context)



#კონკრეტული ჩანაწერის ნახვა 
@login_required(login_url='my-login')
def view_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'webapp/view-record.html', context=context)




#წაშლა ჩანაწერის
@login_required(login_url='my-login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)

    record.delete()

    return redirect('dashboard')




#კოგაუთი იუზერის
def user_logout(request):

    auth.logout(request)

    return redirect('my-login')