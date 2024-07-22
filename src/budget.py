import click
import crud
import pickle
import os

@click.group()
@click.pass_context
def cli(ctx: click.Context) -> None:
    """Run the CLI."""
    #print("CLI Development in progress!")
    data_directory = ".data"
    data_file = "data.pkl"
    data_path = os.path.join(data_directory, data_file)
    ctx.obj = {'data_path': data_path, 'data': None}

    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    
    if os.path.exists(data_path):
        with open(data_path, 'rb') as f:
            ctx.obj['data'] = pickle.load(f)

cli.add_command(crud.create)
