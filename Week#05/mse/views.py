from django.shortcuts import render, redirect
from .forms import PropertyForm
# def show_my_form(request):
#     form = PropertyForm()
#     return render(request, 'my_form_template.html', {'form': form})
def show_my_form(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the property to the database
            return redirect('property_form')  # Redirect to clear the form or to a success page
    else:
        form = PropertyForm() # A blank form for GET requests
        
    return render(request, 'mse/my_form_template.html', {'form': form})