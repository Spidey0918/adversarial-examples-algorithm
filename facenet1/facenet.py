import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
import facenet.src.facenet as facenet
import facenet.src.align.detect_face as detect_face
def get_img_pairs_list(pairs_txt_path, img_path):
    """ 指定图片组合及其所在文件，返回各图片对的绝对路径
        Args:
            pairs_txt_path：图片pairs文件，里面是6000对图片名字的组合
            img_path：图片所在文件夹
        return:
            img_pairs_list：深度为2的list，每一个二级list存放的是一对图片的绝对路径
    """
    file = open(pairs_txt_path)
    img_pairs_list, labels = [], []
    while 1:
        img_pairs = []
        line = file.readline().replace('\n', '')
        if line == '':
            break
        line_list = line.split('\t')
        if len(line_list) == 3:
            # 图片路径示例：
            # 'C:\Users\thinkpad1\Desktop\image_set\lfw_funneled\Tina_Fey\Tina_Fey_0001.jpg'
            img_pairs.append(
                img_path + '\\' + line_list[0] + '\\' + line_list[0] + '_' + ('000' + line_list[1])[-4:] + '.jpg')
            img_pairs.append(
                img_path + '\\' + line_list[0] + '\\' + line_list[0] + '_' + ('000' + line_list[2])[-4:] + '.jpg')
            labels.append(1)
        elif len(line_list) == 4:
            img_pairs.append(
                img_path + '\\' + line_list[0] + '\\' + line_list[0] + '_' + ('000' + line_list[1])[-4:] + '.jpg')
            img_pairs.append(
                img_path + '\\' + line_list[2] + '\\' + line_list[2] + '_' + ('000' + line_list[3])[-4:] + '.jpg')
            labels.append(0)
        else:
            continue

        img_pairs_list.append(img_pairs)
    return img_pairs_list, labels
def face_verification(img_pairs_list):
    model = r'facenet\src\align'
    model_facenet = './20170512-110547.pb'
    # mtcnn相关参数
    minsize = 40
    threshold = [0.4, 0.5, 0.6]  # pnet、rnet、onet三个网络输出人脸的阈值，大于阈值则保留，小于阈值则丢弃
    factor = 0.709  # scale factor

    # 创建mtcnn网络
    with tf.Graph().as_default():
        sess = tf.compat.v1.Session()
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, model)

    margin = 44
    image_size = 160

    with tf.Graph().as_default():

        with tf.compat.v1.Session() as sess:

            # 根据模型文件载入模型
            facenet.load_model(model_facenet)
            # 得到输入、输出等张量
            images_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.compat.v1.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.compat.v1.get_default_graph().get_tensor_by_name("phase_train:0")
            result, dist = [], []
            for i in range(len(img_pairs_list)):
            # 读取一对人脸图像
                img_pairs = img_pairs_list[i]
                img_list = []
                img1 = cv2.imread(img_pairs[0])
                img2 = cv2.imread(img_pairs[1])

                img_size1 = np.asarray(img1.shape)[0:2]
                img_size2 = np.asarray(img2.shape)[0:2]

                # 检测该对图像中的人脸
                bounding_box1, _1 = detect_face.detect_face(img1, minsize, pnet, rnet, onet, threshold, factor)
                bounding_box2, _2 = detect_face.detect_face(img2, minsize, pnet, rnet, onet, threshold, factor)

                # 未检测到人脸，则将结果标为-1，后续计算准确率时排除
                if len(bounding_box1) < 1 or len(bounding_box2) < 1:
                    result.append(-1)
                    dist.append(-1)
                    continue
                display_grid=np.zeros(shape=(img1.shape[0],img1.shape[1]*2,3))

                # 将图片1加入img_list
                det = np.squeeze(bounding_box1[0, 0:4])
                bb = np.zeros(4, dtype=np.int32)
                bb[0] = np.maximum(det[0] - margin / 2, 0)
                bb[1] = np.maximum(det[1] - margin / 2, 0)
                bb[2] = np.minimum(det[2] + margin / 2, img_size1[1])
                bb[3] = np.minimum(det[3] + margin / 2, img_size1[0])
                cropped = img1[bb[1]:bb[3], bb[0]:bb[2], :]
                aligned = cv2.resize(cropped, (image_size, image_size))
                display_grid[:img1.shape[0],:img1.shape[0],:]=img1/255.
                prewhitened = facenet.prewhiten(aligned)
                img_list.append(prewhitened)

                # 将图片2加入img_list
                det = np.squeeze(bounding_box2[0, 0:4])
                bb = np.zeros(4, dtype=np.int32)
                bb[0] = np.maximum(det[0] - margin / 2, 0)
                bb[1] = np.maximum(det[1] - margin / 2, 0)
                bb[2] = np.minimum(det[2] + margin / 2, img_size2[1])
                bb[3] = np.minimum(det[3] + margin / 2, img_size2[0])
                cropped = img2[bb[1]:bb[3], bb[0]:bb[2], :]
                aligned = cv2.resize(cropped, (image_size, image_size))
                display_grid[:img1.shape[0],img1.shape[0]:,:]=img2/255.
                prewhitened = facenet.prewhiten(aligned)
                img_list.append(prewhitened)

                images = np.stack(img_list)

                # 将两个人脸转化为512维的向量
                feed_dict = {images_placeholder: images, phase_train_placeholder: False}
                emb = sess.run(embeddings, feed_dict=feed_dict)

                # 计算两个人脸向量的距离
                ed = np.sqrt(np.sum(np.square(np.subtract(emb[0], emb[1]))))
                if ed <= 1.1:
                    result.append(1)
                else:
                    result.append(0)
                dist.append(ed)
                #plt.subplot(len(img_pairs_list),1,i)
                plt.figure(figsize=(len(img_pairs_list),2))
                plt.imshow(display_grid,aspect='auto')
                plt.title("distance:{:.2f} acc:{}".format(ed,result[i]))
                plt.grid(False)
                plt.show()
    return result, dist

pairs_txt_path = './pairs2.txt'
img_path = r'dataset\lfw'
img_pairs_list, labels = get_img_pairs_list(pairs_txt_path, img_path)
result, dist = face_verification(img_pairs_list)