from subprocess import call
import click


@click.command(help="Given a video file and a timing file, "
                    "a clip will be created by cutting at given timestamps and then combining.\n\n"
                    "FFmpeg needs to be installed on your system in order to use this program.\n\n"
                    "The timing file should be a text file with clip timestamps separated by new lines,"
                    "in a format like this '30 70'.")
@click.argument("video_file",
                type=click.Path())
@click.argument("timing_file",
                type=click.File())
@click.option("--out",
              default="out.mkv",
              help="Output file, default is out.mkv in current directory",
              type=click.Path(writable=True))
def mergecat(video_file, timing_file, *, out):
    concat = open("concat.txt", "w")

    for count, timestamp in enumerate(timing_file):
        start, end = timestamp.split(" ")
        duration = str(int(end) - int(start))

        click.echo(f"Creating clip {count}")
        call(["ffmpeg", "-y", "-loglevel", "panic",
              "-i", video_file,
              "-ss", start, "-t", duration,
              "-c", "copy", f"in{count}.mkv"])
        concat.write(f'file \'in{count}.mkv\'\n')

    concat.close()
    click.echo(f'Creating final output')
    call(["ffmpeg", "-y", "-loglevel", "panic",
          "-f", "concat", "-i", "concat.txt",
          "-c", "copy", out])


if __name__ == '__main__':
    mergecat()
