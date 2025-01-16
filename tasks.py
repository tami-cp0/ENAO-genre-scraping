from invoke import task
import subprocess

# run the genres spider
@task
def genres(ctx):
    subprocess.run(["scrapy", "crawl", "genres", "-O", "genres.json"])

# generate a new spider    
@task
def spider(ctx, name, url="example.com"):
    subprocess.run(["scrapy", "genspider", f"{name}", f"{url}"])
