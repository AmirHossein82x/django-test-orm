from typing import Any
from django.core.management.base import BaseCommand
from django.core.management import call_command
from core.models import User, City, Profile
from store.models import Category, Product, Promotion, Comment, Order, OrderItem
from datetime import datetime


class Command(BaseCommand):
    help = "loading information!!!!"

    def handle(self, *args: Any, **options: Any) -> str | None:
        users = []
        cities = []
        profiles = []
        categories = []
        promotions = []
        products = []
        comments = []
        orders = []
        order_items = []
        call_command("migrate", "--noinput")
        call_command("flush", "--noinput")
        self.stdout.write(
            self.style.NOTICE("clearing old data!")

        )
        admin = User.objects.create(username="amirhossein", first_name="amirhossein", last_name="ghasemi",
                                    email="amirhosseing983@gmail.com", is_superuser=True, is_staff=True)
        users.append(admin)

        user1 = User.objects.create(
            username="mohammad_taha", first_name="mohammad taha", last_name="abbasi")
        users.append(user1)

        user2 = User.objects.create(
            username="mohammad", first_name="mohammad", last_name="mohammadi", email="mohammadi@gmail.com")
        users.append(user2)

        user3 = User.objects.create(
            username="yashar", first_name="yahsar", last_name="mohammadi", email="yashar@gmail.com")
        users.append(user3)

        user4 = User.objects.create(
            username="matin", first_name="matin", last_name="lotfi")
        users.append(user4)

        user5 = User.objects.create(username="sajjad", first_name="sajjad",
                                    last_name="barkhordari", email="barkhordari@gmail.com")
        users.append(user5)

        city1 = City.objects.create(title="Gharchack")
        cities.append(city1)
        city2 = City.objects.create(title="Varamin")
        cities.append(city2)
        city3 = City.objects.create(title="Tehran")
        cities.append(city3)

        profile1 = Profile.objects.create(
            user=admin, city=city1, age=21, phone_number="09301234567")
        profiles.append(profile1)
        profile2 = Profile.objects.create(
            user=user1, city=city1, age=20, phone_number="09123452123")
        profiles.append(profile2)
        profile3 = Profile.objects.create(
            user=user2, city=city2, age=19, phone_number="09123452123")
        profiles.append(profile3)
        profile4 = Profile.objects.create(
            user=user3, city=city2, age=18, phone_number="09124542546")
        profiles.append(profile4)
        profile5 = Profile.objects.create(user=user4, city=city3, age=17)
        profiles.append(profile5)
        profile6 = Profile.objects.create(user=user5, city=city1, age=16)
        profiles.append(profile6)

        category1 = Category.objects.create(title="shirt")
        categories.append(category1)
        category2 = Category.objects.create(title="sport")
        categories.append(category2)
        category3 = Category.objects.create(title="book")
        categories.append(category3)

        promotion1 = Promotion.objects.create(discount=0.20)
        promotions.append(promotion1)
        promotion2 = Promotion.objects.create(discount=0.30)
        promotions.append(promotion2)
        promotion3 = Promotion.objects.create(discount=0.50)
        promotions.append(promotion3)

        product1 = Product.objects.create(
            title="literature", price=2000, promotion=promotion1, is_active=True)
        product1.categories.add(category1, category2)
        products.append(product1)

        product2 = Product.objects.create(
            title="ball", price=2000, promotion=promotion2, is_active=True)
        product2.categories.add(category2)
        products.append(product2)

        product3 = Product.objects.create(
            title="long shirt", price=4000, promotion=promotion3, is_active=False)
        product3.categories.add(category1)
        products.append(product3)

        product4 = Product.objects.create(
            title="math", price=2000, is_active=False)
        product4.categories.add(category3)
        products.append(product4)

        product5 = Product.objects.create(
            title="water bottle", price=1000, is_active=False)
        product5.categories.add(category1)
        products.append(product5)

        product6 = Product.objects.create(
            title="sport shirt", promotion=promotion1,  price=4000, is_active=True)
        product6.categories.add(category1, category2)
        products.append(product6)

        product7 = Product.objects.create(
            title="shoes", price=2000, is_active=False)
        product7.categories.add(category1, category2)
        products.append(product7)

        product8 = Product.objects.create(
            title="T-shirt", price=4000, is_active=True)
        product8.categories.add(category1, category2)
        products.append(product8)

        product9 = Product.objects.create(
            title="badminton", promotion=promotion2,  price=5000, is_active=True)
        product9.categories.add(category2)
        products.append(product9)

        product10 = Product.objects.create(
            title="art", price=3000, promotion=promotion3,  is_active=True)
        product10.categories.add(category3)
        products.append(product10)

        product11 = Product.objects.create(
            title="science", price=1000, is_active=False)
        product11.categories.add(category3)
        products.append(product11)

        product12 = Product.objects.create(
            title="watch", promotion=promotion3,  price=2000, is_active=False)
        product12.categories.add(category1)
        products.append(product12)

        comment1 = Comment.objects.create(
            user=user1, product=product1, text="good", created=datetime(year=2024, month=12, day=1), is_show=True)
        comments.append(comment1)
        comment2 = Comment.objects.create(
            user=user1, product=product2, text="good", created=datetime(year=2024, month=11, day=2), is_show=True)
        comments.append(comment2)
        comment3 = Comment.objects.create(
            user=user1, product=product3, text="good", created=datetime(year=2024, month=10, day=3), is_show=True)
        comments.append(comment3)
        comment4 = Comment.objects.create(
            user=user1, product=product4, text="good", created=datetime(year=2024, month=9, day=6))
        comments.append(comment4)
        comment5 = Comment.objects.create(
            user=user2, product=product5, text="bad", created=datetime(year=2024, month=8, day=7), is_show=True)
        comments.append(comment5)
        comment6 = Comment.objects.create(
            user=user2, product=product1, text="bad", created=datetime(year=2024, month=7, day=12))
        comments.append(comment6)
        comment7 = Comment.objects.create(
            user=user2, product=product11, text="bad", created=datetime(year=2024, month=6, day=10), is_show=True)
        comments.append(comment7)
        comment8 = Comment.objects.create(
            user=user2, product=product3, text="bad", created=datetime(year=2024, month=5, day=20))
        comments.append(comment8)
        comment9 = Comment.objects.create(
            user=user3, product=product4, text="bad", created=datetime(year=2022, month=4, day=29), is_show=True)
        comments.append(comment9)
        comment10 = Comment.objects.create(
            user=user3, product=product5, text="normal", created=datetime(year=2022, month=3, day=13))
        comments.append(comment10)
        comment11 = Comment.objects.create(
            user=user3, product=product2, text="normal", created=datetime(year=2022, month=2, day=16), is_show=True)
        comments.append(comment11)
        comment12 = Comment.objects.create(
            user=user3, product=product3, text="normal", created=datetime(year=2022, month=1, day=17))
        comments.append(comment12)
        comment13 = Comment.objects.create(
            user=user3, product=product2, text="normal", created=datetime(year=2022, month=1, day=18), is_show=True)
        comments.append(comment13)
        comment15 = Comment.objects.create(
            user=user4, product=product1, text="normal", created=datetime(year=2022, month=2, day=14))
        comments.append(comment15)
        comment16 = Comment.objects.create(
            user=user4, product=product2, text="great", created=datetime(year=2019, month=3, day=19), is_show=True)
        comments.append(comment16)
        comment17 = Comment.objects.create(
            user=user4, product=product3, text="great", created=datetime(year=2019, month=4, day=26))
        comments.append(comment17)
        comment18 = Comment.objects.create(
            user=user4, product=product4, text="great", created=datetime(year=2019, month=5, day=25), is_show=True)
        comments.append(comment18)
        comment19 = Comment.objects.create(
            user=user4, product=product5, text="great", created=datetime(year=2019, month=6, day=27))
        comments.append(comment19)
        comment20 = Comment.objects.create(
            user=user5, product=product6, text="great", created=datetime(year=2019, month=7, day=17), is_show=True)
        comments.append(comment20)
        comment21 = Comment.objects.create(
            user=user5, product=product7, text="not bad", created=datetime(year=2018, month=8, day=19), is_show=True)
        comments.append(comment21)
        comment22 = Comment.objects.create(
            user=user5, product=product8, text="not bad", created=datetime(year=2018, month=9, day=6))
        comments.append(comment22)
        comment23 = Comment.objects.create(
            user=user5, product=product9, text="not bad", created=datetime(year=2018, month=10, day=9), is_show=True)
        comments.append(comment23)
        comment24 = Comment.objects.create(
            user=user5, product=product10, text="not bad", created=datetime(year=2018, month=11, day=4), is_show=True)
        comments.append(comment24)
        comment25 = Comment.objects.create(
            user=user5, product=product11, text="the best", created=datetime(year=2018, month=11, day=2))
        comments.append(comment25)
        comment26 = Comment.objects.create(
            user=user5, product=product11, text="the best", created=datetime(year=2018, month=1, day=13), is_show=True)
        comments.append(comment26)

        order1 = Order.objects.create(user=user1, shipping="car", created=datetime(
            year=2019, month=7, day=17), is_delivered=True)
        orders.append(order1)

        order2 = Order.objects.create(user=user1, shipping="motor", created=datetime(
            year=2019, month=4, day=16), is_delivered=True)
        orders.append(order2)

        order3 = Order.objects.create(user=user2, shipping="motor", created=datetime(
            year=2024, month=2, day=18), is_delivered=False)
        orders.append(order3)

        order4 = Order.objects.create(user=user2, shipping="motor", created=datetime(
            year=2019, month=10, day=6), is_delivered=True)
        orders.append(order4)

        order5 = Order.objects.create(user=user3, shipping="truck", created=datetime(
            year=2024, month=4, day=9), is_delivered=False)
        orders.append(order5)

        order6 = Order.objects.create(user=user1, shipping="car", created=datetime(
            year=2019, month=12, day=20), is_delivered=True)
        orders.append(order6)

        orderItem1 = OrderItem.objects.create(
            order=order1, product=product1, quantity=2, price=3200)
        order_items.append(orderItem1)

        orderItem2 = OrderItem.objects.create(
            order=order1, product=product2, quantity=3, price=4200)
        order_items.append(orderItem2)

        orderItem3 = OrderItem.objects.create(
            order=order1, product=product7, quantity=1, price=2000)
        order_items.append(orderItem3)

        orderItem4 = OrderItem.objects.create(
            order=order1, product=product10, quantity=2, price=3000)
        order_items.append(orderItem4)

        orderItem5 = OrderItem.objects.create(
            order=order2, product=product1, quantity=2, price=3200)
        order_items.append(orderItem5)

        orderItem6 = OrderItem.objects.create(
            order=order2, product=product2, quantity=3, price=4200)
        order_items.append(orderItem6)

        orderItem7 = OrderItem.objects.create(
            order=order3, product=product8, quantity=3, price=1200)
        order_items.append(orderItem7)

        orderItem7 = OrderItem.objects.create(
            order=order4, product=product1, quantity=3, price=4800)
        order_items.append(orderItem7)
        orderItem7 = OrderItem.objects.create(
            order=order4, product=product2, quantity=2, price=2800)
        order_items.append(orderItem7)
        orderItem7 = OrderItem.objects.create(
            order=order4, product=product3, quantity=1, price=2000)
        order_items.append(orderItem7)

        orderItem8 = OrderItem.objects.create(
            order=order5, product=product6, quantity=3, price=9600)
        order_items.append(orderItem8)
        orderItem9 = OrderItem.objects.create(
            order=order5, product=product9, quantity=2, price=7000)
        order_items.append(orderItem9)

        orderItem10 = OrderItem.objects.create(
            order=order6, product=product6, quantity=1, price=3200)
        order_items.append(orderItem10)

        for user in users:
            user.set_password("1234")
            user.save()
            self.stdout.write(
                self.style.HTTP_INFO(
                    f"user {user.id} created --> {user.username}")

            )

        print("*" * 30)

        for city in cities:
            self.stdout.write(
                self.style.HTTP_INFO(f"city: {city.title} created")

            )

        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for profile in profiles:
            self.stdout.write(
                self.style.HTTP_INFO(
                    f"profile created for {profile.user.username}")

            )

        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for category in categories:
            self.stdout.write(
                self.style.HTTP_INFO(f"category: {category.title} created")

            )

        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for promotion in promotions:
            self.stdout.write(
                self.style.HTTP_INFO(
                    f"promotion: {promotion.discount:.0%} created")

            )

        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for product in products:
            self.stdout.write(
                self.style.HTTP_INFO(f"product : {product.title} created")

            )

        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for comment in comments:
            self.stdout.write(
                self.style.HTTP_INFO(
                    f"comment created: user -> {comment.user.username}  product --> {comment.product.title}")

            )
        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for order in orders:
            self.stdout.write(
                self.style.HTTP_INFO(f"order {order.id} created")

            )
        self.stdout.write(
            self.style.HTTP_INFO("*"*30 + '\n')

        )

        for items in order_items:
            self.stdout.write(
                self.style.HTTP_INFO(f"order item {items.id} created")

            )

        self.stdout.write(
            self.style.SUCCESS('Successfully created data')
        )
