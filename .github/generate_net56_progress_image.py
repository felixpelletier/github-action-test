import cairo
import click

@click.command()
@click.option('--width', default=640)
@click.option('--height', default=60)
@click.option('--output', default="net56_progress.png")
def generate_image(width, height, output):

    total_crawler_count = 33
    net5_crawler_count = 17
    net5_ratio = float(net5_crawler_count) / float(total_crawler_count)

    LINE_W = 2.0
    INNER_MARGIN = 4.0 + LINE_W
    TOP_MARGIN = 0.3 * height

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    ctx = cairo.Context(surface)

    ctx.rectangle(LINE_W / 2, LINE_W / 2 + TOP_MARGIN, 1.0 * (width - LINE_W), 1 * (height - LINE_W - TOP_MARGIN))
    ctx.set_source_rgb(0.00, 0.00, 0.00)
    ctx.set_line_width(LINE_W)
    ctx.set_line_cap(cairo.LINE_CAP_BUTT)
    ctx.stroke()

    ctx.rectangle(INNER_MARGIN / 2, INNER_MARGIN / 2 + TOP_MARGIN, net5_ratio * (width - INNER_MARGIN), 1 * (height - INNER_MARGIN - TOP_MARGIN))
    ctx.set_source_rgb(0.18, 0.80, 0.25) # Some kind of green.
    ctx.fill()

    ctx.move_to(LINE_W, TOP_MARGIN * 0.90)
    ctx.set_font_size(TOP_MARGIN * 0.95)
    ctx.show_text(f"{net5_ratio * 100:.0f}% ({net5_crawler_count}/{total_crawler_count})")

    surface.write_to_png(output)


if __name__ == '__main__':
    generate_image()

print("Hello world!")