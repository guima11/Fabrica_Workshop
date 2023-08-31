from rest_framework import routers
from .views import TodoListViewset, PessoaViewset

router = routers.DefaultRouter()
router.register(r'todo', TodoListViewset)
router.register(r'pessoa', PessoaViewset)

urlpatterns = router.urls
