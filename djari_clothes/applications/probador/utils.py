import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt


def cast_InMemoryUploadFile_numpy_array(image_person, image_shirt, plot=False):
    # print(type(image_person))
    # print(type(image_shirt_person))
    bytes_person = image_person.file
    bytes_shirt = image_shirt.file

    image_person = Image.open(bytes_person)
    image_shirt = Image.open(bytes_shirt)

    image_person_np = np.array(image_person)
    image_shirt_np = np.array(image_shirt)
    # print(image_np)
    if plot:
        f, ax = plt.subplots(2)
        ax[0].imshow(image_person_np)
        ax[1].imshow(image_shirt_np)
    plt.show()
    return image_person_np, image_shirt_np
