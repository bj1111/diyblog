from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Blog, Comment
from django.core.paginator import Paginator

class BlogModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        self.blog = Blog.objects.create(
            author=user,
            title="Test Blog",
            text="This is a test blog.",
        )

    def test_blog_str_method(self):
        """Test __str__ method of Blog model"""
        self.assertEqual(str(self.blog), "Test Blog")

    def test_blog_label_length(self):
        """Test if the labels and lengths are as expected"""
        field_label = self.blog._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')
        field_length = self.blog._meta.get_field('title').max_length
        self.assertEqual(field_length, 150)


class CommentModelTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        blog = Blog.objects.create(
            author=user,
            title="Test Blog",
            text="This is a test blog.",
        )
        self.comment = Comment.objects.create(
            blog=blog,
            author=user,
            text="test comment",
        )

    def test_comment_str_method(self):
        """Test __str__ method of Comment model"""
        self.assertEqual(str(self.comment), "test comment")

    def test_comment_label_length(self):
        """Test if the labels and lengths are as expected"""
        field_label = self.comment._meta.get_field('text').verbose_name
        self.assertEqual(field_label, 'text')


class BlogListViewTest(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="testuser", password="testpass")
        for i in range(15):
            Blog.objects.create(
                author=user,
                title=f"Test Blog {i}",
                text="This is a test blog.",
            )
        self.client.login(username='testuser', password='testpass') 

    def test_blog_list_view_url(self):
        """Test if the BlogListView is accessible at the expected URL"""
        response = self.client.get('/blogs/')  # Direct URL path
        self.assertEqual(response.status_code, 200)  # Should return 200 OK

    def test_blog_list_view_named_url(self):
        """Test if the BlogListView is accessible at the expected named URL"""
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)

    def test_blog_list_view_template(self):
        """Test if the BlogListView uses the expected template"""
        response = self.client.get(reverse('blog:list'))
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_blog_list_view_pagination(self):
        """Test if the BlogListView paginates the blogs by 5"""
        response = self.client.get(reverse('blog:list'))
        blogs = response.context['page_obj']
        self.assertEqual(len(blogs), 5)  # Check if first page has 5 blogs

    def test_blog_list_view_second_page(self):
        """Test if pagination works on the second page"""
        response = self.client.get(reverse('blog:list') + '?page=2')
        blogs = response.context['page_obj']
        self.assertEqual(len(blogs), 5)  # Check if second page also has 5 blogs
