from movies.viewsets import MoviesViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('movies', MoviesViewset)  



