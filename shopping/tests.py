from django.test import TestCase
from django.urls import reverse


class ShoppingActionsTests(TestCase):
    fixtures = ['initial_data.json']

    def test_add_to_cart_increments_header_count(self):
        url = reverse("add_to_cart", args=["everyday-shoulder-bag"])

        self.client.post(url)
        response = self.client.post(url)

        self.assertRedirects(response, reverse("home"))
        self.assertEqual(self.client.session["cart"]["everyday-shoulder-bag"], 2)
        response = self.client.get(reverse("home"))
        self.assertContains(response, ">2</span>")
        self.assertContains(response, 'data-bs-target="#shoppingCart"')
        self.assertContains(response, "Everyday shoulder bag")
        self.assertContains(response, "Rs. 4900")
        self.assertContains(response, f'href="{reverse("cart")}"')

    def test_like_can_be_toggled_on_and_off(self):
        url = reverse("toggle_like", args=["daily-classic-watch"])

        self.client.post(url)
        response = self.client.get(reverse("home"))
        self.assertContains(response, "bi-heart-fill")

        self.client.post(url)
        response = self.client.get(reverse("home"))
        self.assertContains(response, "bi-heart")

    def test_wishlist_count_is_visible_in_header(self):
        self.client.post(reverse("toggle_like", args=["daily-classic-watch"]))
        self.client.post(reverse("toggle_like", args=["weekend-slip-ons"]))

        response = self.client.get(reverse("home"))
        self.assertContains(response, '>2</span>')

    def test_home_page_includes_csrf_tokens_for_forms(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, 'name="csrfmiddlewaretoken"')
        self.assertNotIn('<!-- {% csrf_token %}', response.content.decode())

    def test_header_wishlist_is_clickable(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, f'href="{reverse("wishlist")}"')

    def test_wishlist_page_lists_saved_items(self):
        self.client.post(reverse("toggle_like", args=["daily-classic-watch"]))
        self.client.post(reverse("toggle_like", args=["weekend-slip-ons"]))

        response = self.client.get(reverse("wishlist"))
        self.assertContains(response, "Daily classic watch")
        self.assertContains(response, "Weekend slip-ons")
        self.assertContains(response, "Your Wishlist")

    def test_unknown_product_is_not_added(self):
        self.client.post(reverse("add_to_cart", args=["not-a-product"]))

        self.assertNotIn("cart", self.client.session)
