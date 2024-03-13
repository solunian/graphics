from PIL import Image

def gif_to_png_frames():
  with Image.open("./website/nyan_cat_kawaii.gif") as im:
    for i in range(num_key_frames):
      im.seek(im.n_frames // num_key_frames * i)
      im.save(f"./website/frames/{i}.png")

# print(gif.format, gif.size, gif.mode)

num_key_frames = 48
im_len = 497

def get_pixels(im: Image.Image, dx: tuple[int, int], dy: tuple[int, int]):
  pixels = []
  for x in range(dx[0], dx[1]):
      for y in range(dy[0], dy[1]):
        pixels.append(im.getpixel((x, y)))
  return pixels


def best_pixel(pixels: list[tuple[int, int, int]]):
  most_common_pixel = max(set(pixels), key=pixels.count) # code for best pixel color to get in 7x7 "filter"
  # faskfl;sdajflksdfjsakldfj ughhhhh i cant do this easily except manually cuz this darn pixel cat is weird!
  return most_common_pixel
  

def simplify(name: str):
  with Image.open(f"./website/frames/{name}.png") as im:
    # print(im.mode)
    im = im.convert("RGB").crop((0, 0, im_len, im_len)) # use 7x7 pixel size

    new_im = Image.new(mode="RGB", size=(im_len // 7, im_len // 7))
    for x in range(0, im.size[0], 7):
      for y in range(0, im.size[1], 7):
        pixels = get_pixels(im, (x, x + 7), (y, y + 7))
        
        best = best_pixel(pixels)
        # pixel = im.getpixel((x, y))
        # print(pixel, end=" ")
        new_im.putpixel((x // 7, y // 7), best)
    new_im.show()
        
        
    


simplify("3")

