from django.core.management.base import BaseCommand
from pytube import Playlist as pyPlaylist, YouTube

from tutorials.models import Tutorial, Playlist
from tricks.models import Trick


class Command(BaseCommand):
    help = 'adds new tutorials to database'

    def add_arguments(self, parser):
        parser.add_argument(
            '-m', '--max',
            type=int,
            dest='max',
            help='maximum number of new tricks to add'
        )

    def setup(self):
        self.playlists = Playlist.objects.all()
        self.count_added = 0
        self.null_trick, created = Trick.objects.get_or_create(
            name='null', difficulty='o')

    def add_tutorial(self, playlist, video_url):
        if not Tutorial.objects.filter(url=video_url).exists():
            video = YouTube(video_url)
            Tutorial.objects.create(
                yt_title=f'{playlist.name} - {video.title}',
                trick=self.null_trick,
                author=playlist.author,
                url=video_url,
            )
            self.count_added += 1

    def handle(self, *args, **options):
        self.setup()
        self.max = options.get('max', 10)

        for playlist in self.playlists:
            for video_url in pyPlaylist(playlist.url).video_urls:
                self.add_tutorial(playlist, video_url)
                if self.count_added >= self.max:
                    break
            if self.count_added >= self.max:
                break

        self.stdout.write(self.style.SUCCESS(
            f'added {self.count_added} tutorials'))
