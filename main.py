import click
import os


def select(choice):
    name=choice.split(':')[0]
    path=choice.split(':')[1]

    click.echo("Selected project: " + name)

    os.chdir(path)
    os.system("tmux .")
    os.system("nvim .")

@click.command()
def projects():
    projects = os.environ['PROJECTS'].split(',')

    if projects == None:
        click.echo("There are no projects under the PROJECTS env.")
        return

    click.echo('Select the project you desire:')

    i = 0
    for project in projects:
        click.echo(str(i) + ' -> ' + project)
        i+=1

    choice = click.prompt(
        "Please select:",
        type=click.Choice([str(i) for i in range(len(projects))]),
        show_default=False,
    )

    select(projects[int(choice)])


if __name__ == '__main__':
    projects()
