import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User

from market.models import Profile, Favorites, Product


class FavoriteAddConsumer(WebsocketConsumer):
    def connect(self):
        print('Вошел!')
        self.accept()

    def disconnect(self, close_code):
        print('Вышел')

    # Receive message from WebSocket
    def receive(self, text_data):
        print('1')
        text_data_json = json.loads(text_data)
        pr_slug = text_data_json['product_slug']
        print(pr_slug)
        user = text_data_json['user']
        try:
            print('user')
            user = Profile.objects.get(user__username=user)
            fav = Favorites.objects.get(user=user)
            fav.products.add(Product.objects.get(slug=pr_slug))
            print(pr_slug)
            self.send(text_data=json.dumps({
                'pr_slug': pr_slug,
                'sus': 'true',
            }))
        except Exception as e:
            print(e)
            pass
