Interfaces de programmation
=========================

Structure des vues
---------------

L'application est organisée autour de vues fonctionnelles réparties dans trois modules principaux.

Module principal (oc_lettings_site)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def index(request):
       """
       Vue de la page d'accueil principale.
       
       Cette vue affiche la page d'accueil avec les liens vers 
       les sections principales de l'application.
       """
       return render(request, 'index.html')


Module Lettings
~~~~~~~~~~~~

.. code-block:: python

   def index(request):
       """
       Vue de la liste des locations.
       
       Affiche toutes les locations disponibles dans le système.
       """
       lettings_list = Letting.objects.all()
       context = {'lettings_list': lettings_list}
       return render(request, 'lettings/index.html', context)

   def letting(request, letting_id):
       """
       Vue détaillée d'une location.
       
       Affiche les détails d'une location spécifique identifiée par son ID.
       Lève une 404 si la location n'existe pas.
       """
       letting = get_object_or_404(Letting, id=letting_id)
       context = {
           'title': letting.title,
           'address': letting.address,
       }
       return render(request, 'lettings/letting.html', context)

Module Profiles
~~~~~~~~~~~~

.. code-block:: python

   def index(request):
       """
       Vue de la liste des profils.
       
       Affiche tous les profils utilisateurs disponibles.
       """
       profiles_list = Profile.objects.all()
       context = {'profiles_list': profiles_list}
       return render(request, 'profiles/index.html', context)

   def profile(request, username):
       """
       Vue détaillée d'un profil.
       
       Affiche les détails d'un profil utilisateur spécifique.
       Lève une 404 si le profil n'existe pas.
       """
       profile = get_object_or_404(Profile, user__username=username)
       context = {'profile': profile}
       return render(request, 'profiles/profile.html', context)

Organisation des URLs
------------------

.. code-block:: python

   # URLs principales (oc_lettings_site/urls.py)
   urlpatterns = [
       path('', views.index, name='index'),
       path('lettings/', include('lettings.urls', namespace='lettings')),
       path('profiles/', include('profiles.urls', namespace='profiles')),
       path('admin/', admin.site.urls),
       path('sentry-test/', lambda request: 1 / 0, name='sentry-test'),
   ]
   
   # URLs de l'application lettings (lettings/urls.py)
   app_name = 'lettings'
   urlpatterns = [
       path('', views.index, name='index'),
       path('<int:letting_id>/', views.letting, name='letting'),
   ]
   
   # URLs de l'application profiles (profiles/urls.py)
   app_name = 'profiles'
   urlpatterns = [
       path('', views.index, name='index'),
       path('<str:username>/', views.profile, name='profile'),
   ]
