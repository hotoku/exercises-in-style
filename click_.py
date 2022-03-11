import subprocess as sp
import click


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    if ctx.invoked_subcommand is None:
        run()


@main.command()
def fizz():
    print("Fizz", end="")


@main.command()
def buzz():
    print("Buzz", end="")


@main.command()
@click.argument("n", type=int)
def num(n):
    print(n, end="")


@main.command()
def run():
    for n in range(1, 101):
        flag = True
        if n % 3 == 0:
            sp.run(["python", __file__, "fizz"])
            flag = False
        if n % 5 == 0:
            sp.run(["python", __file__, "buzz"])
            flag = False
        if flag:
            sp.run(["python", __file__, "num", str(n)])
        print("")


main()
