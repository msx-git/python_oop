from PIL import Image
import os


class ImageDataset:
    def __init__(self, root):
        self.root = root
        self.filenames = os.listdir(self.root)

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, index):
        image = Image.open(f'{self.root}/{self.filenames[index]}')
        return image


ds = ImageDataset('images')

print(f'images: {ds.filenames}')
print(f'number of images: {len(ds)}')
print(f'last image: {ds[5]}')
img = ds[5]
img.show()
