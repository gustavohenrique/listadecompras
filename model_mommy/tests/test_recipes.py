#coding: utf-8

from django.test import TestCase
from model_mommy import mommy
from model_mommy.models import Person, DummyNumbersModel, DummyBlankFieldsModel
from model_mommy.recipe import Recipe, foreign_key
from datetime import date, datetime

class TestDefiningRecipes(TestCase):
    def setUp(self):
        self.recipe_attrs = {
          'name': 'John Doe',
          'nickname': 'joe',
          'age': 18,
          'bio': 'Someone in the crowd',
          'birthday': date.today(),
          'appointment': date.today(),
          'blog': 'http://joe.blogspot.com',
          'wanted_games_qtd': 4,
          'birth_time': datetime.now()
        }
        self.person_recipe = Recipe(
          Person,
          **self.recipe_attrs
        )

    def test_flat_model_make_recipe_with_the_correct_attributes(self):
        """
          A 'flat model' means a model without associations, like
          foreign keys, many to many and one to one
        """
        person = self.person_recipe.make()
        self.assertEqual(person.name, self.recipe_attrs['name'])
        self.assertEqual(person.nickname, self.recipe_attrs['nickname'])
        self.assertEqual(person.age, self.recipe_attrs['age'])
        self.assertEqual(person.bio, self.recipe_attrs['bio'])
        self.assertEqual(person.birthday, self.recipe_attrs['birthday'])
        self.assertEqual(person.appointment, self.recipe_attrs['appointment'])
        self.assertEqual(person.blog, self.recipe_attrs['blog'])
        self.assertEqual(person.wanted_games_qtd, self.recipe_attrs['wanted_games_qtd'])
        self.assertNotEqual(person.id, None)

    def test_flat_model_prepare_recipe_with_the_correct_attributes(self):
        person = self.person_recipe.prepare()
        self.assertEqual(person.name, self.recipe_attrs['name'])
        self.assertEqual(person.nickname, self.recipe_attrs['nickname'])
        self.assertEqual(person.age, self.recipe_attrs['age'])
        self.assertEqual(person.bio, self.recipe_attrs['bio'])
        self.assertEqual(person.birthday, self.recipe_attrs['birthday'])
        self.assertEqual(person.appointment, self.recipe_attrs['appointment'])
        self.assertEqual(person.blog, self.recipe_attrs['blog'])
        self.assertEqual(person.wanted_games_qtd, self.recipe_attrs['wanted_games_qtd'])
        self.assertEqual(person.id, None)

    def test_accepts_callable(self):
        r = Recipe(DummyBlankFieldsModel,
            blank_char_field = lambda: 'callable!!'
        )
        value = r.make().blank_char_field
        self.assertEqual(value, 'callable!!')

    def test_make_recipes_with_args(self):
        """
          Overriding some fields values at recipe execution
        """
        person = self.person_recipe.make(name='Guido', age=56)
        self.assertNotEqual(person.name, self.recipe_attrs['name'])
        self.assertEqual(person.name, 'Guido')

        self.assertNotEqual(person.age, self.recipe_attrs['age'])
        self.assertEqual(person.age, 56)

        self.assertEqual(person.nickname, self.recipe_attrs['nickname'])
        self.assertEqual(person.bio, self.recipe_attrs['bio'])
        self.assertEqual(person.birthday, self.recipe_attrs['birthday'])
        self.assertEqual(person.appointment, self.recipe_attrs['appointment'])
        self.assertEqual(person.blog, self.recipe_attrs['blog'])
        self.assertEqual(person.wanted_games_qtd, self.recipe_attrs['wanted_games_qtd'])
        self.assertNotEqual(person.id, None)

    def test_prepare_recipes_with_args(self):
        """
          Overriding some fields values at recipe execution
        """
        person = self.person_recipe.prepare(name='Guido', age=56)
        self.assertNotEqual(person.name, self.recipe_attrs['name'])
        self.assertEqual(person.name, 'Guido')

        self.assertNotEqual(person.age, self.recipe_attrs['age'])
        self.assertEqual(person.age, 56)

        self.assertEqual(person.nickname, self.recipe_attrs['nickname'])
        self.assertEqual(person.bio, self.recipe_attrs['bio'])
        self.assertEqual(person.birthday, self.recipe_attrs['birthday'])
        self.assertEqual(person.appointment, self.recipe_attrs['appointment'])
        self.assertEqual(person.blog, self.recipe_attrs['blog'])
        self.assertEqual(person.wanted_games_qtd, self.recipe_attrs['wanted_games_qtd'])
        self.assertEqual(person.id, None)

class TestExecutingRecipes(TestCase):
    """
      Tests for calling recipes defined in mommy_recipes.py
    """
    def test_model_with_foreign_key(self):
        dog = mommy.make_recipe('model_mommy.dog')
        self.assertEqual(dog.breed, 'Pug')
        self.assertTrue(isinstance(dog.owner, Person))
        self.assertNotEqual(dog.owner.id, None)

        dog = mommy.prepare_recipe('model_mommy.dog')
        self.assertEqual(dog.breed, 'Pug')
        self.assertTrue(isinstance(dog.owner, Person))
        self.assertNotEqual(dog.owner.id, None)

    def test_make_recipe(self):
        person = mommy.make_recipe('model_mommy.person')
        self.assertTrue(isinstance(person, Person))
        self.assertNotEqual(person.id, None)

    def test_prepare_recipe(self):
        person = mommy.prepare_recipe('model_mommy.person')
        self.assertTrue(isinstance(person, Person))
        self.assertEqual(person.id, None)

    def test_make_recipe_with_args(self):
        person = mommy.make_recipe('model_mommy.person', name='Dennis Ritchie', age=70)
        self.assertEqual(person.name, 'Dennis Ritchie')
        self.assertEqual(person.age, 70)

    def test_prepare_recipe_with_args(self):
        person = mommy.prepare_recipe('model_mommy.person', name='Dennis Ritchie', age=70)
        self.assertEqual(person.name, 'Dennis Ritchie')
        self.assertEqual(person.age, 70)

class ForeignKeyTestCase(TestCase):
    def test_returns_a_callable(self):
        number_recipe = Recipe(DummyNumbersModel,
            float_field = 1.6
        )
        method = foreign_key(number_recipe)
        self.assertTrue(callable(method))
        self.assertTrue(method.im_self, number_recipe)

    def test_not_accept_other_type(self):
        with self.assertRaises(TypeError) as c:
            foreign_key('something')
        exception = c.exception
        self.assertEqual(exception.message, 'Not a recipe')
