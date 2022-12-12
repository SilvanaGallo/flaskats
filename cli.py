import click
import requests
import json
from flaskats.broker import RabbitmqConsumer
from flaskats import repository


items_url = 'http://localhost:5000/items'
reports_url = 'http://localhost:5000/reports'

@click.group()
def worker():
    pass

# @worker.command()
# @click.option('-u','--assigned-user', default='', help='If not empty, only items assigned to the specified user will be returned. Must be a valid Rollbar username, or you can use the keywords assigned (items that are assigned to any owner) or unassigned (items with no owner).')
# @click.option('-e','--environment', default='', help='If not empty, only items in the specified environment will be returned. Specify multiple times to filter by multiple environments.')
# @click.option('-f','--framework', default='', help='If not empty, only items in the specified framework will be returned. Specify multiple times to filter by multiple frameworks.')
# @click.option('-i','--ids', default='', help='(comma-separated list of integers) if not empty, list of item IDs to return, instead of using all items in the project')
# @click.option('-l','--level', default='', help='If not empty, only items with the specified level will be returned. Valid values: debug, info, warning, error, critical. Specifiy multiple times to filter by multiple levels.')
# @click.option('-p','--page', default=None, help='Page number, starting from 1. 100 items are returned per page.')
# @click.option('-q','--query', default='', help='A search string, using the same format as the search box on the Items page.')
# @click.option('-s','--status', default='', help='If not empty, only items with the specified status will be returned. Valid values: active, resolved, muted, archived. Specify multiple times to filter by multiple statuses.')
# def get_items(assigned_user, environment, framework, ids, level, page, query, status):
    
#     params = {  'assigned-user': assigned_user, 
#                 'environment': environment, 
#                 'framework': framework,
#                 'ids': ids, 
#                 'level': level, 
#                 'page': page,
#                 'query': query,
#                 'status': status
#             }
#     real_params= {k:v for k,v in params.items() if v}
#     r = requests.get(items_url, params=real_params)
#     click.echo(json.dumps(r.json(), indent=2))

@worker.command()
def start_worker():
    worker = RabbitmqConsumer(repository=repository)
    worker.start()


# @items.command()
# @click.argument('id', required=True)
# def get_item(id):
#     url = f"{items_url}/{id}"
#     r = requests.get(url)
#     click.echo(json.dumps(r.json(), indent=2))


# @items.command()
# @click.option('-t','--title', default='', help='Title.')
# @click.option('-l','--level', default='', help='Valid values: debug, info, warning, error, critical.')
# @click.option('-u','--user-id', default=None, help='User assigned')
# @click.option('-s','--status', default='', help='Valid values: active, resolved, muted, archived. ')
# @click.option('-r','--resolved-in-version', default='', help='Version in which the item was resolved.')
# @click.argument('id', required=True)
# def update_item(title, level, user_id, status, resolved_in_version, id):
#     params = {  
#                 'title': title, 
#                 'level': level, 
#                 'assigned_user_id': user_id,
#                 'status': status,
#                 'resolved_in_version': resolved_in_version 
#             }
#     url = f"{items_url}/{id}"
#     real_params = {k:v for k,v in params.items() if v}
#     r = requests.patch(url, json=real_params)
#     click.echo(json.dumps(r.json(), indent=2))


# @items.command()
# @click.argument('id', required=True)
# def delete_item(id):
#     url = f"{items_url}/{id}"
#     r = requests.delete(url)
#     click.echo(json.dumps(r.json(), indent=2))


# @click.group()
# def reports():
#     pass


# @reports.command()
# @click.option('-e','--environment', default='', help='Comma-separated list of environments to consider. If empty, then returns results for "any environment".')
# @click.option('-h','--hours', default=24, help='Number of recent hours to consider. Min 1, max 168.')
# def top_active_items(environment, hours):
#     params = {  
#                 'environment': environment, 
#                 'hours': hours 
#     }
#     real_params= {k:v for k,v in params.items() if v}
#     r = requests.get(reports_url, params=real_params)
#     click.echo(json.dumps(r.json(), indent=2))

# @reports.command()
# def clear_reports():
#     r = requests.delete(reports_url)
#     click.echo(json.dumps(r.json(), indent=2))


cli = click.CommandCollection(sources=[worker])

if __name__ == '__main__':
    cli()
