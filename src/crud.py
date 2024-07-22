import click
from utils import inlist_convert
import os
import pickle

@click.command()
@click.argument('account')
@click.option('-b', '--balance', required=True, type=int)
@click.pass_context
def create(ctx: click.Context, account: str, balance: int) -> None:
    """Create a new account."""
    
    if ctx.obj['data']:
        data = ctx.obj['data']
        data['account'][account] = {'balance': balance, 'categories': {}}
    else:   
        data = {'account': {account: {'balance': balance, 'categories': {}}}}
        data = data
    
    add_cats = True
    while add_cats:
        category = click.prompt('Enter a category or list of categories separated by commas (enter to skip)')
        if not category:
            category = []
            add_cats = False
            break
        category = inlist_convert(category)
        confirm = click.confirm('Add another category?')
        if not confirm:
            add_cats = False

    if len(category) > 0:
        for cat in category:
            cat_balance = click.prompt(f'Enter the balance for {cat}:', type=int)
            data['account'][account]['categories'][cat] = cat_balance


    print(f'{account} Created!')
    print(data)
    with open(ctx.obj['data_path'], 'wb') as f:
        pickle.dump(data, f)