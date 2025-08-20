from PIL import Image
import requests
import musicbrainzngs
from flask import Flask, render_template
import os

app = Flask(__name__) 

musicbrainzngs.set_useragent("Dotwell", "1.0", "twmedina6@gmail.com")

def get_artist(name):
    result = musicbrainzngs.search_artists(artist=name)
    artist = result['artist-list'][0]
    if artist:
        return artist
    return None

def get_album_id(artistName, albumName):
    result = musicbrainzngs.search_releases(artistname=artistName, release=albumName, format="Digital Media")
    if result['release-list']:
        for release in result['release-list']:
            if not release.get('disambiguation'):
                return [release['id']]
    return None

def get_cover(artistName, albumName):
    album_ids = get_album_id(artistName, albumName)
    for id in album_ids:
        images = musicbrainzngs.get_image_list(id)
        print(images['images'][0]['image'])
        return images['images'][0]['image']

def save_pixel_cover(artistName, albumName):
    img = get_cover(artistName, albumName)
    img = Image.open(requests.get(img, stream=True).raw)
    if img:
        img = img.resize((30, 30), resample=2)
        img.save("./albumCovers/" + albumName.replace(" ", "_") + "-" + artistName.strip().replace(" ", "_") + ".jpg")
    else:
        print(f"Cover not found for {artistName} - {albumName}")

def display_album_cover(artistName, albumName):
    #code to display cover pixel by pixel on virtual dot-matrix display
    img = None
    if(os.path.exists("./albumCovers/" + albumName.replace(" ", "_") + "-" + artistName.strip().replace(" ", "_") + ".jpg")):
        img = Image.open("./albumCovers/" + albumName.replace(" ", "_") + "-" + artistName.strip().replace(" ", "_") + ".jpg")
    else:
        save_pixel_cover(artistName, albumName)

    img = img.load()
    for y in range(30):
        for x in range(30):
            r, g, b = img[x, y][:3]
            #edit html style

display_album_cover("Tame Impala", "Currents")