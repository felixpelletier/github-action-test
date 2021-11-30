import cairo
import click

@click.command()
@click.option('--width', default=640)
@click.option('--height', default=60)
@click.option('--output', default="net56_progress.png")
def generate_image(width, height, output):

    net5_percentage = 0.1

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)
    ctx.scale(width, height)  # Normalizing the canvas

    ctx.rectangle(0, 0, net5_percentage * 0.9, 1)
    ctx.set_source_rgb(0.18, 0.80, 0.25)
    ctx.fill()

    ctx.move_to(0, 0)

    surface.write_to_png(output)


if __name__ == '__main__':
    generate_image()

print("Hello world!")