from urllib import urlencode, urlopen
from json import loads
from should_dsl import should
from lettuce import *
from restfulie import Restfulie

@step(r'Given there is an URL accepting posts at "(.*)"')
def given_there_is_an_url_accepting_posts_at(step, uri):
    world.uri = uri

@step(r'When I post "(.*)" as "(.*)"')
def when_i_post_the_following_content_as(step, content, content_type):
    Restfulie.at(world.uri).as_(content_type).post(content)

@step(r'And I request the resource at "(.*)" as raw')
def then_i_request_the_resource_as_raw(step, uri):
    world.resource = Restfulie.at(uri).raw().get()

@step(r'When I post a dict containing "(.*)" as "(.*)"')
def when_i_post_a_dict_containing_group1_as_group2(step, content, content_type):
    Restfulie.at(world.uri).as_(content_type).post(eval(content))

@step(r'Then the response body is "(.*)" as json')
def then_the_response_body_is_group1_as_group2(step, response_body):
    actual = loads(world.resource.response.body)
    expected = eval(response_body)
    actual |should| equal_to(expected)

