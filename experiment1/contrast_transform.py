import cv2 as cv
import numpy as np

def read_image():
    image = cv.imread(r'C:\Users\CharlesKinx\Desktop\project\image.jpg')

    return image


if __name__ == '__main__':
    data = read_image()
    b1, g1, r1 = cv.split(data)

    data[:, :, 0] = 0
    data[:, :, 1] = 0
    data[:, :, 2] = 0
    b, g, r = cv.split(data)

    image1 = cv.merge((b1, g1, r))
    image2 = cv.merge((b1, g, r1))
    image3 = cv.merge((b, g1, r1))



    image = np.hstack((image1, image2, image3))

    print(image.shape)

    # data[:,:,2] = 0
    # data[:, :, 0] = 0
    cv.namedWindow("Image",cv.WINDOW_NORMAL)
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()